[[Household reflector]]
---
## Householder on "Reduction to Hessenberg form": 

Householder reflectors are a key component in various numerical algorithms, especially in the context of reducing a matrix to Hessenberg form. A Hessenberg matrix is a square matrix that is upper triangular, except for the subdiagonal directly below the main diagonal. The Householder transformation is used to zero out elements below the first subdiagonal, transforming a matrix into Hessenberg form. There are different types of Householder reflectors, and the choice of reflector depends on the specific requirements of the problem at hand.

Recall the definition of Householder reflector: 
$$ H = I - 2 \times \frac{vv^T}{\|v\|^2}$$

where $I$ is the identity matrix and $\|v\|$ represents the Euclidean norm of the vector $v$. The vector $v$ is carefully chosen to achieve specific numerical properties. For a Householder transformation to be effective in reducing a matrix to Hessenberg form, it is crucial that the resulting transformation zeroes out the appropriate entries below the first subdiagonal.

If the Householder reflector is chosen such that it zeroes out the correct entries below the first subdiagonal, it will effectively reduce the matrix to Hessenberg form. However, if the Householder reflector is not appropriately chosen, it may not zero out the necessary entries, leaving the matrix in a form that is not Hessenberg.

In summary, the effectiveness of a Householder reflector in producing a Hessenberg form depends on the careful selection of the reflector vector $v$. Choosing the right reflector vector ensures that the Householder transformation correctly zeroes out the desired entries, leading to a Hessenberg matrix. Different types of Householder reflectors might be suitable for different situations, and the choice of reflector depends on the specific problem and the mathematical properties required for the transformation.

---
## Observations

1. Eigenvalues during reducing matrices to Hessenberg form, would not change the eigenvalues of the matrix. 

Reducing a matrix to Hessenberg form involves a sequence of similarity transformations that aim to upper-triangularize the matrix, with the exception that the lower sub-diagonal can have non-zero elements. A matrix is said to be in Hessenberg form if it has zeros below the first sub-diagonal. Eigenvalues are special numbers associated with a square matrix that do not change under similarity transformations. This property is crucial to understanding why eigenvalues remain unchanged during the process of reducing matrices to Hessenberg form.

Let's consider a square matrix $A$ and its eigenvalue equation:
$$ A \mathbf{v} = \lambda \mathbf{v}$$

where $\lambda$ is an eigenvalue of $A$ and $\mathbf{v}$ is the corresponding eigenvector. Now, if we perform a similarity transformation on $A$ to obtain a Hessenberg matrix $H$ as follows:
$$ H = P^{-1} A P$$

where $P$ is an invertible matrix, the eigenvalue equation for $H$ becomes:
$$ H (\mathbf{u}) = P^{-1} A P (\mathbf{u}) = \lambda (\mathbf{u})$$

where $\mathbf{u} = P^{-1} \mathbf{v}$.

Here's why the eigenvalues remain unchanged:

1. **Similarity Transformations**: The eigenvalues of a matrix are invariant under similarity transformations. That means if $A$ and $B$ are similar matrices (i.e., $B = P^{-1} A P$ for some invertible matrix $P$), they share the same eigenvalues.

2. **Hessenberg Form as a Special Case**: When you reduce a matrix to Hessenberg form, you are essentially performing a similarity transformation on the original matrix $A$ to get $H$. Since eigenvalues are preserved under similarity transformations, the eigenvalues of $A$ and $H$ are the same.

In summary, reducing a matrix to Hessenberg form involves only similarity transformations, and eigenvalues are preserved under such transformations. Therefore, the eigenvalues of the original matrix will not change during the process of reducing it to Hessenberg form.


2. A bad Householder reflector cannot leading us transforming the matrix $A$ towards upper triangular matrix (when $A$ is non-hermitian), or transforming the matrix $A$ towards diagonal matrix (when $A$ is hermitian)


---

## How to choose a good $v$?

Choosing a good vector $v$ for the Householder transformation is crucial to ensuring that the resulting matrix is reduced to Hessenberg form effectively. Here's how you can choose a suitable $v$:

1. **Choose the Correct Dimensions**: The vector $v$ should have the same dimensions as the column of the matrix that you want to transform. If you're transforming an $n \times n$ matrix $A$, $v$ should be an $n$-dimensional vector.

2. **Select the Target Column**: Determine the column of the matrix that you want to zero out below the first subdiagonal. Typically, you start with the second column since the first column is already in the correct position for a Hessenberg matrix.

3. **Construct $v$ to Target the Subdiagonal Elements**: Let's say you want to zero out elements in column $j$ below the diagonal. The vector $v$ should be constructed as follows:
$$v = [0, 0, ..., 0, \text{sign}(A[j+1,j]), A[j+1,j], A[j+2,j], ..., A[n,j]]$$

   Here, $\text{sign}(x)$ is a function that returns -1 if $x$ is negative, 1 if $x$ is positive, and 0 if $x$ is zero. This ensures that the Householder reflector flips the sign of the subdiagonal element to make it zero.

4. **Normalize $v$**: To ensure that the Householder transformation is unitary, $v$ needs to be normalized. Compute the Euclidean norm of $v$ (i.e., $||v||$) and divide each element of $v$ by this norm:
$$v = \frac{v}{||v||}$$

   Normalizing $v$ makes the Householder reflector a unitary matrix, preserving the orthogonality and ensuring numerical stability.

5. **Apply the Householder Transformation**: Using the formula I provided in the previous response:
$$H = I - 2 \times \frac{vv^T}{\|v\|^2}$$

   Multiply $H$ with the matrix $A$ from the left side: $HA$. This will zero out the subdiagonal elements in column $j$.

6. **Iterate**: Repeat steps 3 to 5 for columns $j+1, j+2, \ldots, n-1$ to zero out the subdiagonal elements in those columns as well.

By carefully selecting the vector $v$ for each column, you can systematically transform the given matrix into Hessenberg form. The choice of $v$ ensures that the Householder reflectors remove the appropriate elements below the subdiagonal, leading to an upper Hessenberg matrix.


----
