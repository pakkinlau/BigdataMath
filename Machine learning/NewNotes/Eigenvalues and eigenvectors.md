- [[eigenvalues]]
- [[eigenvectors]]

---

- When studying eigenvalues and eigenvectors, or, [[eigendecomposition]], 

- Motives of bringing up the following concepts in this chapter 
	- 1. Understanding transformation
		- Eigenvalues represents the scaling factors by which a matrix transforms an eigenvector.
		- If $A$ is a square matrix and $v$ is an eigenvector of $A$ with eigenvalue $λ$, then when $A$ is applied to $v$, it only stretches or compresses $v$ by the factor of λ. This is crucial in understanding how matrices transform space.
	- 2. Limitation: We can't change the form of $A$ anymore. 
		- When we study [[eigenvalues and eigenvectors]], the matrix represent a [[linear transformation]]. 
		- During computation, we can't change the form of the matrix, otherwise the eigenvalue and eigenvector will change immediately. 
		- So we cannot change our matrix $A$. 
	- 3. When studying eigenvalues and eigenvectors, we also study about change (steady state / decaying state)
		- Time enters the picture - continuous time in a differential equation $du/dt = Au$, or $u_{k+1} = Au_k$. Those equations are not solved by elimination.
		- After having eigenvector $x$ and eigenvalue $\lambda$ , we can literally forget the transformation matrix $A$ .
			- Because $A^nX = \lambda^nX$
		- $n$ times $A$ transformation to the object, instead of multiplying $A$ many times. We could just multiply a single scalar $\lambda$ to take the effect. 
		- decaying state:
			- if all eigenvalues have negative real parts?

- Q: Is that any dependencies between eigenvector $x$ and the matrix $A$? 
	- A: We talk about square matrix because Eigendecomposition mainly used on square matrix. For any matrix in $(n \times n)$, in the maximum could have 

- 1. The basic equation that defines eigenvalues and eigenvectors: $Ax = \lambda x$
	- What is the detailed structure of $\lambda$? 
		- $\lambda$ is a list of values, i.e. $\lambda = ( \lambda_1 , \dots , \lambda_n)$
	- 1. Transformation matrix $A$ (Eigenvalues and eigenvectors are all coming from $A$) 
		- We might draft the value of $A$ by considering geometric property that we want to have
			- eg: reflection, do it 2 times = did nothing. i.e. $R^2 = I$ 
			- eg: projection: vectors after transformation land on a straight line. i.e. 
	- 2. The [[eigenvectors]] $x$ (the direction that won't change direction when multiply by $A$)
	- 3. The [[eigenvalues]] $\lambda$

- Linearity of the transformation
	- The result won't be affected by the order of "multiplication" and "transformation". Like, you can reflect a vector first, or scalar multiplication first. It won't change the result. 

- 1. Computation:
	- b. Finding $\lambda = [\lambda_1, \dots, \lambda_n]$
		- If $Ax = \lambda x$, then $(A - \lambda I)x = 0$, and $A - \lambda I$ is [[singular]], and $det(A - \lambda I) = 0$. $n$ eigenvalues. 
			- Every time we determine [[eigenvalues]] and [[eigenvectors]] of a matrix, we often need to calculate $det(A - \lambda I)$.
			- Solving this will give us a polynomial with $n$ roots. They are the $n$ eigenvalues of $A$. They make $A -\lambda I$ singular. 
			- The specific order of eigenvalues does not affect the mathematical properties of $Ax = \lambda x$. It is because there are 1-to-1 relationship between eigenvalue and eigenvector. If we change the order of eigenvalues, the order of eigenvectors will also change respectively. 
	- c. For each eigenvalues $\lambda$, solve $(A - \lambda I)x = 0$ to find the respective eigenvector $x$. 
		- Say For $Ax = \lambda x$, we solve $det(A - \lambda I) = 0$ ad we have got $\lambda = 0$ or $5$. 
		- $(A - 5 I) x = \begin{bmatrix}  -4 & 2 \\ 2 & -1  \end{bmatrix}  \begin{bmatrix} y \\ z  \end{bmatrix} =  \begin{bmatrix}  0 \\ 0 \end{bmatrix}$, $\begin{bmatrix} y \\ z  \end{bmatrix}  =  \begin{bmatrix}  1 \\ 2 \end{bmatrix}$  
		- Then our original equation would be $A \begin{bmatrix}  1 \\ 2 \end{bmatrix} = 5 \begin{bmatrix}  1 \\ 2 \end{bmatrix}$. 
		- You can verify they are eigenvectors and eigenvalues by performing multiplication in both sides. 
	- d. Transformations: Eigenvalues and eigenvectors are making applying many of times easier. 
		- Before this chapter, we deal with $A$ only. 
		- When $x$ is an eigenvector, multiplication by $A$ is just multiplication by a number $\lambda$. All the difficulties of matrices are swept away. 
		- So the first part is about $Ax = b$: balance and equilibrium and steady state. 
		- We observe the equation $Ax = \lambda x$, the left hand side is before transformation, the right hand side is after transformation. 

---

- [[powers of matrix]]


---

- Two theorems:
	- The product of $n$ eigenvalues equals the determinant
		- The proof is very tedious. Can ask chatGPT for that later. (https://chat.openai.com/share/c100d6ba-0d32-4c65-8086-a8370783bfbf)
	- The sum of the $n$ eigenvalues equals the sum of $n$ diagonal entries. 
		- $\lambda_1 + \dots + \lambda_n$ = trace = $a_{11} + a_{22} + \dots + a_{nn}$


---


- 3. We study a few types of special matrices.
	- [[symmetric matrix]]
	- [[positive definite matrix]]
	- Markov matrices
	- [[singular matrix]]
	- [[triangular matrix]]
	- [[diagonal matrix]]

1. For projection matrix $P$, we can see when $Px$ is parallel to $x$. 
	- The eigenvectors for $\lambda = 1$ and $\lambda = 0$ fill the column space and nullspace. 
	- The column space doesn't move ($Px = x$)
	- The nullspace goes to zero ($P= 0x$)
2. Projection $P$, reflection $R$, rotation $Q$ have special eigenvalues $1,0, -1, i, -i$. 
3. Singular matrices have $\lambda = 0$
4. Triangular matrices have $\lambda$'s on their diagonal.

---

- 4. We look at typical transformations briefly: 
	- Reflection, projection, rotation
	- Q: why linear transformation is related to eigenvalues and eigenvectors?
	- A: (draft) When we study [[eigenvalues and eigenvectors]], the matrix represent a [[linear transformation]]. 


- 5. We learn how to diagonalize a matrix
	- Q: why diagonal matrix is related to eigenvalues and eivenvectors?

- 6. Similar matrix (matrix with the same set of eigenvalues)