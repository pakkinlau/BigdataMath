---
alias: SIND, SINDy
---

Considers $\frac{d}{dx} x = f(x)$, we seek the following approximation of $f(x)$ 
$f(x) \approx \sum_{k=1}^p \theta_k (x) \xi = \Theta(x) \xi$, with the fewest nonzero terms in $\xi$.

Breakdown of the terms:
- $f(x)$: the unknown function representing the derivative of $x$ with respect to some variables.
- $p$: denotes the number of terms we are considering for the approximation
- $\theta_k (x)$: function of $x$ that we use to construct the approximation.
- $\xi$: coefficient vector with the fewest nonzero elements, indicating the importance or weight of each $\theta_k(x)$. 
- $\Theta(x)$: a matrix that collects the functions $\theta_k(x)$ evaluated at $x$. 

Objective:
- The objective of SINDy is to find a sparse set of terms in $\xi$ (ideally with many zeros) that best approximate $f(x)$. This allows for a simplified representation of the dynamics governing the system, revealing the most influential components contributing to the derivative of $x$ with respect to $x$.


---

Compose $\Theta(x)$ 

- figure:
	- Initiation
		- Say we have Lorenz attractor toy model
		- we have a set of vectors $x,y,z$, and $\dot x, \dot y, \dot z$
		- We collect data into column vectors, but this time across row it is t-axis.
	- Construction:
		-  Construct vectors of all possible polynomial nonlinearities, up to order 5.
		- apply sparse regression to find which linear combination of these nonlinearity terms represent $\dot x, \dot y, \dot z$. 
	- Sparse regression for each variable
	- Putting the combinations of weights into $\Xi$. 
![[Pasted image 20231112032012.png]]
![[Pasted image 20231112033607.png]]
![[Pasted image 20231112033637.png]]


