
- Idea 1: While power iteration we can find the most dominant eigenvector, inverse iteration we can find any single eigernvector. 
	- Inverse iteration is particularly useful when you need to find the eigenvectors corresponding to a specific eigenvalue, or when you want to find eigenvalues close to a certain target value.
**Advantages:**
1. Inverse iteration is particularly effective for finding eigenvalues close to the specified target value ($\sigma$).
2. It converges faster when the target eigenvalue is well-separated from the other eigenvalues.

Idea 2: $(A - μI)$ alone won't work because this will stretching and squishing the matrix from eigenvector; the inverse of $(A - μI)$ undoes the stretching and squishing
- Consider the case that $(\lambda - \mu) v$:
	- When $\lambda$ and $\mu$ are close to each others, then $(A - \mu I) v \approx (\lambda - \mu) v$, which $(\lambda - \mu) v$ is close to zero vector if $\lambda$ is close to $\mu$. 
	- $μ$ is greater than 1, the vector is stretched (its length is increased); $μ$ is less than 1, the vector is squished (its length is decreased).
	- The closer $\mu$ approach towards $\lambda$, the smaller value we could get. 
- In opposite, in the case of having $(A - \mu I)^{-1}$:
	- if $\lambda$ and $\mu$ are close to each others, the effect of multiplying $v$ by $(A - \mu I)^{-1}$ is to stretch $v$ significantly. The closer $\mu$ approach towards $\lambda$, the bigger value we could get. 

Idea 3: While $(A - \mu I)^{-1} v$ naturally arise its value in each iteration, by normalizing the vector we can controlling it from exploding gradient. 
- Therefore, at each step, $v$ becomes more aligned with the desired eigenvector. 

Idea 4: $A$ and $(A - \mu I)^{-1}$ has the same set of eigenvectors. And the eigenvalue becomes $\frac{1}{\lambda - \mu}$
	Part 1: Unchanged eigenvector, shifted eigenvalue on $A$ versus $(A - \mu I)$
	- $Av = \lambda v$, where $v$ is eigenvector of $A$ 
	- If $v$ is an eigenvector of $A$ corresponding to $\lambda$, then $(A - \mu I)v = Av - \mu Iv = \lambda v - \mu v = (\lambda - \mu) v$
		- Which shows $v$ is eigenvector of $(A - \mu I)$ corresponding to eigenvalue $\lambda - \mu$. 
	- From this, we observe that "the eigenvector $v$ remain the same while eigenvalues of $A$ are shifted when we just subtract $A$ by $\mu I$. "
	- We can also explain this by the fact that all matrix $A$ is similar to their eigenvalue matrix due to $A = X^{-1} \Lambda X$ for all $A$ which has non singular eigenvector matrices. 
	Part 2: Unchanged eigenvector, inversed eigenvalue on $(A - \mu I)$ versus $(A - \mu I)^{-1}$
	- Given $(A - \mu I)$, the inverse $(A  - \mu I)^{-1}$ exists if it is invertible.
	- Then $(A - \mu I)^{-1} v = \frac{1}{\lambda} v$
	- From this, we observe that "the eigenvector $v$ remain the same while eigenvalues of $A$ are inverted. "
	Conclusion: $A$ and $(A - \mu I)^{-1}$ has the same set of eigenvectors. And the eigenvalue becomes $\frac{1}{\lambda - \mu}$
	- The algorithm leverages the shared eigenvectors to compute the desired eigenvalues. 
	- The way of obtaining corresponding eigenvalues is by [[Rayleigh quotient]]. 

Idea 5: Stability analysis
- $||v^{(k)}-(\pm q_{J})||=O\left(\left|\frac{\mu-\lambda_{J}}{\mu-\lambda_{K}}\right|^{k}\right)$
	- This expression can be obtained from what we got in [[power iteration]]: $||v^{(k)} - (\pm q_1)|| = O(| \frac{\lambda_2}{\lambda_1})|^k)$
	- During inverse iteration, $\lambda$ drifted by $\mu$ therefore we have such changes. 
- $|\lambda^{(k)}-\lambda_{J}|=\,{O}\left(\left|\frac{\mu-\lambda_{J}}{\mu-\lambda_{K}}\right|^{2k}\right)$ 
	- This expression also can be obtained from what we have got in [Power iteration](Power%20iteration.md). 

Idea 6: While [Power iteration](Power%20iteration.md) obtain eigenvalue estimate from an eigenvector estimate, inverse iteration obtain eigenvector from an eigenvalue estimate. 

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
