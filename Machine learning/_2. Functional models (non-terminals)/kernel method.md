---
alias: [kernel trick]
---

- 5-10-2022: created

- Kernel enable us to work with high dimensional feature very quickly. 

- Feature of kernel trick:
	- 1. Write algorithm in terms of $\langle x^{(i)} , x^{(j)} \rangle$ (or $\langle x , z \rangle$. 
	- 2. mapping: $x \mapsto \phi(x)$ 
		- x: we might have a 1D or 2D feature
		- $\phi(x)$: we could have 100,000 dimensional, or infinite dimensional. 
		- eg: predicting house prices: expand house size x, we can take this 1D feature into a high dimensional feature vector with x, $x^2$, $x^3$, ... 
		- eg: `[x1 , x2]` , we can map it into `[x1, x2, x1x2, x1^2, x1^2 x2 ......]`
	- 3. Find a way to compute $K(x,z) = \phi(x)^T\phi(z)$.
		- you can compute the [[dot product]] between X and Z, even when X and Z are high dimensional. 
	- 4. Replace $\langle x,z \rangle$ in algorithm with $K(x,z)$.
	- 5. We are gonna prove $K(x,z) = \phi(x)^T\phi(z)$ can be computed as $(x^T z)^2$, which $\phi(x)$ is the expanded monomial terms, $x$ is the original input vector  (The proof is on below.)
		- The cool thing is, $x^T \in R^n$ and $z \in R^n$, so $(x^T z)^2$ is a $O(n)$ computation. It is because a product of two n-dimensional vectors, and then you get a real number. You take that number, you just square the number. So it is $O(n)$ computation.
	- 6. Now we have $K(x,z) = (x^Tz)^2$, we expand it to be $K(x,z) = (x^Tz + c)^2$, where $c \in R$. 
		- If you add $x^Tz +c$, the corresponding $\phi(x)$ would have $x_1,x_2,x_3,\dots$. and there is a corresponding weighting $\sqrt{2c}$ and a constant term $c$.
	- 7. We can further expand $K(x,z)= (x^Tz)^d$, which is also cost $O(n)$ [[computational cost]]. 
		- Notice that $\phi(x) = \begin{pmatrix} n+d \\ d \end{pmatrix}$ contains all features of monomials up to order d. say the number of feature inputs n = 30, the degree of monomials d = 5, and this will be a fifth degree thing eg: ($x_1, x_3, x_7, x_{17}, x_{29}$)
		- Roughly there is $(n+d)^d$ terms in the $\phi(x)$, but your computation doesn't blow up exponentially even as $d$ increases.  



![[Pasted image 20221009120203.png|200x300]]
- Figure: showing the last four terms, corresponding the step 6 added term c.



---
- Proof:

- (a) Setting up the environment:
	- Say we have a linear function $y = \theta_3 x^3 + \theta_2 x^2 + \theta_1 x + \theta_0$
	- the function could be represented as $\theta^T\phi(x)$, $\theta = \begin{bmatrix} \theta_3 \\ \theta_2 \\ \theta_1 \\ \theta_0 \end{bmatrix}$
	- $x = \begin{bmatrix} x^3 \\ x^2 \\ x \\ 1 \end{bmatrix}$
- In kernel tricks we expand the original $\phi(x)$ (later we name it as $x \in R^n$) to a higher dimensional term by using monomials, such that tha mapping would be $x \mapsto \phi(x)$ and $\phi(x) \in R^{n^m}$ would be: $$\phi(x) = \begin{bmatrix} 1 \\ x_1 \\ x_2 \\ \vdots \\x_1^2 \\ x_1 x_2 \\ x_1 x_3 \\ \vdots \\ x_2 x_1 \\ \vdots \\ x_1^3 \\ x_1^2 x_2 \\ 
 \vdots \\ \end{bmatrix}$$
 ^6f9b04
- (b) Computation 
$\begin{align*} (x^T z)^2 &= (\sum_{i=1}^n x_i z_i)(\sum_{i=1}^n x_i z_i) \\ &=  \sum_{i=1}^n \sum_{i=1}^n (x_i x_j) (z_i z_j) \\ &= \phi(x)\phi(z)  \end{align*}$  
(The first step see [[vector#^cb4cf6]], the second step see [[summation sign]])

---
- (R1) Video - SVM with a polynomial kernel visualization

- The intuition of kernel is that projecting the data points from lower dimensions to higher dimension (it could be very very large, like 1 trillion dimension) surface , and in that higher dimension surface, we find a linear decision boundary in that space (which is going to be a hyperplane). And in the original feature space, you found a very non-linear decision boundary. 

![[Pasted image 20221009124815.png|200x150]]![[Pasted image 20221009124907.png|200x150]]
![[Pasted image 20221009125000.png|200x150]]
- Say we have a learning algorithm separate the blue dots form red dots. It can't be separated with a straight line. 
- If you use $\phi$ to throw these points into higher-dimensional space, 
- And in this 3D space, you can find a plane that separate the blue dots and the red dots. 
- If you look back the original space, then your linear classifier actually defines that elliptical decision boundary. 
---
## Some intuitions of kernels (R1)

- In one perspective (projecting data into higher dimensional space) If $x$, $z$ are "similar" (close to each other), then $K(x,z) = \phi(x) \phi(z)$  presumeably should be large; and if they are dissimilar, then $K(x,z)$ should be small. 
- Another perspective, If we treat $\phi(x)$ and $\phi(z)$ as vectors, their [[dot product]] is large when their direction is close to each other. 
![[Pasted image 20221009130133.png]]

---

- If you think of kernels as similarity measure of a function, the right hand side of the following expression is that if $x$ and $z$ are very close, that would be $e^0$ which is about 1. But if they are very far apart, that should be very small. 
$$K(x,z) = exp(-{||x-z||^2 \over 2\sigma^2})$$

- We can use the RHS as kernel function if and only if there exists some $\phi$ such that $K(x,z) = \phi(x)^T \phi(z)$.
	- This puts constraints on what functions could be a kernel.
		- 1. It is better to have $K(x,z) = \phi(x)^T \phi(x) \geq 0$, because inner product of a vector with itself had better be non-negative. (??????????????????)

---
## Necessary conditions for valid kernels 

- Let $\{ x^{(1)}, \dots, x^{(d)} \}$ be any d points. 
- Let $K \in R^{d \times d}$ , "kernel matrix", "gram matrix".
	- So $K_{ij} = K(x^{(i)},x^{(j)})$ , so you have d points, and the kernel function apply to every pair of points and put them in a matrix, in a big d x d matrix. 

- See more in lecture notes. 




---



- In [[machine learning]], kernel machine are a class of [[algorithm]] of algorithms for [[pattern]]. (wiki)
- The best known member of [[kernel method]] is [[Support vector machine]]. (wiki)

- [[Feature map]]

- [[regression]]

- The [[kernel method|kernel trick]] reduces the computation time of [[Least mean squares (LMS) algorithm]] from $O(n^3)$ to $O(p)$.  


---
## Reference

1. CS229 youtube https://www.youtube.com/watch?v=8NYoQiRANpg&list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU&index=7