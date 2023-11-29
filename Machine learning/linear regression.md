9/9/2023


---

- linear regression as an [[over-determined|overdetermined]] linear problem

## 1. SVD on linear regression

  

The least squares solution $\tilde{x}$ for the linear regression problem can be expressed as:

$\tilde{x} = V^T \left( \Sigma^{-1} \right) U^T b$

Where:

- $\tilde{x}$ is the vector representing the coefficients of the regression line.
- $V^T$ is the transpose of the right singular matrix.
- $\Sigma^{-1}$ represents the inverse of the diagonal matrix $\Sigma$, obtained by taking the reciprocal of its non-zero elements.
- $U^T$ is the transpose of the left singular matrix.
- $b$ is the vector representing the noisy measurements.

This formula represents the mathematical expression of the least squares regression calculation using the singular value decomposition.

---

## Derivation

- See [[Least Squares]]