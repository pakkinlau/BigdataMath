---
category: 
alias: SVD
tags :
---

## Use SVD to solve [[Least Squares]] problem

First we have $A = \hat U \Sigma \hat V^*$
- The [[Orthogonal Projector]] $P$ is given by $P = \hat U \hat U^*$. 
	- Here, $P = \hat U \hat U^*$ is referred as the [[Orthogonal Projector]] onto the column space of $A$. 
	- For $Ax =b$, it is not always the case that an exact solution exists. It is especially true if $A$ is a rectangular where $m > n$.
- From [[residual vector , error]] we have $Ax = Pb$. 
- So $Ax = Pb \rightarrow \hat U \Sigma  \hat V^* x = \hat U \hat U^* b$ 

---
Why we need $P = \hat U \hat U^*$?

In the context of a least squares problem, the matrix $P = \hat U \hat U^*$ is referred to as the orthogonal projector onto the column space of $A$. Here's why it's important:

When we are dealing with a system of linear equations $Ax = b$, it's not always the case that an exact solution exists. 

Compare the dimensions of $Ax =b$ and $Ax = Pb$.

1. $Ax = b$:
   - $A$ is an $m \times n$ matrix.
   - $x$ is an $n \times 1$ vector.
   - $b$ is an $m \times 1$ vector.
   
   So, $Ax$ is an $m \times 1$ vector, which can be directly compared to $b$, an $m \times 1$ vector.

2. $Ax = Pb$:
   - $A$ is still an $m \times n$ matrix.
   - $x$ is still an $n \times 1$ vector.
   - $P$ is an $m \times m$ matrix (the orthogonal projector onto the column space of $A$).
   - $b$ is still an $m \times 1$ vector.
   
   In this case, $Pb$ is an $m \times 1$ vector, which is the projection of $b$ onto the column space of $A$. Thus, $Ax$ in this case represents the $m \times 1$ vector in the column space of $A$ that is closest to $b$ in terms of Euclidean distance.

The dimensions of the vectors and matrices remain consistent in both equations. The key difference is that in the original system $Ax = b$, we are trying to find an exact solution, while in the modified system $Ax = Pb$, we are trying to find a vector $x$ such that $Ax$ is as close as possible to $b$ when an exact solution may not exist. This is achieved by projecting $b$ onto the column space of $A$ to get $Pb$, which is the "closest" vector to $b$ in the column space of $A$.

---
How to solve $\hat U \Sigma  \hat V^* x = \hat U \hat U^* b$ ?

Firstly, let's denote $\hat U \Sigma \hat V^* = A$ to simplify the notation. So, your equation looks as follows:

$Ax = \hat U \hat U^* b$.

Now, if $\hat U \Sigma \hat V^*$ is a singular value decomposition, $\hat U$ and $\hat V$ are unitary matrices (i.e., $\hat U \hat U^* = \hat U^* \hat U = I$, and similarly for $\hat V$). With this in mind, the equation can be simplified to:

$Ax = b$.

You're therefore left with a standard linear algebra problem, where you need to find $x$ given $A$ and $b$.

If $A$ is invertible, the solution is straightforward:

$x = A^{-1} b$.

However, if $A$ is not invertible, you can't directly find $A^{-1}$ and the solution may not exist, or there may be an infinite number of solutions. In such cases, you can use methods like the pseudo-inverse or least squares to find an approximate solution.

Given $\hat U \Sigma \hat V^*$ is a singular value decomposition of $A$, you can use the pseudo-inverse to solve the equation. The pseudo-inverse of $A$, denoted as $A^+$, is constructed from the SVD of $A$ as follows:

$A^+ = \hat V \Sigma^+ \hat U^*$,

where $\Sigma^+$ is the pseudo-inverse of $\Sigma$ and can be obtained by taking the reciprocal of its non-zero elements and then taking the transpose.

So, the solution to the equation using the pseudo-inverse is:

$x = A^+ b = \hat V \Sigma^+ \hat U^* b$.

This solution minimizes the Euclidean norm $||Ax - b||_2$. If $A$ is invertible, this solution is the same as $A^{-1} b$. If not, it gives the least squares solution.

---

- 8/11/2023
### SVD in the context of PCA

First we assume the points have center at the origin, that is, 
$\sum_{i=1}^n x_i = 0$

projected point $p_i$ 
$p_i = (x_i \cdot u) u$

achieve projection by maximizing the variance 
We find $u$ such that we have a maximized $\sigma^2$, where $\sigma^2 = \frac{1}{n} \sum_{j=1}^n(x_j \cdot u)^2$

We define the matrix $Q = \frac{1}{n} \sum_{j=1}^n x_j x_j^T$ 
Our problem can be formulated as: find a vector $u$ such that $u^TQu$ is maximized, subject to $u^T u =1$
We use the method of Lagrange multiplier, define $L(u) = u^TQu - \lambda (u^T u -1)$

We obtain the system $Qu = \lambda u$, $u^Tu = 1$

We see that the solution $u$ is an eigenvector of $Q$. 

---


- Similar concept: [[eigendecomposition]]

- Related:
	- [[Matrix factorization]]
	- [[Spectral theorem]]

- why SVD is important
	- [[Eigenvalues and eigenvectors]] is for square matrix. But it reality, data are not square.
	- For non-square matrix, we can still use [[Eigenvalues and eigenvectors]], with [[Pseudo-inverse matrix]] 


![[Pasted image 20230913030131.png|300]]

- Intuition of Singular value decomposition (SVD)
	- 1. Basic equation
		- Now we want to formulate a linear transformation for non square matrix.
		- Say there is vectors $v_1, v_2, \dots, v_n$ in the row space of the matrix $A$. And we want to find a way to transform them to be vectors in column space $u_1, u_2, \dots, u_n$ 
		- So we have:
			- $Av_1 = \sigma_1u_1$
			- $Av_2 = \sigma_2u_2$
			- $Av_n = \sigma_nu_n$
		- And then we can formulate these equations as $AV = U \Sigma$
	- 2. $A = U\Sigma V^{-1} = U\Sigma V^T = \begin{bmatrix} u_1 & u_2 \end{bmatrix} \begin{bmatrix} \sigma_1 & 0 \\ 0 & \sigma_2 \end{bmatrix} \begin{bmatrix} v_1^T \\ v_2^T \end{bmatrix}$
		- Since $U$ and $V$ are orthogonal matrix, so $V^{-1} = V^T$
	- 3. Find a good square matrix that could find U and V of SVD
		- Good matrix 1: $A^T A = (V\Sigma^T U^T) (U \Sigma V^T)$
			- We have $U^TU =I$, and we also have $\Sigma^T = \Sigma$
			- So $A^TA = V \Sigma^2 V^T$
			- Now $A^TA$ is computable since we already have $A$. 
			- Now we already can solve $V$ from the equation. To see it, multiply $V$ on the both sides. Then we have $(A^TA)V = V \Sigma^2$. That is clearly a classic eigendecomposition problem. 
			- Arrange the eigenvalues in descending order, and the corresponding eigenvectors will form the columns of matrix $V$.
			- Normalize the columns of $V$ to ensure they are unit vectors.
		- Good matrix 2: $AA^T$
			- $(U \Sigma V^T)(V\Sigma^T U^T)$
			- So we have $AA^T = U \Sigma^2 U^T$
			- Then we use similar way to find $U$. 

- New formation
	- In SVD, we look for [[orthogonal matrix]] times [[diagonal matrix]] times [[orthogonal matrix]]
	- We need two sets of singular vectors. $U$ and $V$ provide us with orthogonal bases for the row and column spaces of $A$, respectively. 
	- Where we mention "orthogonal bases", it means the column vectors of $U$ and $V$ are orthogonal to each others. However, they are not essentially have a unit length.
	- $U$ and $V$ are [[unitary matrices|unitary matrix]].
	- Meaning:
		- $U$ capture the structure of the data in the [[column space]] of $A$.
			- Because $u_k$ forms orthonormal basis for the column space of $A$.
				- 1. We put SVD into $AV = U\Sigma$. And since $\Sigma$ are scalar we can omit it temporarily. Recall $Ax = b$, the matrix $A$ acting as function, it maps [[row space]] of $A$ to [[column space]] of $A$. So by comparing $Ax = b$ and  $AV = U$, we know that $V$ is capturing row space of $A$ and $U$ is capturing column space of $A$. 
				- 2. columns of $U$ are orthogonal to each others, so column vectors of $U$ can effectively span the column space of $A$. 
				- 3. If normalizing each column of $U$ to have a length of $1$, then $U$ forms an orthonormal basis than could span the column space of $A$. 
		- $U$ helps us understand the relationship between the data points in the original space
			- It is often referred to as the left singular vectors.
			- It can be used for [[dimensionality reduction]], [[Compress|compression]], and [[systems of linear equations|solving systems of linear equations]]. 
		- $V$ represent the transformation of the [[row space]] of the original matrix $A$ into another orthogonal basis. They capture the structure of the data in the column space of $A$. 
			- It can be used for [[dimensionality reduction]], [[Feature selection]], and [[principal component analysis]]
		- $\Sigma$ represent the importance of each basis vector. The singular values in $\Sigma$ are arranged in descending order. These values provide insights into significance of the corresponding singular vectors. 
	- Construction:
		- $U = \begin{bmatrix} u_1 & \dots & u_n \end{bmatrix}$ and $u_k$ is called left singular vectors, which is the unit eigenvectors of $AA^T$.  $V = \begin{bmatrix} v_1 & \dots & v_n \end{bmatrix}$ and $v_k$ are right singular vectors (unit eigenvectors of $A^TA$.) The $\sigma$ are singular values, square roots of the equal eigenvalues of $AA^T$ and $A^TA$. 

- Functional nature of SVD
	- When we write $Ax = U \Sigma V^* x =b$, it indicates $\Sigma V^* x  = U^* b$. From this expression, we can see a change of basis $V^* x = x'$ and $U^* b = b'$. 
	- The original linear transformation can be re-written as $\Sigma x' = b'$. 

- Components nature of SVD
	- We can write $A = \sum_{j = 1}^r \sigma_j u_j v_j^*$. That is, $A$ is a sum of rank one matrices. 

- Factorization nature of SVD
	- In linear algebra, the singular value decomposition (SVD) is a factorization of a real or complex matrix. It generalizes the [[eigendecomposition]] of a square normal matrix with an [[orthonormal]] [[eigenbasis]] to any $m \times n$ matrix. It is related to the polar decomposition. (wiki)
	- $X$
		- The matrix $X \in \mathbb{C}^{n \times m}$ may be decomposed into the product of three matrices 
		- Each column $x_k \in \mathbb{C}^n$ represents one data, called snapshot. 
			- snapshot example:
				- different images
				- state of a physical system at different times
		- The dimension $n$ is usually very large
		- $m$ is the number of snapshots

	- $X = U\Sigma V^* = \begin{bmatrix} \tilde U & \tilde U^\bot \end{bmatrix}\begin{bmatrix} \tilde \Sigma \\ 0 \end{bmatrix} V^* \approx \tilde U \tilde \Sigma \tilde V^*$
		- $U, V$: 
			- $U \in C^{n \times n}$, $V \in C^{m \times m}$
			- [[unitary matrices|unitary matrix]]
				- The matrices $U$ and $V^*$ are [[unitary matrices]] with [[orthonormal]] column, so that $UU^* = U^*U = I_{n \times n}$ and $VV^* = V^*V = I_{m \times m}$, where $*$ denotes complex conjugate transpose. 
				- The condition that $U$ and $V$ are [[unitary matrices|unitary matrix]] is used extensively.
			- The columns of $U$ (resp. $V$) are [[orthogonal matrix|orthogonal]], called left [[singular vectors]].
		- $\Sigma$: 
			- $\Sigma \in C^{n \times m}$ is a matrix with real, non-negative entries on the [[diagonal matrix|diagonal]], and zeros off the diagonal. 
			- When $n \geq m$, which means $X$ is a tall-skin matrix, $\Sigma$ has most $m$ nonzero elements on the diagonal, and may be written as $\Sigma = \begin{bmatrix} \tilde \Sigma \\ 0 \end{bmatrix}$
			- The matrix $\Sigma$ contains decreasing, non-negative [[diagonal matrix|diagonal]] entries called [[singular values]]
			- The non-singular values of $A$ are the sqaure roots of the nonzero eigenvalues of $A^*A$ and $AA^*$. 
		- $V^*$:
			- It denotes the complex conjugate transpose matrix

- How to compute SVD?
	- 1. Start with matrix $A$: $A = U \Sigma V^T$
	- 2. Compute $A^T A$ and $AA^T$
	- 3. Find the eigenvalues and corresponding eigenvectors for both $A^TA$ and $AA^T$. 
	- 4. Calculate $V$: The columns of $V$ are the normalized eigenvectors of $A^TA$. 
	- 5. Calculate $U$: The columns of $U$ are the eigenvectors of $AA^T$ corresponding to the non-zero eigenvalues. 

- Special case of SVD
	- If we solve the linear data fitting problem $Ax = b$, where both $A$ and $b$ have only 1 column, then: 
		- $\tilde \Sigma = ||A||_2 = \sigma_1$: it is because we just have 1 column. And $||A||_2$ is the 2-norm of the vector $A$, which is equal to its singular value $\sigma_1$.
		- $\tilde V = 1$: Since $A$ has only one column, $\tilde V$ is a scalar value, which is 1 in this case.
		- $\tilde U = \frac{A}{||A||_2}$: $\tilde U$ is the normalized left singular vector corresponding to the singular value $\tilde \Sigma$. Dividing $A$ by its 2-norm ($||A||_2$) provides the normalized left singular vector.



- Theorems in SVD
	- $||A||_2 = \sqrt{\lambda_{max}(A^TA)} = \sigma_{max}$


- Generalization nature of SVD
	- We could say, SVD is a generalization of [[eigendecomposition]] of symmetric matrix, $S = Q \Lambda Q^T$. 

- Transformation nature of SVD
	The notation $AV = U \times \Sigma$ that you mentioned seems to be a slight variation of the typical Singular Value Decomposition (SVD) notation $A = U \times \Sigma \times V^T$. The standard notation represents the SVD of a matrix $A$ as the product of three matrices $U$, $\Sigma$, and $V^T$, as explained in the previous response. However, there might be cases where you see a variation in notation like $AV = U \times \Sigma$. Let me explain why this form can be used and what it represents:
	
	In the context of SVD, $A$ is a matrix, and $U$, $\Sigma$, and $V$ are matrices resulting from the decomposition. $U$ and $V$ are orthogonal matrices, and $\Sigma$ is a diagonal matrix containing the singular values of $A$.
	
	When we multiply $A$ by $V$, it effectively means transforming the columns of $A$ into the basis represented by $V$. In other words, $AV$ represents the action of $A$ in the coordinate system defined by the right singular vectors ($V$). Similarly, $U$ represents the left singular vectors of $A$.
	
	So, the expression $AV = U \times \Sigma$ can be interpreted as follows:
	
	- $AV$ transforms the original data ($A$) into a new coordinate system represented by the right singular vectors ($V$).
	- $U \times \Sigma$ represents the transformed data in the coordinate system defined by the left singular vectors ($U$) and the singular values ($\Sigma$).

- Left singular matrix $U$: 
	In this form, we can see that the left singular matrix $U$ represents the transformation of the original data in a way that captures the directions of maximum variance in the input data. 
	In practical terms, the left singular matrix $U$ is used to rotate and scale the data points, providing a new perspective on the dataset. 
	In some contexts or specific applications, people might be interested in the transformed data $AV$ in relation to the left singular vectors ($U$) and singular values ($\Sigma$), which is why you might encounter this notation.
	
	In summary, both notations represent different aspects of the SVD: $A = U \times \Sigma \times V^T$ provides a complete factorization of $A$, whereas $AV = U \times \Sigma$ emphasizes the transformation of the data into a new coordinate system defined by the singular vectors. The choice of notation depends on the specific focus and interpretation required in a given situation.

- Geometric interpretation of SVD:
	**Introduction:**
	Singular Value Decomposition (SVD) is a fundamental technique in linear algebra that breaks down a matrix into simpler, meaningful components. Beyond its algebraic significance, SVD also has a profound geometric interpretation, shedding light on the fundamental properties of matrices and their transformations.
	
	**Understanding SVD:**
	SVD of a matrix $A$ can be represented as $A = U\Sigma V^T$, where $U$ and $V$ are orthogonal matrices, and $\Sigma$ is a diagonal matrix containing singular values of $A$. Geometrically, this decomposition can be visualized as a sequence of three fundamental transformations:
	
	1. **Rotation/Reflection (V):**
	   Matrix $V$ represents the rotation or reflection operation. When $V$ operates on a vector, it transforms the vector without changing its length. The columns of $V$ form orthonormal basis vectors in the output space. These vectors define the new coordinate system after rotation/reflection.
	   Recalling that $U$ and $V$ are [[unitary matrices|unitary matrix]], which means they also inherit [[invariance under unitary matrix multiplication]]. With this property, 
	
	2. **Scaling (Σ):**
	   The singular values in $\Sigma$ represent the scaling factors. Larger singular values imply greater importance in the transformation. Multiplying a vector by $\Sigma$ scales the vector along each of the orthogonal axes defined by $V$. This step resizes the transformed vectors by different amounts along different axes.
	
	3. **Rotation/Reflection (U):**
	   Matrix $U$ represents another rotation or reflection operation in a different space. The columns of $U$ form orthonormal basis vectors in the input space. These vectors define the original coordinate system. The interaction of $U$ with the scaled vectors (resulting from $V$ and $\Sigma$) aligns them with the appropriate dimensions in the output space.
	
	**Geometric Interpretation:**
	- SVD geometrically breaks down any linear transformation into these basic operations: rotation/reflection, scaling, and another rotation/reflection. This decomposition is incredibly useful in understanding and analyzing various transformations and their effects on vectors and spaces.
	- In the context of data analysis, SVD can be used for dimensionality reduction, noise reduction, and feature extraction. Geometrically, this means finding the most important directions in the data space and projecting data onto those directions.
	
	**Applications:**
	1. **Image Compression:** SVD is used in image compression, where it captures the most important features (singular values) of an image, allowing efficient storage and transmission.
	2. **Collaborative Filtering:** In recommendation systems, SVD is applied to user-item matrices to discover latent factors, aiding in making personalized recommendations.
	3. **Signal Processing:** SVD is employed in noise reduction and signal denoising by isolating significant signal components from noise.

![[Pasted image 20230925043226.png]]


- Low rank approximation
	- Often, $X$ is approximated with a low-rank matrix $\tilde X = \tilde U \tilde \Sigma \tilde V^*$, where $\tilde U$ and $\tilde V$ contain the first $r << n$ columns of $U$ and $V$, respectively, and $\tilde \Sigma$ contains the first $r \times r$ block or $\Sigma$. The matrix $\tilde U$ is often denoted $\Phi$ in the context of spatial modes, reduced order models, and sensor placement. 

- [[dimensionality reduction]] perspective of SVD
	- SVD can be used for dimensionality reduction. By keeping only the first $k$ columns of $U$, where �k is less than $m$, you can obtain an approximate representation of the original data with reduced dimensions. This reduction is valuable in various machine learning applications.
	- $A_{[n \times m]}=U_{[n \times r]}R_{[r \times r]} (V_{[m \times r]})^T$ 
		- $A_{[n \times m]}$: Original matrix that represent the [[document]]: A document that has all terms. 
		- $U_{[n \times r]}$: document - concept matrix: each row of document, which has n attributes (terms) has been compressed into r (concepts). 
		- $R_{[r \times r]}$: Adapter matrix that connecting U and V
		- $(V_{[m \times r]})^T$: concept - term matrix: This matrix tries to decode what that concept could possibly means. 
![[Pasted image 20220831185340.png]]
- How to search "system"?


---
## Reference

1. 

