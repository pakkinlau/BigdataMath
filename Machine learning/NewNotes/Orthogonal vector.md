---
alias: orthogonal, Orthogonality
---

-  It refers to the relationship between [[vector]] or [[subspace]] in a [[vector space]]. In this set of notes, we will explore the concept of orthogonality in the context of linear algebra.

1. Definition of Orthogonality:
   - In linear algebra, two vectors are considered orthogonal if their dot product (also known as the inner product) is equal to zero. Mathematically, for vectors a and b, if 
	   - 1. $\vec v \cdot \vec w = \vec v^T \vec w =  0$, 
	   - 2. $||v||^2 + ||w||^2 = ||v + w||^2$ (that is basically Pythagorean theorem)
	   - then they are orthogonal.

2. Geometric Interpretation:
   - Geometrically, orthogonal vectors are perpendicular to each other in n-dimensional space. In 2D space, this corresponds to a 90-degree angle between vectors, while in 3D space, it represents a 90-degree angle between planes formed by the vectors.

3. Orthogonal Subspaces:
   - [[subspace]] within a [[vector space]] can also be orthogonal to each other. Two subspaces, U and V, are orthogonal if every vector in U is orthogonal to every vector in V. This concept is particularly important in applications like least squares regression and the decomposition of matrices.

4. [[Orthogonal Matrix]]:
   - An orthogonal matrix is a square matrix whose rows and columns are orthogonal [[unit vectors]]. The [[invert|inverse]] of an orthogonal matrix is its [[transpose]], and this property has various applications in [[systems of linear equations]] and in rotations.

5. Gram-Schmidt Process:
   - The Gram-Schmidt process is a method for finding an orthogonal basis for a subspace. It is a crucial tool in linear algebra for orthogonalizing a set of linearly independent vectors.

6. Orthogonal [[diagonalization]]:
   - In the context of eigenvalues and eigenvectors, orthogonal diagonalization is a process where a matrix is decomposed into three matrices: P (a matrix of eigenvectors), D (a diagonal matrix of eigenvalues), and P^T (the transpose of the eigenvector matrix).

7. Applications:
   - Orthogonality has numerous applications in various fields, including physics, engineering, computer graphics, and signal processing. For instance, it is used in image compression, data analysis, and solving systems of linear equations.

8. Inner Product Spaces:
   - Orthogonality is a fundamental concept in inner product spaces, where an inner product generalizes the dot product. Inner product spaces allow for the extension of orthogonality to more abstract mathematical structures.

Conclusion:
Orthogonality is a central concept in linear algebra with wide-ranging applications in mathematics and beyond. Understanding how vectors, subspaces, matrices, and transformations relate to orthogonality is essential for solving a variety of problems in science and engineering. Whether you're working on linear systems, data analysis, or geometric transformations, the concept of orthogonality will frequently appear as a powerful tool in your toolkit.