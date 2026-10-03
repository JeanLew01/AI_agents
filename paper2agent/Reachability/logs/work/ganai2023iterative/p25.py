from pagelib import *
P = 25
ROWS = [
    ["Hyperparameters for Safe RL Algorithms", "Values"],
    ["On-policy parameters", ""],
    ["Network Architecture", "MLP"],
    ["Units per Hidden Layer", "256"],
    ["Numbers of Hidden Layers", "2"],
    ["Hidden Layer Activation Function", "tanh"],
    ["Actor/Critic Output Layer Activation Function", "linear"],
    ["Lagrange multiplier Output Layer Activation Function", "softplus"],
    ["Optimizer", "Adam"],
    ["Discount factor γ", "0.99"],
    ["GAE lambda parameter", "0.97"],
    ["Clip Ratio", "0.2"],
    ["Target KL divergence", "0.1"],
    ["Total Env Interactions", "9e6"],
    ["Reward/Cost Critic Learning rate", "Linear Decay 1e−3 → 0"],
    ["Actor Learning rate", "Linear Decay 3e−4 → 0"],
    ["Lagrange Multiplier Learning rate", "Linear Decay 5e−5 → 0"],
    ["Number Seeds per algorithm per experiment", "5"],
    ["RESPO specific parameters", ""],
    ["REF Output Layer Activation Function", "sigmoid"],
    ["REF Learning rate", "1e−4 → 0"],
    ["CBF specific parameters", ""],
    ["ν", "0.2"],
    ["RCRL/FAC Note", ""],
    ["Lagrange Multiplier", "2-Layer, MLP"],
    ["", "(other algs just use scalar parameter)"],
]
t2 = table("p0025-b001", [110.0, 97.0, 499.0, 386.5], "Table 2", "supplementary-table-2", ROWS)
t2["asset_category"] = "supp_table"
items = [
    heading("p0025-b000", B(P, "p0025-b000"), "### D.3 Hyperparameters/Other Details"),
    t2,
    caption("p0025-b002", B(P, "p0025-b002"), r"Table 2: Hyperparameter Settings Details"),
    text("p0025-b002n", [111.0, 386.8, 498.0, 387.8],
         r"Conversion note for Table 2 (not part of the paper): the first row is the printed header. The rows 'On-policy parameters', 'RESPO specific parameters', 'CBF specific parameters' and 'RCRL/FAC Note' are bold group titles printed in the first column with an empty second column; horizontal rules separate the four groups. The last value is printed on two lines ('2-Layer, MLP' and, on the next line with an empty first column, '(other algs just use scalar parameter)'). The symbols in the cells are plain characters: the discount factor is $\gamma$, the CBF parameter is $\nu$, and the learning-rate schedules are printed as $1e{-3}\rightarrow 0$, $3e{-4}\rightarrow 0$, $5e{-5}\rightarrow 0$ and $1e{-4}\rightarrow 0$ (linear decay from the stated value to 0; the REF row has no words 'Linear Decay')."),
    text("p0025-b003", B(P, "p0025-b003"),
         r"To ensure a fair comparison, the primal-dual based approaches and unconstrained Vanilla PPO were implemented based off of the same code base [59]. The other three approaches were implemented based on [60] with the similar corresponding hyperparameters as the primal-dual approaches. We run our experiments on Intel(R) Core(TM) i7-8700 CPU @ 3.20GHz with $6$ cores. For Safety Gym, PyBullet, MuJoCo, and the multi-drone environments, each algorithm, per seed, per environment, takes $\sim4$ hours to train."),
    pageno(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 25 and with main.tex (D.3). Table 2 (hyperparameters; second and last table
of the paper, in the appendix): table item with category supp_table and asset name 'supplementary-table-2' (printed
label 'Table 2' kept). All 26 rows were retyped from the tabular source and read against the render cell by cell: the
extractor had merged the bold group titles with the following row, glued words ('Seedsper', 'Learningrate',
'algsjust') and scattered emphasis markers through the numbers ('0_._99', '1_e-_3'). Cells are plain strings with
Unicode characters (gamma, nu, minus sign, arrow) because the builder doubles backslashes inside table cells; a
clearly marked conversion note under the caption explains the group rows, the two-line last value and gives the
learning-rate schedules in LaTeX. Values read on the render: 256, 2, 0.99, 0.97, 0.2, 0.1, 9e6, 1e-3, 3e-4, 5e-5 (each
'-> 0'), 5 seeds, REF learning rate 1e-4 -> 0, nu = 0.2, '2-Layer, MLP'. The table bbox was tightened so that it ends
above the caption. Caption verbatim (no final full stop). Paragraph below the table: text from the source checked on
the render; math-mode numbers restored ('$6$ cores', '$\sim4$ hours', printed with a tilde relation sign before the 4);
'Intel(R) Core(TM) i7-8700 CPU @ 3.20GHz' as printed; citations [59], [60] checked. The lower half of the page is
blank (page break before D.4 in the source). Heading D.3 level 3. Omitted: printed page number 25.
""")
