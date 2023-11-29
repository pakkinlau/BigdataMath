---
alias: QR factorization, Gram-Schmidt iteration, Gram-Schmidt orthogonalization
---

- Content: 
	- the process of QR decomposition, a technique in linear algebra used to decompose a matrix into the product of an orthogonal matrix (Q) and an upper triangular matrix (R). Let's break down the explanation and define the variables used in the notes:


Goal of QR decomposition
- Find $\langle q_1, q_2, \dots, q_j \rangle = \langle a_1, a_2, \dots, a_j \rangle$, where $j = 1, \dots, n$.
	- Remark: 
		- The above expression means those orthonormal vector set spans the same space as the set of column vectors of $A$. 
	- And of course as we discussed in "idea", the set of orthonormal vectors will span [[successive spaces]].

Idea of QR decomposition

- Idea 1. We would like to perceive columns of matrix $A$ as a [[successive spaces]] spanned by $a_1, a_2, \dots$ of $A$.  So $A = \sum_{j=1}^n \alpha_j a_j$, where $\alpha_j$ represents the coefficient. 
	- The idea of QR decomposition is the construction of a sequence of orthonormal vectors $q_1, q_2, \dots$ that span those [[successive spaces]] $a_1, a_2, \dots$
	- So that $a_1$ is constructed by 1 orthonormal vectors from $Q$,  $a_2$ is constructed by 2 orthonormal vectors from $Q$, and so on.
	- Advantages: 
	- 1. [[Stability]]:
		- The Gram-Schmidt process constructs orthonormal vectors one at a time, making it numerically stable, even for ill-conditioned matrices. It avoids the accumulation of round-off errors, which can occur when orthogonalizing a set of vectors all at once.
	- 2. Unique decomposition:
		- By constructing a sequence of orthonormal vectors that span successive spaces, you ensure that the resulting Q and R matrices are unique for a given input matrix A. 
	- 3. [[Orthogonal vector|Orthogonality]] preservation
		- The construction of Q as an orthogonal matrix ensures that the columns of Q remain mutually orthogonal. This property is useful in various applications, such as solving least-squares problems or computing orthogonal projections.
	- 4. Easy to apply for [[systems of linear equations|solving systems of linear equations]]:
		- The upper triangular matrix R makes it easy to solve for x using back-substitution. Additionally, the orthogonal matrix Q can be used to solve linear systems or perform other operations without affecting the orthonormality of its columns.

- Idea 2. Regarding to $Q$ matrix -- It is a list of [[orthonormal]] [[Basis]] 
	- We adopt [[orthogonal matrix]] $Q$ in QR decomposition.
	- Advantage:
		- 1. [[Stability]]:
			- Orthogonal matrices are numerically stable. When you perform QR decomposition using orthogonal matrices (e.g., the Gram-Schmidt process or Householder transformations), you minimise the accumulation of rounding errors. 
		- 2. [[Orthogonal transformation]]
			- The orthogonal matrix Q represents an orthogonal transformation, meaning it preserves the lengths and angles between vectors. This can be beneficial in various applications, such as signal processing
		- 3. [[Orthogonal eigenvectors]]:
			- When performing eigenvalue decomposition ([[eigendecomposition]]) or [[Singular value decomposition|SVD]], having an orthogonal matrix as Q simplifies the calculation and interpretation of [[eigenvectors]] or [[singular vectors]].
			- The calculation of: [[diagonalization]], [[Eigenvalue Decomposition|spectral decomposition]], 
		- 4. [[Orthogonalization]]
			- QR decomposition is widely used in [[systems of linear equations|solving systems of linear equations]], where you find the best-fitting linear model to a set of data points. The [[orthogonal matrix]] $Q$ simplifies the mathematical formulation and leads to more stable and efficient computations. 

- Idea 3: Regarding to $R$ matrix -- $R$ is always in the shape of upper [[triangular matrix]]
	- $R$ is an upper triangular matrix obtained from the [[Orthogonalization]] process. 
	- Why $R$ are always upper triangular matrix:
		- The formation of $a_k$ in matrix $A$: 
			- Recall that $A = \sum_{j=1}^n \alpha_j a_j$. 
			- Since we are going to form $a_j$ in matrix $A$ as a [[successive spaces]] (which is the idea of QR decomposition), which means $a_j$ will be constructed by a total of $j$ components selected from $Q$. 
				- $a_1 = r_{11}q_1$, 
				- $a_2 = r_{12}q_1 + r_{22}q_2$,
				- $a_k = \sum_i r_{ik}q_i$
		- Dependence of orthogonal vectors:
			- The next column in $A$ have to mentions the orthogonal vectors that the prior column vector in $A$, when constructing $a_k$ in QR decomposition. 
			- So we can observe a fact that $q_1$ are mentioned by all construction lines for column vectors of $A$. $q_j$ is mention by $m - j + 1$ construction lines for column vectors of $A$.
		- The iterative process in the construction of $A$: 
			- So the iterative process repeat itself, and we see the upper-triangular matrix forms in the right hand side of Q, in $A = QR$. 

- Idea 4: The shape of $Q$ and $R$ will be adjusted according to the shape of $A$. 
	- Case 1: $m > n$
		- This case arises when you have more observations than features, and QR decomposition simplifies to handle this [[over-determined|overdetermined]] system. 
		- $Q$ would be of shape $m \times m$. 
		- $R$ would be of shape $m \times n$. The entries below its main diagonal are zero. While those rows are zero, $R$ cannot be reduced to $n \times n$ because it would make the $QR$ multiplication becomes not working anymore 
	- Case 2: $m = n$
		- The [[Orthogonality]] of $Q$ and $R$ remain consistent with the original matrix $A$. This is useful in [[systems of linear equations|solving systems of linear equations]].
		- $Q, R$ are $m \times m$
	- Case 3: $m < n$
		- This case is useful in scenarios where you have more columns than rows. Which is [[Under-determined|Underdetermined]] system. 
		- The squareness reflects the fact that $A$ has more columns than rows. The QR decomposition ensures that $R$ remains upper triangular. 
		- $Q$ will be of shape $m \times n$. The rows of $Q$ corresponds to the rows of $A$. The rectangular shape of $Q$ allows for efficient representation and manipulation of the original matrix $A$ in applications like [[dimensionality reduction]] and [[Compress|data compression]].
		- $R$ will be of shape $n \times n$. 

- Idea 5: physical meaning of $QR$ decomposition
	- $Q$ capture the relevant information from $A$'s column. 
	- $R$ encapsulates the structural relationship among those columns. 

- To put of of these 5 ideas together, we have:
	- $a_1, a_2, \dots, a_n$: They are the columns in $A$
	- $q_1, q_2, \dots, q_n$: They are the variable orthonormal vectors in $Q$, which $Q$ is orthogonal matrix.
	- $r_{11}, r_{12}, \dots$: They are variable factors elements in our factor matrix $R$. 
![[Pasted image 20231010004256.png]]

---
## Expression 2 of 2 of QR decomposition: Expressing QR decomposition as a succession of elementary triangular matrices

- Succession of elementary triangular matrices $R_k$ on the right of $A$:
	- We have the [[Unstable Gram-Schmidt process|Gram-Schmidt process]] iteration applies a succession of elementary triangular matrices $R_k$ on the right of $A$, so that the resulting matrix is: 
		- $A R_1 R_2 \dots R_n = \hat Q$
		- And we say that $\hat Q$ has orthonormal columns.
	- we can rewrite it as $A \hat R^{-1} = \hat Q$, where $\hat R^{-1} = R_1 R_2 \dots R_n$ , and $\hat R = R_n^{-1} \dots R_2^{-1} R_1^{-1}$ is upper-triangular. 
	- Therefore, $A = \hat Q \hat R$ is a reduced QR factorisation of $A$. 

---
### Exact calculation steps of QR decomposition

- See [[Unstable Gram-Schmidt process]]

---

## Using QR factorization to solve [[Least Squares]] problems

find $x \in \mathbb{C}^n$ such  that $||b - Ax||_2$ is minimized

First we have $A = \hat Q \hat R$. 
Then $y = Pv = \hat Q \hat Q^* b$. 
- The [[Orthogonal Projector]] $P$ is given by $P = \hat Q \hat Q^*$. ([[projection operator (QQT)]])
And $Ax = Pb \rightarrow \hat Q \hat R x = \hat Q \hat Q^* b$. $\rightarrow \hat R x = \hat Q^* b$ for $x$. 
- $Ax = Pb$ always hold true, see [[residual vector , error]]. 
- Without that, we need other ways to come up $\hat Q \hat R x = \hat Q \hat Q^* b$. ($Ax = Pb$ is not the only possible way)


Note: there are multiple of ways of leading to the expression of $\hat R x = \hat Q^* b$. 

How to solve $\hat Q \hat R x = \hat Q \hat Q^* b$?

The big picture is, we solve this from the bottom row of $\hat R$, which relates to one element of $x$ only. Then we iteratively move upwards through the row of $\hat R$. 

1. **Initialize**: Start from the last row of $\hat{R}$ and set $x_n = \frac{b_n}{\hat{R}_{nn}}$, where $n$ is the size of the system.

2. **Back Substitution**: Move upwards through the rows of $\hat{R}$ and use the values of $x$ that you have already found to solve for the remaining components. The formula for the $i$-th component ($x_i$) is given by:
$$ x_i = \frac{1}{\hat{R}_{ii}} \left( b_i - \sum_{j=i+1}^{n} \hat{R}_{ij} x_j \right)$$

   Here, $i$ ranges from $n-1$ to 1.

This process is possible because $\hat{R}$ is upper triangular, and the system can be solved efficiently starting from the last equation and moving upwards.

Here's a Python-like pseudocode to illustrate the back substitution process:

```python
# Initialize x
x[n] = b[n] / R[n, n]

# Back substitution
for i in range(n-1, 0, -1):
    summation = sum(R[i, j] * x[j] for j in range(i+1, n+1))
    x[i] = (b[i] - summation) / R[i, i]
```

This pseudocode assumes 1-based indexing. If you're using 0-based indexing, you may need to adjust the range accordingly.

Remember to handle cases where $\hat{R}_{ii} = 0$ carefully, as this would result in division by zero.

---

Remark
- This method is good when $A$ is full rank. 

---


