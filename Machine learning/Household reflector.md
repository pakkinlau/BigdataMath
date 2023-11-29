
Say we have $A = QR \in \mathbb{C}^{m \times n}$

$Q_k = \begin{pmatrix}I & 0 \\ 0 & F  \end{pmatrix}$
- where $I$ is $(k-1) \times (k-1)$ identity matrix. It is because we want to keep $k-1$ th columns remain unchanged. 
- where $F$ is $(m - k + 1) \times (m - k +1)$ unitary

- figure: 
	- Source: https://www.youtube.com/watch?v=gvnFVCWI044
	- $F$ just work for the entry values of right bottom corner of the matrix
![[Pasted image 20231125204013.png|300]]

- we consider the $k$th column of the matrix as vector $\xi$ , we try to construct this $F$. 
![[Pasted image 20231125204130.png|300]]

- We want to project our $\xi$ to $e_1$, the direct way of doing it is adding a vector $v = || \xi || e_1 - \xi$
![[Pasted image 20231125205238.png|300]]

---

- To obtain $v$ from $xi$, we use [[reflection operator]] $I - P$ 
![[Pasted image 20231125205508.png|300]]


- Think about a hyperplane that we could have orthogonal projector. 
	- Q: Why we assume the triangle is isosceles triangle?
		- It is based on the simplification of the geometry involved in the reflection operation.
		- We made an assumption that our $\xi$ will project into $e_1$ axis having $|| \xi ||$ length. By such assumption, we have isosceles triangle.

- what is the meaning of $\frac{vv^*}{v^* v}$? 
	- See [[Projection formula]]. 

- What is the meaning of $I - \frac{vv^*}{v^*v}$? 
	- See [[reflection operator]]. 


---

- We want to go twice the distance of $v$, so we have $H = I - 2 \times \frac{vv^T}{\|v\|^2}$
![[Pasted image 20231125205034.png|300]]
---

- Definition:
$$ H = I - 2 \times \frac{vv^T}{\|v\|^2}$$
- Then, $v^{\pm} = \pm ||x|| e_1 - x$
	- There is two choices, but it is no difference. 
	- The main difference lies in the direction in which the direction occurs. But these difference do not affect the practical use of the Housholder transformation, as both yield the same essential result 




---

**Concept: Household Reflector**
**Context: Linear Algebra**

Householder reflectors, also known as Householder transformations or reflectors, are fundamental concepts in linear algebra. They are mathematical operations used for various purposes, including solving systems of linear equations, eigenvalue problems, and least squares approximations.

**Key Characteristics:**
1. **Reflection Operation:** A Householder reflector is a linear transformation that reflects points through a hyperplane.
2. **Orthogonality:** Householder reflectors are orthogonal transformations, meaning they preserve distances and angles between vectors.
3. **Simplicity:** They are simple, numerically stable, and efficient to compute, making them valuable in numerical algorithms.

**Definition and Representation:**
For a given vector $\mathbf{v}$ (of dimension $n$), the Householder reflection is defined as $\mathbf{H} = \mathbf{I} - 2\mathbf{vv}^T/\|\mathbf{v}\|^2$, where $\mathbf{I}$ is the identity matrix, $\mathbf{vv}^T$ is an outer product, and $\|\mathbf{v}\|$ is the Euclidean norm of $\mathbf{v}$. 

**Applications:**
1. **Solving Linear Systems:** Householder reflectors are used in techniques like QR factorization, which decomposes a matrix into an orthogonal matrix ($\mathbf{Q}$) and an upper triangular matrix ($\mathbf{R}$), enabling efficient solutions to linear systems.
2. **Least Squares Approximation:** They play a crucial role in solving the least squares problem, where the goal is to minimize the sum of the squares of the residuals between observed and calculated values.
3. **Eigenvalue Computations:** Householder transformations are employed in algorithms for eigenvalue computations, aiding in various scientific and engineering applications.

**Advantages:**
1. **Numerical Stability:** Householder reflections are numerically stable, providing accurate results in numerical computations.
2. **Efficiency:** They can be efficiently implemented and parallelized, making them suitable for large-scale applications.
3. **Versatility:** Their applicability extends to diverse problems in linear algebra, making them a versatile tool in computational mathematics.

**Conclusion:**
Householder reflectors are essential tools in the toolkit of linear algebra, providing elegant and efficient solutions to various numerical problems. Their simplicity, stability, and versatility make them indispensable in both theoretical understanding and practical implementations in the field of mathematics and its applications.

