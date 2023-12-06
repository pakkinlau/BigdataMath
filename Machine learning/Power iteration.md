- Idea 1: Power iteration is particularly efficient for large matrices, 
	- as it doesn't require the explicit computation of the matrix's eigenvalues and eigenvectors.
- Idea 2:Power iterations only find the dominant eigenvalue (the largest one, $\lambda_1$), not all the eigenvalues. 
- Idea 3: The terms after the dominant term diminishing
	$v^{(0)} = a_1 q_1 + a_2 q_2 + \dots + a_m q_m$
	- Where $v^{(0)}$ is a vector that represent our initial guess of the sequence of eigenvectors of the matrix. 
	- We can always express this vector as some linear combination of the eigenvectors. While we don't know the exact value of eigenvectors, coefficient $a_i$ does the job.
	After $k$ power iterations, our initial guess vector becomes: $v^{(k)} = c_k (a_1 \lambda_1^k q_1 + a_2 \lambda_2^k q_2 + \dots ) = c_k \lambda_1^k (a_1 q_1 + (\frac{\lambda_2}{\lambda_1})^k q_2 + \dots )$
	- where $c_k$ is normalization constant. 
	- Every time $q_k$ hitting $A$ in the power iteration, because $Ax_k = \lambda_k x_k$, it produces $\lambda_k$. And $a_l$ and $q_k$ remain in there in each power iteration. 
	Diminishing higher order terms, 
	- When $k \rightarrow \infty$, , $\lambda_1 \geq \lambda_2 \geq \lambda_3 \dots$. So $\frac{\lambda_2}{\lambda_1}$, $\frac{\lambda_3}{\lambda_1}$, ... are smaller than $1$. And as $k$ goes to infinity, all other terms drops away. That leaves us $v^{(k)} = c_k \lambda_1^k a_1 q_1$. 
- Idea 4: Stability analysis and convergence rate
	Error between initial 
	- In the previous step, we see that power iteration guarantees it will converges to the largest eigenvalue $\lambda_1$. 
	- So we have $||v^{(k)} - (\pm q_1)|| = O(| \frac{\lambda_2}{\lambda_1})|^k)$
		- where $||v^{(k)} - (\pm q_1)||$ represents our knowledge of "power iterations of $v^{(o)}$approximate to the first eigenvector of the matrix $A$"
		- The order of error is $|\frac{\lambda_2}{\lambda_1}|^k$ is because the largest error term is the second term. 
	- And we have $|\lambda^{(k)} - \lambda_1| =  O(| \frac{\lambda_2}{\lambda_1})|^{2k})$
		- Power iterations give as a resulting vector $v^{(k)}$ approximate the most dominant eigenvector. 
		- We can past this eigenvector to [Rayleigh quotient](Rayleigh%20quotient.md). In the expression of [Rayleigh quotient](Rayleigh%20quotient.md) we can see that there is two $v^{(k)}$ there. Therefore, the error order is double powered. 
- Idea 5: It is a linear convergence
	- When we say "linear convergence" in the context of power iteration, we are not referring to the shape of the convergence curve on a logarithmic chart. Instead, it indicates a specific convergence rate.
	- In power iteration, the convergence is considered linear because the error or difference between the estimated eigenvector and the true eigenvector decreases at a fixed rate with each iteration. More precisely, the error decreases by a constant factor at each iteration.

---

Algorithm:

![[Pasted image 20231126163102.png]]

**Key Steps of Power Iteration:**

Setting:

Say we have matrix $A \in \mathbb{m \times m}$ 
- We have a set of eigenvalues of matrix $A$ $\lambda_1, \lambda_2, \dots, \lambda_m$ are real and distinct
- We have a set of orthonormal basis $q_1, q_2, \dots, q_m$ of matrix $A$ 


1. **Initialization:** Start with a random vector $v_0$. This vector can be generated randomly or chosen based on domain knowledge.
	- Options of $v_0$:
		- a. Random generation - The choice of the initial vector $v_0$ does not affect the convergence of the power iteration to the dominant eigenpair 
		- b. Choosing from column space of $A$ - This can potentially lead to faster convergence, especially if the dominant eigenvector has significant components along the columns of the matrix
	- Condition:
		- $||v^{(0)}|| = 1$, select an initial guess $v^{(0)}$ with norm one.

2. **Iteration:**
	- **Matrix-Vector Multiplication:** Compute $w = Av_k$, where $A$ is the given square matrix and $v_k$ is the current approximation of the dominant eigenvector.
	- **Normalization:** Update the approximation of the dominant eigenvector: $v_{k+1} = \frac{w}{\|w\|}$. This step ensures that the vector remains normalized.
	- **Generating the next guess**: after normalizing the it, the resulting vector will be our next guess. 
	- [[Rayleigh quotient]]: To find the corresponding eigenvalue for that eigenvector we just obtained. 

3. **Convergence:** Repeat the iteration process until the dominant eigenvalue and its corresponding eigenvector converge to a stable solution. 
	- Typically, the algorithm converges to the dominant eigenpair (eigenvalue and eigenvector) of the matrix $A$.
	- I guess, to gauge whether it is stable, we compare $R(x_k)$ with $R(x_{k-1})$ .
