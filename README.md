## Dynamic Programming to find minimum sum combinations

I completed this project as part of coursework for the AI & ML module taught in semester 1. 

The function `minsumcomb(x,M)` aims to search for the minimum sum combination of size `M` given a list of integers.
It takes in a list of integers `x` and a positive integer `M` and returns all iterations of the Bellman recursion below:

```math
\begin{align*}
S^{\star}_{0,0} &= 0 \\
S^{\star}_{0,m} &= \infty \\
S^{\star}_{n,0} &= S^{\star}_{n-1,0} \\
S^{\star}_{n,m} &= \min \left( S^{\star}_{n-1,m},\; S^{\star}_{n-1,m-1} + x_n \right)
\end{align*}
```

### Skills demonstrated
- implementation of dynamic programming and Bellman recursion
- a modular implementation of an algorithm as a single Python function
- application of object oriented programming
