
- Idea 1: The basic idea of QR algorithm is to decompose the matrix into its QR factorization and then multiply the factors in reversed order
	- That is, $Q^{(k)}R^{(k)} = A^{(k-1)}$, and then $A^{(k)} = R^{(k)} Q^{(k)}$

- Idea 2: When you multiply $RQ$, you are basically performing Schur transformation $Q^{-1}AQ$, which is a similarity transformation that preserves the eigenvalues of$A$. 
	- Rearranging terms, we have $R^{(k)} = (Q^{(k)})^T A^{(k-1)}$, and $R^{(k)}Q^{(k)} = (Q^{(k)})^T A^{(k-1)}Q^{(k)}$
	- $R^{(k)}Q^{(k)}$ is an allowable move is because $A$ is similar to $(Q^{(k)})^T A^{(k-1)}Q^{(k)}$, and 

- Idea 3: Eigenvalues do not change during iterations, eigenvector does.
	- Since the idea is similar transformation underneath the algorithm, eigenvalues of the initial guess matrix $A^{(0)}$ would not change.
	- To see how eigenvectors evolves during iterations, consider the following:
		- Before any changes, we have $A v = \lambda v$. 
		- After 1 iteration, we have $A_1 v = (RQ) v = R(Qv)$, which $RQ$ is a similar transformation of $A$. 
		- An idea of how $v$ evolve as follow: Since `R` is upper triangular, its columns are becoming sparser (more zeros) as you move from left to right. Therefore, if `Qv` is aligned more with a right-side column (which has more zeros), the resulting vector after multiplication by `R` will have more zero components, making it "closer" to the coordinate axes in a certain sense.

- Idea 4: To understand how eigenvectors evolves in QR algorithm, study [Simultaneous iteration](Simultaneous%20iteration.md). 
---

## Algorithm

![](Pasted%20image%2020231206143515.png)

---
## Key Notes

- The QR algorithm is computationally expensive, but there are various ways to optimize it, such as using the shifted QR algorithm, which includes an additional step to speed up convergence.
- The QR algorithm does not work well with all types of matrices. For example, it can fail to converge for some complex or non-diagonalizable matrices.
- Despite its limitations, the QR algorithm is still one of the most reliable numerical methods for finding the eigenvalues and eigenvectors of a matrix.

## Applications

The QR algorithm is used in a wide range of fields and applications, including:

- Linear algebra and matrix computations
- Machine learning and data analysis
- Quantum physics and engineering
- Computer graphics and image processing

## Further Reading

For a deep dive into the mathematical details of the QR algorithm, you may refer to:

1. Golub, G. H., & Van Loan, C. F. (2012). "Matrix Computations" (Vol. 3). JHU press.
2. Trefethen, L. N., & Bau III, D. (1997). "Numerical linear algebra" (Vol. 50). SIAM.

## Summary

The QR algorithm is a powerful tool in numerical linear algebra for the computation of eigenvalues and eigenvectors. Although it is computationally expensive, it is widely used due to its reliability and the availability of various optimizations.