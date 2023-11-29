---
tag: index
---


- Textbook:
	- Part 1: Numerical linear algebra by Trefethen and Bau (1997): https://www.doc88.com/p-0146438184053.html
	- Part 2: Data-driven modeling and scientific computation by Kutz (2013): 
		- downloaded into local folder
		- also can be found: https://www.doc88.com/p-2816742355875.html
- Homework:
	- [[homework 1]]

---
# Part 1

## Concepts mentioned in the subject

- lecture 3


- Not mentioned:
	- [[Eigenvalues and eigenvectors]]
- Lecture 1
	- [[matrix]]
	- [[Matrix-matrix multiplication]]
	- [[Matrix-Vector Multiplication]]
	- [[column space]]
	- [[rank]]
	- [[invert|inverse]]
	- [[column space|image]]
	- [[span]] / $\langle \cdot \rangle$
- Lecture 2
	- [[hermitian matrix]]
	- [[dot product|inner product]]
		- Euclidean length
		- Cosine of the angle $\alpha$ between $x$ and $y$
	- [[Orthogonal vector]]
	- [[Vector decomposition]]
	- [[unitary matrices|unitary matrix]]
	- [[Vector decomposition]]
	- [[adjoint|adjoint matrix]]
	- [[hermitian matrix]]
	- [[unitary matrices|unitary matrix]]
	- [[symmetric matrix]]
- Lecture 3
	- [[Vector Norm]]
		- 3 properties of "norm" being a "norm"
		- p-norm
		- infinity norm 
	- [[weighted p-norms]]
	- [[Induced matrix norm]]
	- [[Frobenius Norm]]
	- [[cauchy-schwarz inequalities and holder inequalities]]
	- Multiplicative properties in studying norms:
	- Inequalities in studying norms:
		- inequalities that comparing [[Vector Norm]] where $n$ is $0,1,2,\infty$ etc 
		- triangular inequalities
			- [[cauchy-schwarz inequalities and holder inequalities]] (these inequalities is useful when proving some norms are vector norms)
	- [[general matrix norm]]
	- [[invariance under unitary matrix multiplication]]
- Lecture 4
	- [[singular vectors]]
	- [[singular matrix]]
	- [[singular value decomposition]]
- Lecture 5
	- [[Change of basis]]
- Lecture 6
	- [[Idempotence]]
	- [[projector]]
	- [[Projection]]
	- [[Projection formula]]
	- [[Orthogonal Projector]]
- [[invariance under unitary matrix multiplication]]
- Lecture 6
	- Check matrix $K$ is a projector: $K^2 = K$
	- Check matrix $K$ is a orthogonal projector: $K^* = K$, of it is not orthogonal, then it is oblique projector.
- Lecture 7
	- [[Orthogonalization]]
	- [[successive spaces]] spanned by columns
	- Notation of [[span]]
	- [[Gram-Schmidt coefficient $r_{ij}$]]
	- [[Unstable Gram-Schmidt process]]
		- (So we should also introduce stable Gram-Schmidt later)
	- [[Reduced QR decomposition]]
	- [[Full QR decomposition]]
- Lecture 8
	- [[vector decomposition]]
	- [[Gram-Schmidt coefficient $r_{ij}$]]
	- [[projection operator (QQT)]]
	- [[Gram-Schmidt projection]]
	- [[Modified Gram-Schmidt iteration]]
	- [[Operation count]]
	- [[Triangular orthogonalization]]
- Lecture 9
	- MATLAB implementation of Gram Schmidt algorithm 
		- Compute classical Gram-Schmidt
		- Compute modified Gram-Schmidt
	- Numerical loss of orthogonality
- Lecture 10
	- [[Household triangularization]]
	- Orthogonal triangularization (looks similar to the concept in lecture 8??)
	- [[Household reflector]]
	- [[Householder QR factorization]]
	- [[reflection operator]]
	- [[outer product]]
- Lecture 11
	- [[Least Squares]]
	- [[Data fitting]]
	- [[residual vector , error]]
	- [[Normal equation]]
	- [[Pseudo-inverse matrix|Pseudo-inverse]]
	- Three methods to find (2 norm) of linear equation $||b - Ax||_2$ 
		- [[Normal equation]]
		- [[Reduced QR decomposition|QR factorization]]
		- [[Singular value decomposition|SVD]]
- Lecture 12
	- [[Absolute condition number]]
	- [[Relative condition number]] (more useful)
	- Ill-conditioned
	- [[Condition of matrix-vector multiplication]]
	- [[Condition of a system of equations]]
- Lecture 14
	- [[Stability]]


- Lecture 24
	- [[Eigenvalue problems]]
		- [[Eigenvalue Decomposition]] ($A = X \Lambda X^{-1}$)
	- [[eigenspace]]
	- Multiplicity
		- [[geometric multiplicity]]
			- [[characteristic polynomial]]
		- [[algebraic multiplicity]]
	- [[Similarity transformation]] ($A \mapsto X^{-1}AX$)
	- [[Defective matrix]]
	- [[diagonalization]] ($A = Q \Lambda Q^*$)
		- [[unitary diagonalizable]]
	- [[Schur factorization]] ($A = QTQ^*$)
- Lecture 25 - Overview of eigenvalue algorithms 
	- 3 eigenvalue revealing factorizations / algorithms
		- [[diagonalization]] ($A = Q \Lambda Q^*$)
		- [[unitarily diagonalization]]
		- [[Schur factorization]]
	- Two phases of eigenvalue computations
		- Transform the matrix to [[upper Hessenberg]]
		- Generate a sequence of upper Hessenberg matrices that converges to  an upper triangular matrix
- Lecture 26 - Reduction to Hessenberg form
	- Discuss why [[Household triangularization]] cannot approximate triangular matrices
	- [[Hessenberg form]]
	- [[Reduction to Hessenberg form]]
- Lecture 27 - Classical methods for eigenvalues 
	- (Why we assume $A$ is real and symmetric?)
	- Classical methods for eigenvalues
		- Phase 1: [[tri-diagonal matrices]]
		- Phase 2: [[diagonal matrix]]
	- [[Rayleigh quotient]]
	- [[Power iteration]] (it does not require the matrix $A$ to be real and symmetric)
		- If $A$ is a full matrix, the count is $O(m^2)$
		- If $A$ is tri-diagonal, the count is $O(m)$ 
	- [[Inverse iteration]]
	- [[Rayleigh quotient iteration]]
		- If $A$ is a full matrix, the count is $O(m^3)$
		- If $A$ is tri-diagonal, the count is $O(m)$
- Lecture 28 - QR algorithm
	- [[QR algorithm]]
	- [[Simultaneous iteration]]
	- [[Convergence of QR algorithm]]
- Lecture 29
	- QR iteration with shifts
	- It seems the teacher skipped this part
- Lecture 31
	- Computing the SVD
	- A different eigenvalue problem
	- It seems the teacher skipped this part

---
# Proof of theorems
- Lecture 2:
	- The vector in an orthogonal set $S$ are linearly independent. (The reverse direction is not true)
- Lecture 3:
	- prove the vectors in an orthogonal set $S$ are linearly independent
		- if vectors in $S$ are not independent, then some $v_k \in S$ can be expressed as a linear combination of other vectors $v_k = \sum_{i - 1, i \neq k}^n c_i v_i$
		- recall $||v_k||^2 = v_k^* v_k$, we have $v_k^*(\sum_{i - 1, i \neq k}^n c_i v_i) = 0$ , which leads to contradiction of "Set $S$ are linearly independent."
	- prove some norms are [[Vector Norm]], with the properties of it.
	- prove  [[weighted p-norms]] are [[Vector Norm]], with the properties of vector norm
	- prove matrix 1-norm (give up) $||Ax||_1 = \underset{1 \leq j \leq n}{max} ||a_j||_1$ (which means the norm of Ax is the largest column vector norm of $A$)
	- prove For any $A$ and unitary $Q \in \mathbb{C}^{m \times m}$, we have $||QA||_2 = ||A||_2$, $||QA||_F = ||A||_F$
		- $||QA||_2 = \underset{x \in C^n , x \neq 0}{sup} \frac{||QAx||_{m}}{||x||_{(n)}}$ (by definition)
		- $= \underset{x \in C^n , x \neq 0}{sup} \frac{||Ax||_{m}}{||x||_{(n)}}$ (by showing $QAx = Ax$, by using the property of unitary matrix)
		- $= ||A||_2$
		- Similarly, $||QA||_F = ||A||_F$
- Lecture 4:
	- prove all eigenvalues of $A$ are real, if $A \in \mathbb{C}^{m \times m}$ is Hermitian.
		- strategy:
			- construct $\lambda v^*v  = \lambda v^*v$ to show
	- prove that if $A$ is Hermitian, then all eigenvalues of $A$ are $1$ or $-1$
		- strategy: 
			- construct $x = \lambda^2 x$ to show
	- prove the square of singular values of $A$, is the square of eigenvalues of $A$
		- strategy:
			- expand the SVD of $A^2$, and the eigen-expression of $A^2$ to see that. 
	- prove that if $A$ is Hermitian, then $\sigma_1 = \dots = \sigma_m = 1$
		- strategy:
			- use $||A||_2 = \sigma_1 = \underset{j}{max}\ \sigma_j$   to prove the first term
			- Use $||A^*||_2 = ||A^{-1}||_2 = ||\Sigma^{-1}||_2 = \sigma_m$ to prove the last term (knowledge depends on: lecture 3)
- Lecture 5:
	- $||A||_2 = \sigma_1$
		- 1. Compute the eigenvalues of $A^TA$. These eigenvalues will be non-negative.
		- 2. Compute the singular value of $A$ and order them in non-increasing order.
		- 3. The 2-norm ($||A||_2$) of $A$ is the square root of the largest eigenvalue $A^TA$. 
		- So $||A||_2 = \sigma_1$
		- $||A - A_v||_2 = \underset{B \in \mathbb{C}^{m \times n}, rank(B) \leq v}{inf} ||A - B||_2 = \sigma_{v+1}$
			- This is Eckart-Young-Mirsky theorem
			- Left hand side:
				- 2-norm of the error matrix: $||A - A_v||_2 = \sigma_{v + 1}$
			- Right hand side:
				- $v+1$ th singular value $\sigma_{v+1}$
			- Inf:
				- Infimum, the greatest lower bound of a set. 
	- The rank of $A$ is $r$, the number of nonzero singular values. 

- Lecture 6:
	- A projector $P$ is orthogonal if and only if it is Hermitian ($P = P^*$).
		*Proof:*
		*a. $P = P^*$*
		Assuming $P = P^*$, where $P$ projects $\mathbb{C}^m$ onto $S_1 = \text{range}(P)$ along $S_2 = \text{null}(P) = \text{range}(I - P)$:
		- Let $s_1 \in S_1$ and $s_2 \in S_2$. Then $s_1 = Px$ and $s_2 = (I - P)y$.
		- $s_1^* s_2 = (Px)^* (I - P)y = x^*P^* (I - P)y = x^*(P - P^2)y$ (since $P$ is Hermitian) $= x^*(P - P)y = 0$.
		- Thus, $S_1$ and $S_2$ are orthogonal when $P = P^*$.
		*b. $P$ is Orthogonal*
		Assuming $P$ is orthogonal, projecting onto $S_1$ along $S_2$ where $S_1 \perp S_2$:
		- Let $\{q_1, q_2, \dots, q_m\}$ be an orthonormal basis for $\mathbb{C}^m$, with $\{q_1, q_2, \dots, q_n\}$ as the basis for $S_1$ and $\{q_{n+1}, \dots, q_m\}$ as the basis for $S_2$.
		- For $j \leq n$, $Pq_j = q_j$. For $j > n$, $Pq_j = 0$.
		- Let $Q$ be the unitary matrix with columns $q_j$. $PQ = \begin{bmatrix} q_1, \dots, q_n, 0, \dots \end{bmatrix}$.
		- $Q^*PQ$ is a square singular value matrix with its first $n$ diagonal elements as $1$ (since $q_k^*q_k = 1$) and the rest $0$.
		- Rearranging, $P = Q\Sigma Q^*$.
		- Taking the conjugate transpose of $P$, $P^* = (Q\Sigma Q^*)^* = Q \Sigma Q^* = P$.
- Lecture 7:
	- Unique QR decomposition
		- Let $A \in \mathbb{R}^{m \times m}$ be a matrix of full rank, and suppose there are two QR factorizations of $A$, i.e. $A = Q_1R_1 = Q_2R_2$ such that the entries of main diagonals of $R_1$ and $R_2$ are all positive. Show that $Q_1 = Q_2$ and $R_1 = R_2$. 
			- Answer: 
			- Let $A = Q_1 R_1 = Q_2 R_2$. So we have $Q_2^T Q_1 = R_2R_1^{-1}$
			- The left hand side is orthogonal, while the right hand side is upper triangular.
			- We have $R$ is an non-negative upper triangular matrix here. And like previous question, $R^T$ and $R^{-1}$ must be lower triangular matrix. 
			- So $Q_2^TQ_1 = I$ and $R_2R_1^{-1} = I$. 
			- So $Q_2^TQ_1 = I \rightarrow Q_1 = Q_2$
- Lecture 11:
	- [[residual vector , error]]
- Lecture 12:
	- [[Condition of matrix-vector multiplication]]
	- [[Condition of a system of equations]]
- Lecture 24:
	- [[geometric multiplicity]]
	- [[Similarity transformation]]
	- [[diagonalization]]
	- [[Schur factorization]]
- Lecture 28:
	- [[Simultaneous iteration]] x2 
	- [[Convergence of QR algorithm]]
---


---
# Relevance to machine learning and big data analytics

- Linear algebra 9.5
	- Linear algebra forms the foundation for many machine learning algorithms, particularly those involving matrix operations. It's essential for understanding algorithms like linear regression, PCA, and deep learning. 
	- In big data analytics, linear algebra is crucial for data manipulation and analysis.
- Singular value decomposition 7.5
	- SVD is used in dimensionality reduction techniques like PCA and in collaborative filtering recommendation systems in machine learning. 
	- In big data analytics, SVD can help reduce data dimensionality for efficient processing, but it may not be used as frequently as other techniques.
- QR Factorization and Least Square Problems 7.5
	- QR factorization and least squares are important for solving optimization problems, which are common in machine learning. 
	- They are used in regression, for example. In big data analytics, they can be useful for fitting models to data.
- Eigenvalue Problems and Algorithms 6.5
	- PCA is widely used in both machine learning and big data analytics for dimensionality reduction, data compression, and feature selection. It's a fundamental technique for handling high-dimensional data.
- Principal Component Analysis 8.5
	- PCA is widely used in both machine learning and big data analytics for dimensionality reduction, data compression, and feature selection. It's a fundamental technique for handling high-dimensional data.
- Independent Component Analysis (ICA) 6.5
	- ICA is used for separating mixed signals in various applications, including blind source separation. While less common than PCA, it has applications in certain machine learning scenarios and signal processing.
- Compressed sensing 5.5
	- Compressed sensing is mainly used in scenarios where data is highly sparse, which may not be as common in machine learning and big data analytics. 
- Image denoising and processing 8
	- Image denoising and processing are essential in computer vision and image analysis, which are crucial fields in machine learning. In big data analytics, image processing may be relevant in certain applications.
- Data assimilation 7.5
	- Data assimilation is used in fields like weather forecasting and environmental modeling. In machine learning, it can be relevant for integrating multiple data sources. 
	- In big data analytics, it can help combine heterogeneous data for analysis.
---
- Prompts to generate the following content:
	- Refer to `meta > Registers of sequences > understanding a concept`
```
{concept}: X
{context}: linear algebra

Write me a notes about the {concept} of {context}. Please include some mathematics notations in your response. 
```


---
$\begin{bmatrix} 1 & i \\ -i & -1 \end{bmatrix}$

$det(\lambda I - A) = (\lambda - 1) (\lambda +1) +i^2$ 


q1g:

$\begin{bmatrix} 1 & 1 \\  0 & 1 \end{bmatrix}

- Lecture 2

## Singular value decomposition (Chapter 1 of the book)

## QR factorization, Least square problem (Chapter 2 of the book)

## Eigenvalue problems, Eigenvalue algorithms (Chapter 5 of the book)

---

# Part 2

## Principal component analysis (Chapter 15 of the book)

## Independent component analysis (Chapter 16 of the book)

## Compress sensing (Chapter 18 of the book)

## Image denoising and processing (Chapter 14 of the book)

## Data assimilation (Chapter 21 of the book)

