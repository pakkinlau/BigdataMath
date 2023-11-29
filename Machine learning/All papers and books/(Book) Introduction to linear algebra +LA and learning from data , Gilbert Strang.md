- Solution manual of Intro-to-linear-algebra
	- https://www.studocu.com/row/document/north-south-university/calculus/gilbert-strang-solutions-manual/9691007
- Another easier book but having new way:
	- Linear algebra for everyone: 
		- https://www.doc88.com/p-48773903576903.html
		- Solution manual for LAFE
			- https://math.mit.edu/~gs/everyone/lafe_sols23.pdf

![[Pasted image 20221225232213.png]]
- Fig: Book cover of the book 1

![[Pasted image 20230213065055.png]]
- Fig: Book cover of the book 2

- $Ax = b$ is solvable when $b$ is in the (orange) column space of $A$. One particular solution $y$ is in the (red) row space $Ay = b$. Add any vector $z$ from the (green) nullspace of $A$: $Az = 0$ 
- The complete solution is $x = y + z$ , then $Ax = Ay + Az = b$.

- ![[Introduction to Linear Algebra, 5th  (Solutions) – 2016.pdf]]
- [[Introduction to Linear Algebra, 5th  (Solutions) – 2016.pdf]]

---
## Chapter 1 Introduction to vectors


### Linear equations 
- simple expression: $Ax = b$
- There are two ways to think of the problem: 
	- 1. We know $Ax$, find b
	- 2. We know $A$ and $b$, find $x$
		- For 1, we multiply $A$ and $x$ once at a time.
		- For 2, it is a inverse problem of 1. That 
### Solutions 
- $x = A^{-1} b$ 

---
# 2020 vision on linear algebra

- 1. [[Column-row decomposition -- $A = CR$]]


- 2. [[Rank-Nullity Theorem]]


- 3. [[4 fundamental subspaces, or big picture of linear algebra]]

- 4. Triangular matrix decomposition A = LU



---
# Part 1 - The data construction of Linear algebra
## Chapter 1 - Introduction to vectors
## Chatper 2 - Solving linear equations

2.1 Vectors and linear equations

- [[row picture]]
	- recognizing systems of linear equations as row-by-row equations
- [[column space]]
	- 1. recognizing systems of linear equations as a linear combinations of columns
	- 2. Grouping up column vectors into $A$, we call $A$ "coefficient matrix". The systems of linear equations become $Ax = b$, and we solve $x$ to solve it. 
- [[Elimination using matrices]]
	- [[Breakdown]]

## Chapter 3 - Vector spaces and subspace

---
- Prompts to generate the following content:
	- Refer to `meta > Registers of sequences > understanding a concept`
```
{concept}: X
{context}: linear algebra

Write me a notes about the {concept} of {context}
```


---
- Data
	- [[vector]]
		- unit vectors
		- [[zero vector]]
		- [[row vector]]
		- [[column vector]]
	- [[Basis vectors]]
	- [[linear combination]]
	- [[column vectors]]
	- [[vector space]]
		- [[hyperplane]]
		- [[subspace]]
		- [[nullspace]]
	- About crossing origin:
		- [[Position vectors ]]
		- [[Free vectors]]
	- [[matrix]]
		- [[invert|inverse]]
		- [[transpose]]
		- [[adjoint]]
		- [[unitary matrices]]
		- [[diagonal matrix]]
		- [[square matrix]]
		- [[orthogonal matrix]]
		- [[triangular matrix]]
		- [[conjugate transpose]]
- Forms of data
	- [[Matrix form]]
		- [[row picture]]
		- [[column picture]]
- Description of vector
	- [[Vector Norm]]
	- [[angle between 2 vectors]]
- Description of matrix
	- [[Linear independence]]
	- [[Rank]]
	- [[column space]] / [[span]]
	- [[induced p-matrix norm]]
	- [[Orthogonal vector]]
	- [[orthonormal]]
- Frameworks of data
	- [[Basis]]
	- [[vector space]]
	- [[closure]]
- Vector operations:
	  [[Decomposition of a vector]]
- Matrix operations:
	- Finding [[Determinant]]
	- calculating matrix [[rank]]
	- determining [[Linear independence]] of vectors 
	- determining matrix [[invert|inverse]]
	- matrix transposition
	- finding [[trace]]
	- determining matrix [[Eigenvalues and eigenvectors]]
	- matrix [[diagonalization]]
	- matrix [[Vector Norm]]
	- [[Matrix factorization]]
	- [[matrix convolution]]
- Decomposition:
	- [[vector decomposition]]
	- matrix [[singular value decomposition]]
	- matrix [[Eigenvalue Decomposition]]
	- [[Reduced QR decomposition]]
- Operations:
	- [[Matrix-Vector Multiplication]]
	- [[Matrix-matrix multiplication]]
	-  [[dot product]]
	- [[systems of linear equations]]
		- [[row reduction]]
		- [[pivot]]
	- [[Unstable Gram-Schmidt process]]
- Transformation 
	- [[Basis matrix]]
	- [[Change of basis]]
	- [[Linear transformation]]
	- [[Orthogonal transformation]]
- Theorems:
	- [[Rank-Nullity Theorem]]
		- Related:
			- [[nullspace]]
			- [[rank]]
	- [[Counting theorem]]

---
# Part 2 - The derived data format and computations

### [[4 fundamental subspaces, or big picture of linear algebra]] 


- [[singular value decomposition]]
- [[principal component analysis]]

---

###  Cosine formula
- If $u$ and $w$ are nonzero, then ${v \cdot w \over {||v|| ||w||}} = cos \theta$


### Professor's preference on row picture / column picture
- To combine column vectors. **It is a lot easier to see a combinations of four vectors in 4-dimensional space, than to visualize how four hyperplanes might possibly meet at a point.** 


---


### Inverse matrix:
- $Ax = b$ is solvable by having $\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} b_1 \\ b_1 + b_2 \\ b_1 + b_2 + b_3 \end{bmatrix}$
- Requirements:
	- 1. If the matrix is rectangular, it has no inverse matrix for it. 
	- 2. The matrix has linearly independent columns. 
- The sum matrix $S$ in this equation is the inverse of the difference matrix $A$. 
- A matrix is inversible if and only if its determinant is zero.
- The probability that the matrix is singular is 


### Difference matrix
### Cyclic difference
- three equations either have infinitely many solutions or else no solutions
- The cyclic matrix $C$ has no inverse. 
- Its three columns lie in the same plane. 
- Those dependent columns add to the zero vector. $Cx = 0$ has many solutions. 
![[Pasted image 20221226015854.png|300]]
![[Pasted image 20221226015904.png|300]]


### Independence:
- These concepts are central to the definition of dimension in mathematics. 
- A set of vectors is said to be linear independent if there is no non-trivial linear combination of the vectors that equal the zero vector. 
- That means no vector in the sequence can be represented as a linear combination of the remaining vectors in the sequence. 
- eg:
	- $w$ is not in the plane of $u$ and $v$
- If $d$ vectors in $S$ are independent, they span $S$. If $d$ vectors span $S$, they are independent. 

### Dependence:
- A set of vectors is said to be linear dependent if there is a non-trivial linear combination of the vectors that equal the zero vector. 
- If at least 1 vector in the set of vectors that can be written as a linear combination of the others, then all vectors in the matrix are linearly dependent. 
	- That means at least 1 vector is on the plane of some combinations of other vectors. 
	- That means it is not linearly independent. 
- eg:
	- $w$ is in the plane of $u$ and $v$. 
	- $w$ can be expressed by a linear combination of $u$ and $v$. 
- Linear independence versus orthogonality 


---
## Chapter 2: solving linear equation


### Coefficient matrix ($A$)
- It is on the left side of the equation. 
- The term coefficient, that means the coefficient collected from the system of linear equations. 

### Matrix notation
- The first row of a 2-by-2 matrix contains $a_{11}$ and $a_{12}$.
- Those subscript is not convenient. We also type $A(i,j)$ for $a_{ij}$ entry.


### Conditions to compute $Ax = B$
- 1. $A$ is invertible
- 2. The columns are independent
- 3. The determinant isn't zero. 
- 4. We need a full set of three non-zero pivots. 

### [[Elimination using matrices ]]-> [[LU decomposition]]



### Inner product
- A row times a column is an inner product. A column times a row is an outer product. 
	- We can memorize it by the position of $T$. $x^Ty$: inner product.  $xy^T$: outer product. 
- Properties
	- 1. An inner product naturally induces an associated norm.( eg: $|x|$). A norm is the formalization and the generalization to real vector spaces of the intuitive notion of "length" in the real (physical) world.
- Convention:
	- It is often denoted with angle brackets such as $\langle a,b \rangle$
	- every vector are basically column vectors. Therefore, $x^T$ is a row, $y$ is a column.
- Axioms:
	- Associativity, etc. 
	- See wikis
- Applications:
	- Inner product spaces generalized Euclidean vector space, in which the inner products is the dot product or scalar product of Cartesian coordinates. 
- Distinction:
	- Dot product  $x \cdot y$ 
		- Dot product is an algebraic operation that takes 2 equal-length sequences of numbers and returns a single number.
		- Every dot products that involves 2 column vectors are inner products. 
	- Inner product $x^Ty$: the dot product or inner product, $(1 \times n)(n \times 1)$
		- The rank is $n$, the number of elements is 1.
	- Outer product $xy^T$: 
		- the rank one product, or outer product $(n \times 1)(1 \times n)$
		- It produces a matrix


### Outer product
- A column times a row is an outer product. 


### Block matrices
- Matrices can be cut into blocks (which are smaller matrices). This often happens naturally. 

### Block multiplication
- If blocks of A can multiply blocks of B, then block multiplication of AB is allowed. Cuts between columns of A match cuts between rows of B.

### Determinant
- Determinant as coefficient of linear systems
	- The determinant is a scalar value that is a function of the entries of a square matrix. 
	- The determinant is nonzero if and only if the matrix is invertible and the linear map represented by the matrix is an isomorphism.
	- Determinants occur throughout mathematics -- a matrix is often used to represent the coefficients in a system of linear equations, and determinants can be used to solve these equations (Cramer's rule).
	- Determinants are used for defining the characteristic polynomial of a matrix, whose roots are the eigenvalues. 
- Geometric meaning of determinant
	- say we have a matrix $\begin{bmatrix} a \ c \\ b \  d \end{bmatrix}$, column vectors are $\begin{bmatrix} a  \\ b \end{bmatrix}$ and $\begin{bmatrix}  c \\  d \end{bmatrix}$ respectively. 
	- The absolute value of ad-bc is the area of the parallelogram. 

![[Area_parallellogram_as_determinant.svg.png|400]]
- Fig: method 1 of determining the area. Another method will be $A = |u||v| sin \theta$ for angle $\theta$ between the vectors.


### Inverse matrix
- [[invert|inverse]]


- Gauss-Jordan Elimination
	- augmented matrix
	- [[row echelon form]]
	- [[Reduced Row Echelon Form]]

- In row echelon form, the matrix satisfies the following conditions:
    
    1. The first nonzero element in each row (called the leading entry) is 1.
    2. The leading entry in the second row and beyond is to the right of the leading entry in the row just above it.
    3. Any rows consisting entirely of zeros are at the bottom of the matrix.
- Other elements in the same column as a leading entry can be any real numbers (they do not have to be zero).
    
- Row echelon form does not require that the leading entries in a column below or above the current row be zeros.]]

### [[Reduced Row Echelon Form|Reduced Row-Echelon Form (RREF)]]



### Matrix merging / splitting
- Entrywise sum
	- $A + B = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix} + \begin{bmatrix} b_{11} & b_{12} & \cdots & b_{1n} \\ b_{21} & b_{22} & \cdots & b_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ b_{m1} & b_{m2} & \cdots & b_{mn} \end{bmatrix}$
	- $= \begin{bmatrix} a_{11}+b_{11} & a_{12}+b_{12} & \cdots & a_{1n}+b_{1n} \\ a_{21}+b_{21} & a_{22}+b_{22} & \cdots & a_{2n}+b_{2n} \\ \vdots & \vdots & \ddots & \vdots \\  a_{m1}+b_{m1} & a_{m2}+b_{m2} & \cdots & a_{mn}+b_{mn} \end{bmatrix}$

### Determinant merging / splitting
- The determinant is a linear function of each row separately. 
- $\begin{vmatrix} a + a' & b+b' \\ c & d\end{vmatrix} = \begin{vmatrix} a  & b \\ c & d\end{vmatrix} + \begin{vmatrix} a' & b' \\ c & d\end{vmatrix}$


### Matrix factorization / multiplications
- Case 1: The matrix is a m by n matrix
	- 1. We express diagonal matrix as $\begin{bmatrix}d_{1} & & \\ & \ddots & \\ & & d_{r} \end{bmatrix}$, the empty area means 0.
	- 2. We can factorize a row of a time for a matrix by $\begin{bmatrix} a&b&c \\ d&e&f \\ g&h&i \end{bmatrix} = \begin{bmatrix}d_{1} & & \\ & \ddots & \\ & & d_{r} \end{bmatrix} \begin{bmatrix} a/d_1 & b/d_2 & c/d_3 \\ d/d_4 &e/d_5 & f/d_6 \\ g/d_7 & h/d_8 & i/d_9\end{bmatrix}$
		- To reduce each row of a "row echelon form" matrix to it lowest term, i.e. "reduced row echelon form", we most often want to have all pivots to be 1. We can have this.  $\begin{bmatrix}d_{1} & & \\ & \ddots & \\ & & d_{r} \end{bmatrix} \begin{bmatrix}1 & u_{12}/d_1 & u_{13}/d_1 & \cdots \\ & 1 &  u_{23}/d_2 & \cdots \\ & & \ddots & \vdots \\ & & & 1 \end{bmatrix}$.
- Case 2: It is a 1 by n matrix
	- $\begin{bmatrix} \lambda_1 x_1 \cdots \lambda_nx_n \end{bmatrix} = \begin{bmatrix}  x_1 \cdots x_n \end{bmatrix}\begin{bmatrix}\lambda_{1} & & \\ & \ddots & \\ & & \lambda{r} \end{bmatrix}$
	- The first matrix is a (1 by n). The second matrix is (n by n). So it works.
	- If we switch the order of them. It becomes (n by n) x (1 by n). Which is not working in matrix multiplication. 

### Reduction pathways for matrices
- $A \rightarrow U \rightarrow D$
- Every matrices can be reduced to reduced row-echelon form.
- Every rref matrix, having their pivots, we can further reduce them to be diagonal matrix.



### [[LU decomposition]]


### Band matrix
- Defined as: A matrix which has only $w$ nonzero diagonals below and above its main diagonal. 
- Now considering doing elimination for row = 2, it involves 3 eliminations and 3 subtractions. 
- Computation time in a PC
	- For $n=1000$ matrix, in a PC it's 1 second.
	- According to $n^3$ rule, if n is doubled, then the cost is multiplied by 8.
	- If matrices are sparse (in practice most matrices are sparse), $A = LU$ is much faster. 
![[Pasted image 20221230131859.png]]
- Fig: band matrix




- [[singular matrix]]

---

- Rules for matrix operations
	- (AB)C = A(BC)
	- $(m \times n)(n \times p) = (m \times p)$
	- 4 ways to compute [[Matrix-matrix multiplication]]
		- 1. The entry in row $i$ and column $j$ of $AB$ is: (row $i$ of $A$) $\cdot$ (column $j$ of $B$)
		- 2. Matrix $A$ times every column of $B$: 
			- $A \begin{bmatrix} b_1, \dots, b_p \end{bmatrix} = \begin{bmatrix} AB_1, \dots, Ab_p \end{bmatrix}$
			- That is [[column picture]] of $B$. 
		- 3. Every row of $A$ times matrix $B$:  
			- $\begin{bmatrix} \text{row i of A} \end{bmatrix}\begin{bmatrix} 1&2&3 \\ 4&5&6 \\ 7&8&9 \end{bmatrix} =  \begin{bmatrix} \text{row i of AB} \end{bmatrix}$
			- That is [[row picture]] of $A$. 
		- 4. Columns multiply rows
			- $\begin{bmatrix} c_1 & c_2 & c_3 \end{bmatrix} \begin{bmatrix} r_1 \\ r_2 \\ r_3 \end{bmatrix} = (c_1)(r_1) + (c_2)(r_2)+(c_3)(r_3)$

- The laws of matrix operations
	- Associative law
	- Distributive law

- Block matrices and block multiplications

---


---
# Chapter 3 Vector space 
### Image

^a21ede
- [[column space]]


- [[column space]]
- [[row space]]
- 

### Row space

### Kernel
- We already have image = $C(A)$ 
- Kernel (in linear algebra) is a concept that deals with the inverse image of zero under a homomorphism
- A homomorphism is a mapping between two algebraic structures.
- The kernel of this homomorphism is the set of all elements in the domain that map to zero in the codomain.
- Application:
	- Provide insight into how different objects interact with each other
	- Determine whether two objects are related by a given homomorphism.

### Null space $N(A)$: 





---

[[Temperaty space]]

---
## Chapter 3: vector space and subspace

### Vector space
- Vector space is an algebraic structure in linear algebra that allows for the manipulation of vectors, where are mathematical objects that have magnitude and direction.
- Vector space is a set whose elements, often called vectors, maybe added together and multiplied by numbers called scalars.
- Vector spaces generalized Euclidean vectors.
- Vector spaces are characterized by their dimension, which specifies the number of independent directions in the space.
- The components of $v$ are real numbers, then we denote the space as $R^n$. For complex number components, we denote it as $C^n$, etc. 
- Requirements:
	- 1. If only positive value is allowed, it is not a vector space
		- Proof:
			- Vector space allows matrix addition and multiplications.
			- And it has restriction on "only positive number", the assumption above won't stand.
			- QED. 
- Properties:
	- 1. The space $R^n$ consists of all column vectors $v$ with $n$ components. The dimension of a vector space depends on the maximum $n$ among all vectors $v$. 
		- Matrices can be considered as a collection of column vectors 
		- (i.e. $\begin{bmatrix} v_1&v_2& \dots&v_n\end{bmatrix}$ and each vector $v_k$ are like $\begin{bmatrix} e_1 \\ e_2 \\ \vdots \\ e_n \end{bmatrix})$. In most of the case $e_k$ are just plain scalars. 
	- 2. It can be of finite dimension or infinite dimension, depending on the maximum number of linearly independent vectors. 
	- 3. Vector spaces satisfies 8 vector axioms. (associativity, commutativity, ...)
	- 4. At all times, the vectors that we need most are ordinary column vectors.
		- Examples:
			- $\begin{bmatrix} 4 \\  \pi \end{bmatrix}$ is in $R^2$
			- $(1,1,0,1,1)$ is in $R^5$
			- $\begin{bmatrix} 1+i \\ 1-i \end{bmatrix}$ is in $C^2$, $C$ denotes complex number
	- 5. Two essential vector operations go inside the vector space, produce linear combinations: 
		- To multiple $v$ by 7, multiply every components by 7.
		- To add vectors in $R^5$, add them a component at a time. 
		- "Inside the vector space" means the result stays in the space.
- More vector space
	- types
		- $M$: The vector space of all $2 \times 2$ matrices
		- $F$: The vector space of all real functions $f(x)$
		- $Z$: The vector space that consists only of zero vector
	- In each case we can add/multiply matrices to matrices, functions to functions, zero vectors to zero vectors. 
	- $F$ is infinite-dimensional.
- Function space
	- A set of functions between 2 fixed sets.
	- Often the domain and/or codomain will have additional structure which is inherited by the function space. 
- If $v$ and $w$ are in a vector space $S$ , every combination of these 2 vectors (span) must be in $S$. 

- The fact we have:
	- $\text{det}(A)= \begin{bmatrix} a_{11} & a_{12}\\ a_{21}&a_{22}\end{bmatrix} =(a_{11})(a_{22}) - a_{12}a_{21}$
	- $\text{det}(A - \lambda I) = \begin{bmatrix} a_{11}-\lambda&a_{12} \\ a_{21}&a_{22}-\lambda\end{bmatrix} =(a_{11} - \lambda)(a_{22}-\lambda) - a_{12}a_{21}$
- Step 1:
	- $det(A-\lambda I) = (a - \lambda)(b - \lambda)\dots(n - \lambda) = 0$ (by assumption, by looking at the pattern)
- Step 2: 
	- The goal is to discover the terms from the equation from step 1 so that:
		- 1. $\text{det}(A)$ on one side
		- 2. $\lambda_1\lambda_2\dots\lambda_n$ on the other side.
	- Say, if the matrix is 3x3, then the expansion would be like![[Pasted image 20230206101305.png]]
	- $\lambda_1\lambda_2\dots\lambda_n$ exists in the characteristic polynomial.  (the $x^3$)
	- But the remaining terms seems not looking like detA, because a lot of terms involves eigenvalue itself
	- ![[Screenshot 2023-02-06 101404.jpg]]


### Other special vector (space)
- Matrix space
	- In the space the vectors are really matrices
	- We add matrices to matrices. (fulfills rule 1 of subspace)
	- It can multiply scalars (fulfills rule 2 of subspace)
	- eg: 2x2 matrix space, each matrix has 4 components (identifiers). It is pretty much like n=4 vector space, except 2x2 matrix cannot add to n=4 vector. 
- Function space
	- The vectors are functions.
	- It is infinite-dimensional.
	- The smaller function space is $P$ , which contains all polynomials $a_0 + a_1x + \dots + a_n x^n$.
- Zero vector space
	- $Z$ is the smallest possible vector space
	- it can add another zero vectors (fulfills rule 1 of subspace)
	- It can multiply scalars (fulfills rule 2 of subspace)

### Subspace
- Subspace = A subset of some larger vector space. 
- Subspace could be 1 dimensional, 2 dimensional, ..., n dimensional. Or zero dimensional ($\mathbb{Z}$).
- Every subspace $R^m$ is contained within a vector space $R^n$. 
	- eg: $y=3x$ inside $R^2$. 
- A subspace of a vector space is a set of vectors (including 0) that satisfies two requirements
	- If $v$ and $w$ are vectors in the subspace and $c$ is any scalar, then
		- $v+w$ is in the subspace
		- $cv$ is in the subspace
	- Quarter-space and planes that don't contain the origin are not subspace. 
- A subspace containing $v$ and $w$ must contain all linear combinations $cv + dw$. 
- if we try to keep only part of a plane / line, the requirements for a subspace don't hold. 
	- why?
	- eg:
		- keep only vectors $(x,y)$ whose components are positive or 0. The vector $(2,3)$ is included but $(-2,-3)$ is not. So it violates rule 2, which the vector cannot multiple -1.
- The best description of a subspace is a basis. We 

- To get a subspace
	- 1. Start with any set of vectors in a vector space $V$. 
	- 2. With any combinations of set S (eg: 2 random vectors from $V$), we have all combinations of these set S vectors. 


### Column space of $A$
- Say matrix $A$ is sized in $m \times n$.
- The column space of $A$ contains all combinations of the columns of $A$: a subspace of $R^m$. 
- The column space contains all the vectors $Ax$, so $Ax = b$ is solvable when some $b$ is in $C(A)$, and not for other $b$
- It is the most important subspaces, because column spaces are tied directly to a matrix $A$.

- Describe column spaces for $I$:
	- It is the whole space $R^n$. Every vector is a combination of the columns of $I$. 
	- In vector space language, $C(I)$ is $R^n$. 

- Describe columns space for non-zero elements $2 \times 2$ matrix:
	- If column 1 is the multiple of column 2, The column space of it is only a line. The equation of $Ax = b$ is only solvable when $b$ is on the line. 

### Solving $Ax=0$ and $Rx=0$
- The $m \times n$ matrix can be square or rectangular.
- The right hand side is $b=0$, one immediate solution is $x=0$. For invertible matrices it is the only solution. 
- For invertible matrices to solve $Ax=0$, $x=0$ is the only solution for $b=0$
- For not invertible matrices, there are nonzero solution to $Ax=0$, each solution $x$ belongs to the nullspace of $A$.


![[Pasted image 20221231094917.png]]
- Fig: Demonstrating , clarify some misconceptions
	- For solving $Ax = b$, $b$ is solvable if b is in column space of $A$, namely $C(A)$. 
		- $C(A)$ is in dimension $R^m$.
		- Column vectors is also related to "the number of terms for a single basis vector"
	- For solving $Ax = 0$, we focus on the dimension of $x$ instead
		- $R(A)$ has the same number of component
		- So $x$ has dimension = $n$
	- For the whole matrix $A$, the matrix should be $R^{m \times n}$

- column space of $A$:
	- It contains all combinations of the columns of $A$, a subspace of $R^m$.
	- Start with the columns of $A$ and take all their linear combinations. This produces the column space of $A$. It is a vector space made up of column vectors. 
	- $C(A)$ contains not just the $n$ columns of $A$, but all their combinations $Ax$. 
	- Column space is crucial to the whole book of linear algebra, because the column space contains all the vectors $Ax$. So $Ax = b$ is solvable when $b$ is in $C(A)$.
	- Suppose A is an m by n matrix. So columns belongs to $R^m$. The columns space of $A$ is a subspace of $R^m$ (not $R^n$).
	- With $R^m$ column space, if we just have n columns and $n < m$ , $C(A)$ can't be all of $R^m$. 

![[Pasted image 20221227084605.png]]
- Fig: A matrix. 
	- We said "columns belongs to $R^m$, not $R^n$." The demonstration is as follow: We took a random column from this matrix. That column has m components. A row / column has m matrix, we would say it is.

![[Pasted image 20221227090826.png|400]]
- Fig: 
	- With $R^m$ column space, if we just have n columns and $n < m$ , $C(A)$ can't be all of $R^m$. 


### Nullspace
- This is a very important subspace. 
- $N(A)$ in $R^n$ contains all solutions to $Ax=0$. These vectors $x$ are in $R^n$. This includes $x=0$.(also fits the definition of subspace)
- Elimination ($A$ to $U$ to $R$) does not change the nullspace $N(A)=N(U)=N(R)$
- A nullspace for a vector is perpendicular to the vector itself.

- Example of nullspace
	- Consider $A = \begin{bmatrix} 1\ 2 \\ 3\ 6 \end{bmatrix}$, there is really only one equation, to describe the solution, we can choose one point on the line, then all points on the line are multiples of this point. 
	- So for $Ax = 0$, $N(A)$ contains all multiples of $s = \begin{bmatrix} -2 \\ 1 \end{bmatrix}$.



- Number of pivots = number of nonzero rows in $R = rank\ r$. There are $n-r$ free columns and then $n-r$ special solution for determining the nullspace. 
	- n: dimension of the matrix A
	- r: the rank of the matrix A
- Every matrix with $m < n$ has nonzero solutions to $Ax=0$ in its nullspace. 

### Basis / basis vector
- a set B of vectors in a vector space V is called a basis, if **every** element of V may be written in a unique way as a finite linear combination of elements of B. 
- Requirements / properties:
	- 1. Linear independence
		- The basis vectors $v_1, \dots, v_k$ are independent to each other.
	- 2. Spanning property
		- full collection of them span the space $S$. Which means, the set of vectors are already fully coverage the space $S$. 
- Properties:
	- 1. Unique bilinear representation 
		- Say $v = \begin{bmatrix} e_1 \\ e_2 \\ \vdots \\ e_n \end{bmatrix}$. There is one and only one way to write $v$ as a combination of the basis vectors. 
		- Every vector in the space is a unique combination of the basis vectors.
- Not required:
	- 1. Basis do not have to be unitary vector.
	- 2. Orthogonality
		- `[[1,0],[1,1]]` forms a non-orthogonal basis for $R^2$. But these basis are not orthogonal.
		- That is why we have Gram-Schmidt

- Video
	- plane
		- $a_1, a_2$ span a plane, so they are the basis of that plane.
		- Suppose we take the third vector $a_3$ as any linear combination of these 2 vectors, it is still on that plane. 
		- $a_3$ is dependent to $a_1, a_2$.
	- space
		- if $a_3$ is independent to $a_1, a_2$, these 3 vectors all together forms a space.
		- And these three vectors are the basis of that space. 
	- Dimension of subspace
		- = Number of basis vectors for the subspace

### Cardinality
- The cardinality of a set is a measure of the number of element of the set. 
- eg:
	- $A = \{ 2,4,6\}$ contains 3 elements, and therefore $A$ has a cardinality of 3. 

### Dimension of a vector space
- The dimension of a vector space $V$ is the cardinality of a basis of $V$ over its base field. 
- Properties:
	- 1. If $W$ is a linear subspace of $V$, then $\text{dim}(W) \leq \text{dim}(V)$
	- 2. The dimension is measured by counting independent columns / counting the number of pivots in a matrix
		- Dimension depends on the width ($n$) of the matrix, and totally not related to $m$ (the breadth of the matrix)
		- Why?
			- Attempt 1: Say we have a $m \times n$ matrix $A$. If $m \geq n$, then there exists at least $m - n$ amount of dependent rows in the sense of linear equation system. If $m \leq n$, there are $n - m$ dependent column vector that spans the space. End up only $\text{min}(m,n)$ amount of pivots in the matrix. 
			- Attempt 2: We could define a plane in a 3 dimensional space. Spanning a plane we just need any 2 vectors, and these vectors could be specified with 3D coordinates, or as many dimension as possible to define that vector. But it turns out the spanned subspace is 2 dimensional. 
	- 3. The true dimension of the column space is the rank $r$. 
- Conventions
	- $dim_F(F^n)=n$ for any field $F$. 
- Examples
	- $R^3$ has $\{ \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} , \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} , \begin{pmatrix}  0 \\ 0 \\ 1 \end{pmatrix}\}$ as a standard basis. and therefor $dim_R(R^3) = 3$. 



- Dimension versus rank
	- Dimension is just the length of the sequence of $x$ in $Ax = b$. Rank is the number of pivots (Fixed solution that can be obtained by a reduced echelon form matrix). Sometimes their values could be the same, sometimes not. 
	- when $n=r$ , (which means the matrix is a tall one, or a squared one), its nullspace $N(A) = \mathbb{Z}$ (zero vector).
- Q:
	- Say we have 4 variables and 2 linearly independent equations. What is the dimension.
- A:
	- We still need to look at whether there are dependent columns exist in the matrix. 

### Rank
- In linear algebra, the rank of a matrix $A$ is the dimension of the vector space generated (or spanned) by its columns.
- Properties:
	- 1. The rank of $A$ is the number of pivots. This number is $r$. 
	- 2. Rank $r$ could be smaller then either $m$ or $n$, for a $m \times n$ matrix
		- Rank is not coming from the size of the matrix. Like, a $n \times n$ matrix could have dependent columns or rows which turns out the matrix is having only rank $r$ less then $n$. 
		- eg:
			- $0 = 0$ should not count.
			- 2 identical rows in $A$ should not be counted twice in elimination.
			- if any rows is dependent to other rows, then that row should be eliminated as well.
	- 3. Rank theorem: column rank = row rank
		- Because the number of independent rows = the number of independent columns.
		- Proof 1: Turn $A$ into $rref(A)$ , simply count the number of pivots of column vectors is the same as the number of pivots of row vectors. 
		- Proof 2: say $A$ is $m \times n$ matrix. $r$ is column rank. Place basis for the column space of $A$ as $m \times r$ matrix $C$. Every column of $A$ can be expressed as a linear combination of the $r$ columns in $C$. That means there is an $r \times n$ matrix $R$ such that $A = C \cdot R$. $R$ is the matrix whose $i^{\text{th}}$ column is formed form the coefficient giving the $i^{\text{th}}$ column of $A$ as a linear combination of the $r$ columns of $C$. In other words, $R$ is the matrix which contains the multiples for the bases of the column space of $A$ (which is $C$). 
	- 4. $rank(A) = rank(A^T)$
		- The proof should be similar to property 3. 


### Elementary row operations
- The operation is similar to how we solve linear equation systems. 
- These elementary operations can be performed in two ways
	- 1. Directly on the rows of the system
	- 2. On the rows of the identity matrix, the system is then pre-multiplied by the resultant matrix. 
		- $RAx = Rb$
			- Say we have some elementary operations over some rows of $Ax = b$. 
			- First we add an identity matrix nearby $A$. 
			- Then we apply elementary row operations. $I$ captures those operations and then becomes $R$. 

### Elementary column operations
- These following operations are completely analogous to the elementary row operations performed on systems written vertically.
	- Multiplying a column by a non-zero constant
	- Adding a multiple of one column to another column
	- Interchanging columns
- Explanation:
	- We have 2 expressions for $Ax = b$
		- $x^TA^T = b^T$
			- Notice that, in the system of $x^TA^T = b^T$, each column is an equation. 
		- $x^TA^TR^T = b^TR^T$
			- In row operations, we have $RAx = Rb$
			- If we transpose both sides, we get $x^TA^TR^T = b^TR^T$, where $R^T$ is the matrix obtained by performing column operations on the identity matrix. 

- The steps of getting ranks
	- 1. Preprocessing
		- Rank is the number of pivots of a FULL RANK matrix. By FULL RANK, it means we need to takes out the rows that solely contains zeros ($0=0$), and the rows that are dependent to another rows. 
		- A better mechanical way should be making $A$ to be $rref(A)$ be elementary row operations. 
		- By doing these preprocessing, that would gives us the TURE SIZE of the matrix, which means not counting the $0 = 0$ rows. 
	- 2. Counting the pivots
		- The rank of the matrix is the number of pivots in the matrix.
		- Turning matrix into reduced echelon form, we can observe these pivots easier. 
- Getting the rank of a matrix
	- If we can get $0 = 0$ row, that row should not count as the true size of a linear system.
	- If there are any columns that are dependent (can be expressed as a linear combination of other vectors), three columns are linearly dependent. 

### Rank factorization


### Full column rank (r=n)
- Every matrix $A$ with full matrix rank ($r = n$) has all these properties:
	- All columns of $A$ are pivot columns
	- There are no free variables or special solutions
	- The nullspace $N(A)$ contains only the zero vector $x=0$.
	- If $Ax=b$ has a solution (it might not) then it has only one solution.




- Columns (Matrix times vector)
	- $Ax =$ combination of the columns of $A$. 
- Column vectors 
	- Column vectors with $m$ elements is an $m \times 1$ matrix consisting a single column of $m$ entries. 
	- column vectors - $v_1, v_2, v_3, v_4, \dots, v_n$ 
	- or $\begin{bmatrix} v_1 \\ v_2 \\ v_3 \\ \vdots \\ v_n \end{bmatrix}$
- Row vectors
	- $1 \times n$ matrix for some $n$, consisting a single row of $n$ entries $a = [ a_1\ a_2\ \dots\ a_n]$
	- Transpose of any row vector is a column vector and vice versa. 
![[Pasted image 20221226034620.png]]
- Fig: row vectors of a matrix

![[Pasted image 20221226034632.png]]
- Fig: column vectors of a matrix

### Field
- Many sets of elements have the familiar operations from arithmetic: addition, subtraction, multiplication and division. 
- Additions and multiplications $\in$ "binary operations"
- subtraction = additive inverse ($\neg$ addictive ? ) 
- division = multiplicative inverse
- Some relatives mathematical structure
	- If you can +/-, you have a group
	- if you can +/-/x, you have a ring
	- if you have +/-/x/div, you have a field.
		- the object behave similarly to the numbers you learned about in arithmetic and algebra.


### Vector field versus vector space
- Vector space: 
	- a set of possible vectors that can be added together and can be scaled using scalars from an associated field.
	- something like actual space, a bunch of points.
	- it is you can draw as a coordinate system
- Vector field: 
	- a map from some set into a vector space, which is achieved by choosing one vector at each point, provided that the vector field is smooth (infinitely differentiable over coordinates)
	- an association of a vector with every point in actual space
	- it is something you can draw a bunch of vectors al over your plane/space/etc

### Span / linear span (of a set $S$ of vectors)(from a vector space)
- the linear span (of a set $S$ of vectors)(from a vector space), is defined as the set of all linear combinations of the vectors in $S$. 
- To express that a vector space $V$ is a linear span of a subset $S$, one commonly uses the following phrase -- $S$ spans $V$.
	- $S$ is a spanning set of $V$. 
	- $V$ is spanned / generated by $S$. 
- Denoted as $\text{span}(S)$.
- formally definition:
	- given a vector space $V$ over a field $K$, the span of a set S of vectors is defined to be the intersection W of all subspaces of V that contain S. W is referred to as the subspace spanned by S, or by the vectors in S. Conversely, S is called a spanning set of W, and we say that S spans W. 
	- $S = \{ \sum_{i=1}^k \lambda_i v_i | k \in \mathbb{N}, v_i \in S, \lambda_i \in K\}$
		- k is in the set of Natural numbers
		- $\lambda$ is in the set of field K?
			- field types:
				- the field of rational numbers
				- the field of real numbers
				- the field of complex numbers 




- Matrix form of the equations
	- Multiplication by rows
	- Multiplication by columns
	- They are no different other than the notation.


---

### Complete solution to $Ax = b$
- s = $x_p$ + $x_n$ , where $x_p$ is the particular solution and $x_n$ is any null space vector in the nullspace. 
- ??




### Square matrix
- a matrix with the same number of rows and columns. 
- Two square matrices of the same order can be added and multiplied

### Identity matrix
- size $n \times n$ square matrix with ones on the main diagonal and zeros elsewhere.
- It is the whole space $R^n$. Every vector is a combination of the columns of $I$. 
- In vector space language, $C(I)$ is $R^n$. 

### Special solution
- When the pivots is less then the number of basis, or in other words, if $n > m$ in $A$, $A$ always has a free column. Then $Ax=0$ always have nonzero solution.
- To describe the solutions to $Ax = 0$, we make this in 2 steps
	- 1. Choose one point on the line, if the solution is going to be a line. That point is our special solution
	- 2. All multiples of that points would be our solution.

### Pivot variables
- 1. For a $m \times n$ matrix, the number of pivots depends on the $min(m,n)$ and there will be dependent variables (or we call them free variables) if $m \neq n$.
- 2. Pivot variables is something we have in reduced echelon form, which we can use the matrix to solve these variables by back substitution.
- 3. By comparing columns, we might be able to find out some columns are the linear combination of another columns. So we can tell which columns are free columns.
	- But no matter how we tune the values of those components. There is still a way to combine these columns to be dependent. (By LCM, least common multiplier)

![[Pasted image 20230102164446.png]]
- Fig: In this matrix, pivot means "the first non-zero entry in row echelon reduced form". So in this example, the pivot variables are x1 and x3. 


### Pivot columns
- The columns that contains pivot variables. 

### Free columns
- Free columns are the columns that contain free variables.
- Properties:
	- 1. If there are no free variables, the solution $x$ is unique.
	- 2. Every free column leads to a special solution. That free variable is 1, the other are 0.
	- 3. Every free column is a combination of earlier pivot columns. 
	- 4. $A$ always has a free column if $n > m$ 
	- 5. Free columns giving a nonzero solution to $Ax=0$
- Q: Why we consider "Free column", not "free rows"?
	- This is a bad question. A better question should be "Why we consider pivot columns, not free rows"
	- The actual thing we concern is how many "pivot columns" it has. The number of pivot columns = the number of variables of $x$ in $Ax=0$. 
	- Concerning "Free columns" because what matters is columns. 
	- Consider $Ax=0$ can be expressed as col1 X1 + col2 X2 + col3 X3 = 0, if any columns are the linear combination of the rest of other columns (dependent), then there is free columns that we assign any values to it, and also linear dependent to pivot columns. 
	- "Free rows" typically falls into the category of $0=0$ and its

- [[free variable]]
### Particular solution
- Particular solution exists if there are free variables in the linear equation system. 
- the particular solution $x_{\text{particular}}$ solves $Ax_p = b$.
- The $n - r$ special solution $Ax_{\text{nullspace}}$ solves $Ax_n = 0$.

### Triangular echelon matrix U
- Mentioned in p.149


### Independent columns
- The columns of $A$ are linear independent when the only solution to $Ax=0$ is $x=0$. The nullspace of the matrix $N(A)$ is $\mathbb{Z}$.
- No other combination $Ax$ of the columns gives the zero vector.
- If three vectors $w_1, w_2, w_3$ are in the same plane, they are dependent.
- In $R^2$, any three vectors $(a,b)$, $(c,d)$ and $(e,f)$ are dependent. 
- Independent columns produce full column rank $r = n$.  

### Independent vectors
- Independent vectors: the only zero combination $c_1v_1 + \dots + c_kv_k = 0$ has all $c$'s = 0.
- The sequence of vectors $v_1, \dots, v_n$ is linearly independent if and only if combination that gives the zero vector is $0v_1 + 0v_2 + \dots + 0v_n$.

### Spans
- The vectors $v_1, \dots, v_k$ span the space $S$ if $S$ is all combinations of $v$'s.




- For any $m \times n$ matrix $A$, if $m \neq n$, there always exists some vectors dependent to another vectors. 
	- 

---
- Multiple levels of looking at $Ax$
	- First level it is only numbers
	- Second level it is a combination of column vectors
	- Third level it shows subspaces
	- Fourth level shows "full picture" / relationships between subspaces
---
3.5 [[dimension]] for the four subspace 



---
## Chapter 4 - Orthogonality 


### Orthogonal vectors
- If $v$ and $u$ are orthogonal, their dot product is zero, then the following properties is true:
	- $v \cdot u  = v^Tw = 0$. (dot product property)
	- $||v||^2 + ||w||^2 = ||v + w||^2$ (orthogonal complement property) (can be proven by right triangle) 

### Orthogonal matrices
- Properties:
	- 1. Orthogonal basis i.e. $QAQ^T$ used in SVD (i.e. $\sum_i c_iu_iv_i^2$),  in theory says. will produce a smaller second piece and sequentially following pieces are also smaller.


### Orthogonal subspaces ($V^\perp$)
- Way two subspace $V$ and $W$ of a vector space are orthogonal if every vector $v$ in $V$ is perpendicular to every vector $w$ in $W$:
- Properties:
	- 1. $v^Tw=0$ , $\forall v \in V$ and $\forall w \in W$
	- 2. Orthogonality is impossible when $dimV + dimW > dim(whole space)$
		- The maximum dimension of the nullspace is determined by $dimV + dim_{\text{null}} = dim(whole space)$
			- If we are in 2D space. We find the nullspace for a plane. The nullspace is zero vector space.
			- If we are in 3D space. We find a nullspace for a plane (2D). The nullspace is a line (1D space)
			- If we are in 3D space, we find a nullspace for a line (1D). The nullspace is a plane (2D space)
	- 3. Every vector $x$ in the nullspace is perpendicular to every row of $A$, because $Ax = 0$. 
	- 4. The nullspace $N(A)$ and the row space $C(A^T)$ are orthogonal subspaces of $R^n$. 
- Examples:
	- 1. Row space is perpendicular to the nullspace
	- 2. The column space is perpendicular to the nullspace of $A^T$.

![[Pasted image 20230107090157.png|400]]
- Fig: Orthogonality is impossible when $dimV + dimW > dim(whole space)$

The process of getting that orthogonal nullspace
- Setup Ax = 0, the specific set of x that satisfies Ax = 0 we call that $x_\text{null}$
	- $x_\text{null}$ is orthogonal to row 1, row 2, …, row n of A, and also the linear combination of row i of A.
- Say, xy plane and the z axis are orthogonal subspace. Like a floor of a room and the line between 2 walls.
- If orthogonal subspaces fully compose the whole space, then they are orthogonal complements.  

### Orthogonal (subspace) complements
- The pair of orthogonal complements are not only perpendicular to each others, their basis vectors adding together also span the whole space. 
- Properties
	- 1. The orthogonal complement of a subspace $V$ contains every vector that is perpendicular to $V$. 
		- $V \perp V^{\perp}$
	- 2. $dim(V) + dim(V^{\perp}) = R^n$, $dim(V)=R^r$, $dim(V^{\perp})=R^{n-r}$
	- 3. For  every vector $b$ projecting onto a pair of orthogonal complement subspace. If we got $p_1$ and $p_2$. 
		- The vectors give $p_1 + p_2 = b$. 
		- The matrices give $P_1 + P_2 = I$. 
- Notation:
	- orthogonal subspace: $V^{\perp}$ 
- eg 1: 
	- Two lines could be perpendicular in $R^3$ but those lines could not be orthogonal complement in $R^3$ space. 
	- The correct dimension should be $dim(V) + dim(V^{\perp}) = R^n$
- eg 2:
	- Nullspace and row space are orthogonal complement in $R^n$.
	- Nullspace contains all vectors $\perp$ row space.
- eg 3:
	- Solve $Ax = b$ when there is no solution
		- if $m > n$, we are sure that there is no solution?
			- maybe we measure thousands time, so there is thousands equations. But maybe that's actually 6 variables. 

### Orthogonal decomposition
- This concept is closely related to "Orthogonal complement"
- The orthogonal decomposition of a vector $y \in R^n$ is the sum of a vector in a subspace $W \in R^n$ and a vector in the orthogonal complement $W^{\perp}$ to $W$. 
- let $x$ be a vector in $R^n$. 
- $x = x_w + x_w^{\perp}$, where $x_w$ is the closest vector to $x$ to $W$ and $x_{w^{\perp}}$ is in $W^\perp$.
- $Ax = Ax_r + Ax_n$
	- We already know that $x_r + x_n = x$ (property of orthogonal vectors)
	- The point of "complements" is that $x$ can be split into a row space component $x_r$ and a nullspace component $x_n$.
	- When $A$ multiplies $x = x_r + x_n$, it shows $Ax = Ax_r + Ax_n$


- Changes of spaces during multiplications (p.198 of the book)
	- The nullspace component goes to zero: $Ax_n = 0$
	- The row space component goes to the column space: $Ax_r = Ax$
	- Every vector goes to the column space $Ax = b$

- Every vector $b$ in the column space comes from one and only one vector $x_r$ in the row space.
	- Proof: If $Ax_r = Ax_r^{'}$ , 
		- the difference $x_r - x_r^{'}$ is in the nullspace. we have $Ax_r = Ax_r^{'} \rightarrow Ax_r - Ax_r^{'} = 0 \rightarrow x_r - x_r^{'} = 0$
		- It is also in the row space, where $x_r$ and $x_r^{'}$ came from.
		- The difference must be zero vector because the nullspace and row space are perpendicular. 
		- Therefore $x_r = x_r^{'}$
	- The difference must be zero vector, because the nullspace and row space are perpendicular. Therefore $x_r = x_r^{'}$
- Every matrix $A$ of rank $r$ has a $r \times r$ invertible matrix hiding inside $A$, if we throw away the two nullspace.
	- From the row space to the column space, $A$ is invertible. 
	- Every matrix can be diagonalized, where we choose the right bases for $R^n$ and $R^m$.

![[Pasted image 20230107164028.png|600]]
![[Pasted image 20230107164100.png|600]]

- If a vector $v$ is orthogonal to itself, then $v$ is the zero vector. 

### Uniqueness of solution
- Uniqueness, in math, refers to the property of being the one and only object satisfying a certain condition. 
- Denotation: $\exists !$ (means only one object satisfying that condition)
	- eg:
		- $\exists ! n \in \mathbb{N}(n-2 = 4)$
- Proving uniqueness:
	- eg:
		- Step1: Show at least 1 solution exists
		- Step 2: Assuming there are two solutions (say, $a$ and $b$)satisfying the solution. Substitute them to the equation and put it in parallel, and see whether could make use of transitivity of equality to put two equation. Turns out we get $a = b$ , which completes the proof that $a$ is the only solution. 

### Existence of solutions
- Existence means at least one solution can be determined for a given problem, a solution to that problem is said to exist. 
- It need not tell how many such objects there are, nor give hints on how to find them.
- Mathematicians seek to prove the existence of solutions (by means of existence theorem) and then investigate their uniqueness. 

### Uniqueness and existence on linear algebra

- Uniqueness implies existence
	- eg:
		- If there are no free variables, the solution $x$ is unique. (because there is no particular solution)
		- There must be $n$ pivot columns. 
		- Then back substitution solves $Ax = b$ (solution exists)
- Existence implies uniqueness
	- eg:
		- Suppose $Ax = b$ can be solved for every $b$ (Existence of solutions)
		- Then elimination produced no zero rows.
		- There are $n$ pivots and no free variables. 
		- The nullspace contains only $x = 0$ (uniqueness of solutions).


---


### [[Projection]]


---


### Flow of demonstration
- Flow of demonstration (13th Jan 2023)
	- 1. Describe the setup, objects. 
	- 2. Describe the relationship that is crucial
	- 3. Use up the relationship to determine the value we need. 
- Level of details
	- 1. General flow (often we would see many mathematics books don't have such clean general steps at the beginning of the detailed demonstration)
	- 2. Display the detailed steps

### Matrix as a set of column vector
- Matrix = a set of column vectors that could span a space. 
- We can write in the form of: 
	- $n$ vectors $a_1, a_2, \dots, a_n \in R^m$. and they could be either linearly dependent or independent. If there is at least $m$ linearly independent vectors in the matrix, the matrix span a full space. 
	- eg 1:
		- say we have a m x n matrix, each vector is in m-dimension. So for n > m, we have at most m independent vectors in the matrix. For m > n , 
	- eg 2:
		- For 1 dimension (a line). It is a single column vector. 

- Q: Is inverse matrix same as quotient, in general?
	- ordinary number quotients are commutative 
		- if we think of $a/b$,  $a/b = x$, $bx = a$ and $xb = a$. 
	- But matrix is not commutative. 
		- Say we have $AB^{-1}$ , $AB^{-1} = X$ , the only way is $A = XB$. 

for n = 1:
- Setup and objects:
	- To specify the object and the line, we would have at least two vectors. 
	- So say we project object $b$ onto the line $a$. 
	- We add a new item, projection $p$, to the problem. 
		- The direction is controlled by the plane, the magnitude is controlled by the object.  So we have the direction, and the only unknown is the proportion between $p$ and $a$. More than that, $p$ and $a$ is living in the same subspace. 
- The relationship: 
	- We use up the property of orthogonality to compute the changing ratio of $b$.
	- We introduce a new term $e$ , which is the difference of $b$ and $p$. 
		- $e$ could be expressed by $b$, $p$ (i.e. $\hat x$ and $a$)
		- By using up the property of  $e \perp a$ , we have 

- $A$:
	- The matrix a in 1 dimension is simply a column (or a vector)
	- So $p = a  \hat x$
- $\hat x$ :
	- Using the fact that the error vector is perpendicular to $a$, we have:
		- $a \cdot e = 0 \rightarrow a \cdot (b - \hat x a) = 0 \rightarrow \hat x = {{a \cdot b} \over {a \cdot a}}$
	- $\hat x = a^Tb / a^Ta$ when $n=1$ .
	- It is came from dot product
- $p$:
	- $p = \hat x a = {{a \cdot b} \over {a \cdot a}}a$


---

for n > 1:
- Task specification
	- Setup
		- To specify the object, and the plane, 
		- The line is in the column space of $A$, which has only one column.
		- In general the matrix $A$ has $n$ columns $a_1, a_2, \dots, a_n$ ; the vectors $a_1, a_2, \dots, a_n$ in the base. That is form the definition of $\hat x$. That is from the request from us. And we have to compute the actual value of $\hat x$. 
	- Key of the problem
		- The key of projections onto n-dimensional subspaces is, error $b - A \hat x$ makes a right angle with all 
	- 
	- The combination in $R^m$ are the vectors $Ax$ in the column space.
	- We look for a particular combination $p = A \hat x$ (the projection) that is closest to $b$. 
- eg: n =2 
- $A$:
	- 
- Strategy:
	- Looks for right proportions of columns so that the plane vector is perpendicular to the error vector.
	- Key: error vector, $b - A \hat x$ , is perpendicular to plane
- $\hat x$:
	- We are looking for the full dimension solution for $\hat x$ in coordinate $(\hat x_1, \hat x_2, \dots, \hat x_n)$
	- we have $a_1^T (b - A \hat x) = 0$ , $a_2^T (b - A \hat x) = 0, \dots , a_n^T (b - A \hat x) = 0$
	- $\begin{bmatrix} a_1^T \\ a_2^T \end{bmatrix} (b - A \hat x) = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$
	- $A^T (b - A \hat x) = 0$
	- Say $e = (b - A \hat x)$:
		- We compare $e$ with the 4 subspaces.
		- We have $A^T (b - A \hat x) = 0$, so $e$ is in $N(A^T)$
		- So $e \perp C(A)$
	- Come back to the equation:
		- $A^Tb = A^TA \hat x$, this equation gives us $\hat x$.
		- $\hat x = (A^TA)^{-1}A^Tb$
	- What's the projection?
		- $p = A \hat x$
		- $p = A(A^TA)^{-1}A^Tb$
		- So back to 1D, $A$ becomes a single column $a$. Then it is the same format. 
	- The projection matrix $P$ is $A(A^TA)^{-1}A^T$ 
	- $P^T = P$, $P^2 = P$ and $Pb = p$.

- Computing $\hat x$ and $P$: 
	- $A^TA$
		- When $A$ has independent columns, $A^TA$ is square, symmetric and invertible.
		- Square:
			- By looking at its size, $(m \times n)(n \times m)$ always produce square matrix
		- Symmetric:
			- $(A^TA)^T =A^T(A^T)^T = A^TA$ 
		- Invertible:
			- $A^TA$ is invertible if and only if $A$ has linearly independent columns. 
			- Proof:
				- 1. Show $A^TA$ has the same nullspace as $A$. 
				- 2. Show when the columns of $A$ are linearly independent, its nullspace contains only the zero vector. 
				- 3. When nullspace contains only zero vector. Then $A$ and $A^TA$ are both invertible. 

**![[Pasted image 20230107214208.png|600]]
![[Pasted image 20230107215434.png|600]]



---


- 4.3 Least squares approximations

- When $Ax = b$ has no solution, multiply by $A^T$ and solve $A^TA \hat x = A^T b$ 

![[Pasted image 20230108083932.png]]
- Example: 3 equations, 2 variables, which won't have exact solution.
	- The best solution is taken is to solve not $Ax = b$, but $A^T A \hat x = A^Tb$.
	- best = minimize the sum-squared error

![[Pasted image 20230108102555.png]]
- Approximate
	- error vectors: $e_1, e_2, e_3$ 
	- approximate vectors that lies on the line: $p_1, p_2, p_3$
		- The closest combinations
		- The column space
	- The out of line original vectors: $b_1, b_2, b_3$

- 

---
- 4.4 Orthonormal bases and Gram-Schmidt

### Diagonality
- When 2 vectors are orthogonal to each others. 
	- Their dot products are zero.
	- $A^TA$ will be diagonal. So it become easy to find $\hat x$ and $p = A \hat x$. 

---

### Different ways of proving identities in linear algebra
- 1. Elementary representation.
	- Example: prove $Q^TQ = I$ for orthogonal matrices 
		- The proof is, in $Q^TQ$, each row of $Q^T$ multiples with each column of $Q$. And each column of $Q$ are orthonormal vector. 
			- $Q^TQ = \begin{bmatrix}-&q_1^T&- \\ -&q_2^T&- \\  \vdots&\vdots&\vdots \\ -&q_n^T&-\end{bmatrix} \begin{bmatrix} |&|&\cdots&| \\ q_1&q_2&\cdots&q_n \\ |&|&\cdots&| \end{bmatrix}$
			- In the multiplication process:
				- Diagonal entries: 
					- only diagonal entries of the output matrix would return non-zero value. That used up the property of orthogonality $q_k = 1$ when $i=j$. And that value is 1 for column vectors $q_k$ of orthogonal matrix $Q$. 
					- $q_1^Tq_1$ = $\sum_i e_i^2 = ||l_1||^2 = 1$ 
				- Off-diagonal entries$(i \neq j)$: 
					- The dot product is zero by orthogonality.
			- Therefore, the final product of $Q^TQ$ is $I$. 
- 2.  
- 3. By working on example problems, with putting variable representation 
	- Example:
		- 
---


### Orthonormal / Orthonormality


- 4.1 Orthogonality of [[4 fundamental subspaces, or big picture of linear algebra]]

- Orthonormality: Two vectors in an inner product space are orthonormal if they are orthogonal unit vector.
- Description:
	- 1. The vectors $q_1, \cdots, q_n$ are orthonormal if: $\begin{cases} 0\  when\  i \neq j \\ 1\  when\  i = j \end{cases}$
		- The first case represents orthogonal vectors.
		- The second case represents unit vectors. $||q_i|| = 1$. 
	- 2. Orthonormal basis vectors will be the columns of a new matrix $Q$ in Gram-Schmidt process that combines the original basis vectors to produce right angles. 
		- $Q = \begin{bmatrix} |&|&\cdots&| \\ q_1&q_2&\cdots&q_n \\ |&|&\cdots&| \end{bmatrix}$
- Properties:
	- 1. A matrix $Q$ with orthonormal columns satisfies $Q^TQ = I$. So $Q$ are easy to work with. 
		- The proof is, in $Q^TQ$, each row of $Q^T$ multiples with each column of $Q$. And each column of $Q$ are orthonormal vector. 
			- $Q^TQ = \begin{bmatrix}-&q_1^T&- \\ -&q_2^T&- \\  \vdots&\vdots&\vdots \\ -&q_n^T&-\end{bmatrix} \begin{bmatrix} |&|&\cdots&| \\ q_1&q_2&\cdots&q_n \\ |&|&\cdots&| \end{bmatrix}$
			- In the multiplication process:
				- Diagonal entries: 
					- only diagonal entries of the output matrix would return non-zero value. That used up the property of orthogonality $q_k = 1$ when $i=j$. And that value is 1 for column vectors $q_k$ of orthogonal matrix $Q$. 
					- $q_1^Tq_1$ = $\sum_i e_i^2 = ||l_1||^2 = 1$ 
				- Off-diagonal entries$(i \neq j)$: 
					- The dot product is zero by orthogonality.
			- Therefore, the final product of $Q^TQ$ is $I$. 
	- 2. $Q^T = Q^{-1}$ / $Q^TQ = I$, when $Q$ is square 
		- Refer to property 1. 

### Orthogonal matrix (= orthonormal matrix) $Q$
- "Orthogonal matrix" = A real square matrix $Q$ whose columns and rows are orthonormal vectors. It other words, it is formed by the orthonormal basis vectors. 
- Requirements:
	- 1. Columns of $Q$ have to be orthogonal to each others.
	- 2. Each column of $Q$ have to be unit vector. So $\sum x_i = 1$.
- Representation
	- $Q = \begin{bmatrix} |&|&\cdots&| \\ q_1&q_2&\cdots&q_n \\ |&|&\cdots&| \end{bmatrix}$
	- Which $Q$ is the orthogonal matrix, $q_k$ are orthonormal basis vectors.
- Properties:
	- 1. $Q^T = Q^{-1}$
		- Proof:
			- $Q^TQ = \begin{bmatrix}-&q_1^T&- \\ -&q_2^T&- \\  \vdots&\vdots&\vdots \\ -&q_n^T&-\end{bmatrix} \begin{bmatrix} |&|&\cdots&| \\ q_1&q_2&\cdots&q_n \\ |&|&\cdots&| \end{bmatrix}$
			- In the multiplication process:
				- Diagonal entries: 
					- only diagonal entries of the output matrix would return non-zero value. That used up the property of orthogonality $q_k = 1$ when $i=j$. And that value is 1 for column vectors $q_k$ of orthogonal matrix $Q$. 
					- $q_1^Tq_1$ = $\sum_i e_i^2 = ||l_1||^2 = 1$ 
				- Off-diagonal entries$(i \neq j)$: 
					- The dot product is zero by orthogonality.
			- Therefore, the final product of $Q^TQ$ is $I$. 
			- QED.
	- 2. Undoing the transformation with $Q^T$ or $Q^{-1}$
		- From property (1), we can multiply an $Q^T$ or $Q^{-1}$ on the matrix to undo $Q$. 
	- 3. Length of each vectors = 1
		- Since the columns of $Q$ are orthogonal to each other. The length of each column is 1.
	- 4. Unitary transformation / Computational efficient
		- Because the length of the column of these columns is fixed and small (1). The number can never grow too large when the length of vectors are fixed. Stable computer code use $Q$'s as much as possible.
	- 5. Orthogonal matrices arise naturally from dot products
		- Orthogonal matrices preserve dot product, i.e. $u \cdot v = (Qu) \cdot (Qv)$
		- Proof: 
			- $(Qu) \cdot (Qv) = (Qu)^T (Qv) = u^TQ^TQv =  u^TIv = u^Tv = u \cdot v$
	- 6. Linear isometries (like: rotations, reflections, and their combinations) produces orthogonal matrices.
	- 7. Orthogonal matrices implies orthogonal transformation.
		- This property is the opposite of property 6
	- 8. Forming orthogonal group under matrix multiplication
		- $n \times n$ orthogonal matrices form the orthogonal [[group]] $O(n)$ under matrix multiplication.
			- Orthogonal group in dimension n $O(n)$ is the group of distance-preserving transformations of a Euclidean space of dimension $n$ that preserve a fixed point, where the group operation is given by composing transformations. 
			- The orthogonal group in dimension $n$ $O(n)$ is a subset of orthogonal matrices, whose invertible real matrices whose inverse is equal to its transpose. 
				- $O(n) = \{Q \in GL_n(\mathbb{R})|Q^T = Q^{-1}\}$
			- Importance
				- The orthogonal group with its subgroups is widely used in mathematics and the physical science. 
		- It is key to many algorithms in numerical linear algebra, such as $QR$ decomposition. 
		- It is key to MP3 compression too. 
	- 9. Canonical form 
		- If $Q$ is special orthogonal, then one can always find an orthogonal matrix $P$, a change of basis, that brings $Q$ into block diagonal form. $R_k$ are $2 \times 2$ rotation matrices. 
		- $P^TQP = \begin{bmatrix} R_1 && \\ &\ddots& \\ && R_k \end{bmatrix}$, if $n$ is even
		- $P^TQP = \begin{bmatrix} R_1 &&& \\ &\ddots&& \\ && R_k & \\  &&& 1\end{bmatrix}$, if $n$ is odd
- We call the matrix "Orthogonal matrix" when the inverse of the matrix is equal to the transpose of the matrix.
- Examples:
	- 1. Rotation matrix $Q$ : $\begin{bmatrix} cos\theta & -sin\theta \\ sin\theta & cos\theta \end{bmatrix}$
		- This matrix undo the effect of $Q$: 
			- $Q^T = Q^{-1} = \begin{bmatrix}cos\theta & sin\theta \\ -sin\theta & cos\theta \end{bmatrix}$
	- 2. Permutation matrix
		- Every permutation matrix is an orthogonal matrix, because their columns have 1 in different places. 
		- eg: $\begin{bmatrix} 1&0&0&0&0 \\ 0&0&0&1&0 \\ 0&1&0&0&0 \\ 0&0&0&0&1 \\ 0&0&1&0&0 \end{bmatrix}$
	- 3. Reflection matrix 
		- across x-axis $\begin{bmatrix} 1&0 \\ 0&-1 \end{bmatrix}$


- Using Orthogonal matrix in projection. $Q$ replacing $A$
	- $Q$ has orthonormal columns. Project onto its column space. What's the projection matrix that project onto a column space?
	- Recall section 4.2 
		- $p = A \hat x$ , $p = A(A^TA)^{-1}A^Tb$, $p = Pb$
	- Now we have $P = Q(Q^TQ)^{-1}Q^T$ 
		- What's nice is.$Q^TQ = I$, we don't need to do inverse anymore. 
		- So $P = QQ^T$. 
	- So $P = QQ^T = I$ , if $Q$ is square.
		- If we have a square matrix and independent columns. And even orthonormal columns. 
		- Then the column space is the whole space. 
		- What's the projection matrix onto the whole space The identity matrix. Because every vector is right where it's supposed to be. We don't have to move it by projections.
	- Checking projection matrix
		- 1. Projection matrix is symmetric
		- 2. Project the projection matrix, you won't move it a second time. 
			- So $PP = P$, or $(QQ^T)(QQ^T) = QQ^T$
				- $Q^TQ$ sitting at the middle that gives us $I$. So this is valid. 
	- Conclusion:
		- All of our messy formulas become simple when we have orthonormal basis.
		- eg:
			- Normal equation: $A^TA \hat x = A^T b$
				- Now $A$ is $Q$
				- $Q^TQ\hat x  = Q^Tb$
				- $\hat x = Q^Tb$ . No inversion involved. 
				- $\hat x_i = q_i^T b$. Most important formula for some major part of mathematics. 


### Permutation matrix
- What is permutation
	- Permutation of a set is an arrangement of its member into a sequence or linear order. It refers to the process of changing the linear order of an ordered set. 
- Permutation matrix
	- They are all square matrix. They look similar to an identity matrix. 
	- A permutation matrix is a square binary matrix that has exactly one entry of 1 in each row and each column, and 0 elsewhere. 
	- definition:
		- Given a permutation $\pi$ of $m$ elements: $\pi: \{1, \cdots, m \} \rightarrow \{1, \cdots , m\}$. We represent them in two-line form matrix. 
	- Properties:
		- 1. $P^{-1}$ is also permutation matrix.
		- 2. Any product $P_1P_2$ is again a permutation matrix.
		- 3. The simplest permutation matrix is $P=I$ (no exchanges)
		- 4. There are $n!$ permutation matrices of order $n$.
	- Example
		- $P_\pi = \begin{bmatrix} e_{\pi(1)} \\ e_{\pi(2)} \\ e_{\pi(3)} \\ e_{\pi(4)} \\ e_{\pi(5)} \end{bmatrix} = \begin{bmatrix} e_1 \\ e_2 \\ e_2 \\ e_5 \\ e_3 \end{bmatrix} = \begin{bmatrix} 1&0&0&0&0 \\ 0&0&0&1&0 \\ 0&1&0&0&0 \\ 0&0&0&0&1 \\ 0&0&1&0&0 \end{bmatrix}$
			- In this example, we want to change the order of a matrix by 1,4,2,5,3.
			- Depends on we put $P_\pi$ on the left hand side OR right hand side of the matrix. The effect differs. 
			- Say we put the $P_\pi$ on the right side. 
				- Say end-product matrix is $M_{new}$.  
				- We pick the second column of $R_\pi$ to look at how it works. 
				- It is (0,0,1,0,0). 
				- Every entries of the second column of $M_{new}$ is choosing the third element of their row.
			- Say we put the $P_\pi$ on the left side.
				- We pick the third row of $R_\pi$ to look at how it works.
				- It is (0,1,0,0,0)
				- Every entries of the third row of $M_{new}$ pick the value from the second row of the matrix. 



### [[Unstable Gram-Schmidt process]]



### Fundamental theorem of linear algebra
- Basic facts
	- 1. In $Ax = b$, Variables vector $x \in C(A^T)$. Which means $x$ belongs to the row space of $A$.
	- 2. In $Ax = b$, Solution vector $b \in C(A)$. Which means $b$ belongs to the column space of $A$. 
	- 3. We also rarely mention, but $y$ exists. In $A^Ty$, $y\in C(A)$. 
		- $y \neq b$, they are completely different thing.
		- $x \neq y$ if the matrix $A$ is not symmetric. In most cases, $x$ and $y$ are having different length.
	- 4Q: Why we need to study row space and left nullspace?
		- A: These two subspaces are not important when we are dealing with only one kind of associated entries for the matrix $A$. 
	- Properties
		- 1. Orthogonal complements 
			- The row space and nullspace of $A$ ($N(A)$ and $C(A^T)$) are orthogonal complements in $R^n$, The column space and left nullspace of $A$ ($N(A^T)$ and $C(A)$) are orthogonal complements in $R^m$.  
			- Column space and nullspace all together fills the whole space. Row space and left nullspace fills the whole space.
		- 2. Row-space column-space relationship
			- To traverse from row space to column space,  $Ax_{\text{row}} = b$
			- To traverse from column space to row space, $A^Ty_{\text{column}} = b'$ 
		- 3. Complete space representation during traverse.
			- $x = x_r + x_n$ 
			- $Ax = Ax_r + Ax_n = b + 0$

- [[Kernel space]]
![[Pasted image 20230216081322.png]]
- Fig: 
	- Source:
	- Image: [[(Book) Introduction to linear algebra +LA and learning from data , Gilbert Strang#^a21ede|Definition of image]]

![[Pasted image 20230107171053.png|300]]
![[Pasted image 20230107171105.png|300]]



---
## Chapter 5 Determinants

### Linearity
- The order of multiplication and additions won't affect the transformation, then it is linear transformation
	1. $T(u+v) = T(u) + T(v)$
	- 2. $T(\alpha u) = \alpha T(u)$
- Say we have 2 steps: (1) adds up 2 vectors, (2) reflects along the axis. If 2 steps are interchangeable that won't alter the outcome, it is linear. 

### Determinant
- Only applies for a square matrix
- The formula of determinant is which produces a single number
- To define determinant is pretty tricky, but if we can visualize it, it would be easier: for 2 x 2 matrix $\begin{bmatrix} a & b \\ c & d\end{bmatrix}$, the determinant is $ad - bc$. 
- Describing determinant
	- Leibniz formula: 
		- describe it as a sum of signed products of matrix entries such that each summand is the product of n different entries. And the number of these summands is $n!$
		- The formula is:  $$det(A) = \sum_{r \in S_n} sgn(\tau)\prod_{i=1}^na_{i,\tau(i)} = \sum_{\sigma \in S_n} sgn(\sigma)\prod_{i=1}^n a_{\sigma(i),i}$$, where $sgn$ is the sign function of permutations in the permutation group $S_n$, which returns +1 and -1 for even and off permutations, respectively. 
	- Laplace expansion:
		- Express the determinant of $n x n$ matrix as a linear combination of determinants of $(n-1)$ x  $(n-1)$ submatrices.
	- Gaussian elimination:
		- Express the determinant as the product of the diagonal entries of a diagonal matrix that is obtained by a succession of elementary row operations. 
	- For triangular matrices:
		- $\text{det}A = \prod_i a_{ii}$, which $a_{ii}$ denotes the main diagonal entries of the matrix $A$. 
- Properties:
	- 1. $\text{det}A = \prod_i a_{ii} = \prod_i \lambda_i$
		- Proof:
			- (Roughly) Characteristic polynomial for $det(A-\lambda I_n)$: $det(A-\lambda I_n) = (-1)^n(\lambda_1 - \lambda)(\lambda_2 - \lambda) \dots (\lambda_n - \lambda) = (\lambda - \lambda_1)(\lambda - \lambda_2)\dots(\lambda - \lambda_n)$
			- Since $\lambda$ is a variable, we can choose $\lambda = 0$. Which we can get $\text{det}A = (\lambda_1)(\lambda_2)\dots(\lambda_n)$
			- QED. 
	- 2. $\text{det}A = \prod_i a_{ii}$, where $a_{ii}$ is the main diagonal entries of the triangular matrix. 
		- Proof:
			- With big formula, we know a determinant could be expanded into $n!$ terms.
			- For a triangular matrix. All terms except the main diagonal strip would be non-zero.
			- QED. 
	- 3. From properties 1 and 2, we know that when at least one 
- Information
	- 1 Whether the matrix is invertible (non-zero determinant)
	- 2 If A is invertible, then the determinant of its inverse is $1/det(A)$.
	- 3 The determinant leads to a formula for every entry in $A^{-1}$
	- 4 For $\begin{bmatrix} a\ b\ \\ c\ d \end{bmatrix}$ has inverse $A^{-1} = {{1 \over {ad-bc}} \begin{bmatrix} d\ -b \\ -c \ a \end{bmatrix} }$
	- 5 For a 2 x 2 matrix, the pivots are $d - (c/d)b$. 
	- 6 The product of the pivots is the determinant: $a(d - {c \over a}b)$, which is $det(A)$
- Way of finding determinants
	- 1. Pivot formula --- Multiply n pivots
	- 2. Big formula --- Add up n! terms
	- 3. Cofactor formula --- Combine n smaller determinants
- Special note
	- a) 1 and -1 play a big part of determinants.
	- b) The determinant changes sign when two rows are exchanged. 
- Properties of the determinant
	- a) The determinant of the $n x n$ identity matrix is 1.
	- b) The determinant changes sign when two rows are exchanged
	- c) The determinant is a linear function of each row separately. 
		- The determinant is a linear function of each row separately. This rules only applies when the other rows remain unchanged
			- $\begin{vmatrix} ta & tb \\ c &d\  \end{vmatrix}$ = $t\begin{vmatrix} a & b \\ c &d\  \end{vmatrix}$
			- $\begin{vmatrix} a+a' & b+b' \\ c &d\  \end{vmatrix}$ = $\begin{vmatrix} a & b \\ c &d\  \end{vmatrix}$ + $\begin{vmatrix} a' & b' \\ c &d\  \end{vmatrix}$
	- $detA^T = detA$
	- Product rule of determinant: $detAB = (detA)(detB)$

### Column operations in determinant
- We have $\text{det}(A^T) = \text{det}(A)$ , which means we have use elementary column operations to evaluate determinants as well. Since a column operation on $A$ has the same effect as the corresponding row operations of $A^T$. 
- While we can do this on the determinant of a matrix, the same kind of actions cannot be applied on matrix. 


- 5.2 Permutations and cofactors


- Big formula for determinants
	- Requirements:
		- Rule 1 - det I = 1 - the determinant of the n by n identity matrix is 1
		- Rule 2 - Sign reversal - determinant sign change when two rows are exchanged
		- Rule 3 - Linearity - the determinant is a linear function of each row separately

- A computer finds the determinant from the pivots

### Cofactors


### Cross product
- Cross product is an optional application, special for $n$ dimensions. Unlike the dot product, which is a number, the cross product is a vector, also in $n$ dimensions.
- 
- Cross product is defined for vectors in three dimensions. 
	- 2 dimensions:
		- It produce a scalar quantity that is equal to the magnitude of the "cross product" vector.
		- We can calculate the magnitude of vector this way for 3D case.
	- 3 dimensions:
		- Direction of he "cross product" produced by that two vector that is pointing to the orthogonal direction of that two vectors. 
			- We can use "right hand curling finger" rule to find the direction of the cross product vector. 
		- Say $a = (a_1, a_2, a_3)$, $b  (b_1, b_2, b_3)$, then the component of $c$ would be:
			- $c_1 = a_2 b_3 - a_3 b_2$
			- $c_2 = a_3 b_1 - a_1 b_3$
			- $c_3 = a_1 b_2 - a_2 b_1$
	- Higher dimensions
		- While it is feasible to compute a cross-product in other dimensions, the cross-product only has the orthogonality property only in three dimensional spaces. 
		- or example, the wedge product is a generalization of the cross product to higher dimensions, but it does not have the property of producing a vector that is orthogonal to both of the input vectors.
- $u \times v$ = $\text{det} \begin{vmatrix} \vec i & \vec j & \vec k \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3  \end{vmatrix} = (u_2 v_3 - u_3 v_2) \vec i + (u_3v_1 - u_1v_3) \vec j + (u_1v_2 - u_2v_1) \vec k$
	- The beauty of this expression comes from orthogonality, as discussed in "big formula" session. 
	- We use the form of $ad - bc$ to calculate the the magnitude of the cross-product vector in each direction. And why it is $ad-bc$ could be explained by its geometrical interpretation of cross product. 
- $u \times v = - v \times u$
- Observation:
	- We could observe that, in cross product, we put the element of the first variable in the second row; put the element of the second variable in the third row.
	- Example 1:
		- $u \times v$ = $\text{det} \begin{vmatrix} \vec i & \vec j & \vec k \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3  \end{vmatrix} = (u_2 v_3 - u_3 v_2) \vec i - (u_3v_1 - u_1v_3) \vec j + (u_1v_2 - u_2v_1) \vec k$
	- Example 2:
		- $\vec \nabla \times \vec f = \begin{vmatrix} \vec i &\vec i & \vec k \\ \partial / \partial x & \partial / \partial y & \partial / \partial z \\ f_1 & f_2 & f_3 \end{vmatrix} = \vec i (\frac{\partial f_3}{\partial y} - \frac{\partial f_2}{\partial z}) -\vec j (\frac{\partial f_3}{\partial x} - \frac{\partial f_1}{\partial z}) + \vec k(\frac{\partial f_2}{\partial x} - \frac{\partial f_1}{\partial y})$



---

- Prove $(Ax)^Ty = x^T(A^Ty)$
- LHS = $x^TA^Ty$ 

## Ch 6 Eigenvalues and eigenvectors, eigen-decomposition

- [[Eigenvalues and eigenvectors]]

---




### Eigenvector / characteristic vector (of a linear transformation A)
- Origin of word: 
	- "Eigen": In Germen it means 'proper', 'characteristic', 'own'.
- "Eigenvector" = Vectors that map to their fixed scalar multiples, and the associated fixed scalars.
- "Eigenvector" are the certain exceptional vectors $x$ that are in the same direction as $Ax$. If $\lambda$ < 0: The direction is reversed when comparing to $Ax$. Loosely speaking, the eigenvector is not rotated. 
- The concept of eigenvector comes from the equation $Ax = \lambda x$. The eigenvector refers to $x$ in the equation.
- All other rest of vectors are combinations of two eigenvectors???
- examples
	- 1. $A = I$
		- If $A$ is identity matrix, every vectors has $Ax = x$. That means all vector are eigenvectors of $I$. 
	- 2. 2 by 2 matrices
		- Most 2 by 2 matrices have two eigenvector directions and two eigenvalues. 

- How to solve for $x$?
	- Fact: each specific $\lambda$ has a corresponding eigenvector $x$. It is a bilinear mapping between $\lambda_1, \lambda_2, \dots, \lambda_n$  and $x_1, x_2, \dots, x_n$ . 
	- 1. Using the fact that $A - \lambda I$ is singular to obtain $\lambda$ 
		- $Ax = \lambda x \rightarrow (A - \lambda I)x  = 0 \rightarrow A-\lambda I$ is singular, AND 
		- $det(A-\lambda I) = 0$
	- 2. Then we can plug back $\lambda_k$ to $Ax_k = \lambda_k x_k$ to get $x$ for n of them one by one.
		- We compute a matrix multiplication on LHS.
		- We simply multiply $\lambda_k$ with $x$ on RHS
	- 3. The problem becomes a map-reduced problem after we have done LHS and RHS separately. 
		- $\begin{bmatrix} \text{polynomial 1} \\ \text{polynomial 2} \\ \vdots \\ \text{polynomial n}\end{bmatrix} = \begin{bmatrix} \lambda_1 a_1 \\ \lambda_2 a_2 \\ \vdots \\ \lambda_n a_n\end{bmatrix}$
	- 4. $x = \begin{bmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{bmatrix}$

- [[Trace]]

- [[eigenvalues]]





---
### Decay state
- It describes an eigenvector that virtually disappears, because $0 < \lambda < 1$.
- The higher the power of $A$, the more closely its columns approach the steady state. 

### Steady state
- It describes an eigenvector that doesn't change, because $\lambda = 1$. 
- When $\lambda = 0$



---

- Special matrices

### Singular matrices
- Singular matrices have $\lambda = 0$; 
- Singular matrices are all non-invertible. 

### Triangular matrices
- Triangular matrices = A special kind of square matrix.
	- It is called upper triangular if all the entries below the main diagonal are zero. Vice versa. 
- Triangular matrices have $\lambda$'s on their diagonal. It is because the trace minus $\lambda I$ forms up the lambda polynomial by itself already. 
		- Because triangular matrices would just produce 
		- eg: $\begin{pmatrix} 1 & 5 \\ 0 & 6 \end{pmatrix}$ has $\lambda = 1$ and $\lambda = 6$ as eigenvalue. 
- Eigenvalue and determinant
	- The product of the $n$ eigenvalues equals the determinant
- Eigenvalue and diagonal entries
	- The sum of the $n$ eigenvalues equals the sum of the $n$ diagonal entries. 
	- $\lambda_{1} + \lambda_{1} + \cdots + \lambda_{n}$ = trace = $a_{11} + a_{22} + \cdots + a_{nn}$  
		- Why this is true?
			- 1. We obtain lambda from (A- lambda)x = 0. Diagonal entries becomes (aij - lambda), which later forms up the determinant polynomial. Each pair of (aij-lambda) could be equal to zero. So aij = lambda. 
			- 2. Each possible lambda comes from each specific (aij - lambda) pairs. So they are bilinear. 

### Eigenvector matrix $X$
- Eigenvalue and eigenvector matrix $X$
	- Eigenvector matrix is a list of eigenvector, in the context of generalizing which we might have n eigenvector in a question.  
	- When we apply $Ax = \lambda x$ , $A$ pairs up with $X$. And $x_1$ pairs up with $\lambda_1$ $ ; $x_n$ pairs up with $\lambda_n$. Because those pairs are come up in the same bracket in the polynomial we got from $det(A - \lambda I) = 0$.
	- $AX = A \begin{bmatrix} x_1 \cdots x_n  \end{bmatrix} = \begin{bmatrix} \lambda_1x_1 \cdots \lambda_nx_n  \end{bmatrix}$. The rightmost expression can be factorized a single lambda value matrix and a single eigenvector matrix $X$


### Eigenvalue of $AB$
- Wrong proof: $ABx = \beta\lambda x$
	- Usually matrix $A$ and $B$ don't share the same eigenvector $x$. 
- Property
	- $A$ and $B$ share the same $n$ independent eigenvectors if and only if $AB = BA$. 


### Elimination and $\lambda$
- Elimination does not preserve the $\lambda$'s 
	- $U$ has its own eigenvalues, sitting along the diagonal, but they are not the eigenvalues of $A$. 
- The product of $n$ eigenvalues equals the determinant; the sum of $n$ eigenvalues equals the sum of the $n$ diagonal entries. 



### Complex conjugate
- Square rooting negative numbers gives us complex conjugate. 
- In the form of $\alpha \pm \beta i$.

### Typical transformations
- Special properties of a matrix lead to special eigenvalues and eigenvectors. 

- Summarizing these typical transformations:

| |Tranformation matrix|eigenvalue|eigenvector|
|---|---|---|---|
|reflection|$\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$|$\lambda$ = 1 and -1|$x_1 = (1,1)$ \ $x_2 = (1,-1)$|
|projection|$\begin{bmatrix} .5 & .5 \\ .5 & .5 \end{bmatrix}$|$\lambda$ = 1 and 0|$x_1 = (1,1)$ \ $x_2 = (1,-1)$|
|rotation|General: $R(\theta) = \begin{bmatrix} cos(\theta) & -sin(\theta)  \\ sin(\theta) & cos(\theta) \end{bmatrix}$  |$\lambda$ = $e^{i\theta}$|$\begin{pmatrix} 1 \\ i \end{pmatrix}$ , $\begin{pmatrix} 1 \\ -i \end{pmatrix}$|


- and more

---


###  $AX =  X \Lambda$ (Matrix form of a series of $Ax = \lambda x$)
- Suppose the n by n matrix. $A$ has n linearly independent eigenvectors $x_1, \cdots, x_n$. 
- What is matrix form: 
	- Diagonalized matrix $A$ = $X\Lambda X^{-1}$, which $X$ is eigenvector matrix, $X = \begin{bmatrix} x_1, x_2, \cdots, x_n \end{bmatrix}$ and each entry $x_n$ could be something like $\begin{bmatrix} a \\ b \\ c \end{bmatrix}$ . The length of $x_n$ depends on $A$. 
- Steps of getting the two side matrix form $AX = \Lambda X$ from the knowledge up to chapter 6.1: 
	- LHS:
		- At first we can just express a list of $Ax_i$ into $\begin{bmatrix} x_1 & \cdots & x_n  \end{bmatrix} = AX$
		-  $AX = A \begin{bmatrix} x_1 & \cdots & x_n  \end{bmatrix}$
			- Note: $x_1, \dots, x_n$ are independent column vectors 
	- RHS:
		- We keep using $AX = A \begin{bmatrix} x_1 & \cdots & x_n  \end{bmatrix}$ from the above expression of LHS, and write the upcoming process on the RHS.
		- Element-wise multiplying $A$ with $x_i$,  we have $A \begin{bmatrix} x_1 & \cdots & x_n  \end{bmatrix}$ = $\begin{bmatrix} \lambda_1x_1 & \cdots & \lambda_nx_n  \end{bmatrix}$
		- Factorize $\Lambda$ from $\Lambda X$: $\begin{bmatrix} \lambda_1x_1 & \cdots & \lambda_nx_n  \end{bmatrix}$
			- Dimension: $(1 \times n)$
		- The way of factorizing it would be $\begin{bmatrix} x_1 \cdots x_n  \end{bmatrix}\begin{bmatrix} \lambda_1 & & \\ & \ddots & \\ & & \lambda_n \end{bmatrix}$
			- dimension: $(1 \times n)(n \times n)$
	- Afterall:
		- $AX = A \begin{bmatrix} x_1 & \cdots & x_n  \end{bmatrix} = \begin{bmatrix} \lambda_1x_1 & \cdots & \lambda_nx_n  \end{bmatrix}$ = $\begin{bmatrix} x_1 \cdots x_n  \end{bmatrix}\begin{bmatrix} \lambda_1 & & \\ & \ddots & \\ & & \lambda_n \end{bmatrix} = X \Lambda$
	- So now we have $AX = X \Lambda$, and also $A = X\Lambda X^{-1}$
### Diagonalizing a matrix in general
- Motivation:
	- $A^k = (X\Lambda X^{-1})(X\Lambda X^{-1}) \dots (X\Lambda X^{-1}) = (X\Lambda^k X^{-1})$
	- Computing $\Lambda^nX$ is much more efficient because  $\Lambda$ is diagonal matrix, and computing its square is very easy. It sweeps away the cost of computation. 
- Resource:
	- We already have the collection of eigenvalues for the matrix $A$. 
	- We already have the set of eigenvectors $x_1, \cdots, x_n$. Which allows as to prepare $X = \begin{bmatrix} x_1, x_2, \cdots, x_n \end{bmatrix}$
	- The set of eigenvalues $\lambda_1, \cdots, \lambda_n$
- Goal:
	- Diagonalization of a matrix means "producing a diagonal eigenvalue matrix in the middle, and have another matrix that is on the left and right side of that eigenvalue matrix. Such that we can use the eigenvalue matrix telescoping it faster when we have to multiply some matrix a lot of times."
	- Once we have $AX$, we want $\Lambda^n X$ to be applicable to replace $A^n$. 
	- We still need to obtain $x_1, x_2, \dots, x_n$ and $\lambda_1, \lambda_2, \dots, \lambda_n$ by ourselves by the method we had in section 6.1. That gives us $A$ and $X$. 
	- Milestone:
		- Determine "eigenvalue matrix $\Lambda$" and "eigenvector matrix $X$"
- Steps:
	- determine $\Lambda$:
		- Method 1: We have $AX = X\Lambda$, so to determine $\Lambda$, we use $\Lambda = X^{-1}AX$ 
		- Method 2: We have $\lambda_1, \lambda_2, \dots, \lambda_n$, so we can just put in each of them into main diagonal to form the eigenvalue matrix directly. 
	- determine $X$:
		- Just put in eigenvectors from left to right one by one sequentially. 
	- Compute $A^k =  (X\Lambda^k X^{-1})$
- Limitations:
	- Diagonalizability
- If we have $A^k$ and having $k$ goes to infinite, it will approach zero if all $| \lambda| < 1$.


### Diagonalizing an orthogonal matrix
- $S = Q\Lambda Q^{-1}$, where $S$ is symmetric matrix, $Q$ is orthogonal matrix. 

### Diagonalizable / non-defective matrix 
- While invertibility is concerned with the value of eigenvalues, diagonalizability is concerned with the total number of distinct eigenvalues.
- Definition
	- A square matrix $A$ is called diagonalizable or non-defective if it is similar to a diagonal matrix
		- i.e. there exists an invertible matrix $P$ and a diagonal matrix $D$ such that $P^{-1}AP = D$.
	- A matrix is diagonalizable if and only if its eigenvalues are distinct (non-repeating)
- Properties
	- 1. They are square matrix?
	- 2. They can be changed into a diagonal matrix by multiplying them with other matrices?
		- i.e. can be written as a product of a diagonal matrix and an invertible matrix.
	- 3. The number of linearly independent eigenvectors of a diagonalizable matrix equals the number of nonzero entries on its main diagonal. 
- Application
	- Every symmetric or Hermitian matrix is also a normal matrix, which implies it is always diagonalisable.



### Similar matrices
- Definition:
	- Matrix $A$ and $B$ are similar to another if and only if there exists a matrix $P$ such that $B = P^{-1}AP$. 
	- The transformation of $A$ into $P^{-1}AP$ is called similarity transformation. 
	- As we change $P$, we get a whole family of different matrices. All those matrices are called similar, while we keep $A$ unchanged. 
- Requirements:
	- 1. "matrix $A$ and $B$ are sharing the same eigenvalue matrix $\Lambda$, which contains the exactly same number of eigenvalue having the same value.". The  only difference is the basis (eigenvector), which can be arbitrary.
- Properties:
	- 1. Same determinant
		- Proof:
			- Suppose $A$ and $B$ are similar.
			- $det(B) = det(P^{-1}AP) =  det(P^{-1})det(A)det(P) = det(A)$
			- QED
	- 2. Same trace
	- 3. Same eigenvalues 
		- Proof:
			- The strategy is to puzzle the determinant expression of  lambda to end up with same value. Some extra terms would be cancelled out. 
			- 1. Any eigenvalue $\lambda$ of $A$ solves the characteristic equation $det(\lambda I - A) = 0$
			- 2. While the similar matrix would be: $det(\lambda I - B)$
				- $= det(\lambda P^{-1}P - P^{-1}AP)$
				- $= det(P^{-1}[\lambda I - A] P)$
				- $=det(P^{-1})det(\lambda I - A)det(P)$
				- $=det(\lambda I - A)$
			- QED
	- 4. Same rank
	- 5. Similar matrix power
	- 6. Unitarily similar
- Applications:
	- When diagonalizing a matrix,  we have an expression$A = (X\Lambda X^{-1})$. $A$ and $\Lambda$ satisfies the definition of similar matrices.



### Extending similar matrices concept to non-diagonalizable matrices
- Say $C$ denotes one constant matrix. $B$ denotes all invertible matrices. 
- For the matrices $A = BCB^{-1}$. All $A$ are similar --- they all share the eigenvalues of $C$. 


### Application example: Fibonacci
- Slow way: $F_{k+2} = F_{k+1} + F_k$
- Faster: $u_{K+1} = Au_K$.  
	- $\begin{cases} F_{k+2} = F_{k+1}  + F_k \\ F_{k+1} = F_{k+1} \end{cases}$
	- We then write it in matrix form.
		- $u_{k+1} = Au_{k}$
		- $u_k = \begin{bmatrix} F_{k+1}  \\ F_{k} \end{bmatrix}$
		- Then we have $u_{k+1} = \begin{bmatrix} 1 & 1  \\  1 & 0\end{bmatrix} u_k$. Which we can consider the right hand side as our $Ax$. 
		- $\lambda$:1.618 and -0.618
		- eigenvectors $x$: ($x_1: \lambda 1,1$, $x_2: \lambda 2,1$)
		- Diagonalize $A$, we have: $A = S\Lambda S^{-1}$


---
6.3 Application of $Ax = \lambda x$ in systems of differential equations

### Express differential equation as linear transformation.
- The task is i.e. Express $du/dt = Au$
- $A = X \Lambda X^{-1}$ also perfect for $du/dt = Au$. 
- 2 ODEs are solved by "growth factors" exponentials  $Ce^{\lambda t}$
	- $du/dt = u$ , which produces $u(t) = Ce^t$
	- $du/dt = \lambda u$ , which produces $u(t) = Ce^{\lambda t}$
	- Check: $du/dt = Au$: 
		- We could try these solutions by plug it back to the equations: say, the second case would becomes $\lambda_1 e^{\lambda_1 t}x_1=Ae^{\lambda_1t}x_1$. Simplify it, $\lambda_1 x_1 = A x_1$.So $u(t)$ is checked. 
- The solution grows when $\lambda > 0$. The solution decays when $\lambda < 0$. If the solution is a complex number, the real part decides growth or decay. The imaginary part $\omega$ gives oscillation $e^{i \omega t}$ like a sine wave. 
- Solution of ODE would be: $u(t) = c_1e^{\lambda_1 t}x_1 + c_2 e^{\lambda_2 t}x_2$. What are $c_1$ and $c_2$?
- without LA, we could solve 1 by 1 problems. LA moves to n by n.

---

- eg:
- we have $y''' + 2y'' -y' -2y = 0$.
- Express this ODE in LA form $u'(t) = Au(t)$, we have:$$\begin{bmatrix} y''' \\ y'' \\ y' \end{bmatrix} = \begin{bmatrix} -2 & 1 & 2 \\ 1 &0 &0 \\ 0&1&0 \end{bmatrix}\begin{bmatrix} y'' \\ y' \\ y \end{bmatrix}$$
	- The value of the first row of the matrix is referred to $y''' + 2y''-y'-2y = 0$. 
	- The second and the third row is just mimicking a single variable itself. 
- Compute eigenvalue: $det(A - \lambda I)$. The polynomial gives lambda = 1, -1, -2. The eigenvector could be $(1,1,1)^T$, $(1,-1,1)^T$, $(4,-2,1)^T$.
- $u(t) = C_1e^tx_1 + C_2e^{-t}x_2 + C_3e^{-2t}x_3$.
- The first column of $exp(At)$ would be:
---
### Markov matrix / Stochastic matrix / probability matrix / transition matrix / substitution matrix 
- What is it?
	- All entries $\geq 0$
	-  A Markov matrix $A$ always has an eigenvalue 1, and all other eigenvalues are $|\lambda| \leq 1$.  
		- (we wonder why)
	- All components of eigenvector $x$ are positive ($x_i \geq 0$), if the start was? 
	- These properties turns out a Markov matrix must have an eigenvalue = 1. (why?)
	- The largest eigenvalue is 1. 
- General form: 
	- $u_K = A^K u_0 = c_1\lambda_1^Kx_1 + c_2\lambda_2^Kx_2 + \cdots$.  (that's just inheriting a simple $Ax = \lambda x$ property) (that requires a complete set of eigenvector.)
	- If $\lambda_1 = 1$, other $\lambda$s are smaller than 1, then with a large $K$, $u_K = c_1\lambda_1^Kx_1 + 0 + \cdots$
	- We call $u_K = c_1\lambda_1^Kx_1$ "Steady state". 
- Properties
	- lambda value smaller than 1, which could be classified as "decaying mode".
	- Squaring up the matrix, those properties would be true again.
 - Applications
	 - Describe the transitions of a Markov chain.
	 - Population and economics. Probability theories, statistics, mathematical finance and linear algebra. Computer science and population genetics. 
	 - Can be used to describe the transition of a Markov chain. Each of its entries is a nonnegative real number representing a probability. 
- More types of Markov matrix: Left, right and doubly
	- Right stochastic matrix = All rows add to 1. 
	- Left stochastic matrix = All columns add to 1.
	- Doubly stochastic matrix = Each row and column add to 1. 
- Convention
	- Use row vectors of probabilities and right stochastic matrices, rather than column vectors of probabilities and left stochastic matrices. 




- eg:
	- $\begin{bmatrix} .1 & .01 & .3 \\ .2&.99&.9 \\ .7&0&.4\end{bmatrix}$
	- $A - \lambda I$ = $\begin{bmatrix} -.9 & .01 &.3 \\ .2 & -.01 & .3 \\ .7 & 4 & -.6 \end{bmatrix}$
	- All columns adds to zero. $A - I$ is singular. 
		- How do we see it is singular
			- Columns are dependent?
			- Rows are dependent?
			- We could show both of them, by Adding all columns / rows into one column / row. That gives us 0 row. When any row / column the entries are all zeros. That row / column are dependent to any other rows. 
	- Null space
		- (1,1,1) is in the left null space $N(A^T)$
		- then the eigenvector $x_1$  is in the null space $N(A)$

---
- 6.4 Symmetric matrices

### [[Spectral theorem]]



### Symmetric matrices


### Good matrices (in the lecture)
- Real eigenvalues
- Perpendicular eigenvectors
- $A = A^T$ if $A$ is real
- $A = \bar A^T$ if $A$ is complex 

### Modulus
- Modulus is the absolute value of a real or complex number. 
	- For complex number, we define the absolute value $|z|$ as being the distance from $z$ to 0 in the complex plane $C$. 
- $|z|$ is called modulus of $z$. and its value would be $|z| = \sqrt{a^2 + b^2}$ for $z = a + bi$. 
- Properties:
		- 1. $\bar z z = z \bar z = |z|^2$
		- Proof:
			- $|z| = \sqrt{a^2 + b^2}$
			- $z \bar z = a^2 - (-1)b^2 = a^2 + b^2 = |z|^2$ 


### Complex conjugate (of a complex number)
![[Pasted image 20230204033153.png|150]]
- Complex conjugate is a function/transformation for the object, and it is found by reflecting $z$ across the real axis. 
- It is the number with:
	- 1. an equal real part and 
	- 2. an imaginary part equal in magnitude but opposite in sign.
- EG:
	- We have complex number $z = a + bi$
	- The conjugate of it would be $\bar z = a - bi$
- Polar form:
	- $z = re^{i \theta}$
	- $\bar z = re^{-i \theta}$
- Conjugation
	- 1. Equations: Say we have $a = b$. We could apply conjugate to both sides. so $\bar a = \bar b$. 
- Properties:
	- 1. Distributive over addition, subtraction, multiplication and division 
		- $\bar{z + w} = \bar z + \bar w$. 
	- 2. $z = \bar z$ if its imaginary part is zero. 
		- In other words, real numbers are the only fixed points of conjugation.
	- 3. Conjugation does not change the modulus of a complex number:
		- $|\bar z| = |z|$.
	- 4. The product of a complex number with its conjugate is equal to the square of the number's modulus:
		- $z \bar z = |z|^2$
		- Proof:
			-  See "Modulus"
	- 5. From property 4, it is easy to compute multiplicative inverse of a complex number given in rectangular coordinates
		- $z^{-1} = {\bar z \over |z|^2}$
	- 6. Conjugation is commutative under composition
		- $\bar {z^n} = {(\bar z)}^n$ for all $n \in Z$. 
		- $exp(\bar z) = \overline{exp z}$
	- 7. $|z + w| \leq |z| + |w|$
		- Triangular inequality on the complex plane. 

### Complex eigenvalues of real matrices 
- Important application:
	- Fast Fourier transform, Fourier matrix make FFT become fast (might be the most important)
- Normally $n \times n$ matrix multiplications we have $n^2$ multiplications. FFT reduces the computation down to $n log(n)$. 
- When we transpose a complex matrix, we also take conjugation of it.
	- Example
		- $Z = \begin{bmatrix} z_1 \\ z_2 \\ \vdots \\ z_n \end{bmatrix}$, where $z_1$ is in $C^n$. 
		- $Z^TZ$ is not good. because the length square is not positive. 
		- ${\bar Z}Z$ is good because we can get positive length, where $\bar Z$ is conjugate of $Z$. 
		- so $\bar z_1z_1 = |z_1|^2$. I don't know why. ($z = a+bi$ , $\bar z = a - bi$)
- Symmetric matric means $A^T = A$. But its not good if $A$ is complex. So we put $\bar A^T = A$. So that is a right complex version of symmetry. 
	- So now, 
		- 1) the diagonal entries have to be real, because it remain itself after flipping it. 
		- 2) off-diagonal entries could be complex.
		- These matrices are called Hermitian matrices. 
		- These matrices have real eigenvalues.
		- And they have perpendicular eigenvectors $q_1, q_2, \dots, q_n$. 
			- "perpendicular" means the inner product of those eigenvectors $\bar q_i^Tq_j$, equal to 0 if $i \neq j$. equal to 1 if $i = j$. 
			- $\bar Q^TQ = Q^HQ = I_n$


### Hermitian matrix
- Named after the mathematician Hermite.
- For a complex matrix, whenever we take transpose, we also take conjugation of it. Hermitian matrix is one symbol to do both.
	- Same for the situation when we have dot product for complex matrices. 
- $z^Hz$ = $\bar z^Tz$
- $Z^HZ = |z_1|^2 + |z_2|^2 + \dots + |z_n|^2$  (from inner product)

### Fourier matrix
- $F_n = \begin{bmatrix}  1 &1&1&\dots &W^{n-1}\\ 1&W&W^2&\dots &W^{2(n-1)} \\ \vdots&\vdots&\vdots&\vdots & \vdots \\ 1&W^{n-1}&W^{2(n-1)}&\dots &W^{(n-1)(n-1)} \end{bmatrix}$
	- Math people start start off the first column of Fourier matrix with ones. 
	- Electrical engineers start off the first column of Fourier matrix with zeros. But they end at $n-1$. 
- $(F_n)_{ij} = W^{ij}$, $i,j = 0,1,2,\dots, n-1$
- $W^m = 1$

### Antisymmetric matrices
- Antisymmetric matrices $A = -A^T$ have imaginary $\lambda$'s and orthonormal (complex) $q$'s.

---
- 30 years ago, people have no idea of how to compute eigenvalues of like 50x50 sized matrices. 
	- Find the roots of 50-degree polynomial is a very bad way to compute it. 
		- It is good for 2x2 or 3x3
	- But computer is happy to find 50 pivots. 
		- We could see like 28 of them are positive etc. 
		- 1. The sign of pivots' are same as the signs of the eigenvalues'.
		- 2. The number of pivots' are same as the number of the eigenvalues'.
		- By 1 and 2, we can shift the matrix by, say, 7 times the identity.
	- And "product of the pivots = product of the eigenvalues", why?
		- They both equal to the determinant??>??????
- If symmetric matrices are good, then positive definite matrices are subclass of them, and are excellent. 

### [[Positive definite (symmetric) matrix]]


### [[Positive semi-definite (symmetric) matrix]]

### Positive definiteness
- In is a property of any object to which a bilinear form or a sesquilinear form may be naturally associated, which is positive-definite. 

### Positive definite matrix
- a matrix $M$ with real entries is positive definite if the real number $z^TMz$  is positive for every nonzero column vector $z$, where $z^T$ is the transpose of $z$. 
- $A$ is a positive definite matrix when $A = A^T$ and the $\lambda$s are positive. 

### 

---
## Chapter 7 Singular value decomposition

- Insights
	- When nearby pixels are correlated, the image can be compressed
	- SVD separates any matrix $A$ into rank one pieces $vv^T =$ (column)(row)

- Q: The first question is, say we represent an image with the matrix $A$. Why we could stick a "eigenvector" or vector on the image $A$?

- [[singular value decomposition]]
### Singular vector
- Each matrix $A$ as two sets of singular vectors (the eigenvectors of $A^TA$ and $AA^T$).
	- One set of positive singular values 
- $A$ is often rectangular. But $A^TA$ and $AA^T$ are square, symmetric and positive semidefinite. 

### Unitary matrix
- Definition
	- Unitary matrices $U$ are square matrix of complex numbers, whose inverse is equal to its conjugate transpose.
	- $U^H = U^{-1}$
- Properties
	- From definition, we have $UU^H = U^HU = I$. 





---





### Other candidates apart from SVD: 
- Why it is useful:
	- SVD separates any matrix into simple pieces. Each piece is a column vector times a row vector. 
		- But a column and a row only have $m + n$ components, far less than $m \times n$. --> These pieces can be processed with extreme speed. 
	- The SVD can be computed efficiently using numerical algorithms, and the computational cost is usually proportional to $min(m,n)^{2.3}$, where $min(m,n)$ is the smaller of the two dimensions of $A$.
- Requirements for the data inputs 
	- Major success in compression will be impossible if every $a_{ij}$ is an independent random number. 
		- Edges in the image are the hard parts to compress.
		- For a video, we only transmit the small changes. 
- Target: 
- Explain the significance of the SVD:
	- Try:  -- $A = S\Lambda S^{-1}$
		- Because they were symmetric, their eigenvectors were orthogonal. 
		- So my $S$ have become an especially good $Q$. 
		- This is no good because 
			- 1. The eigenvector matrix isn't orthogonal. 
			- 2. We look for orthogonal times diagonal times orthogonal. 
	- Q: Why orthogonal vectors is good?
		- A: Orthogonal basis i.e. $QAQ^T$ used in SVD (i.e. $\sum_i c_iu_iv_i^2$),  in theory says. will produce a smaller second piece and sequentially following pieces are also smaller.
	- Try: Symmetric positive definite $A = Q \Lambda Q^T$ 
		- $Q$:
			- $Q \in R^{n \times n}$ is a square matrix whose columns consist of eigenvectors of $A$.
			- $Q$ is also symmetric positive definite matrix.
			- Because they were symmetric, their eigenvectors were orthogonal, so we could produce an orthogonal matrix 
		- $\Lambda$:
			- $\Lambda$ is a diagonal matrix whose diagonal entries consist of the eigenvalues of $A$. 
		- This decomposition is useful but it has fatal limitations
			- 1. $A$ must be square
			- 2. $A$ must have real eigenvalues (I don't know how to prove, but it is not important in data science)
	- Observations of problems from the previous trial approaches:
		- 1. Most eigenvectors $u_i \in U = [u_1, u_2, \dots, u_n]$  in eigenvalue decomposition $A = X\Lambda X^{-1}$ are not orthogonal
			- Orthogonality will produce a smaller second piece $c_2 u_2 v_2^T$.
			- SVD chooses rank one pieces in order of importance. 
		- 2. $x_1, x_2$ only gives one set of vectors, and we want two sets $u$'s and $v$'s.
			- For a rectangular $m \times n$  matrix, we need to execute two times of rotation that is respect to each axis of the matrix.

### Singular value decomposition 
- SVD ($A = U\sum V^T =\sum_{i=1}^r \sigma_i u_i v_i^T$) is a generalized method of $S = Q\Lambda Q^{-1}$ that breaking down a matrix into 1 diagonal singular value matrix, and 2 singular vectors. 
- What is SVD?
	- For any matrix $A \in R^{m \times n}$, $A = U\sum V^T =\sum_{i=1}^r \sigma_i u_i v_i^T$,
		- $A$:
			- $A$ could be any matrices. 
			- Dimensional analysis:
				- Before SVD: $(m \times n)$
				- After SVD: $(1 \times 1)$
		- $\sum$:
			- Diagonal matrix
			- Entries (singular values) are positive
			- Sorted in decreasing order ($\sigma_1 \geq \sigma_2 \geq \dots \geq 0$)
				- Q: why $\sum$ is not a square matrix?
			- The diagonal entries of $\sum = \begin{bmatrix} \sigma_1 &&& \\ & \sigma_2 && \\ && \ddots & \\ &&& \sigma_i \end{bmatrix}$ consist of $\sigma_i$ , where $i = 1, \dots, p$ and $p = min(m,n)$. $\sigma_i$ is also the $i^{\text{th}}$ singular value, and $u_i$ and $v_i$ are the $i_{\text{th}}$ columns of $U$ and $V$. 
		- $U$, $V$:
			- where $U \in R^{m \times m}$ and $V \in R^{n \times n}$. Both are unitary matrices and orthogonal matrices. $U$ columns consist of the "left singular vectors" of $A$, $V$ consist of the "right singular vectors" of $A$.  
			- Both matrices are also positive semidefinite matrix. Because they are coming from $AA^T$ and $A^TA$. 
			- To find $U$, 
		- $\sigma_i u_i v_i^T$:
			- This is just elementary representation of the final matrix of $U \sum V^T$. 
				- $\sigma_i$: the $i^{\text{th}}$ singular value
				- $u_i, v_i$: the $i^{\text{th}}$ columns of $U$ and $V$. 
			- The sum, which in effect adds new layers of the form $\sigma_i u_i v_i^T$ on the top of one another $r$ times to form $A$, provides valuable insight into how an important application of SVD, approximating matrices works.
		- $\sum_{i=1}^r \sigma_i u_i v_i^T$:
			- $r = \text{rank}(A)$
			- The sequence is a leading positive diagonal entries, in non-decreasing order (the order is coming from the definition of $\sum$. )
			- There are totally maximum $r$ terms because 





- 1. The origin of SVD formula: $A = U \sum V^T$
	- 1. $u_i \in C(A)$,  $v_i \in C(A^T)$ 
		- For linking up row space and column space of $A$, we have to transform row space into column space. 
		- Consider we normally have $Ax_{\text{row}} = b$. First we have $x_{\text{row}} \in C(A^T) \in R^n$, and $b \in C(A) \in R^m$. 
		- Similarly, propose $v_i \in C(A^T)$, $u_i \in C(A)$, then we have $Av_i = u_i$. 
	- 2. $u_i = Av_i$ 
		- (linear transformation between row space and column space)
	- 3. $\sigma_i u_i = A v_i$ (Stretch the vector to maintain the orthogonality after linear transformation)
		- We had $u_i = Av_i$ so far, but there is no reason why orthonormal basis in row space, is still orthonormal in vector space. $\sigma_i$ stretch each $u_i$ until their length become 1. 
			- $Av_1 = \sigma_1 u_1$
			- $Av_2 = \sigma_2 u_2$
			- $Av_r = \sigma_r u_r$
		- Note: Avoiding confusion, use $\sigma$ instead of $\lambda$ to represent that scalar. (The stretching number )
	- 4. When we try to express in matrix form, we know that $A$ is actually diagonalized by $U, V$ and $\Sigma$
		- We had $\sigma_i u_i = A v_i$. Put all of them in parallel, we have $A \begin{bmatrix} v_1, \dots, v_n \end{bmatrix} =\begin{bmatrix} \sigma_1 u_1, \dots, \sigma_n u_n \end{bmatrix}$, that is $AV = U \Sigma$
			- $A \begin{bmatrix} v_1 & v_2 & \dots & v_r \end{bmatrix} = \begin{bmatrix}u_1 & \dots & u_r \end{bmatrix} \begin{bmatrix}\sigma_1 && \\\ & \ddots & \\ && \sigma_r \end{bmatrix}$
			- $AV = U \sum$
			- $A = U \sum V^T$



![[Pasted image 20230215145755.png|400]]
- Fig: dimensional perspective. 

- 2a. Prove $(\sigma_A)^2 =  \lambda_{AA^T}$. 
- 2b. Prove $U$ is orthonormal eigenvectors of $AA^T$.  $V$ is orthonormal eigenvectors of $A^TA$. 
- 2c. Show singular value matrix $\Sigma$ we got from $\text{det}(A^TA - \sigma I) = 0$ and $\text{det}(AA^T - \sigma I) = 0$ is equivalent, while we know $A^TA \neq AA^T$ and $U \neq V$ in general
	- General steps:
		- 1. Connecting first-level equation $A = U \Sigma V^T$ and second-level equation $AA^T$ and $A^TA$. 
		- 2. Express second-level equation with first-level variables, $U$, $V$, $\Sigma$.
		- 3. Extract the relationship from the second-level equation. 
	- Proof:
		- 1. 
			- We already have $A = U \sum V^T$, $A^T = V \sum U^T$ 
		- 2. 
			- $\begin{align*}A^TA &= (V \sum U^T) (U \sum V^T) \\ &= V\sum \sum V^T \\ &= V \begin{bmatrix} \sigma_1^2 && \\ & \sigma_2^2 & \\ && \ddots \end{bmatrix} V^T \\  \end{align*}$
		- 3.
			- $\begin{align*}AA^T &= U \begin{bmatrix} \sigma_1^2 && \\ & \sigma_2^2 & \\ && \ddots \end{bmatrix} U^T \\  \end{align*}$
		- 4. For the expression in 2 and 3, the right sides are diagonalization (format: $S = Q\Lambda Q^T$) 
			- So $A^TA$ produces singular vector $V$ (proved 2b)
			- So $AA^T$ produces singular vector $U$ (proved 2b)
			- So $\sigma_A^2 = \lambda(A^TA) = \lambda_{AA^T} =  \lambda_{A^TA}$  (right hand side means "$\lambda$" of matrix $AA^T$ in its $Ax = \lambda x$ form. ) (proved 2a) (proved 2c)
		- QED. 

- 3.  Prove $\sigma_1, \dots, \sigma_r$ of $\Sigma$ are all positive numbers. 
	- Proof:
		- 1. We have $\begin{align*}A^TA  &= V \begin{bmatrix} \sigma_1^2 && \\ & \sigma_2^2 & \\ && \ddots \end{bmatrix} V^T \\  \end{align*}$ and $\begin{align*}AA^T &= U \begin{bmatrix} \sigma_1^2 && \\ & \sigma_2^2 & \\ && \ddots \end{bmatrix} U^T \\  \end{align*}$
			- These two equations came from applying $AV = U \Sigma$ twice on $A^TA$ and $AA^T$. 
		- 2. Additionally, $A^TA$ and $AA^T$ are positive (semi) definite.
			- There are totally two approaches to verify a matrix is positive (semi)definite. One is knowing all eigenvalues are equal or greater than 0, another is to look at $x^T A^T A x \geq 0$ and $x^TAA^Tx \geq 0$. The expression of $x^T A^T A x$ is came from replacing $A$ of our familiar expression $Ax = \lambda x$ and then $\lambda = x^T Ax$. 
				- For $A^TA$ , we can verify the singular values are positive by  $x^TA^TAx = (Ax)^TAx = Ax\cdot Ax = (|Ax|)^2$. Length itself is positive. Thus $A^TA$ is positive semi-definite.
				- For $AA^T$, we have $x^TAA^Tx = (A^Tx)^TA^Tx = (|A^Tx|)^2$. Length itself is positive. Thus $AA^T$ is positive semi-definite.
			- Note: Although both $A^TA$ and $AA^T$ are both symmetric.  $A^TA \neq AA^T$. The transpose of them are keeping them remain unchanged.
		- 3. We have $\sum = \begin{bmatrix} \sigma_1 && \\ & \sigma_2 & \\ && \ddots \end{bmatrix}$, which came from  $\sigma_i u_i = A v_i$ and $A = U \Sigma V^T$.
			- Nothing else here is either symmetric and positive semi-definite.
		- 4. $\Sigma$ is the square root of the eigenvalue vector for $AA^T$ and $A^TA$. 
		- 5. Using the facts in (1) and (2), we know the entries of $\sum$ is positive. 
		- QED. 


- 4. Ways of determining $\Sigma$, $U$ and $V$
	- 1. Solve $\text{det}(A^TA - \sigma I) = 0$
	- 2. From the $r$-term polynomial comes out and we would have $r$ bilinear pairs of singular-values & singular vectors.
		- Output:
			- 1. $\sum = \begin{bmatrix} \sigma_1 & &  & \\ & \sigma_2 &  & \\ && \ddots &  \\ &&& \sigma_n \end{bmatrix}$, which we have to put $\sigma_i$ in descending magnitude order.  
			- 2. $V = \begin{bmatrix} v_1 & v_2 & \dots & v_n\end{bmatrix}$, which $v_i$ is bilinearly corresponding to $\sigma_i$ in $\Sigma$. 
- How to find singular matrix $U (u_i)$?
	- Solve $\text{det}(AA^T - \sigma I) = 0$
		- Output:
			- 3. $U = \begin{bmatrix} u_1 & u_2 & \dots & u_n \end{bmatrix}$, which $u_i$ are bilinearly corresponding to $\sigma_i$ in $\Sigma$.


- 5. Show rank $r$ of $S$ equals to the rank of $A$. 

- 6. The expansions in eigenvectors and singular vectors are perfectly parallel.
	- $S = Q \Lambda Q^T = \lambda_1q_1q_1^T + \lambda_2q_2q_2^T + \dots + \lambda_rq_rq_r^T$
	- $A = U \Sigma V^T = \sigma_1u_1v_1^T + \sigma_2u_2v_2^T + \dots + \sigma_ru_rv_r^T$
	- $q$'s are orthonormal, $u$'s are orthonormal, $v$'s are orthonormal.

- 7. $U^TU = I$ while we have chosen  $V$ are orthonormal basis vectors (i.e. $V^TV = I$)
	- Proof:
		- 1. $u_i = {Av_i \over \sigma_i}$
			- We divide by $\sigma_i$ because these vector $u$, $v$ are unit vectors. 
		- 2. Elementarily evaluate the values of $U^TU$
			- $({Av_j \over \sigma_j})^T({Av_i \over \sigma_i}) = \frac{v_j^T\sigma_i^2v_i}{\sigma_j \sigma_i} = \frac{v_j^T\sigma_i^2v_i}{\sigma_j \sigma_i} = \begin{cases} 1, \text{if}\ i=j \\ 0, \text{if}\ i \neq j\end{cases}$
		- QED


- Example of SVD of 2 x 2 matrix
![[Pasted image 20230212054314.png|400]]

---

- 8. Geometric meaning of SVD
- The beauty is, with this, we can also make all the $u$'s and all  the $v$'s orthogonal to each others.
- The SVD separates a matrix into three steps: (orthogonal) x (diagonal) x (orthogonal)
- In SVD, a matrix can be decomposed into $A = U\sum V^T$
	- $U$ and $V^T$ are orthogonal matrices. They are linear isometries. Examples including rotation, permutation and reflection. 
	- $\sum$ stretch the circle. It's a diagonal matrix,$\sum  = \begin{bmatrix} \sigma_1 & \\ & \sigma_2 \end{bmatrix}$  is like multiplier along axis 1 and 2. So it doesn't turn things.
	- So $\sum$ and $V^T$ are two different kind of matrix. 
	- So $A = U\Sigma V^T$ is basically rotate-stretch-rotate transformation.
![[Pasted image 20230211142018.png|400]]
- Fig: Demonstration of the geometric meaning of SVD.
	- Source:  A 2020 Vision of Linear Algebra, Spring 2020 https://www.youtube.com/watch?v=IHO7_n7Y09s

- 9. How SVD picks off the largest term $\sigma_1 u_1 v_1^T$ before $\sigma_2 u_2 v_2^T$.
	- Source: p.375-377 of the book 
	- 1. We need to make sure the expansion of S and A are parallel.
		- $S = Q\Lambda Q^T = \lambda_1q_1q_1^T + \lambda_2q_2q_2^T + \dots + \lambda_rq_rq_r^T$
		- $A = U \Sigma V^T = \sigma_1u_1v_1^T + \sigma_2u_2v_2^T + \dots + \sigma_ru_rv_r^T$
	- 2. maximum ratio 
		- for $\lambda_1$ = $\frac{x^TSx}{x^Tx}$ (The formula, I guess, is came from putting $x^T$ on ups and downs of $\frac{Sx}{x}$ )
		- for $\sigma_1 = \frac{||Ax||}{||x||}$
		- for $\lambda_2$ = $\frac{x^TSx}{x^Tx}$, among all x with $q_1^Tx = 0$.
		-  for $\sigma_2 = \frac{||Ax||}{||x||}$ among all x with $v_1^Tx = 0$.
	- 3.  take derivatives $\frac{\partial r}{\partial x_i}$on $r(x) = \frac{x^TSx}{x^Tx}$ Set partial derivatives to zero for $i = 1, \dots, n$. 
		- $\frac{x^TSx}{x^Tx}$ is called Rayleigh quotient
	- 4. Expand it to observe that it will force $w = 0$ and $S_{n-1}^T = S_{n-1}$ 
		- (I can't understand this)
	- 5.By induction, we can use step 1 to 4 to produce $q_1, \dots, q_n$ and $\lambda_1, \dots, \lambda_n$. 

- 10. Prove each $\sigma^2 = \lambda(A^TA)$ (from p.372 of the book)
	- ...


### Singular value
- To avoid confusion, we make a new term "singular value" and "singular matrix" that distinct the concept from "eigenvalue" and "eigenvector".
- While eigenvalues associate with $Ax = \lambda x$, singular values $\sigma_i$ associate with singular value decomposition. 
- In SVD, we have $A = U\sum V^T = \sum_i \sigma_iu_iv_i^T$, 
	- which $\sum$ is singular value matrix. $\sigma_i$ are singular values. 
	- which $U$ are $V$ are singular vectors. 
- Properties
	- 1. $\sigma_1 \geq \sigma_2 \geq \dots \geq \sigma_r \geq 0$
	- 2. $\sum$ sized $r \times r$, and $r = \text{rank}A$
	- 3. $\sigma_1, \dots, \sigma_r$ will be positive numbers. 
		- $\sigma_i$ is the length of $Av_i$. 
		- Proof: 
			- Because both $AA^T$ and $A^TA$ and positive semidefinite. 

### Singular vectors
- While eigenvectors associate with $Ax = \lambda x$ , singular vectors distinct from this formula, and singular matrix associate with singular value decomposition  
- - In SVD, we have $A = U\sum V^T = \sum_i \sigma_iu_iv_i^T$, 
	- which $\sum$ is singular value matrix. $\sigma_i$ are singular values. 
	- which $U$ are $V$ are singular vectors. 
- Properties: 
	- 1. Choosing two eigenvectors, which are closely related to the row space and column space of $A$.
		- a. $u_1, \dots, u_r$ is an orthonormal basis for the column space $C(A)$
		- b. $u_{r+1}, \dots, u_m$ is an orthonormal basis for the left nullspace $N(A^T)$
		- c. $v_1, \dots, v_r$ is an orthonormal basis for the row space 
		- d. $v_{r+1}, \dots, v_n$ is an orthonormal basis for the nullspace $N(A)$. 
		- explanation:
			- 1. $A$ always has column space and row space
			- 2. Row space and column space always has basis
			- 3. Basis always could be chosen orthonormal basis. 
	- 2. $u \in R^m$. $v \in R^n$
		- Explanation:
			- For a $m \times n$ matrix $A$, its column vectors has $m$ coordinates, so $u \in R^m$. Same reason for $b$.
	- 3. 


### Bases and matrices in the SVD
- $r = \text{rank}(A)$
- Properties:
	- 1. Choosing two eigenvectors, which are closely related to the row space and column space of $A$.
		- a. $u_1, \dots, u_r$ is an orthonormal basis for the column space $C(A)$
		- b. $u_{r+1}, \dots, u_m$ is an orthonormal basis for the left nullspace $N(A^T)$
		- c. $v_1, \dots, v_r$ is an orthonormal basis for the row space 
		- d. $v_{r+1}, \dots, v_n$ is an orthonormal basis for the nullspace $N(A)$. 
		- explanation:
			- 1. $A$ always has column space and row space
			- 2. Row space and column space always has basis
			- 3. Basis always could be chosen orthonormal basis. 
	- 2. $u \in R^m$. $v \in R^n$
		- Explanation:
			- For a $m \times n$ matrix $A$, its column vectors has $m$ coordinates, so $u \in R^m$. Same reason for $b$.

![[Pasted image 20230209035044.png|300]]
- A typical vector in the row space (eg: $v_1$) taking over some vector in the column space (eg: $u_1$). So $u_1 = Av_1$. 
- An orthogonal basis in the row space get knocked over into an orthogonal basis over column space. 
- To have an orthogonal basis in the row space that goes over 

---
- Linearly dependent for set of vectors $p_1, \dots, p_k$:
	- $a_1 p_1 + \dots + a_k p_k = 0$
- Linearly independent for set of vectors $p_1, \dots, p_k$:
	- $a_1 p_1 + \dots + a_k p_k \neq 0$
- eg: say we have (4i,3j) and (-3a, 4j). There are only a = 0 and b = 0 can cause their linear combinations to be 0. Therefore these vectors are independent.

- Linearly independent: 

### SVD in principal component analysis
- SVD finds combinations of the data that contain the most information
	- Largest singular value $\sigma_1$ --> Greatest variance --> most information in $u_1$. 
- Settings:
	- Data:
		- $A$ is $m \times n$, with $n$ samples and $m$ measurements per sample
		- eg: 
			- $n$ points, with each points contain 2 measurement variable like height and age. Then we can draw a x-y plot to visualize it. $n$ points are often clustered along a line or close to a plane.  Then $A$ would be $2 \times n$. 
	- Center the matrix $A$ : 
		- subtracting the mean from each measurement
		- $A = \begin{bmatrix} value_{m=1,n=1} && \\ & \ddots & \\ && value_{m=n,n=n}\end{bmatrix}$ ($A$ is a bucket of samples measurement data)
		- $A' = A - \begin{bmatrix} \mu_1 \\  \mu_2 \\ \vdots \\ \mu_n \end{bmatrix}$ (broadcasting across $n$ columns)
		- $AA^T$:
			- Dimensional analysis: $(m \times n)(n \times m) \rightarrow (m \times m)$, each elements should sum up $n$ terms. 
			- $(AA^T)_{ij} =$ $(value_{m = i, n= j} - \mu_{m = i})$
- Sample covariance
	- Formula from statistics: 
		- While variance is only measuring the difference from the data points to their average values, covariance only gets bigger when the data point varies from the centroid on both axes.  
		- $\begin{align*}  cov_{X,Y} \\ &= E((X-E(X))(Y-E(Y))) \\ &= \sum_x \sum_y (x-E(X))(y-E(Y))P_{X,Y}(x,y)  \\ &=\frac{\sum(x_i - \bar x)(y_i - \bar y)}{N-1} \end{align*}$
		- Diagonal values: they are self-covariance, in other words, the variance of each variable. So they must be positive
		- Off-diagonal values: their values can be positive or negative
		- If covariance of two variables is positive, that means they tend to change in the same  direction. 
		- Correlation is a normalized version of covariance. 
	- Sample covariance matrix: $S = \frac{AA^T}{n-1}$
- Using matrix in statistics
	- setting
		- $A$ is $2 \times n$: large nullspace
		- $AA^T$ is $2 \times 2$ (small matrix)
		- $A^TA$ is $n \times n$  (large matrix)
		- Two singular values $\sigma_1 > \sigma_2 > 0$
	- Procedure
		- $AA^T = \begin{bmatrix} s_1^2 & s_{12} \\ s_{21} & s_2^2  \end{bmatrix}$
		- $s_1^2$ and $s_2^2$ are covariance of itself = the sum of squared distance.
		- $s_{12}$ and $s_{21}$ are sample covariance of $x_2$ and $x_1$. 
- Using matrix is SVD
	- The crucial connection to linear algebra is in the singular values and singular vectors of $A$. 
	- We have to use $(\sigma_A)^2 = \lambda_{AA^T}$
	- Total variance $T = \sigma_1^2 + \dots + \sigma_m^2 = \text{trace of } AA^T \text{(diagonal sum)}$
	- Q: 



---
### SVD (in computer science lecture)

(Remember to learn CS246: Mining Massive Datasets!)

- In layman terms:
	- ![[Pasted image 20230211102348.png|300]]
	- ![[Pasted image 20230211103320.png|300]]
	- $A$:
		- Input data matrix 
		- $m \times n$ (eg: $m$ documents, $n$ terms)
	- $U$:
		- Left singular vectors
		- $m \times r$ ($m$ documents, $r$ concepts)
	- $\sum$:
		- singular values
		- $r \times r$ diagonal matrix (strength of each concepts), $r$: rank of the matrix $A$
	- $V$:
		- Right singular matrix
		- $n \times r$ matrix ($n$ terms, $r$ concepts)

- We compress each change matrix by linear algebra (and by nonlinear "quantization") for an efficient step to integers in the computers. 
- The reduction in data inputs
	- 300 x 300 pixels becomes 300 + 300.
	- If we define the all-ones vector $x$ in advance, we only have to send one number.
	- Image base
		- Preselected base (Fourier basis)
		- Adaptive bases (determined by the image)
- Applications
	- Data compression
	- Dimensionality reduction
	- Matrix inversion
	- Solving linear least squares problems
	- Grayscale image
		- 8 bits for its grayscale
		- To copy grayscale image perfectly, we need $8 \times m \times n$ bits of information. 
	- HDTV
		- 24 frames, 1920 x 1080, 3 color scales
		- 1920 x 1080 x 24 x 3 x 8 bits per second.

- Rank 1 example:  French / Italian / German flag: 
	- $\begin{bmatrix} a&a&c&c&e&e \\ a&a&c&c&e&e \\ a&a&c&c&e&e\\ a&a&c&c&e&e \\ a&a&c&c&e&e\\ a&a&c&c&e&e \end{bmatrix} = \begin{bmatrix} 1\\1\\1\\1\\1\\1\end{bmatrix} \begin{bmatrix} a&a&c&c&e&e \end{bmatrix}$
		- These flags has 3 colors but it still has rank 1. 
- Rank 2 example:
	- when the rank moves up to $r = 2$, we need $u_1v_1^T + u_2v_2^T$. 
	- $A = \begin{bmatrix} 1&0 \\ 1&1\end{bmatrix} = \begin{bmatrix} 1 \\1 \end{bmatrix}\begin{bmatrix} 1 & 1\end{bmatrix} - \begin{bmatrix} 1 \\ 0\end{bmatrix}\begin{bmatrix} 0 &1\end{bmatrix}$
- Rank > 2
	- If the rank of $A$ is much higher than 2, as we expect for real images, then $A$ will add up make rank one pieces. 
	- The equation would be: $\sum_i u_iv_i^T$ for $i$ from 1 to $r$. 
	- We want small ones to be really small -- they can be discarded with no loss to visual quality. 
	- Good image compression is virtually undetectable by the human visual system.
- Q: does it mean "Full rank matrix" means the pixels of the image of that matrix is totally not correlated?
	- Original image: N by N
	- If image is rank 1: N
	- Rank 2: 2N
	- Rank N (full rank): N by N
	- So the answer is Yes

- SVD theory said, SVD chooses rank 1,2,3.... pieces in order of importance. Orthogonality will produce a smaller second piece $c_2u_2v_2^T$. 

---

### Independence assumption
- This essentially states that the elements of a matrix should not be randomly generated, otherwise the SVD of the matrix may not be useful.
- The condition number is a scalar that gives you an idea of how much the solution of a system of linear equations will change if there is a small change in the right-hand side of the equations. 
	- A high condition number indicates that the matrix is ill-conditioned, meaning that small perturbations in the data can result in large changes in the solution.
	- if a matrix has a high condition number, it suggests that the independence assumption may not hold and the SVD of the matrix may not be a good representation of the data.
- Example:  
	- `condition_number = max(singular_values) / min(singular_values)`
- Example 2:
```python
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
U, S, VT = np.linalg.svd(A)
condition_number = np.max(S) / np.min(S)
print("The condition number of the matrix is:", condition_number)

```

### Eigenvectors for the SVD
- Requirements
	- 1. We need 2 sets of vectors (why?)
	- 2. We need those sets of vectors are orthogonal, such that the size of the pieces would be smaller in order. (why?)
- The eigenvectors for most images are not orthogonal. 
	- Recall: $Ax = \lambda x$. 
- Also, eigenvectors $x_1$, $x_2$ give only one set of vectors. And we want two sets ($u$'s and $v$'s)
- Use the eigenvectors $u$ of $AA^T$ and the eigenvectors $v$ of $A^TA$.
- Since $AA^T$ are automatically symmetric, the $u$'s will be one orthogonal set and the eigenvector $v$ will be another orthogonal set. 
- Choices from the SVD
	- $AA^Tu_i = \sigma_i^2u_i$
	- $A^TAv_i = \sigma_i^2v_i$
	- $Av_i = \sigma_iu_i$
- EG:
	- Rank 2 matrix $A = \sigma_1u_1v_1^T + \sigma_2u_2v_2^T$. 
	- The size of those numbers $\sigma_1$ and $\sigma_2 will decide whether they can be ignored in compression. 


### Low effective rank of image
- Images mostly have full rank, but they do have low effective rank.
- This means singular values are small and can be set to zero.
- We transmit a low rank approximation. Perfect reproduction needs all $n$ pieces. In compression small $\sigma$'s pieces can be discarded. 


---
## Chapter 9 - Complex vectors and matrices

- [[complex vector]]


- [[fourier matrix]]

Introduction of terms: (PLease refer to p.430 of the book)
[[complex conjugate]]
[[polar form]]

- [[transpose]]
	- [[conjugate transpose]]
- [[dot product]]
	- [[dot product|inner product]]
- [[symmetric matrix]]
	- [[hermitian matrix]]
- [[orthogonal matrix]]
	- [[unitary matrices|unitary matrix]]


---

- [[fast fourier transform]]


---

### Summary of linear algebra?
- source: https://www.youtube.com/watch?v=YrHlHbtiSM0
![[Pasted image 20230212065056.png]]
- Source: Book cover of 6th edition of Strang's book. 
![[Pasted image 20230212070504.png]]
- $A = CR$ is new idea from Strang. 



1234


```tikz
\begin{document}
  \begin{tikzpicture}[domain=0:4]
    \draw[very thin,color=gray] (-0.1,-1.1) grid (3.9,3.9);
    \draw[->] (-0.2,0) -- (4.2,0) node[right] {$x$};
    \draw[->] (0,-1.2) -- (0,4.2) node[above] {$f(x)$};
    \draw[color=red]    plot (\x,\x)             node[right] {$f(x) =x$};
    \draw[color=blue]   plot (\x,{sin(\x r)})    node[right] {$f(x) = \sin x$};
    \draw[color=orange] plot (\x,{0.05*exp(\x)}) node[right] {$f(x) = \frac{1}{20} \mathrm e^x$};
  \end{tikzpicture}
\end{document}
```

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{document}
\begin{tikzpicture}
\begin{axis}[colormap/viridis]
\addplot3[
	surf,
	samples=18,
	domain=-3:3
]
{exp(-x^2-y^2)*x};
\end{axis}
\end{tikzpicture}
\end{document}
```


![[machine learning]]