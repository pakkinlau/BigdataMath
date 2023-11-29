
### part 1 - complex numbers

- Two useful facts: 
	- $\bar z_1 + \bar z_2 = z_1 + z_2$
	- $\bar z_1 \times \bar z_2 = z_1 \times z_2$

---
### Complex linear equations

- Taking conjugates of $Ax = \lambda x$, we have another eigenvalue $\bar \lambda$ and its eigenvector $\bar x$, $A \bar x = \bar \lambda \bar x$. 


---
### part 2 - complex vector and matrix

- 1. notation of $z$:
	- $z = \begin{bmatrix}  z_1 \\ z_2 \\ \vdots z_n \end{bmatrix} \in \mathbb{C}^n$
- 2. flipping $z$: 
	- When you transpose a complex vector $z$ or matrix $A$, take the complex conjugate too. Don't stop at $z^T$ or $A^T$. 
	- From a column vector with $z_j = a_j + ib_j$, the good row vector $\bar z^T$ is the [[conjugate transpose|conjugate transpose]], with components $a_j - ib_j$. 
	- Reason:
		- the length squared of a real vector is $x_1^2 + \dots + x_n^2$. 
		- With that wrong definition, the length of $(1,i)$ would be $1^2 + i^2 = 0$. A non zero vector would have 0 length, which is not good. 
		- Instead of having $(a + bi)^2$ we want $a^2 + b^2$, the absolute value squared. That is $a+bi$ times $a - bi$. 
- 3. length of complex vectors / complex inner product
	- $z^Tz$ is not good:
	- $\begin{bmatrix} z_1 z_2 \dots z_n \end{bmatrix} \begin{bmatrix}  z_1 \\ z_2 \\ \vdots z_n \end{bmatrix}$, which $z_k$ is complex number, and it is not good
		- It is not good having complex number multiplication with $z^Tz$ because the inner product of two complex vectors. 
	- $\begin{bmatrix} \bar z_1 \bar z_2 \dots \bar z_n \end{bmatrix} \begin{bmatrix}  z_1 \\ z_2 \\ \vdots z_n \end{bmatrix}$
		- In many context, especially in linear algebra, it is common to use the conjugate transpose (also known as [[adjoint|hermitian transpose]]) / [[conjugate transpose|conjugate transpose]]
		- $\bar z_1 z_1 = (a + bi) (a - bi)  = a^2 + b^2 = |z_1|^2$, which is what we want. 
- Conclusion:
	- the length $||z||$ is the square root of $\bar z^T z = z^H z = |z_1|^2 + \dots + |z_n|^2$ 
- 4. A symbol that do both: 
	- $\bar z^T = z^H$, this is $z$ "[[conjugate transpose]]", the conjugate transpose of $z$. 
	- For real vectors, the vector Hermitian is just a transpose of the vector. 
- 5. Hermitian matrix
	- Symmetric matrix is not good 
	- we want to have conjugates when flipping a matrix: $A^T = A$ 
	- So we introduce Hermitian matrix: $\bar A^T = A^H$

- perpendicular:
	- $q_1, q_2, \dots, q_n$
	- for complex numbers, $\bar q_i^T q_j$ would be [[Kronecker|kronecker]] product. 
	- $\bar Q^T Q = I = Q^H Q$
	- 