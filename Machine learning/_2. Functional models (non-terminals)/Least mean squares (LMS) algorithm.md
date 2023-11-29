- 26-9-2022: created

- What is [[Least mean squares (LMS) algorithm]]?
	- This is the chapter 1 of machine learning. [[Backpropagation]] that changes the parameters $\theta_i$ of the fitting equations. And [[Least mean squares (LMS) algorithm]] is one of way doing it. (R1) 

---
## Basic form (p.10 of R1)

- $$\theta := \theta - \alpha{\partial \over \partial \theta_j}{J(\theta)}$$, where $\alpha$ is learning rate. 
- Work out the partial derivative:$${\partial \over \partial \theta_j}{J(\theta)} = {\partial \over \partial \theta_j}{1 \over 2}(h_\theta(x) - y )^2 $$$$= 2 \ {1 \over 2}(h_\theta(x) - y ){\partial \over \partial \theta_j}(h_\theta(x) - y )$$$$= (h_\theta(x) - y ){\partial \over \partial \theta_j}( \sum_{i=0}^d \theta_ix_i - y )$$$$= (h_\theta(x) - y ) x_j^{(i)}$$
---
## With [[Feature map]] and [[kernel method]] (p50 of R1)

- In the context of [[Feature map]], a polynomial linear fitting equation can be xpressed as $\theta^T \phi(x)$.  (R1)
	- Let $\phi: R^d \rightarrow R^p$ be a feature map 
	- Let Attribute $x \in R^d$  (it means the attribute is a tuple containing d elements.)
	- Let features $\phi(x) \in R^p$.


- The [[Stochastic gradient descent]] equation (basic form):  (R1)$$\theta := \theta + \alpha \sum_{i=1}^n(y^{(i)}-h_\theta(x^{(i)}))x^{(i)}$$- Convert it to [[vector]] form:  (R1)$$\theta := \theta + \alpha \sum_{i=1}^n(y^{(i)}-\theta^Tx^{(i)})x^{(i)}$$
- Use $\phi: R_d \rightarrow R_p$ be a [[Feature map]] (Replace all occurrences of $x^{(i)}$ into $\phi(x^{(i)})$:  (R1)$$\theta := \theta + \alpha \sum_{i=1}^n(y^{(i)}-\theta^T \phi(x^{(i)})) \phi(x^{(i)}) \tag{1}$$
---
## LMS with the [[kernel method|kernel trick]]

#### Setup the problem: 

- Computational expensive when $\phi(x)$ is high dimensional.  (R1)
	- Suppose $x \in R^d$ 
	- Suppose the original input feature we have (1,$x$,$x^2$, $x^3$)
	- Suppose $\phi(x)$ be the vector that contains all the monomials with degree $\leq 3$  (R1)
	- In the following example, Say we choose the feature mapping $\phi(x)$ to be pair-wise monomial terms. So $\phi(x) \in R^{d^2}$. 
		- If our input dimension is 3, the monomial degree is 2, the mapped feature dimension would be 9. 
		- If D = 1000, our monomial degree is 2, now this is a million dimension. (R2)

	- so we have ($d^3$ elements): 
$$\phi(x) = \begin{bmatrix} 1 \\ x_1 \\ x_2 \\ \vdots \\x_1^2 \\ x_1 x_2 \\ x_1 x_3 \\ \vdots \\ x_2 x_1 \\ \vdots \\ x_1^3 \\ x_1^2 x_2 \\ 
 \vdots \\ \end{bmatrix}$$

 - [[computational cost]]:
	 - A probibitively long vector for computational purpose, when $d=1000$, the monomial degree i 3, each update requires at least $1000^3$ dimensional vector. (R1)
	 - It takes $O(n^m)$ to compute , which m is the monomial degree, n is the number of the original feature. 
	 - $d^3$ runtime per update and memory usage are inevitable. 


#### Using [[kernel method|kernel trick]]:
- $\theta$ can be represented as linear combination of vectors $\phi(x^{(1)}), \dots , \phi(x^{(n)})$  (R1)
- Recall $$\theta := \theta + \alpha \sum_{i=1}^n(y^{(i)}-\theta^T \phi(x^{(i)})) \phi(x^{(i)}) \tag{1}$$
 ^c7c1b0
- Case 1: At initiation, we set value $\theta = 0$, for simplification, the residual term reduce to 0.
	-  $\theta$ (expressed in tagged (1) [[#^c7c1b0]] equation) could be represented as:  (R1)$$\theta :=  \sum_{i=1}^n \beta_i \phi(x^{(i)}) \tag{2}$$, for some $\beta_1, \dots \beta_n \in R$, $$ \beta_i = \alpha (y^{(i)}-\theta^T \phi(x^{(i)}))$$, this result is useful for the derivation of case 2.  ^13e158

- Why this is a reasonable assumption? (R2)
	- Suppo


- Case 2: We don't assume $\theta = 0$:  (R1)
	- $\theta := \theta + \alpha \sum_{i=1}^n(y^{(i)}-\theta^T \phi(x^{(i)})) \phi(x^{(i)})$
	- $= \sum_{i=1}^n \beta_i \phi(x^{(i)}) + \alpha \sum_{i=1}^n(y^{(i)}-\theta^T \phi(x^{(i)})) \phi(x^{(i)})$
	- $= \sum_{i=1}^n ( \beta_i + \alpha (y^{(i)}-\theta^T \phi(x^{(i)})) )  \phi(x^{(i)})$, which the coefficient of this is new $\beta_i$.
	- $=\sum_{i=1}^n \beta_i \phi(x^{(i)})$ 
- We derive the new updating rule for $\beta_i$: $$\beta_i := \beta_i + \alpha (y^{(i)}-\theta^T \phi(x^{(i)}))$$
- Now we still have $\theta$ in the expression, we substitute $\theta$ with equation (tagged (2)[[#^13e158]]) case 1 result to the expression we get:  (R1)$$ \forall i \in \{1,\dots,n\},
 \beta_i := \beta_i + \alpha (y^{(i)}-( \sum_{j=1}^n \beta_j \phi(x^{(j)}))^T \phi(x^{(i)}))$$
 - You might notice why there is $\forall i$ at the front of the equation, it is because there are a series of $\beta_i$.  (R1)
 - We often rewrite $\phi(x^{(j)}))^T \phi(x^{(i)})$ as $\langle \phi(x^{(j)})) ,  \phi(x^{(i)})  \rangle$ to emphasize that it is the [[dot product]] of the two feature [[vector]].  (R1)
 - Now we tranlated the batch gradient descent algorithm into an algorithm that updates the value of $\beta$ iteratively.  (R1)

- Computing $\langle \phi(x^{(j)})) ,  \phi(x^{(i)})  \rangle$ with the feature map $\phi$ can be effieicent and does not require $\phi(x^{(i)})$ explicitly.  (R1)


---

- With matrix derivatives:
	- ![[Pasted image 20220926095936.png]]
	- ![[Pasted image 20220926095942.png]]

- LMS with kernel trick. 
	- Updating feature with LMS algorithm can become computationally expensive when the features $\phi(x)$ is high-dimensional. Consider $\theta := \theta + \alpha(y^{(i)}-\theta^T\phi(x^{(i)}))\phi(x^{(i)})$, the last term indicates 
	- With kernals, we will not need to store $\theta$ explicitly, and the runtime can be significantly improved. 
	- The strategyt is to implicity represent the p-dimensional vector $\theta$ by a set of coefficients $\beta_1, \dots, \beta_n$. Towards doing this, we derive the udate rule of the coefficient of them.


---
## Reference: 

1. [[(Course) CS229 Machine learning]] lecture notes 
2. CS229 youtube https://www.youtube.com/watch?v=8NYoQiRANpg&list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU&index=7