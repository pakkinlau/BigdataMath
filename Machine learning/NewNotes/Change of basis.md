
- basic concepts:
	- [[Basis]]
	- [[domain space]]
	- [[range space]]


**Change of Basis Matrix ($P$):**
Consider two different bases for the same vector space $V$: the original basis $B = \{v_1, v_2, \ldots, v_n\}$ and a new basis $B' = \{v_1', v_2', \ldots, v_n'\}$. To convert a vector from the original basis to the new basis (or vice versa), we use a matrix called the **change of basis matrix**.

# Change of basis with transformation matrix $P$ 

Let $P$ be the matrix whose columns are the vectors of $B'$ written in terms of $B$. If $v$ is a vector in the original basis and $v'$ is the same vector expressed in the new basis, the relationship between $v$ and $v'$ is given by:
$v' = Pv$

**Calculating the Change of Basis Matrix:**
To calculate the change of basis matrix $P$, stack the vectors of $B'$ written in terms of $B$ as columns. If $B' = \{v_1', v_2', \ldots, v_n'\}$ and $B = \{v_1, v_2, \ldots, v_n\}$, then the matrix $P$ is given by:
$P = [v_1' | v_2' | \ldots | v_n']$

# Change of basis with singular vectors in [[SVD]]

- Say $A = U\Sigma V^*$, $A \in \mathbb{C}^{m \times n}$. Where domain space of $A$ is in $\mathbb{C}^m$, range space of $A$ is in $\mathbb{C}^n$ respectively. 
- Transformation of rows and columns vectors: 
	- $Ub = b'$
		- Recall that $U$ and $V$ are unitary matrices. Geometrically they are rotating the data (to the principal axis?) 
		- Any $b \in \mathbb{C}^m$ can be expanded in the basis of left singular vectors $U$ of $A$. 
		- So $U^*b = b'$, 
			- where we use  $U$ here, because $b$ will be aligned with the column vectors in $U$. 
			- where we use $U^*$ here, because conjugate transpose / Hermitian transpose (other name of it) (to have $U^*b = b'$), 
			- Here we raise an interesting problem: Why we put the matrix in complex conjugate when we do change of basis with $U$?  
			- Instead of the standard linear transformation pattern ($Ax = b$) is because $Ax = b$ is sending the data from the row space of $A$ ($Domain(A)$) to the column space of $A$ ($Range(A)$) through $Ax$.  
			- On the other hand, the conjugate transpose multiplication  ($U^*b = b'$) there is not 
			- where $b'$ is the dataset that has been rotated. 
	- $V^*x = x'$
		- Similarly, we have $V^*x = x'$.
	- $A$ reduces to the diagonal matrix when the range is expressed in the basis of columns in $U$ and the domain is expressed in the basis of $V$. ($b = Ax \Longleftrightarrow b' = \Sigma x'$)
		- If $Ax = b$, by the definition of SVD, and the above properties, we have $b = Ax \rightarrow b = U\Sigma V^*x \rightarrow B^*b = \Sigma V^*x \rightarrow b' = \Sigma x'$. 

Change of basis in [[eigendecomposition]]
- Say $A = X \Lambda X^{-1}$, where $\Lambda$ is $m \times m$ diagonal matrix, whose entries are the eigenvalues of $A$. For $b, x \in \mathbb{C}^m$ satisfying $b = Ax$, 
	- $b = Xb'$
	- $x = Xx'$
	- Then the newly expanded vectors $b'$ and $x'$ satisfies $b' = \Lambda x'$. 

---
In the context of linear algebra, when you have an original basis $B = \{v_1, v_2, \ldots, v_n\}$ and a new basis $B' = \{v_1', v_2', \ldots, v_n'\}$, the matrix $P$ used for changing coordinates from the original basis to the new basis (or vice versa) is often called the **change of basis matrix**.

To find the change of basis matrix $P$, follow these steps:

1. **Express New Basis Vectors in Terms of Original Basis:**
   Write down each vector in the new basis ($v_1', v_2', \ldots, v_n'$) as a linear combination of the vectors in the original basis ($v_1, v_2, \ldots, v_n$). For each $i$, solve the equation:
$$ v_i' = c_{i1}v_1 + c_{i2}v_2 + \ldots + c_{in}v_n$$
   This gives you the coefficients $c_{ij}$ for each vector $v_i'$ in terms of the original basis vectors.

2. **Construct the Change of Basis Matrix $P$:**
   Arrange these coefficients as columns in a matrix:
$$P = \begin{bmatrix}
   c_{11} & c_{21} & \ldots & c_{n1} \\
   c_{12} & c_{22} & \ldots & c_{n2} \\
   \vdots & \vdots & \ddots & \vdots \\
   c_{1n} & c_{2n} & \ldots & c_{nn}
   \end{bmatrix}$$

3. **Verification (Optional):**
   You can verify that $P$ is correct by multiplying it with a vector in the original basis ($v$) to see if it gives you the corresponding vector in the new basis ($v'$):
$$ v' = Pv$$

The resulting matrix $P$ can then be used to transform vectors between the original basis and the new basis. This process is essential in various applications where expressing problems in different coordinate systems simplifies calculations and enhances understanding.


---
**Application:**
Change of basis is crucial in various fields, including computer graphics, quantum mechanics, and signal processing. 

- Derivation:
	- 1. Defining vectors in the original 
		- Let $B_{old} = (v_1, \dots, v_n)$ be a basis of a finite-dimensional vector space $V$ over a field $F$.
			- Notation: It's common mathematical notation to represent a basis of a vector space as an ordered list or sequence of vectors. 
		- Let coordinates of vector basis ($v_i$) in the vector space $V$: $a_{i,j}$
			- (which $i$ refers always to the rows of $A$, and $v_i$, while index $j$ refers always to the columns of $A$ and the $w_j$.)
		- For $j = 1, \dots, n$, one can define a vector $w_j$ by its coordinate $a_{i,j}$ over $B_{old}$: 
			- $w_j = \sum_{i=1}^n a_{i,j}v_i$ 
			- (which is just a linear combinations of all basis vectors in vector space $V$.)
	- 2. Let $A = (a_{i,j})_{i.j}$ be the matrix whose $j$th column is formed by the coordinates of $w_j$. 
- Steps of performing change of basis:
	- 1. Given basis
	- 2. New basis
	- 3. Change of basis matrix
	- 4. Coordinate transformation
	- 5. Inverse transformation
- Demonstration:
	- Given basis
		- Suppose we have a vector space $\mathbb{R}^2$ with the standard basis $\{i,j \}$, where $i$ is the unit vector along the x-axis $(1,0)$ and $j$ is the unit vector along the y-axis $(0,1)$.
	- New basis
		- Let's introduce a new basis $\mathbb{R}^2: \{ u_1, u_2\}$, where $u_1 = (1,1)$ and $u_2 = (-1, 1)$.
	- Change of basis matrix $P$:
		- The change of basis matrix $P$ is constructed by arranging the new basis vectors as columns: $P = \begin{bmatrix} 1 &-1 \\ 1 & 1 \end{bmatrix}$ 
	- Coordinate transformation:
		- Suppose we have a vector $\begin{bmatrix} 2 \\ 3 \end{bmatrix}$. To express $v$ in the new basis, we multiply it by the change of basis matrix $P$:
		- $Pv = \begin{bmatrix} 1 &-1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 2 \\ 3 \end{bmatrix} = \begin{bmatrix} -1 \\ 5 \end{bmatrix}$
- Applications:
	- Eigenvalues and eigenvectors
	- Coordinate systems
- Related concepts:
	- Basis
	- Linear independence
	- Linear transformation
	- Vector space
	- Basis matrix
	- Field