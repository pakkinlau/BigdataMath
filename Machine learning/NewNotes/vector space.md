Vector spaces are fundamental structures in linear algebra that provide a framework for studying vectors, vector operations, and linear transformations. A vector space is a collection of vectors that is closed under vector addition and scalar multiplication, satisfying specific properties. Here are the key aspects to understand about vector spaces in the context of linear algebra:

**1. ** **Vector Addition:** In a vector space, any two vectors can be added together to produce another vector in the space. This operation is denoted as $\mathbf{v} + \mathbf{w}$, where $\mathbf{v}$ and $\mathbf{w}$ are vectors in the space. The resulting vector must also belong to the same vector space.

**2. ** **Scalar Multiplication:** Vectors in a vector space can be multiplied by scalars (real numbers or elements from a specific field). If $c$ is a scalar and $\mathbf{v}$ is a vector in the space, the scalar multiplication is denoted as $c\mathbf{v}$. The resulting vector is also in the same vector space.

**3. ** **Vector Space Axioms:** A vector space must satisfy several axioms, including closure under addition and scalar multiplication, commutativity and associativity of addition, existence of an additive identity (zero vector), existence of additive inverses, compatibility of scalar multiplication with field multiplication, and the distributive properties of scalar multiplication over vector addition.

4. [[subspace]] A subspace of a vector space $V$ is a non-empty subset of $V$ that is itself a vector space under the same vector addition and scalar multiplication operations defined for $V$. Subspaces are important in variou4.s applications and theoretical contexts within linear algebra.

5.[[Basis]], [[dimension]] A basis for a vector space is a set of vectors that spans the space and is linearly independent. The dimension of a vector space is the number of vectors in its basis. Different bases for the same vector space have the same number of vectors, which is a fundamental property of vector spaces.

6. [[Linear transformation]] Vector spaces are essential in the study of linear transformations, where functions between vector spaces preserve vector addition and scalar multiplication. Linear transformations are represented by matrices and play a crucial role in many areas, including computer graphics, quantum mechanics, and data analysis.

Understanding vector spaces and their properties is fundamental in various fields such as physics, computer science, engineering, and statistics. They provide a powerful framework for solving systems of linear equations, analyzing geometric shapes, and studying transformations, making them a cornerstone of linear algebra.

---

- Axioms of vector spaces
	- 1. [[Closure]] under vector addition
		- For any two vectors, **u** and **v**, in the vector space, their sum, **u + v**, must also be in the vector space.
	- 2. Closure under scalar multiplication
		- For any vector **u** in the vector space and any scalar (real number) _a_, the product _a ⋅ **u**_ must also be in the vector space.
	- 3. Associativity of vector addition
		- **u + (v + w) = (u + v) + w**
	- 4. Commutativity of vector addition
		- **u + v = v + u**
	- 5. Existence of a zero vector
		- for any vector **u**, **u + 0 = 0 + u = u**
	- 6. Existence of additive inverses
		- **u + (-u) = (-u) + u = 0**
	- 7. Compatibility of scalar multiplication with field
		- 1 ⋅ **u** = **u**
- properties
	- 1. Vector plane and space filling
		- If a third vector is not coplanar with the vectors $u$ and $v$, the combination of all vectors in the form $ew$ and $cu + dv$ will span the entire three-dimensional space.
	- 2. Vector Space Dimensionality:
		- Contrary to a common misconception, a vector space does not necessarily require three vectors. It can be formed by any number of vectors, including just one.
		- This note corrects a common misunderstanding about the minimum number of vectors needed to create a vector space, emphasising that even a single vector can define a vector space.
		- Example:
			- Say $\vec u = \begin{bmatrix}1 \\ 0 \\ 0\end{bmatrix}$, $\vec v= \begin{bmatrix}0 \\ 1 \\ 0\end{bmatrix}$, $\vec w= \begin{bmatrix}0 \\ 0 \\ 1\end{bmatrix}$ are basis vector
			- $\vec u$, $\vec v$, $\vec w$ are orthogonal to each others (i.e. they are linear independent to each other.), ensuring there are no redundancy exists in the basis set. 
			- We can create any vector in 3D space by taking linear combinations of these basis vectors. $\vec x = a\vec v + b\vec w + c\vec u$ 
	- 3. Zero vector space:
		- An example of a vector space with a single vector is when $n = 0$. This vector space is known as the zero vector space, often denoted as $\mathbb{Z}$.
- closely related concepts:
	- [[closure]]
	- [[basis]]
	- [[dimension]]
	- [[span]]
	- [[linear independence]]