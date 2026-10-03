def rep(fn, pairs):
    s=open(fn).read()
    for old,new,count in pairs:
        assert s.count(old)==count, (fn, old, s.count(old))
        s=s.replace(old,new)
    open(fn,'w').write(s)
rep('p15.py', [(r"\ge 1-\frac{k+1}{N+1}", r"\ge 1-\frac{k + 1}{N + 1}", 1),
               (r"> 0 \right) \ge \frac{N-k}{N+1}", r"> 0 \right) \ge \frac{N-k}{N + 1}", 1),
               (r"\text{Beta}(N+1-l,l),\quad l= \lfloor (N+1)\alpha\rfloor", r"\text{Beta}(N + 1 - l, l),\quad l= \lfloor (N + 1)\alpha\rfloor", 1),
               (r"\text{Beta}(N-k,k+1)", r"\text{Beta}(N-k, k + 1)", 1),
               (r"\text{Beta}(n+1-l, l), \quad l=\lfloor (n+1)\alpha \rfloor", r"\text{Beta}(n + 1 - l, l), \quad l=\lfloor (n + 1)\alpha \rfloor", 1)])
rep('p16.py', [(r"$k=\lfloor (n+1)\alpha-1 \rfloor$", r"$k=\lfloor (n + 1)\alpha-1 \rfloor$", 1),
               (r"ratio $I_x(n-k, k+1)=", r"ratio $I_x(n-k, k + 1)=", 1),
               (r"I_{1-\epsilon}(n-k, k+1)=", r"I_{1-\epsilon}(n-k, k + 1)=", 1),
               (r"\frac{\lceil n -(n+1)\alpha + 1 \rceil}{n}", r"\frac{\lceil n -(n+1)\alpha+1 \rceil}{n}", 1)])
