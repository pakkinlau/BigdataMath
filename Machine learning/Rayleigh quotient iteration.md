- Combining [[Power iteration]] and [[Inverse iteration]], we got Rayleigh quotient iteration. 

---

## The changes

- 1. Improved initial guess
	- Instead of pick some random $\mu$, now we pick $v^{(0)}$ and our initial eigenvalue $\lambda^{(0)} = (v^{(0)})^T A v^{(0)}$. This expression is based on [[Rayleigh quotient]].
- 2. Improved convergence
	- Not only changing the initial guess, but also giving a faster convergence by sticking $\mu = \lambda^{(k-1)} = (v^{(k-1)})^T A v^{(k-1)}$

So Rayleigh quotient iteration has such construction:
- $(A-\lambda^{(k-1)}I)w=v^{(k-1)}$
- The shift $\mu = \lambda^{(k-1)}$ helps the iteration converge faster towards the desired eigenvalue and its corresponding eigenvector. 

---
## Algorithm

![[Pasted image 20231126175246.png]]


---

## Cubic convergence

- Rayleigh quotient has a cubic convergence in the following sense:
	- $\|v^{(k+1)}-(\pm q y)\|=O(||v^{(k)}-(\pm q y)|^{3})$ 
	- $|\lambda^{(k+1)}-\lambda_{J}|=O(|\lambda^{(k)}-\lambda_{J}|^{3})$


