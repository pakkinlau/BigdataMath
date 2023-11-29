**Definition:**
In linear algebra, a singular matrix is a square matrix that does not have an [[invert|inverse]]. A square matrix $A$ is said to be singular if its determinant ($\text{det}(A)$) is zero. Determinant measures the scaling factor of the matrix and is crucial in determining whether a matrix has an inverse. If the determinant is zero, the matrix is singular, indicating that the matrix's columns (or rows) are linearly dependent, and it cannot be inverted.

**Properties and Characteristics:**
1. **No Unique Solution:** When a system of linear equations is represented as $AX = B$ and $A$ is singular, the system either has no solutions or infinitely many solutions but never a unique solution.
- alternative for solving equations / transformation containing singular matrices:
	- [[Pseudo-inverse matrix|Pseudo-inverse]]: It provides a solution in the [[Least Squares]] sense. 

1. **Singular Matrices and Determinants:** For an $n \times n$ matrix $A$ to be singular, $\text{det}(A)$ must be equal to zero: $\text{det}(A) = 0$.

2. **Linear Dependence:** The columns (or rows) of a singular matrix are linearly dependent. This means that one or more columns (or rows) can be expressed as a combination of the others.

3. **Rank and Singularity:** The rank of a singular matrix is always less than $n$, where $n$ is the number of rows (or columns) of the matrix.

**Applications:**
1. **Homogeneous Systems:** Singular matrices frequently arise in the context of homogeneous systems of linear equations, where the constant vector $B$ is zero. In such cases, the system may have infinitely many solutions or no solution at all.

2. **Least Squares Problems:** In statistics and data fitting, singular matrices can occur in least squares problems. Dealing with singular matrices in these contexts often involves techniques like regularization or pseudoinverse methods.

3. **Computer Graphics and Transformations:** Singular matrices are used in computer graphics to represent transformations that collapse a higher-dimensional space into a lower-dimensional one, like projecting 3D objects onto a 2D plane.

**Conclusion:**
Understanding singular matrices is fundamental in linear algebra, as they provide critical insights into the solvability of systems of equations and the properties of transformations. Recognizing singular matrices and their implications is essential in various fields, enabling mathematicians, scientists, and engineers to tackle real-world problems involving linear relationships.

---

- It means non-invertible /degenerate matrix / the matrix that don't have inverse matrix. 
- Or when all rows / columns are dependent, then it is singular matrix (See 13:50 of video: https://www.youtube.com/watch?v=lGGDIGizcQ0)
	- If there are dependent rows / columns in a square matrix. It means at least 1 row could be reduced to all zero terms row / column. It means the determinant would be zero. 