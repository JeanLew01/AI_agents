from pt import *
E = "&emsp;&emsp;"  # one nesting level
alg1 = "\n\n".join([
 r"**Algorithm 1** GreedyPack",
 r"**Input:** $\mathcal{X} \subset \mathbb{R}^d$: $d$-dimensional set of input states, $\delta \in \mathbb{R}_+$: packing precision",
 r"**Output:** $\mathcal{S}$: a $\delta$-packing for $\mathcal{X}$",
 r"1: $\mathcal{S} \leftarrow$ Random point chosen from $\mathcal{X}$;",
 r"2: **while** $\exists x \in \mathcal{X} : \forall y \in \mathcal{S}, \|x - y\| \ge \delta$ **do**",
 r"3: " + E + r"$\mathcal{S} \leftarrow \mathcal{S} \cup \{x\}$;",
 r"4: **return** $\mathcal{S}$;",
])
alg2 = "\n\n".join([
 r"**Algorithm 2** ApproximateReachability",
 r"**Input:** $\mathcal{X} \subset \mathbb{R}^d$: a $d$-dimensional set of input states, $\varepsilon \in (0, 1)$: desired approximation accuracy",
 r"**Output:** $\hat{F}_{\mathcal{S}}$: approximate reachable set such that $\mu(\hat{F}_{\mathcal{S}}) \ge (1 - \varepsilon)\mu(F(\mathcal{X}))$",
 r"1: $\alpha \leftarrow$ UpperSurfAreaToVolume$(\mathcal{X})$;",
 r"2: $K \leftarrow$ UpperLipschitzConstant$(\mathcal{X})$;",
 r"3: $\triangleright$ Approximate the universal constant from Lemma 3",
 r"4: $c \leftarrow$ UpperUniversalConstant$(\mathcal{X})$;",
 r"5: $\triangleright$ Set packing precision as established in Theorem 7",
 r"6: $\delta \leftarrow d\left((1 - \varepsilon)^{-1/d} - 1\right)/(\alpha K c)$;",
 r"7: $\mathcal{S} \leftarrow$ GreedyPack$(\mathcal{X}, \delta)$; $\triangleright$ Generate a $\delta$-packing for $\mathcal{X}$",
 r"8: $\hat{F}_{\mathcal{S}} \leftarrow \emptyset$;",
 r"9: **for** $x \in \mathcal{S}$ **do** $\triangleright$ Evaluate the reachable set for each $x \in \mathcal{S}$",
 r"10: " + E + r"$\hat{f}(x) \leftarrow$ EvaluateReachability$(x)$;",
 r"11: " + E + r"$\hat{F}_{\mathcal{S}} \leftarrow \hat{F}_{\mathcal{S}} \cup \hat{f}(x)$;",
 r"12: **return** $\hat{F}_{\mathcal{S}}$;",
])
alg3 = "\n\n".join([
 r"**Algorithm 3** AnytimeApproximateReachability",
 r"**Input:** $\mathcal{X} \subset \mathbb{R}^d$: $d$-dimensional set of input states",
 r"**Output:** $\hat{F}_{\mathcal{S}}$: asymptotically-optimal reachable set",
 r"1: $\varepsilon \leftarrow 1/2$; $\hat{F}_{\mathcal{S}} \leftarrow \emptyset$;",
 r"2: **while** allotted time remains **do**",
 r"3: " + E + r"$\hat{F}_{\mathcal{S}} \leftarrow$ ApproximateReachability$(\mathcal{X}, \varepsilon)$;",
 r"4: " + E + r"$\varepsilon \leftarrow \varepsilon/2$;",
 r"5: **return** $\hat{F}_{\mathcal{S}}$;",
])
items = [
 T(r"**Problem 1 (Approximate Reachability Problem).** For any given $\varepsilon \in (0, 1)$, generate a finite subset $\mathcal{S} \subset \mathcal{X}$ such that", L, 59, 81),
 T(r"$$(1 - \varepsilon)\mu(F(\mathcal{X})) \le \mu(F(\mathcal{S})) \le \mu(F(\mathcal{X})). \tag{1}$$", L, 89, 106),
 H("## IV. Method", (141, 208), 112, 124),
 T("In this section, we present our algorithm for generating reachable sets that are provably competitive with the ground-truth reachable set to any desired accuracy. We show that our main method (Alg. 2) can easily be used as a sub-procedure to obtain an anytime, asymptotically-optimal algorithm (Alg. 3) for reachability analysis.", L, 135, 205),
 H("### A. Overview", (48, 101), 222, 230),
 T(r"Accurate construction of the ground-truth reachable set $F(\mathcal{X})$ requires the evaluation of the reachable set $f(x)$ for all initial states $x \in \mathcal{X}$ in the worst case. However, the set of initial states $\mathcal{X}$ is uncountably infinite, which renders straightforward evaluation of $F(\mathcal{X})$ computationally intractable. To address this challenge, we take a sampling-based approach to reachability analysis.", L, 241, 323),
 T(r"Our method is based on the premise that evaluating the reachability of a carefully constructed finite subset $\mathcal{S} \subset \mathcal{X}$ of the initial states can serve as an accurate approximation of the ground-truth reachable set. The crux of our approach lies in generating a set $\mathcal{S}$ containing points that are sufficiently diverse, i.e., far-apart from one another, to ensure that that the union of the reachable sets $F(\mathcal{S})$ covers as much of $F(\mathcal{X})$ as possible. To this end, we use the GreedyPack [35] algorithm (Alg. 1) to construct a $\delta$-packing for $\mathcal{X}$, i.e., a subset $\mathcal{S} \subset \mathcal{X}$ such that the minimum pairwise distances between the points in $\mathcal{S}$ is greater than $\delta$ (see Sec. V), for an appropriate $\delta > 0$.", L, 326, 455),
 FIG("Algorithm 1", "algorithm-1", [309, 52, 566, 167]),
 T(alg1, R, 56, 161),
 H("### B. Approximately-optimal Algorithm", (48, 199), 472, 482),
 T(r"Our algorithm for approximately-optimal reachability analysis is shown as ApproximateReachability (Alg. 2). We give an overview of our method, which follows directly from the constructive proofs presented in Sec. V. In particular, for any desired approximation accuracy $\varepsilon \in (0, 1)$, our analysis establishes an appropriate value of $\delta$ to be used in constructing the $\delta$-packing for $\mathcal{X}$. Lines 1-4 of Alg. 2 generate upper bounds on the system-specific constraints, which are then used, along with $\varepsilon$, to set the appropriate $\delta$ parameter for the packing (Line 6). The $\delta$-packing, $\mathcal{S}$, is then constructed (Line 7) and the reachability of $\mathcal{S}$ is computed and returned (Lines 8-12).", L, 491, 621),
 FIG("Algorithm 2", "algorithm-2", [309, 176, 566, 430]),
 T(alg2, R, 180, 421),
 H("### C. Anytime, Asymptotically-optimal Algorithm", (48, 239), 638, 648),
 T(r"Our anytime, asymptotically-optimal algorithm is shown as AnytimeApproximateReachability (Alg. 3). The main idea behind our algorithm is that if Alg. 2 is iteratively invoked with increasingly small values of $\varepsilon$ as input, then the generated reachable sets will converge to the ground-truth reachable set as the number of iterations $i$ tends to infinity.", L, 656, 726),
 FIG("Algorithm 3", "algorithm-3", [309, 610, 566, 726]),
 T(alg3, R, 615, 720),
 H("## V. Analysis", (408, 467), 454, 462),
 T(r"We prove under mild assumptions that for any specified error $\varepsilon \in (0, 1)$, Alg. 2 generates an approximately optimal reachable set by computing the reachable sets of only finitely many initial states. As a corollary, we prove that the anytime variant of our approximation algorithm, Alg. 3, is asymptotically optimal. For brevity, some of the proofs have been omitted from this manuscript.", R, 473, 555),
 T("The intuition behind our analysis is as follows. Assuming that the reachability function is Lipschitz continuous, we expect similar states to map to similar reachable sets.", R, 557, 591),
]
notes = ("Compared with a 200 dpi render of the page and 150 dpi renders of the three algorithm crops. "
 "Problem 1 given a bold label and its statement written with LaTeX math (italic statement typography dropped); the extractor's two formula image items replaced: equation (1) is now a LaTeX display with \\tag{1}, and the second 'formula' box was really the section heading 'IV. METHOD', restored as a level-2 heading. "
 "Heading levels fixed (extractor had all as level 1): IV and V level 2, subsections A/B/C level 3; 'Algorithm 1/2' title lines were mis-detected as headings and are now part of the algorithm items. "
 "Algorithms 1-3: each kept as an image crop (rules, title, Input/Output and all numbered lines inside the crop; edges checked) followed by a transcription with one paragraph per printed line, the printed line numbers, and one '&emsp;&emsp;' per nesting level (loop bodies: Alg. 1 line 3, Alg. 2 lines 10-11, Alg. 3 lines 3-4; the comment-only lines 3 and 5 of Alg. 2 are printed flush right and are not nested); small-caps procedure names written in CamelCase (GreedyPack, ApproximateReachability, AnytimeApproximateReachability, UpperSurfAreaToVolume, UpperLipschitzConstant, UpperUniversalConstant, EvaluateReachability); comment marker ▷ written $\\triangleright$. Alg. 2 line 6 checked on the render: δ ← d((1 − ε)^{−1/d} − 1)/(αKc). Alg. 1 line 2 prints the loop condition with '≥ δ' (the text of Sec. IV-A says 'greater than δ' and the proof of Lemma 2 uses '> δ'); transcribed as printed. "
 "Reading order: left column (Problem 1, Sec. IV A-C) first; the floats of the right column are placed next to the subsections that describe them (Alg. 1 after IV-A, Alg. 2 after IV-B, Alg. 3 after IV-C) so that Alg. 3, printed at the bottom of the right column, does not interrupt the Sec. V paragraph that continues on page 4. "
 "Line-wrap hyphens repaired (straightforward, analysis, asymptotically, Assuming); 'ground-truth' compound hyphen kept. Authors' duplicated word 'to ensure that that the union' kept as printed. Hyperlinked numbers (Alg. 2, Alg. 3, Sec. V, Lemma 3, Theorem 7, [35]) checked against the render. No page number or running header.")
write(3, items, notes)
