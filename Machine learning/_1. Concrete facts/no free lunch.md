- 7-10-2022: created

- by David Wolpert -- "averaged over all optimization problems, without re-sampling all optimization algorithms perform equally well." (R1)
	- "Roughly spearking, we show that for both static and time dependent optimization problems, the average performance of any pair of algorithms across all possible problems is exactly identical. (R2)
	- This means in particular that if some algorithm $a$ 's performnace is superior to that of another algorithm $a_2$ over time over some set of optimization problems, then the revenue must be true over the set of all other optimization problems. '"(R2)

the example would be there are a toy universe that exists for exactly two days and on each day contains exactly one object, and it has exactly four possible histories "(square, triangle)", "(square, square)", "(triangle, triangle)", "(triangle, square)". Any prediction strategy  that succeeds for history 2, will fail on history 1. 
	- If all histories are equally likely, then any prediction strategy will score the same, with the same accuracy rate of 0.5.
- In computational complexity and [[optimization]] the no free lunch theorem is a result that states that for certain types of mathematical problems, the [[computational cost]] of finding a solution, averaged over all problems in the class, is the same for any solution method.
	- which suggest "no method offers a short cut".
	- This is under the assumption that the [[General space]] is a probability density function. It does not apply to the case where the search space has underlying structure that can be exploited more efficient;y (eg: Newton's method in optimation) that random search or even has closed-form solutions (eg)

- Theorem 1: Hypothesize [[objective]] that do not change while [[optimization]] is in progress.
	- For any algorithms $a_1$ and $a_2$, at iteration step m.
$$\underset{f}{\sum}P(d_m^y|f,m,a_1)=\underset{f}{\sum}P(d_m^y|f,m,a_2)$$, where $d_m^y$ dentoes the [[ordered set]] of size $m$ of the [[Loss function|cost]] value $y$ associated to input values $x \in X, f: X\rightarrow Y$ is the function being optimized and $P$ is the conditional probability of obtaining a given sequence of [[Loss function|cost]] values from algorithm $a$ run $m$ times on function $f$.



---
## Reference
1. - wiki tab: No free lunch in [[Search algorithm|search]] and [[optimization]].
2. [[(Paper) 1996 Wolpert, No free lunch theorems for optimization]]