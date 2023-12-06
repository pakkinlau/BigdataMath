
- superset:
	- [[Orthogonalization]]

- When people mention "triangular orthogonalization", they are often referring to either the [[Modified Gram-Schmidt iteration]] or [[Household triangularization]]. 

- It is a broad concept that describing "orthogonalizing a matrix, in triangular manner".
- [[Reduced QR decomposition|Gram-Schmidt orthogonalization]] falls into the category of triangular orthogonalization 

---

## Steps of working on triangular orthogonalization

Each step of the modified Gram-Schmidt algorithm can be interpreted as a right-multiplication by a square upper-triangular matrix. 

Recall [[Modified Gram-Schmidt iteration]], we have 
- $v_j = P_j a_j$ 
- $q_j = \frac{v_j}{||v_j||}$
- $P_j = P_{\perp_{qj-1}} \dots  P_{\perp_{q2}} P_{\perp_{q1}}$
- $P_1 = I$

Triangular orthogonalization:
- We think of modified Gram-Schmidt as $AR_1 R_2 \dots R_n = \hat Q$.  Where $R_k = \begin{bmatrix} 1 & & & \\ & 1 & & \\ & & \frac{1}{r_{kk}} &  -\frac{r_{34}}{r_{33}}\\ & & & \ddots \end{bmatrix}$
- The whole sequence of matrix $R_i$ can be thought as $\hat R^{-1}$. 

---
## Details of the progress

Gram-Schmidt as Triangular orthogonalization
- The outer step of [Modified Gram-Schmidt iteration](Modified%20Gram-Schmidt%20iteration.md) can be thought as a right-multiplication by a square upper-triangular matrix. 

## Step 1: 
- $v_1$ is column vector of our matrix $A$. 
- In all $r$ coefficients that is not align with $v_1$, there is $-r_{1k}$. That is corresponding to how we subtract orthogonal components in [Unstable Gram-Schmidt process](Unstable%20Gram-Schmidt%20process.md). Also, all $r$ coefficient has a denominator $r_{11}$ there. It is because we need to normalize $v_1$ into $q_1$. 


$\begin{bmatrix} v_1 & v_2 & \dots & v_n \end{bmatrix} \begin{bmatrix} \frac{1}{r_{11}} & \frac{-r_{12}}{r_{11}} & \frac{-r_{13}}{r_{11}} & \dots \\ & 1 & & \\ & & 1 & \\ & & & \ddots \end{bmatrix} = \begin{bmatrix} q_1 & v_2^{(2)} & \dots & v_n^{(2)} \end{bmatrix}$

This is equivalent to right multiplication by a matrix $R_1$ 

Step 2: 

$\begin{bmatrix} v_1 & v_2 & \dots & v_n \end{bmatrix} \begin{bmatrix} \frac{1}{r_{11}} & \frac{-r_{12}}{r_{11}} & \frac{-r_{13}}{r_{11}} & \dots \\ & 1 & & \\ & & 1 & \\ & & & \ddots \end{bmatrix} \begin{bmatrix} 1 & & & \\ & \frac{1}{r_{22}} & \frac{-r{23}}{r_{22}} & \dots \\ & & 1 & \\ & & & \ddots \end{bmatrix} = \begin{bmatrix} q_1 & q_2 & v_3^{(3)}\dots & v_n^{(3)} \end{bmatrix}$

This is equivalent to right multiplication by a matrix $R_1$ and $R_2$.

Step $i$:

The $i$th column is divided by $r_{ii}$, and then subtract $r_{ij}$ times the result from each of the remaining columns, for $j>i$. 

Finally, we have $AR_1 R_2 \dots R_n = \hat Q$, 
or $A \hat R^{-1} = \hat Q$

This shows [[Modified Gram-Schmidt iteration]] is a method of triangular orthogonalization.


---


---






