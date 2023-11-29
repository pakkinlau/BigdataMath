1. **Definition**: 
	- Say we have a matrix / function $A \in C^{m \times n}$ takes a vector $x \in C^n$([[domain space]]) and outputs a vector $b = Ax \in C^m$ ([[range space]]). $A: C^n \rightarrow C^m$, $x  \mapsto Ax$ , which $A$ is a function that [[Linear transformation]] the vector from the complex vector space $C^n$ as its input, and maps it to a vector in a complex vector space $C^m$ as its output. 
	- A linear transformation satisfies the following properties: 
		- **Additivity**: T(u + v) = T(u) + T(v) for all vectors u and v in V.
		- **Scalar Multiplication Preservation**: T(kv) = kT(v) for all scalar k and vector v in V.

   These properties essentially mean that the transformation preserves vector addition and scalar multiplication operations.

2. **Matrix Representation**: Every linear transformation can be represented by a matrix. Let's say V and W are vector spaces with bases {v₁, v₂, ..., vₙ} and {w₁, w₂, ..., wₘ}, respectively. If T: V → W is a linear transformation, then there exists a matrix A with dimensions m x n (where m is the dimension of W and n is the dimension of V) such that for any vector v in V, the transformation can be represented as T(v) = Av.

3. **Examples**: Linear transformations are abundant in various mathematical and real-world scenarios. Some common examples include:

   - **Matrix Multiplication**: The product of a matrix A and a vector v can be viewed as a linear transformation.
   - **Scaling and Rotation**: Scaling and rotation operations in 2D or 3D space can be expressed as linear transformations.
   - **Projection**: The process of projecting a vector onto a subspace is a linear transformation.
   - **Differential Operators**: In calculus, differentiation and integration operators are linear transformations.

4. **Properties**:
   - Linear transformations preserve the origin; that is, T(0) = 0.
   - The composition of two linear transformations is also a linear transformation.
   - Linear transformations can be represented as a combination of elementary transformations such as translations, rotations, and scaling.

5. **Invertibility**: A linear transformation is invertible if and only if its associated matrix is invertible. In other words, T is invertible if and only if there exists another linear transformation T⁻¹ such that T(T⁻¹(v)) = T⁻¹(T(v)) = v for all vectors v.

Understanding linear transformations is crucial in various fields of mathematics and sciences, as they provide a powerful tool for analyzing and solving problems involving vectors and matrices. They serve as a bridge between abstract algebraic concepts and practical applications in areas like computer graphics, optimization, and physics.