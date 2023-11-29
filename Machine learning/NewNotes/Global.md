- 21-10-2022: created

- subset:
	- [[Global optimization]]
	- [[Global matrix factorization methods]]

- What is global?
	- In mathematics, local means compared to the things around it. Global means compared to everything possible in the domain-range.
	- Global optimization is distinguished from local optimization by its focus on finding the optima over the given set.
	- Finding an arbitrary local minimum is relatively straightforward by using classical local optimization methods.
	- Finding the global minimum of a function is far more difficult -- 
		- analytical methods are frequently not applicable.
		- The use of numerical solution strategies often leads to very hard challenges. 
	- eg: global minimization
		- Formally, given a continuous function $\Omega \subset R^n \rightarrow R$, with the global minima $f^*$,and the set of all global minimizers $X^*$ in $\Omega$, the standard minimization problem can be given as:  $$\underset{x \in \Omega}{\text{min}}f(x)$$