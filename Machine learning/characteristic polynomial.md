**Definition:**
- For a square matrix $A$ of size $n \times n$, characteristic polynomial defined as:  $p_a(z) = det(zI - A)$
	- Q: In some textbook, characteristic polynomial is defined as: $p_a(z) = det(zI - A)$. Is there any difference between these 2 expressions? 
	- A: It is interchangeable. But notice that we need to add a negative sign if there is odd number of $n$ in the polynomial. i.e. multiplying a leading $(-1)^n$ would helps. 

**Key Points:**
- **Eigenvalues:** 
	- The roots of the characteristic polynomial are the eigenvalues of the matrix $A$.
- Eigenvectors:
	- We can also determine eigenvectors after knowing the set of eigenvalues of the matrix. 
- **Matrix Diagonalizability:** 
	- A square matrix is diagonalizable if and only if its characteristic polynomial has $n$ linearly independent eigenvectors, each associated with a distinct eigenvalue.
	- related: [[diagonalization|diagonalizable]]

---
### Determining eigenvalues and eigenvectors for matrix $A$: 

- General steps:
	- Eigenvalues:
		- Solve characteristic polynomial
	- Eigenvectors:
		-  Eigenvectors of matrix $A$ could be determined by putting the set of $\lambda_k$ into [[characteristic polynomial]] $det(A - \lambda I)$. 

- Tricky cases:
	- 2a: Repeated eigenvalues, single eigenvectors
		- Consider matrix $A = \begin{bmatrix}2 & 1 \\ 0 & 2 \end{bmatrix}$
		- The characteristic polynomial is $(2-\lambda)^2 = 0$, which has a repeated root of $\lambda = 2$ (so the algebraic multiplicity of the eigenvalue 2 is 2).
		- The eigenvectors are found by solving $(A - \lambda I) v = 0$ for $v$. We get the system of equations
          $$
          \begin{align*}
          0x_1 + x_2 = 0 \\
          0x_1 + 0x_2 = 0
          \end{align*}
          $$
          - From the first equation, we have $x_2 = 0$. As there is no restriction on $x_1$, we can choose $x_1 = 1$ to get a non-zero solution. So the eigenvector corresponding to the eigenvalue $\lambda = 2$ is $v = [1, 0]$. 
          - This yields a single, non-zero solution for $v$, which is $v = [1,0]$ (so the geometric multiplicity of the eigenvalue 2 is 1).
		- So it is not diagonalizable.
	- 2b: Repeated eigenvalues, but points to distinct eigenvectors
		- Consider matrix $A = \begin{bmatrix} 3 & 0 \\ 0 & 3 \end{bmatrix}$
		- The characteristic equation is $(3-\lambda)^2 = 0$, which gives a repeated root of $\lambda = 3$.
		- When we substitute $\lambda = 3$ into the equation $(A - \lambda I) v = 0$, we get
          $$
          \begin{align*}
          0x_1 + 0x_2 = 0 \\
          0x_1 + 0x_2 = 0
          \end{align*}
          $$
          The solutions to this system are any vectors along the x-axis and y-axis. Hence, we get two linearly independent eigenvectors.
          The first eigenvector is $[1,0]$, which can be interpreted as any multiple of this vector lying on the x-axis. The second eigenvector is $[0,1]$, which can be interpreted as any multiple of this vector lying on the y-axis.
		- So this time $A$ yields non-repeating eigenvectors, making it diagonalizable.

---

**Applications:**
- **Eigenanalysis:** Used extensively in solving systems of linear differential equations, quantum mechanics, and stability analysis in various engineering fields.
  
- **Data Analysis:** Principal Component Analysis (PCA) in data science heavily relies on eigenvalues and eigenvectors obtained from the characteristic polynomial.

Mastering characteristic polynomials is crucial in comprehending the behavior and properties of square matrices, providing a deeper understanding of their structural and algebraic properties.


---

Theorem: $\lambda$ is an eigenvalue of $A$ if and only if $p_a(\lambda) = 0$

- No proof is in the slide. 
