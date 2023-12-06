- Combining [[Power iteration]] and [[Inverse iteration]], we got Rayleigh quotient iteration. 

---

Idea 1: Rayleigh quotient is just [Inverse iteration](Inverse%20iteration.md), with a substitution of $\lambda^{(-1)}$ from $\mu$.  
- Replacing $\mu$ with $\lambda^{(k-1)}$ which would change together with the initial guess vector $v^{(k)}$ in each iteration. 

Idea 2: Since the left multiplying matrix $A-\lambda^{(k-1)}I$ is changing in each iteration, the convergence is much effective. 
- So the convergent rate would be larger. Each iteration triples the number of digits of accuracy. 

Idea 3: In stability analysis, we just put a power of $3$ in the order of error, comparing to power iteration. 
- $||v^{(k+1)}-(\pm q_{J})||=O(||v^{(k)}-(\pm q_{J})||^{3})$
- $|\lambda^{(k+1)}-\lambda_{J}|=O(|\lambda^{(k)}-\lambda_{J}|^{3})$



---
## Algorithm

![[Pasted image 20231126175246.png]]


---

## Cubic convergence

- Rayleigh quotient has a cubic convergence in the following sense:
	- $\|v^{(k+1)}-(\pm q y)\|=O(||v^{(k)}-(\pm q y)|^{3})$ 
	- $|\lambda^{(k+1)}-\lambda_{J}|=O(|\lambda^{(k)}-\lambda_{J}|^{3})$


