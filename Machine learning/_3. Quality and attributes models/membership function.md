---
alias: [membership]
---

- 6-10-2022: created

- [[membership function]] of a a [[fuzzy set]]  is a generalization of the [[indicator function]] (which set the proper subset as 1, and non-members as 0), for classical sets. (wiki)
- In represents the [[degree of truth]] as an extension of valuation.  (wiki)

- In classical set theory, [[indicator function]] express membership like this: (wiki)

$1_A(x) :=\begin{cases} 1,\ if\ x \in A, \\ 0,\ if\ x \notin A \end{cases}$

![[Pasted image 20221006111154.png]]
- Figure:  Membership function of a fuzzy set $X$ (wiki). the vectical axis $\mu(X)$ is called membership degree of $x \in X$ in a fuzzy set A. $\mu(X)$ reach the highest value = 1 if X is matching the centroid of the feature value from the samples.  (wiki)
- If $u(X) \geq 0.5$ in fuzzy set theoretical sense, which is equivalent to  $1_A = 1$ in classical set theoretical sense. 
---
## Limitation

- 1. How do we define the membership function?
	- No learning mechanism
- 2. Defuzzification can produce undesired results. 
- 3. Membership values begin to move away from expectations when chains of logic are lengthy.
- 4. Crisp/precise models can be more efficient and even convenient.


- See also
	- [[defuzzification]]
	- Fuzzy measure theory
	- Fuzzy set operation
	- Rought set
