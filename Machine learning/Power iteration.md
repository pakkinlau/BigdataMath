- Power iteration is an iterative numerical method used in linear algebra to find the dominant eigenvalue and its corresponding eigenvector of a square matrix. 
- Eigenvalues and eigenvectors play a crucial role in various applications, such as analyzing dynamic systems, image processing, and machine learning algorithms. 
- Power iteration is particularly efficient for large matrices, as it doesn't require the explicit computation of the matrix's eigenvalues and eigenvectors.


---

Algorithm:

![[Pasted image 20231126163102.png]]

---

Setting:

Say we have Hermitian matrix $A \in \mathbb{m \times m}$ 
- We have a set of eigenvalues: $\lambda_1, \lambda_2, \dots, \lambda_m$ are real and distinct
- We have a set of orthonormal basis $q_1, q_2, \dots, q_m$ 

---
Power iterations only find the dominant eigenvector (the largest one, $\lambda_1$), not all the eigenvectors. 

---

**Key Steps of Power Iteration:**

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

---
How it works?

$v^{(0)} = a_1 q_1 + a_2 q_2 + \dots + a_m q_m$
- Because $A$ is Hermitian, we can always express this vector as some linear combination of the eigenvectors. 
$v^{(k)} = c_k (a_1 \lambda_1^k q_1 + a_2 \lambda_2^k q_2 + \dots ) = c_k \lambda_1^k (a_1 q_1 + (\frac{\lambda_2}{\lambda_1})^k q_2 + \dots )$
- where $c_k$ is normalization constant. 
- Every time $q_k$ hitting $A$ in the power iteration, because $Ax_k = \lambda_k x_k$, it produces $\lambda_k$. And $a_l$ and $q_k$ remain in there in each power iteration. 
- Remember, $\lambda_1 \geq \lambda_2 \geq \lambda_3 \dots$. So $\frac{\lambda_2}{\lambda_1}$, $\frac{\lambda_3}{\lambda_1}$, ... are smaller than $1$. And as $k$ goes to infinity, all other terms drops away. That leaves us $v^{(k)} = c_k \lambda_1^k a_1 q_1$. 

So power iteration guarantees it will converges to the largest eigenvalue $\lambda_1$. 



---
Q: why $w = Av_k$ can lead to vector converge to eigenvector (changing to the direction of eigenvectors)?
 
The equation $w = Av_k$ in the power iteration method leads to the vector changing its direction closer to the direction of the eigenvector due to the fundamental properties of eigenvalues and eigenvectors in linear transformations. Let me explain this in more detail:

1. **Eigenvalues and Eigenvectors:**
   - For a square matrix $A$, an eigenvector $v$ and its corresponding eigenvalue $\lambda$ satisfy the equation $Av = \lambda v$.
   - Geometrically, an eigenvalue-eigenvector pair represents a special case where the transformation $A$ only stretches or compresses the vector $v$ without changing its direction. The eigenvalue $\lambda$ represents the scaling factor, and $v$ represents the direction.

2. **Matrix-Vector Multiplication $Av_k$:**
   - When you multiply the current approximation $v_k$ by the matrix $A$, you are essentially applying the linear transformation represented by $A$ to the vector $v_k$.
   - In this context, $Av_k$ represents the transformation of $v_k$ by $A$, which may stretch, compress, or rotate $v_k$ depending on the eigenvalues and eigenvectors of $A$.

3. **Dominant Eigenvector and Eigenvalue:**
   - In power iteration, the algorithm is designed to find the dominant eigenvector, which corresponds to the largest eigenvalue in magnitude.
   - If $A$ has a dominant eigenvalue $\lambda_1$ with a corresponding eigenvector $v_1$, multiplying $v_k$ by $A$ magnifies the component of $v_k$ in the direction of $v_1$, as $Av_k$ aligns more with $v_1$.
   - With each iteration, the direction of $v_k$ becomes closer to the direction of $v_1$ due to the repeated application of $A$.

4. **Normalization Step:**
   - After multiplying $v_k$ by $A$ to get $w = Av_k$, the vector $w$ is normalized ($v_{k+1} = \frac{w}{\|w\|}$) to ensure that the vector doesn't grow infinitely.
   - Normalization adjusts the length of the vector while preserving its direction, focusing the algorithm on the direction rather than the magnitude.

5. **Convergence:**
   - Due to the repeated multiplication by $A$ and normalization, the components of $v_k$ corresponding to the dominant eigenvector $v_1$ become more prominent in each iteration.
   - The algorithm converges as $v_k$ gradually aligns its direction with the dominant eigenvector $v_1$.

In summary, the matrix-vector multiplication $Av_k$ allows the algorithm to emphasize the direction of the dominant eigenvector, leading to the vector $v_k$ changing its direction and converging closer to the direction of the eigenvector associated with the dominant eigenvalue.


---

**Working Principle:**

Power iteration relies on the fact that, after several iterations, the vector $v_k$ converges to the dominant eigenvector of the matrix $A$, and the corresponding eigenvalue approaches the dominant eigenvalue. The method takes advantage of the property that the dominant eigenpair of a matrix has the largest magnitude eigenvalue, making it easier to converge using iterative methods.

**Limitations:**

- Power iteration only finds the dominant eigenpair. It won't work well if you need multiple eigenpairs.
- It may converge to a different eigenpair if the matrix has repeated eigenvalues.
- The method may converge slowly if the ratio between the dominant eigenvalue and the next largest eigenvalue is close to 1.

**Applications:**

- **PageRank Algorithm:** Power iteration is used in the PageRank algorithm, which Google uses to rank web pages in its search engine results.
- **Principal Component Analysis (PCA):** Power iteration is employed to find principal components in PCA, a technique used for dimensionality reduction and data analysis.
- **Markov Chains:** Power iteration is utilized in analyzing Markov chains, which model random processes with specific transition probabilities between states.

In summary, power iteration is a fundamental technique in linear algebra, providing an efficient way to find the dominant eigenpair of a matrix, which has diverse applications in various fields.