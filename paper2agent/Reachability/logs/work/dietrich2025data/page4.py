from common import Page
p = Page(4)

p.text(r'clustering algorithm and choose the initial widths, $\sigma_i$, of our RBFs arbitrarily. We then use the SciPy Python library to solve this optimization problem using Sequential Least Squares Programming.', [54, 55, 299, 101], join_previous='space')
p.text(r'We take $\gamma = 0.25$ as the threshold of our RBF and consider 3000 samples. To apply the holdout method, we partition our data set into a training and test set, $N + M = 3000$, and take $\beta = 10^{-9}$. We compute reachable set estimates and $\epsilon$ a-posteriori for various combinations of $N$ and $M$, as seen in Tables I and II. Additionally, we investigate the difference in volume proxy of our reachable set estimates, to gauge the effect of training set sample complexity. For a comparative baseline, we examine the wait-and-judge technique over $N = 3000$ scenarios. When presenting the runtime of the holdout method, this measure includes the calculation of the reachable set over $N$ training samples, test-set generation of $M$ samples, and a-posteriori bound computation. In contrast, runtimes of the wait-and-judge method account for calculation of the reachable set over $N = 3000$ samples and a-posteriori bound computation using support scenarios.', [54, 103, 299, 293])

p.heading('#### 1) Duffing Oscillator:', [54, 295, 160, 305])
p.text(r'The first example is a reachable set estimation problem for the nonlinear, time-varying system with dynamics: $\ddot{x} = -\alpha y + x - x^3 + \gamma \cos(\omega t)$, with states $x, y \in \mathbb{R}$ and parameters $\alpha, \gamma, \omega \in \mathbb{R}$. This system is known as the Duffing oscillator, a nonlinear oscillator which exhibits chaotic behavior for certain values of $\alpha, \gamma$ and $\omega$, for instance $\alpha = 0.05, \gamma = 0.4, \omega = 1.3$. The set of initial states is the interval such that $x(0) \in [0.95, 1.05]$, $y(0) \in [-0.05, 0.05]$, and we take $\mu_{X_0}$ to be the uniform random variable over this interval. The time range is $[t_0, t_1] = [0, 100]$.', [54, 306, 299, 413])

p.caption(r'TABLE I. Duffing Oscillator: Calculation of $\epsilon$ for the Holdout Method using a Binomial Tail Inversion.', [54, 426, 299, 456])
rows = [
    ['Holdout Method:', 'Training (N)', 'Testing (M)', 'Vol(R̂(θ))', 'ε'],
    ['', 'N = 10', 'M = 2990', '0.57', '0.776'],
    ['', 'N = 50', 'M = 2950', '1.27', '0.147'],
    ['', 'N = 100', 'M = 2900', '1.44', '0.089'],
    ['', 'N = 1000', 'M = 2000', '1.64', '0.024'],
    ['', 'N = 1500', 'M = 1500', '1.54', '0.018'],
    ['', 'N = 2000', 'M = 1000', '1.56', '0.024'],
    ['', 'N = 2900', 'M = 100', '1.55', '0.214'],
    ['', 'N = 2950', 'M = 50', '1.53', '0.384'],
    ['', 'N = 2990', 'M = 10', '1.53', '0.874'],
    ['Wait and Judge:', 'N = 3000', '', '1.55', '0.035'],
]
p.table([49, 466, 295, 591], 'Table I', 'table-1', rows)
p.text('*Conversion note on Table I: the cells are copied as printed; the last two column headers are $\\mathrm{Vol}(\\hat{R}(\\theta))$ (the volume proxy) and $\\epsilon$, written in plain Unicode in the table. The first header cell, "Holdout Method:", is the row-group label of the nine rows below it, whose first cells are blank in print; the last row, "Wait and Judge:", is the wait-and-judge baseline, for which no testing set size is printed.*', [54, 592, 299, 602])

p.text(r'We calculate a reachable set estimate, using two radial basis functions, such that $m = 2$. We apply the holdout method, for combinations of $N$ and $M$, all of which exhibited a runtime of approximately 10-15 sec. When varying the size of the training set, we encounter a significant decrease in volume of our reachable set estimates when the training set has 1000 or less samples. Further, extreme values of $N$, such as $N = 10$ or $N = 2990$, provide similarly poor probability measures. As seen in Fig. 2, it is best to balance the size of $N$ and $M$. We observe that $N = 1500$, $M = 1500$ provides the smallest epsilon, $\epsilon = 0.018$. In contrast, the wait-and-judge approach exhibited a runtime of approximately 22 min and resulted in $\epsilon = 0.035$, with a volume proxy of $\mathrm{Vol}(\hat{R}(\theta)) = 1.55$.', [54, 605, 299, 734])

p.figure([318, 566, 552, 716], 'Figure 2', 'figure-2')
p.caption(r'Fig. 2. Duffing Oscillator: $\epsilon$ and $\hat{e}$ for various sizes of the holdout dataset.', [313, 724, 559, 732])

p.heading('#### 2) Quadrotor:', [313, 91, 380, 101])
p.text(r'The next example is for a nonlinear model of a quadrotor used as an example in [14], [30], [31]. The dynamics for this system are', [313, 102, 559, 124])
p.math(r'''\begin{aligned}
\ddot{x} &= u_1 K \sin(\theta), \\
\ddot{h} &= -g + u_1 K \cos(\theta), \\
\ddot{\theta} &= -d_0 \theta - d_1 \dot{\theta} + n_0 u_2
\end{aligned} \tag{13}''', [382, 126, 559, 177])
p.text(r'where $x$ and $h$ denote the quadrotor’s horizontal position and altitude in meters, respectively, and $\theta$ denotes its angular displacement. The system has 6 states, which we take to be $x, h, \theta$, and their first derivatives. The two system inputs $u_1$ and $u_2$ represent the motor thrust and the desired angle, respectively. The parameter values used (following [31]) are $g = 9.81, K = 0.89/1.4, d_0 = 70, d_1 = 17, n_0 = 55$. The set of initial states is the interval such that', [313, 179, 559, 271])
p.math(r'''\begin{aligned}
& x(0) \in [-1.7, 1.7], h(0) \in [0.3, 2.0], \theta(0) \in [-\pi/12, \pi/12], \\
& \dot{x}(0) \in [-0.8, 0.8], \dot{h}(0) \in [-1.0, 1.0], \dot{\theta}(0) \in [-\pi/2, \pi/2],
\end{aligned}''', [313, 272, 558, 309])
p.text(r'the set of inputs is the set of constant functions $u_1(t) = u_1$, $u_2(t) = u_2$ $\forall t \in [t_0, t_1]$, whose values lie in the interval $u_1 \in [-1.5 + g/K, 1.5 + g/K], u_2 \in [-\pi/4, \pi/4]$, and we take $\mu_{X_0}$ and $\mu_D$ to be the uniform random variables defined over these intervals. The time range is $[t_0, t_1] = [0, 5]$.', [313, 310, 559, 369])
p.text(r'We calculate a reachable set estimate using three radial basis functions, such that $m = 3$. We apply the holdout method, for combinations of $N$ and $M$, all of which exhibited a runtime of approximately 35-50 sec. When varying training set size, we observed very similar behavior as that depicted in Fig. 2 for the duffing oscillator. Extreme values of $N$ provide poor probability measures and less than 1000 training samples results in decreased volume of the reachable set estimate. In contrast, the wait-and-judge approach exhibited a runtime of approximately 5.5 hrs and resulted in $\epsilon = 0.051$, with a volume proxy of $\mathrm{Vol}(\hat{R}(\theta)) = 27.80$.', [313, 371, 559, 501])
p.text(r'**Sample Complexity.** In the section above, we utilize equal size datasets to compare the wait-and-judge and holdout method, highlighting the improved accuracy and computational cost of the holdout method. To demonstrate futher', [313, 502, 559, 546])

p.write('Compared the 220 dpi renders of all four quadrants with the text; prose and math taken from the authors\' TeX and checked on the render. First item continues the last paragraph of page 3 (join_previous: space). All numbers in the prose checked against the render: gamma = 0.25, 3000 samples, N + M = 3000, beta = 10^{-9}; Duffing: alpha = 0.05, gamma = 0.4, omega = 1.3, x(0) in [0.95, 1.05], y(0) in [-0.05, 0.05], [0, 100], m = 2, 10-15 sec, N = M = 1500 with epsilon = 0.018, wait-and-judge 22 min, epsilon = 0.035, Vol = 1.55; quadrotor: g = 9.81, K = 0.89/1.4, d_0 = 70, d_1 = 17, n_0 = 55, the six initial-state intervals, the two input intervals, [0, 5], m = 3, 35-50 sec, 5.5 hrs, epsilon = 0.051, Vol = 27.80. Table I transcribed as an 11 x 5 CSV (header, nine holdout rows, wait-and-judge row); every cell compared with the render and with the TeX tabular; printed precision kept. The printed caption is "TABLE I" on its own line above the caption text; given here as one caption item placed before the table as printed, followed by a conversion note on the row-group label. Formula images converted to LaTeX: (13) and the unnumbered display of the initial-state intervals. Run-in subsubsection titles "1) Duffing Oscillator:" and "2) Quadrotor:" are given as level-4 headings. Figure 2 (bottom of the right column; crop [318, 566, 552, 716] pt checked on a 200 dpi render: legend, both axes, all tick labels and the axis label M are inside, caption excluded) is placed with its caption after the Duffing paragraph that cites it, so that the "Sample Complexity." paragraph, which continues on page 5, stays last on the page. The paragraph "We calculate a reachable set estimate, using two radial ..." split by the column break was merged ("wait-and-judge" is a real compound). Authors\' wording kept: "futher" (typo), "duffing oscillator" in lower case, "1000 or less samples"; gamma denotes both the RBF threshold (0.25) and a Duffing parameter (0.4); theta denotes both the estimator parameter and the quadrotor angle; the Duffing dynamics are printed as a single equation for \\ddot{x} involving the second state y.')
