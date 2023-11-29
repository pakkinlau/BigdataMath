---
alias: [invariant, Shift-invariant, shift-invariant, translation-invariant, equivariance, invariance]
---


- 28-9-2022: created

- That means discrete equivalent of the system.
	- Let say $x(n) \rightarrow y(n)$, then $x(n-k) \rightarrow y(n-k)$

- Permutation invariance / Permutation equivariance
	- Graph does not have a [[canonical]] order of the node
	- We can have many different order plans

- Example: ^714cff
	- Consider we learn a function $f$ that maps $G = (A,X)$ to a vector $R^d$ then $f(A_1, X_1) = f(A_2, X_2)$. If $f(A_i, X_i) = f(A_j, X_j)$ for any order of $i$ and $j$, we formally say $f$ is a permutation invariant function.
	- For a graph with $m$ nodes, there are $m!$ different order plans.
	- We learn a function $f$ that maps nodes of $G$ to a matrix $R^{m \times d}$.

---
## Reference
- Wikipedia: https://www.wikiwand.com/en/Shift-invariant_system