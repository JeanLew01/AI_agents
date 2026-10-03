"""Compare the transcription of equation (7) with the second parser (pypdf) text of page 12."""
import re, json, sys, warnings, logging
logging.disable(logging.CRITICAL)
from pypdf import PdfReader
D = sys.argv[1]
r = PdfReader(D + "/source.pdf")
t = r.pages[11].extract_text()
i = t.find("x1 ="); print("start", i, repr(t[max(0,i-5):i+60]))
j = t.find("x12 = v12") + len("x12 = v12")
src = t[i:j]
src = re.sub(r"[-⏐]", "", src)
src = src.replace("˙", "").replace("−", "-")
src = re.sub(r"\s+", "", src)
st = json.load(open(D + "/pages/page-0012.json"))
md = st["items"][0]["markdown"]
a = md.index(r"\dot{x}_1"); b = md.index(r"\end{array}")
m = md[a:b]
m = m.replace("\\\\", "").replace(r"\quad", "").replace(r"\dot{x}", "x")
m = re.sub(r"\\(cos|sin)", r"\1", m)
m = re.sub(r"_\{(\d+)\}", r"\1", m); m = re.sub(r"_(\d)", r"\1", m)
m = re.sub(r"\s+", "", m)
print(len(src), len(m), src == m)
if src != m:
    k = next((k for k in range(min(len(src), len(m))) if src[k] != m[k]), min(len(src), len(m)))
    print("pdf :", src[max(0,k-40):k+60]); print("mine:", m[max(0,k-40):k+60])
