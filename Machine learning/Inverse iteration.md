

**Introduction:**
Inverse iteration is a numerical method used in linear algebra to find the eigenvectors and eigenvalues of a square matrix. Eigenvectors and eigenvalues are essential in various applications, including solving systems of linear differential equations, stability analysis, and computer graphics. Inverse iteration is particularly useful when you need to find the eigenvectors corresponding to a specific eigenvalue, or when you want to find eigenvalues close to a certain target value.

---

**Basic Idea:**
The fundamental concept behind inverse iteration is to apply the power iteration method to the inverse of the matrix in question. Power iteration is an iterative method for approximating the dominant eigenvector of a matrix. Inverse iteration takes advantage of this approach by using it on the inverse of the original matrix.

---

Q: Why $A$ and $(A - \mu I)^{-1}$ has the same set of eigenvectors?

Part 1: $A$ versus $(A - \mu I)$
- $Av = \lambda v$, where $v$ is eigenvector of $A$ 
- If $v$ is an eigenvector of $A$ corresponding to $\lambda$, then $(A - \mu I)v = Av - \mu Iv = \lambda v - \mu v = (\lambda - \mu) v$
	- Which shows $v$ is eigenvector of $(A - \mu I)$ corresponding to eigenvalue $\lambda - \mu$. 
- From this, we observe that "the eigenvector $v$ remain the same while eigenvalues of $A$ are shifted when we just subtract $A$ by $\mu I$. "

Part 2: $(A - \mu I)$ versus $(A - \mu I)^{-1}$
- Given $(A - \mu I)$, the inverse $(A  - \mu I)^{-1}$ exists if it is invertible.
- Then $(A - \mu I)^{-1} v = \frac{1}{\lambda} v$
- From this, we observe that "the eigenvector $v$ remain the same while eigenvalues of $A$ are inverted. "

Conclusion: $A$ and $(A - \mu I)^{-1}$ has the same set of eigenvectors. 
- The algorithm leverages the shared eigenvectors to compute the desired eigenvalues. 
- The way of obtaining corresponding eigenvalues is by [[Rayleigh quotient]]. 

Not used fact
- (And the corresponding eigenvalues are $\frac{1}{\lambda - \mu})$ . 
- This is not used in the algorithm. 

---
**Algorithm:**

![[Pasted image 20231126174200.png]]

1. **Choose an initial guess for the eigenvector $x_0$**. This can be any non-zero vector.
2. **Solve the system of equations $Ax = \lambda x$**, where $A$ is the matrix for which you want to find eigenvalues and $x$ is the current approximation of the eigenvector.
3. **Compute the new approximation $x_1$ using the formula**:  
$x_1 = (A - \sigma I)^{-1}x_0$$  
where $I$ is the identity matrix and $\sigma$ is an estimate of the eigenvalue you are interested in.
4. **Normalize $x_1$** to ensure it remains a unit vector.
5. **Repeat steps 2-4 until convergence**. Convergence can be determined by checking the difference between successive approximations or by a tolerance criterion.


---


---
**Advantages:**
1. Inverse iteration is particularly effective for finding eigenvalues close to the specified target value ($\sigma$).
2. It converges faster when the target eigenvalue is well-separated from the other eigenvalues.

**Considerations:**
1. **Choice of Initial Guess ($x_0$):** The accuracy and speed of convergence can be influenced by the initial guess for the eigenvector.
2. **Handling Singular Matrices:** Inverse iteration may not work well for singular or nearly singular matrices. Special techniques are needed to handle such cases.

**Conclusion:**
Inverse iteration is a powerful technique in linear algebra, allowing for the computation of specific eigenvalues and their corresponding eigenvectors. Understanding this method is valuable for various scientific and engineering applications where eigenvalues play a crucial role in analyzing the behavior of linear systems.