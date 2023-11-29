- Related: [[Linear transformation]]

- a. Each [[eigenvectors]] is multiplied by its [[eigenvalues]], when we multiply by $A$. 
	- Say $x = [x_1, x_2]$ and $\lambda = [\lambda_1, \lambda_2]$, 
		- the numerical value of $\lambda_k$ is larger than 1 
		- equal to 1 (steady state),
		- or smaller than 1  (decaying state), 
		- will affect how $x$ aggregate in the long rule multiplication. 
	- The example matrix that is [[eigenvectors]] is the steady state:
		- [[markov matrix]]


### Chained transformation 
- Consider a sequential times of transformation as $A^n x$.
	- Squaring transformation
		- When $A$ is squared, the eigenvectors stay the same. The eigenvalues are squared. 
- Meaning of value of $\lambda$:
	- $\lambda = 1$: Steady state that doesn't change. 
	- $\lambda < 1$: Decaying state  that virtually disappears. 
	- $\lambda = 0$: Trivial answer. 
	- $\lambda$ < 0: The direction is reversed 
- First we have $A$, its corresponding $\lambda$ and $x$  are determined by solving $Ax = \lambda x$.

### Telescoping process of linear transformation
- After having $\lambda$ value of $Ax = \lambda x$, we can see the left side of the equation is "before transformation", and the right hand side of the equation is "after transformation". We could see that the process is a telescoping action. If we apply $n$ times such transformation. It just meant $\lambda^n x$.
	- When $A$ is squared, the eigenvectors stay the same
	- When $A$ is squared, the eigenvalue are squared