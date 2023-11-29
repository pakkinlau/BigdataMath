---
alias: linearly independent

---

- Definition:
	- Linear independence is a fundamental concept in linear algebra that characterize the relationship between [[vector]] (in a vector space). 
	- It is a crucial property that helps us understand the structure and behavior of vector sets and is used extensively in various mathematical and scientific fields.
- Importance:
	- Linear independence is a critical concept in linear algebra because it determines the [[dimensionality]] of vector spaces and the existence of unique solutions to systems of linear equations.
	- Linearly independent sets of vectors are fundamental in creating a basis for vector spaces, which is a minimal set of vectors that can [[span]] the entire space.
- Key points:
	- [[vector]] and [[vector space]]
	- [[linear combination]]
- Geometric interpretation:
	- Geometrically, linearly independent vectors in 2D or 3D space do not lie on the same line or plane, respectively. In higher dimensions, linear independence indicates that the vectors span a [[hyperplane]] of the vector space.


- Independent columns
	- The only solution to $Ax = 0$ is $x = 0$. The nullspace is $\mathbb{Z}$
- Independent vectors
	- 1. Set up a linear combination
		- $c_1v_1 + c_2v_2 + \dots + c_nv_n = 0$
	- 2. Solve for coefficients
	- 3. Check for solutions
		- If the only solution is the trivial solution ($c_1 = c_2 = \dots = c_n$), then the set of vectors is linear independent. 
	- 4. Linearly dependent if non-trivial solutions exist
		- if there exist values of $c_1, c_2, \dots, c_n$ that are not all zero and still satisfy the equation $c_1v_1 + c_2v_2 + \dots + c_nv_n = 0$, then the set of vectors is linearly dependent. 
			- Which means that at least some of the vectors in the set are dependent on each other. 

- Check linear independent using python program
	- `np.linalg.rref(matrix)` 
		- returns the [[row echelon form]] of the matrix
	- `rref_matrix`: 
		- It is a numpy array, and a numpy array is packed by row by row basis. 
	- `np.allclose()`: 
		- Used to check if all elements of two arrays are approximately equal within a specified tolerance. 
		- If `np.allclose(row,0)` return true, it means all elements in the row approximates to zero.
```python
import numpy as np
from scipy.linalg import rref

def are_linearly_independent(vectors):
    matrix = np.array(vectors)
    rref_matrix, _ = rref(matrix)
    
    # Check if there are any rows of zeros in the RREF
    for row in rref_matrix:
        if np.allclose(row, 0):
            return False
    return True

# Example usage
vectors = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = are_linearly_independent(vectors)
if result:
    print("The vectors are linearly independent.")
else:
    print("The vectors are linearly dependent.")

```


- Related concepts:
	- Basis
	- Span
	- Subspace
	- Dimension
	- Rank
	- Nullity
	- Linear transformation
	- Orthogonality
	- Eigenvalues and eigenvectors
	- Linear Algebraic Equations
	- [[Gram-Schmidt Process
