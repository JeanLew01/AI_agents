"""Compare USAGE.md's stated tool names / required parameters / defaults with the live input schemas
(taken from the verifier report of the extracted server). No JAX. argv: <schemas json (verifier report)> <USAGE.md> <out>"""
import json
import re
import sys

rep = json.load(open(sys.argv[1]))
schemas = {k: v["input"] for k, v in rep["schemas"].items()}
usage = open(sys.argv[2]).read()
NONE = object()

# Claims transcribed from USAGE.md "Tools" section (value None = "no default stated" / null default).
claims = {
    "diffres_resample_particles_diffusion": {
        "required": ["particles_path"],
        "defaults": {"a": -2.0, "T": 1.0, "nsteps": 32, "integrator": "euler", "ode": True},
        "params_mentioned": ["a", "T", "nsteps", "integrator", "ode", "jitter", "seed", "prng_key", "output_dir"],
        "enums": {"integrator": ["euler", "jentzen_and_kloeden", "lord_and_rougemont", "tweedie", "diffrax"]},
    },
    "diffres_resample_particles_baseline": {
        "required": ["particles_path"],
        "defaults": {"method": "multinomial", "eps": None, "alpha": None, "tau": None},
        "doc_effective_defaults": {"eps": "1/log N", "alpha": 0.5, "tau": 0.5},
        "params_mentioned": ["method", "eps", "alpha", "tau"],
        "enums": {"method": ["multinomial", "stratified", "systematic", "multinomial_stopped", "ensemble_ot", "soft",
                             "gumbel_softmax"]},
    },
    "diffres_run_lgssm_particle_filter": {
        "required": ["model_path", "observations_path"],
        "defaults": {"nparticles": 32, "resampling_method": "diffusion", "resampling_threshold": 1.0,
                     "diffusion_a": -0.5, "diffusion_T": 3.0, "diffusion_steps": 8},
        "params_mentioned": ["nparticles", "resampling_method", "resampling_threshold", "diffusion_a", "diffusion_T",
                             "diffusion_steps", "diffusion_integrator", "diffusion_ode", "diffusion_jitter", "ot_eps",
                             "ot_implicit_diff", "soft_alpha", "gumbel_tau", "save_particle_path", "compute_gradient",
                             "compare_to_kalman", "seed", "prng_key", "output_dir"],
    },
    "diffres_run_lgssm_kalman_filter": {
        "required": ["model_path", "observations_path"],
        "defaults": {},
        "params_mentioned": ["smooth", "compute_gradient", "output_dir"],
    },
    "diffres_simulate_lgssm_data": {
        "required": ["model_path", "nsteps"],
        "defaults": {},
        "params_mentioned": ["seed", "prng_key", "output_dir"],
    },
}


def enum_of(prop):
    if "enum" in prop:
        return prop["enum"]
    for alt in prop.get("anyOf", []):
        if "enum" in alt:
            return alt["enum"]
    return None


out = {"tools_in_usage_and_server": {}, "per_tool": {}, "problems": []}
for name in schemas:
    out["tools_in_usage_and_server"][name] = f"`{name}`" in usage
for name, c in claims.items():
    s = schemas.get(name)
    t = {"in_server": s is not None}
    if s is None:
        out["problems"].append(f"{name} documented but not exposed")
        out["per_tool"][name] = t
        continue
    props = s.get("properties", {})
    t["schema_required"] = sorted(s.get("required", []))
    t["usage_required"] = sorted(c["required"])
    t["required_match"] = t["schema_required"] == t["usage_required"]
    if not t["required_match"]:
        out["problems"].append(f"{name}: required mismatch {t}")
    t["schema_params"] = sorted(props)
    t["usage_params_missing_in_schema"] = [p for p in c["params_mentioned"] if p not in props]
    if t["usage_params_missing_in_schema"]:
        out["problems"].append(f"{name}: USAGE mentions params not in schema {t['usage_params_missing_in_schema']}")
    t["schema_params_not_in_usage_text"] = [p for p in props if not re.search(r"`%s`" % re.escape(p), usage)]
    dd = {}
    for p, v in c["defaults"].items():
        sv = props.get(p, {}).get("default", NONE)
        if v is None:
            ok = sv is None
        else:
            ok = sv is not NONE and sv == v and isinstance(sv, bool) == isinstance(v, bool)
        dd[p] = {"usage": v, "schema": None if sv is NONE else sv, "match": bool(ok)}
        if not ok:
            out["problems"].append(f"{name}: default of {p} usage={v} schema={sv if sv is not NONE else 'absent'}")
    t["defaults"] = dd
    for p, vals in c.get("enums", {}).items():
        e = enum_of(props.get(p, {}))
        t.setdefault("enums", {})[p] = {"usage": sorted(vals), "schema": sorted(e) if e else e,
                                        "match": e is not None and sorted(e) == sorted(vals)}
        if not t["enums"][p]["match"]:
            out["problems"].append(f"{name}: enum {p} usage={vals} schema={e}")
    out["per_tool"][name] = t
out["undocumented_tools"] = [n for n in schemas if n not in claims]
out["consistent"] = not out["problems"] and not out["undocumented_tools"] and all(out["tools_in_usage_and_server"].values())
json.dump(out, open(sys.argv[3], "w"), indent=1)
print(json.dumps(out, indent=1)[:5000])
