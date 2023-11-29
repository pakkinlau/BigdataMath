- 5-10-2022: created

- Some embedded methods guide their [[Search algorithm|search]] by estimating changes in the [[objective]] value incurred by "making moves" in variable subset space.  (R1)
- Combined with greedy [[Search algorithm|search strategy]] ([[backward elimination]] or[[ forward selection]]) they yield nested subsets of variables. (R1)

![[Pasted image 20221005201734.png|200x200]]
- Figure: example of nested subset variables.



---
## Formulation

- Let $s$ the number of variables selected at a given algorithm step.  
- $J(s)$ the value of the objective function of the trained learning machine using such a variable subset.  (R1)
- Predicting the change in the [[objective]] is obtained by:  (R1) 
	- 1. Finite difference calculation: 
		- The difference between $J(s)$ and $J(s+1)$ or $J(s-1)$ is computed for the variables that are candidates for addition or removal. 
		- Exact differences can be computed efficiently at the time new data arrives, without retrainig new models for each candidate variable.
	- 2. Quadratic approximation of the [[Loss function|cost]] function:
		- This method was originally 1990 proposed to prune weights in [[neural network]].
		- In can be used for [[backward elimination]] of variables, via the pruning of the input variable weights $w_i$. 
		- A second order expansion of $J$ is made.
		- At the optimum of $J$, the first-order term can be neglected, and for variable $i$ to the variation $DJ_i = (1 /2 ) {\partial^2J \over \partial w_i^2} (Dw_i)^2$.
		- The change in weight $Dw_i = w_i$ corresponds to removing variable $i$.
	- 3. Sensitivity of the [[objective]] calculation
		- The absolute value or the square of the derivative of $J$ with respect to $x_i$ (or with respect to $w_i$) is used.

- Algorithms for these three 
- 1. Finite difference
	- (a) Linear least-square model
		- Gram-Schmidt orthogonalization procedure permits the performance of forward variable selection by adding at each step teh variable that most decreases the mean-squared-error.
		- Two papers in this issue are devoted to this technique (Stoppiglia et al., 2003, Rivals and Personnaz, 2003). 
	- (b) [[kernel method]]
		-  For other algorithms like kernel methods, approximations of the difference can be computed efficiently. 
		- Kernel methods are learning machines of the form $f(x) = \sum_{k=1}^m \alpha_k K(x,x_k)$, where $K$ is the kernel function, which measures the similarity between $x$ and $x_k$ (Schoelkopf and Smola, 2002). 
		- The variation in $J(s)$ is computed by keeping the $\alpha_k$ values constant. 
		- This procedure originally proposed for SVMs (Guyon et al., 2002) is used in this issue as a baseline method (Rakotomamonjy, 2003, Weston et al., 2003).
	- 2. Quadratic approximation (skip)
	- 3. Sensitivity of the objective function (skip)


---
## Reference
1. [[(Paper) 2003  18500 citation, Guyon and Elisseeff, An introduction to Variable and feature selection