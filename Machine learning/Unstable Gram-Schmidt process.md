---
alias: Gram-Schmidt process, 
---

- basic knowledge:
	- [[Projection]]
- related:
	- [[Reduced QR decomposition]]

**Introduction:**
Gram-Schmidt process is a fundamental technique in linear algebra used to transform a set of linearly independent vectors into an orthonormal set. This process plays a crucial role in various applications, including solving systems of linear equations, eigenvalue problems, and signal processing.

- Input:
	- Say we have $1$ original vector $\vec b$ and we want to project / decompose it into a orthogonal space. 

- Intuition:
	- Introduce our new set of orthogonal vector: $(A,B,C,\dots, Z)$. 
	- Choose the first direction to project, and call it $A$ 
	- decompose $q_k$ into orthonormal vectors that is align to that set of basis. We divide $(A,B,C,\dots, Z)$ with their length. $q_1 = \frac{A}{||A||}$, $q_2 = \frac{B}{||B||}$
	- Error vector would be $B = b - \frac{A^Tb}{A^TA}A$

Idea of unstable Gram-Schmidt 
- We pick the first vector $a_1$ as our first vector. The choice of first pick does not matter to the calculation result. 
- And then we consider b.
- We subtract all parts of b that are parallel to a from vector b, the remaining parts of b would be orthogonal to a. 
![](Pasted%20image%2020231205205655.png)

For a matrix $A$, there are $n$ column vectors in there. 

Vector $a_1$: 
- $v_1 = a_1$
- $q_1 = v_1 / ||v_1||$
Vector $a_2$:
- $v_2 = a_2 - a_{2 \perp {a_1}} = a_2 - (q_1^* a_2) q_1$ (notice that $q_1^* a_2$ is computing the scalar, and $q_1$ is providing unitary direction)
- $q_2 = v_2 / ||v_2||$

Vector $a_k$, where $k$ is from $2$ to $n:
- $v_k = a_k - \sum_{i=1}^{k-1} (q_{i}^* a_k) q_i$ (not sure this expression is correct)
- $q_k  = v_k / ||v_k||$

[Gram-Schmidt coefficient $r_{ij}$](Gram-Schmidt%20coefficient%20$r_{ij}$.md):
In general, 
$r_{ij}$ are coefficients related to subject vector $j$ to prior object vector $i$ that are orthogonal to itself. And we use dot product to $q_i^* a_2$ to compute such scalar. 
$r_{jj}$ is related to the scalar of subject vector to itself. So it is basically the 2-norm of itself before we normalize $v_j$. 

In general we have following formula to obtain Gram-Schmidt coefficients $r_{jj}$: 
$r_{ij} = q_i^* a_j$
$r_{jj} = || v_j||$

---






- Write it in formula, it would be:
![](Pasted%20image%2020231205200104.png)



- Algorithm:
![[Pasted image 20231101035820.png]]

---

## Exact steps of Unstable Gram-Schmidt process

   a. **Orthogonalization of A and B**:

- Step 0: Obtaining the first basis vector $a$ from our matrix $A$
	- Just choice any column vectors from $A$ as a starting point. 

  - **Step 1**: Calculate the first column of Q and the first row of R:
	- $q_1 = \frac{a}{||A||}$ (normalize the first basis vector)
	- $r_{11} = ||A||$ (magnitude of the first basis vector)

  - **Step 2**: Calculate the second column of Q and the second row of R:
	- $B = b - \frac{A^Tb}{A^TA}A$ (orthogonalize the second basis vector relative to A)
	- $q_2 = \frac{B}{||B||}$ (normalize the second orthogonal vector)
	- $r_{12} = A^Tb$ (dot product of the first basis vector and the original second basis vector)
	- $r_{22} = ||B||$ (magnitude of the second orthogonal vector)

b. **Orthogonalization of C**:

  - **Step 3**: Calculate the third column of Q and the third row of R:
	- $C = c - \frac{A^Tc}{A^TA}A - \frac{B^Tc}{B^TB}B$ (orthogonalize the third vector relative to both A and B)
	- $r_{13} = A^Tc$ (dot product of the first basis vector and the original third basis vector)
	- $r_{23} = B^Tc$ (dot product of the second orthogonal vector and the original third basis vector)
	- $r_{33} = ||C||$ (magnitude of the third orthogonal vector)

1. **Result**:

   - Matrix Q: $Q = [q_1, q_2, q_3]$ (matrix formed by the normalized orthogonal vectors)
   - Matrix R: $R = \begin{bmatrix} r_{11} & r_{12} & r_{13} \\ 0 & r_{22} & r_{23} \\ 0 & 0 & r_{33} \end{bmatrix}$ (upper triangular matrix)

---
General writing:

1. **Input:** Consider a set of linearly independent vectors $v_1, v_2, \ldots, v_n$ in an inner product space.

2. **Orthogonalization:** The process begins by creating a new set of orthogonal vectors $u_1, u_2, \ldots, u_n$ such that $u_1 = v_1$. For $i > 1$, each $u_i$ is computed as follows:
$$
   u_i = v_i - \sum_{j=1}^{i-1} \frac{\langle v_i, u_j \rangle}{\langle u_j, u_j \rangle} u_j
$$
   
   Where $\langle \cdot, \cdot \rangle$ represents the inner product.

3. **Normalization:** After obtaining orthogonal vectors, the final step is normalization, which involves dividing each orthogonal vector by its magnitude:
$$
   e_i = \frac{u_i}{\|u_i\|}
$$
   
   Here, $e_i$ represents the orthonormal vectors.

- Example
	- $a = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$, $b = \begin{bmatrix} 1 \\  0 \\ 2 \end{bmatrix}$
	- $B = \begin{bmatrix} 1 \\  0 \\ 2 \end{bmatrix} - {3 \over 3}\begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\  -1 \\ 1 \end{bmatrix}$
	- $A = a$
	- Check for $A \perp B$: Dot product
	- $Q = \begin{bmatrix} q_1 & q_2 \end{bmatrix} = \begin{bmatrix} 1\over\sqrt{3} & 0 \\ 1\over\sqrt{3} & -1\over\sqrt{2} \\ 1\over\sqrt{3} & 1\over\sqrt{2} \end{bmatrix}$
	- So $Q$ is our matrix with orthonormal columns that coming from Gram-Schmidt.
	- Original $A$: $\begin{bmatrix} a_1 & a_2 \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & 0 \\ 1 & 2  \end{bmatrix}$

- One more point Factorization $A = QR$
	- Like elimination, we look back, in matrix language, $A = LU$ in elimination.
	- Now we want to do the same for Gram-Schmidt, in the form of $A = QR$.
	- $A = \begin{bmatrix} a & b \end{bmatrix}  = \begin{bmatrix} q_1 & q_2 \end{bmatrix}  \begin{bmatrix} a_1^Tq_1 & b \\ a_1^Tq_2 & d \end{bmatrix}$

![[Pasted image 20230127045152.png]]
- Fig: Gram-Schmidt orthogonalization

---

**Significance:**

1. **Orthonormal Basis:** Gram-Schmidt process converts a set of linearly independent vectors into an orthonormal basis for the subspace they span. Orthonormal bases simplify many computations in linear algebra.

2. **Projection:** Orthonormal bases are essential in applications like projection, where finding the component of a vector along a particular direction is needed. Orthonormal basis vectors simplify this calculation significantly.

3. **Numerical Stability:** Gram-Schmidt process, when implemented numerically, can be prone to numerical instability, especially if the vectors are nearly linearly dependent. Modified algorithms, like the Modified Gram-Schmidt, are used to mitigate these issues.
