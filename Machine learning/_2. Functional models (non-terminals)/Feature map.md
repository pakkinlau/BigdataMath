---
alias: [map]
---

- 26-9-2022: created

- What is feature map?
	- Maps "attributes" into "features". Check the following demonstration for the meaning.
	- $\phi$ in the following example: 

---
## Demonstrating feature map $\phi$:  (R1)

- Consider a fitting linear function: $y = \theta_3 x^3 + \theta_2 x^2 + \theta_1 x + \theta_0$
- Concretely, we represent this feature map with $\phi: R \rightarrow R^4$ as: $\theta_3 x^3 + \theta_2 x^2 + \theta_1 x + \theta_0 = \theta^T\phi(x)$ 
- $\phi(x) \in R^4$ be the vector containing $\theta_0$, $\theta_1$, $\theta_2$, $\theta_3$ as entries.

---
## Terminologies in "feature map" / "[[kernel method]]" context:  (R1)

- Attributes x: 
	- To distinguish between these two sets of variables, in the context of [[kernel method]], we will call the "original" input value the input "attribute" of a problem ( in this case, x).
- Features $\phi(x)$: 
	- When the original input is mapped to some new set of quantities $\phi(x)$, we will call those new quantities the "feature" variables. 
- Feature map $\phi$: 
	- We will call $\phi$ a feature map, which maps the attributes to the features.


---
## Reference

- [[(Course) CS229 Machine learning]]