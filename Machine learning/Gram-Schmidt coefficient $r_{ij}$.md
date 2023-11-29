12/11/2023

**Concept: Gram-Schmidt Coefficient**

**Context: Linear Algebra**

The Gram-Schmidt process is a fundamental technique in linear algebra used for transforming a set of linearly independent vectors into an orthogonal orthonormal set. The Gram-Schmidt coefficients play a crucial role in this process.

**Gram-Schmidt Process Overview:**

1. **Given Set of Vectors:** Start with a set of linearly independent vectors $\{v_1, v_2, \ldots, v_n\}$.

2. [[Projection formula]]: Recall the projection of $v$ onto $u_i$, we have formula:
$$
\text{proj}_{u_i}(v) = c_i u_i = \frac{v \cdot u_i}{\|u_i\|^2} \cdot u_i$$

3. **Orthogonalization:** The Gram-Schmidt process involves iteratively constructing orthogonal vectors. For $i = 1, 2, \ldots, n$, the $i$-th vector, $u_i$, is obtained by subtracting the projections of $v_i$ onto the previously constructed vectors $u_1, u_2, \ldots, u_{i-1}$:
$$ u_i = v_i - \sum_{j=1}^{i-1} \text{proj}_{u_j}(v_i)$$
After the subtraction, $u_i$ now is orthogonal to $v_i$. 


4. **Normalization:** Once all the orthogonal vectors are obtained, they are normalized to form an orthonormal set:
$$ e_i = \frac{u_i}{\|u_i\|}$$

   Here, $e_i$ represents the orthonormalized vectors.

**Gram-Schmidt Coefficients:**

The Gram-Schmidt coefficients are the scalars used in the orthogonalization step of the process. For each $i$, the coefficients $\text{proj}_{u_j}(v_i)$ determine the projection of $v_i$ onto the subspace spanned by the vectors $u_1, u_2, \ldots, u_{i-1}$.

Mathematically, the projection of $v_i$ onto $u_j$ is given by:
$$ \text{proj}_{u_j}(v_i) = \frac{\langle v_i, u_j \rangle}{\langle u_j, u_j \rangle}u_j$$

Here, $\langle \cdot, \cdot \rangle$ denotes the inner product. The Gram-Schmidt coefficients are the scalar multiples $\frac{\langle v_i, u_j \rangle}{\langle u_j, u_j \rangle}$ in the orthogonalization process.

We can rewrite the projection as: $\text{proj}_{u_j}(v_i) = r_{ij} u_j$

This simplification highlights the role of Gram-Schmidt coefficient in determining the projection of $v_i$ onto the subspace spanned by $u_j$, making the understanding and computation of $r_{ij}$ essential in the orthogonalization process. 

---

**Significance:**

- The Gram-Schmidt process and coefficients are crucial in various applications, including solving linear systems, computing eigenvalues, and constructing orthonormal bases.

- The orthonormal basis obtained through the Gram-Schmidt process simplifies many linear algebraic computations and provides a clearer geometric understanding of vector spaces.

Understanding the Gram-Schmidt coefficients is essential for grasping the intricacies of the Gram-Schmidt process and its applications in linear algebra.