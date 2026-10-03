from pagelib import *

items = [
    running_header(6),
    text("p0006-b001", [72.0, 99.0, 442.0, 121.0],
         "nomial features. By expressing the dyadic sum this way, we can apply the matrix inversion lemma to express the inverse of the empirical moment matrix as",
         join_previous="none"),
    text("p0006-b002", [67.0, 126.0, 405.0, 155.0],
         r"$$\hat{M}_{m,\sigma} = \left( \sigma^2 I + \tfrac{1}{N} Z Z^\top \right)^{-1} = \sigma^{-2}\left(I - Z\left(\sigma^2 N I + Z^\top Z\right)^{-1}Z^\top\right). \tag{2.4}$$"),
    text("p0006-b003", [72.0, 160.0, 442.0, 183.0],
         r"This expression for $\hat{M}_{m\sigma}$ allows us to rewrite the empirical inverse Christoffel function as"),
    text("p0006-b004", [67.0, 187.0, 432.0, 213.0],
         r"$$\hat{\kappa}^{-1}(x) = N \sigma_0^{-2} z_m(x)^\top z_m(x) - N \sigma_0^{-2} z_m(x)^\top Z \left(\sigma_0^2 I + Z^\top Z\right)^{-1}Z^\top z_m(x), \tag{2.5}$$"),
    text("p0006-b005", [71.0, 217.0, 442.0, 300.0],
         r"where we have made the change of variables $\sigma^2=\sigma_0^2/N$. The vector $z_m$ enters (2.5) only through the inner products $z_m(x_i)^\top z_m(x_j)$: The matrix $Z^\top Z\in\mathbb{R}^{N\times N}$ has elements $(Z^\top Z)_{ij}=z_m(x_i)^\top z_m(x_j)$, and the matrix-vector product $Z^\top z_m(x)$ has elements $(Z^\top z_m(x))_i=z_m(x_i)^\top z_m(x)$. By replacing the inner product $z_m(x_i)^\top z_m(x_j)$ with an arbitrary positive definite$^1$ function $k:\mathbb{R}^{n}\times\mathbb{R}^{n}\to\mathbb{R}$ and rescaling by a factor of $\sigma_0^{2}/N$, we obtain the kernelized variant of the empirical inverse Christoffel function,"),
    text("p0006-b006", [66.0, 305.0, 365.0, 331.0],
         r"$$\kappa^{-1}(x) = k(x,x) - k_D(x)^\top\left(\sigma_0^2 I + K\right)^{-1}k_D(x), \tag{2.6}$$"),
    text("p0006-b007", [71.0, 335.0, 289.0, 347.0],
         r"where $K\in\mathbb{R}^{N\times N}$ and $k_D(x)\in\mathbb{R}^N$ are defined as"),
    text("p0006-b008", [71.0, 358.0, 334.0, 369.0],
         r"$$K_{ij} = k(x_i,x_j), \qquad (k_D(x))_i = k(x_i,x). \tag{2.7}$$"),
    text("p0006-b013", [72.0, 666.0, 441.0, 694.0],
         r"Footnote 1: Here, and throughout the paper, we mean positive definite in the sense of reproducing kernel Hilbert spaces and kernel machines, which is that a square matrix $K$ with elements $(K)_{ij}=k(x_i,x_j)$ is a positive definite matrix."),
    heading("p0006-sec3-h", [72.0, 381.0, 247.0, 402.0], "## 3. Christoffel Function Estimators of Support"),
    figure("p0006-alg31", [250.0, 400.0, 435.0, 625.0], "Algorithm 3.1", "algorithm-3-1"),
    text("p0006-alg31-text", [256.0, 408.0, 427.0, 616.0], r"""
**Algorithm 3.1** To estimate a support set by a polynomial empirical inverse Christoffel function satisfying a classical PAC bound.

- inputs: random variable $X$ with support in $\mathcal{X}$; polynomial order $m\in\mathbb{N}_+$; PAC parameters $\epsilon,\delta\in(0,1)$; noise parameter $\sigma_0^2\in\mathbb{R}_{++}$;
- $N\gets \lceil\frac{5}{\epsilon}\left(\log\frac{4}{\delta}+\binom{n+2m}{n}\log\frac{40}{\epsilon}\right)\rceil$
- **for** $i\in\{1,\dotsc,N\}$ **do**
    - sample $x_i\sim X$
- **end for**
- $\hat{M}_{m,\sigma_0}\gets \sigma_0^2I + \frac{1}{N}\sum\limits_{i=1}^N z_m(x_i)z_m(x_i)^\top$
- $\alpha \gets \max_i z_m(x_i)^\top\hat{M}_{m,\sigma_0}^{-1} z_m(x_i)$
- $C(x)=z_m(x)^\top\hat{M}_{m,\sigma_0}^{-1}z_m(x)$;
- **return** $\mathbb{1}\{C(x)\le\alpha\}$;
"""),
    text("p0006-b009", [72.0, 381.0, 442.0, 654.0],
         "Algorithms 3.1 and 3.2 are procedures to estimate the support of a random variable with a sublevel set of an empirical inverse Christoffel function, where the only information needed from the random variable is a collection of iid samples. Algorithm 3.1 is designed to satisfy a classical PAC bound. This has the advantages of providing an *a priori* sample bound, and of admitting a fairly direct proof, which is given in Section 3.1. The essence of the proof is to demonstrate that the sublevel sets of a polynomial empirical inverse Christoffel function of a given order inhabit a concept class of known VC dimension. This argument is valid for polynomial Christoffel functions of any order, but it is generally not valid for kernelized Christoffel functions. Indeed, the classes of sublevel sets of certain kernelized empirical inverse Christoffel functions can have infinite VC dimension, so a classical PAC bound is not possible in general"),
]

save(6, items, r"""
Compared with the 130-dpi render and a 300-dpi crop of the algorithm box. First item continues the word 'poly-nomial' from page 5 (join_previous 'none'). Displays (2.4)-(2.7) taken from the authors' TeX and checked symbol by symbol; the four extractor formula images were replaced by LaTeX with \tag. Source errors kept as printed: (2.4) has $\hat{M}_{m,\sigma}$ on the left although the right-hand sides are its inverse (the text says 'the inverse of the empirical moment matrix'); the next line prints the subscript without comma, $\hat{M}_{m\sigma}$. (2.5)/(2.6) use $\sigma_0$ after the change of variables $\sigma^2=\sigma_0^2/N$. (2.7) is printed on one line with one number; written with \qquad between the two definitions. Footnote 1 (marker after 'positive definite', written $^1$) is printed at the foot of the page; it was placed after (2.7), at the end of Section 2, so that it does not interrupt the sentence that runs on to page 7. Section 3: the bold run-in title is written as ## heading. Algorithm 3.1 is a wrapped float in the right half of the column: kept as image crop 'algorithm-3-1' (all edges checked on the 300-dpi crop: top rule, caption, 9 statement lines, bottom rule; no body text inside) plus a transcription from the TeX source placed before the paragraph, so the paragraph reads continuously. The box has no printed line numbers; the transcription has one paragraph per statement and the for-loop body is marked with '&emsp;&emsp;' (one nesting level). Sample size line checked on the crop: $N\gets\lceil\frac{5}{\epsilon}(\log\frac{4}{\delta}+\binom{n+2m}{n}\log\frac{40}{\epsilon})\rceil$; the last two lines end with semicolons as printed. References resolved to printed values: 'Algorithms 3.1 and 3.2', 'Algorithm 3.1', 'Section 3.1', '(2.5)'. Line-wrap hyphens of the narrow wrapped column removed (Esti-mators, sub-level, Christof-fel, pro-viding, sub-level, in-verse, or-der, el-ements). The Section 3 paragraph continues on page 7 (join there). Omitted: running header (page number 6 and author short list).
""")
