---
alias: vectors

---


- Related concepts:
	- [[Vector space]]
	- [[Linear independence]]
	- [[Linear combination]]
	- Span
	- [[Vector Norm]]
	- [[Dot product]] 
	- [[Cross product]]
	- Component
	- Unit vector
	- [[Vector field]]
	- [[Orthogonal vector]]
	- [[Linear transformation]]
	- [[Eigenvalues and eigenvectors]]
	- [[Matrix]]
	- [[Determinant]]

- Definition:
	- 1. a vector is typically defined as an ordered list of numbers, often represented as a column matrix or an array. These numbers are called components or elements of the vector. 
	- 2. A vector can be denoted as: $V = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix}$
		- where $V$ is the vector, $v_1, v_2, \dots, v_n$ are its components. 
		- where the number of components, denoted as $n$, defines the dimensionality of the vector.
	- 3. A linear equation can be expressed in vector
		- Say we have a linear regression function $y = \theta_3 x^3 + \theta_2 x^2 + \theta_1 x + \theta_0$, the function could be represented as $\theta^T\phi(x)$, $\theta = \begin{bmatrix} \theta_3 \\ \theta_2 \\ \theta_1 \\ \theta_0 \end{bmatrix}$ (Transposed matrix, dot product, inner product)
		- 
- Euclidean vector is frequently represented by a directed line segment. 
- Mathematical Representation: 
	- Vectors are typically represented as ordered sets of values. In a three-dimensional space, for instance, a vector can be denoted as (x, y, z), where each component represents a dimension.
- Independence of components:
	- This independence of components is a fundamental property of vectors and is crucial for their utility in various mathematical and physical contexts.
	- Why?
		- Vector addition:
			- The property of vector addition shows that each component's behaviour is independent of the others; changing one component does not affect the others.
		- Vector multiplications:
			- Scalar multiplication involves multiplying each component of a vector by the same scalar value, again treating each component independently. 
	- Independence of components means that you can manipulate or analyse each dimension of a vector separately.
	- each of the elements are independent to each others. So we consume 1 dimension to capture each of them.
- Magnitude and Direction: 
	- Vectors are characterised by two essential properties—magnitude and direction. The magnitude represents the length or size of the vector, while the direction indicates the orientation of the vector in space.
- Vector Operations: 
	- Vectors can undergo various operations, including addition, subtraction, scalar multiplication, dot product, and cross product. These operations are essential for solving complex problems in vector mathematics.
- Geometric Interpretation: 
	- Geometrically, vectors are often visualized as arrows or directed line segments in space. 
	- The length of the arrow corresponds to the magnitude, and the direction of the arrow signifies the vector's orientation.


- Feature vector multiplications: ^cb4cf6
	- related: [[kernel method]]
	- S
	- $\phi(x) = \begin{bmatrix} x^3 \\ x^2 \\ x \\ 1 \end{bmatrix}$
	-  say $z$ and $x$ are having the same dimension n, $\phi(x)^T\phi(z)$ = $x^Tz$  = $\sum_{i=1}^n x_i z_i$


