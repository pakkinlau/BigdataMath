
The concept of the relative condition number ($\kappa$) is fundamental in evaluating the stability and sensitivity of mathematical problems concerning input variations and resulting output changes. It involves two key elements: a mathematical function or operation and a set of input values.


---

## Perturbation of vectors 

For a given problem represented by the function $f(x)$, where $x$ denotes the input and $\delta x$ represents a small perturbation in $x$, the relative condition number is defined as:


$$ \kappa = \sup_{{ \delta x }} \frac{{\| \delta f \| / \| f \|}}{{\| \delta x \| / \| x \|}}$$

Here:
- $\| \cdot \|$ signifies a norm (e.g., Euclidean norm) measuring vector or matrix magnitude.
- $\delta f$ embodies the change in the output $f(x)$ due to the perturbation $\delta x$ in the input.

Kappa and Jacobian
- A key normalization factor accounts for the initial scale of $f(x)$. If $J$ denotes the Jacobian matrix of $f(x)$, then $\kappa$ can be expressed as $\kappa = \frac{{\|J(x)\|}}{{\|f(x)\| / \|x\|}}$, indicating the ratio of the norms of $J(x)$ and the normalized output and input.
- The interpretation of $\kappa$ is pivotal. A condition number around $10^2$ signifies a well-conditioned problem, indicating stability against input variations. In contrast, a $\kappa$ reaching $10^6$ signifies an ill-conditioned problem, showcasing heightened sensitivity to input perturbations.

Magnitude and condition
- Moreover, in practical numerical operations, such as matrix multiplications involving double precision (limited to around 16 decimal places), the maximum attainable condition number typically caps around $10^{16}$. This limitation arises due to numerical round-off errors influencing the precision of calculations.

In summary, the relative condition number offers crucial insights into the stability of mathematical problems against input perturbations. Understanding its implications helps assess the reliability and robustness of computational algorithms and mathematical models.

---
## Perturbation of matrices

Now consider we have the action $x \mapsto Ax$, where $A \in \mathbf{C}^{m \times n}$. 

$$ \kappa = \sup_{{ \delta x }} \frac{{\| \delta f \| / \| f \|}}{{\| \delta x \| / \| x \|}} = \sup_{{ \delta x }}  \frac{||A(x + \delta x) - Ax||}{||Ax||} / \frac{|| \delta x||}{||x||})$$

If $A$ is square / non-singular, (thus it has an inverse), then we have:  
- $||x|| = ||A^{-1}(Ax)|| \leq ||A^{-1}|| ||Ax||$
	- This inequality is true, and we have already discussed this in [[cauchy-schwarz inequalities and holder inequalities]] section. 
- Note that $\underset{\delta x}{sup} \frac{||A \delta x||}{||\delta x||} = ||A||$. (Recall definition of [[Norm]]). 
- substitute back this result to the definition of $\kappa$, then we have: $\kappa = ||A|| \frac{||x||}{||Ax||} \leq ||A|| ||A^{-1}||$ for square and non-singular matrix, 

So it is starting to set you up about computing inverses. 
The way we compute the inverse matrix is by SVD. 

---
condition number of a nonsingular matrix $A$ is defined by $\kappa (A) = ||A|| ||A^{-1}||$ for square and non-singular matrix, $\kappa(A) = ||A||||A^+||$ for non-square and singular matrix.

From SVD, $||A|| = \sigma_1$. 
- How can get this?
	- $A = U \Sigma V^{*}$. 
	- When computing $||A||$, norm of $U$ and $V$ are 1. And the norm of diagonal matrix is the largest diagonal value, which is $\sigma_1$. 

Considering $A^{-1}$ or $A^+$ (pseudo-inverse matrix)
- $A^{-1} = V\Sigma^{-1}U^*$
- When computing $||A^{-1}$||, comparing the case of $||A||$, now we have $\Sigma^{-1}$ that is flipped and also values of diagonal values was became denominators. So we have  $\frac{1}{\sigma_m}$.

Coming back to the definition of $\kappa$, 
$\kappa(A) = ||A||||A^+|| = \frac{\sigma_1}{\sigma_m}$

---

## Perturbation of Systems of Equations

Consider a linear system represented as $Ax = b$, where $A$ is a matrix of coefficients, $x$ is the vector of unknowns, and $b$ is the vector of constants.

### Perturbation in Matrix $A$

When matrix $A$ experiences a perturbation denoted by $\delta A$, it influences the solution $x$ by a corresponding perturbation $\delta x$. The perturbed system becomes $(A + \delta A)(x + \delta x) = b$.

Expanding this equation yields:
$$
Ax + A(\delta x) + (\delta A)x + \delta A(\delta x) = b
$$

Considering only the linear terms and leveraging the original equation $Ax = b$, we can isolate the impact of the perturbation:
$$
A(\delta x) + (\delta A)x = 0 \implies \delta x = - A^{-1} (\delta A) x
$$

This expression reveals that the perturbation in the solution ($\delta x$) is linked to the perturbation in $A$ ($\delta A$) and the solution $x$ itself through the inverse of $A$.

Again, we make use of [[cauchy-schwarz inequalities and holder inequalities|triangular inequality]] again, we can see that this equation also implies that $||\delta x|| \leq ||A^{-1}|| || \delta A|| || x ||$, or equivalently, $\frac{|| \delta x||}{||x||} / \frac{|| \delta A||}{||A||} \leq ||A^{-1}|| ||A|| = \kappa(A)$.

Equality in this bound will hold whenever $\delta A$ is such that $||A^{-1}( \delta A) x|| = ||A^{-1}|| ||\delta A || ||x||$.


### Implications and Stability

The sensitivity of the solution to perturbations in $A$ relies heavily on the properties of $A$ and its inverse. If $A$ is well-conditioned, meaning its condition number ($\kappa$) is moderate, small changes in $A$ lead to proportional changes in the solution.

However, if $A$ is ill-conditioned, having a high condition number, even minor perturbations in $A$ can lead to significant variations in the solution. This sensitivity underscores the importance of considering numerical stability and conditioning when solving linear systems, especially in computational applications.

### Computational Considerations

In practical scenarios, the computation of $A^{-1}$ directly might be numerically challenging due to potential issues such as singularity or ill-conditioning. Instead, methods like LU decomposition, QR factorization, or iterative solvers are often preferred for solving linear systems due to their stability and efficiency.

Furthermore, evaluating the impact of perturbations in $A$ helps in understanding the robustness of numerical algorithms used to solve linear systems. Techniques that account for these perturbations, ensuring reliable and accurate solutions, are fundamental in various fields, including engineering, physics, and data analysis.
