**Eigenvalues in Linear Algebra**

Eigenvalues are a fundamental concept in linear algebra, playing a crucial role in various mathematical and scientific disciplines. They are particularly significant when dealing with [[square matrix]], as they provide essential information about the behavior of [[linear transformations]] and [[systems of linear equations]].

**Definition:**
Let A be a [[square matrix]] of order n. An eigenvalue of A is a scalar $\lambda$ such that there exists a nonzero vector $v$, called an eigenvector, satisfying the equation:

$Av = λv$

In other words, when you multiply the matrix A by an eigenvector v, the result is a scaled version of v, represented by λ. Eigenvalues are denoted by the Greek letter λ.

**Calculating Eigenvalues:**
To find the eigenvalues of a matrix A, you need to solve the characteristic equation:

$|A - λI| = 0$

Here, $I$ is the identity matrix of the same size as $A$. Solving this equation will yield the eigenvalues $\lambda_1, \lambda_2, \dots, \lambda_n$. It's important to note that not all matrices have eigenvalues, and the number of eigenvalues can be less than the matrix's order.

**Properties of Eigenvalues:**

1. Eigenvalues are unique for a given matrix A but not necessarily distinct. Multiple eigenvectors can correspond to the same eigenvalue.

2. The sum of the eigenvalues of A is equal to the [[trace]] of the matrix, which is the sum of its [[diagonal matrix|diagonal]] elements.

3. The product of the eigenvalues of A is equal to the determinant of the matrix.

4. If A is a [[symmetric matrix]], all its eigenvalues are real numbers.

5. If A is [[conjugate transpose]] (the complex analog of a real symmetric matrix), all its eigenvalues are real.

**Applications:**
Eigenvalues and eigenvectors find extensive applications in various fields, including physics, engineering, data analysis, and computer science. Some common applications include:

- [[Principal Component Analysis]] (PCA) for dimensionality reduction in data analysis.
- Vibrations and oscillations analysis in mechanical engineering.
- Quantum mechanics, where eigenvalues represent measurable properties of physical systems.
- Structural analysis to understand the stability of structures under various loads.

Understanding eigenvalues is essential for solving systems of linear differential equations, optimizing algorithms, and studying the behavior of complex systems.

In conclusion, eigenvalues are a fundamental concept in linear algebra with broad applications in mathematics and science. They provide valuable insights into the properties and behavior of square matrices, making them a crucial topic for anyone studying big data analytics or related fields.

---
# Old notes

### Eigenvalue
- "Eigenvalue" = the associated scalar when we are having eigenvector. 
	- While eigenvector $x$  that are the exceptional vector that are in the same direction as $Ax$. There is a fixed proportional scalar between $Ax$ and $x$. That is our eigenvalue. 
	- The best matrices for finding eigenvalues is: upper triangular matrices. 
- Property:
	- 1a. Eigenvalues of a triangular matrix lie along its diagonal.
	- 1b. We have a bilinear mapping between eigenvalues $\lambda_1, \lambda_2, \dots,\lambda_n$ and main diagonal entries $a_{11}, a_{22} , \dots , a_{nn}$ of matrix $A$ if it is in either upper triangular form or diagonal form. 
		- Proof of 1a and 1b:
			- 1.  We can convert every matrix into upper triangular matrix, and we can convert every upper triangular matrix unto diagonal matrix. 
			- 2. We have $Ax = \lambda x$ and also $detA - \lambda I)x = 0$. 
				- Notice the $A$ must be upper triangular matrix to make it work. 
			- 3. Now taking determinant for the both sides. It gives us a polynomial $(a_{11} - \lambda_{11})(a_{22} - \lambda_{22}) \dots (a_{nn} - \lambda_{nn}) = 0$
			- 4. So we have the fact that $a_{ii} = \lambda_{ii}$ by having a non-trivial solution of the polynomial. 
				- Each specific lambda value comes from a specific entry-lambda pair. So they are bilinear.
			- QED
	- 2. We have distinct eigenvalues and eigenvector pairs if we eliminate the matrix.
		- eg: $U = \begin{bmatrix}  1&3 \\ 0&0\end{bmatrix}$: $\lambda = 0,1$
		- eg: $U = \begin{bmatrix}  1&3 \\ 2&6\end{bmatrix}$: $\lambda = 0,7$
	- 3. The sum of $n$ eigenvalues equals to the sum of the $n$ diagonal entries (the trace)
		- $\lambda_1 + \lambda_2 + \dots + \lambda_n$ = trace = $a_{11} +a_{22} + \dots + a_{nn}$
		- Proof:
			- Refer to property 1. 
			- Then  $\lambda_1 + \lambda_2 + \dots + \lambda_n$ = trace = $a_{11} +a_{22} + \dots + a_{nn}$
			- QED
	- 4. $\text{det} A = (\lambda_1)(\lambda_2) \cdots (\lambda_n)$
		- Proof:
			- 1. Convert the matrix $A$ into upper triangular form before bringing them into $detA - \lambda I)x = 0$. 
			- 2. The fact $a_{ii} = \lambda_{ii}$ holds for $(A - \lambda I)$ and $A$ is an upper triangular matrix, from the derivation of property 1. 
			- Then we would multiply the main diagonal to get the determinant. 
			- QED. 
- How to solve for $\lambda$?
	- Method 1: $\text{det} A = (\lambda_1)(\lambda_2) \cdots (\lambda_n)$ 
	- Method 2: $a_{11} + a_{22} + \cdots + a_{nn} = \text{ sum of } \lambda's$ 
