
- Related:
	- [[Generic Regression]]
	- [[linear regression]]

---

- 5-10-2022: created


- To perform [[supervised learning]], we must decide how we are going to represent functions / hypotheses h in a computer. 

---
## Step 1: setting up the linear function (R1)


- approximate $y$ as a linear function of $x$:
$$h_\theta(x)=\theta_0 + \theta_1x_1+\theta_2x_2$$, which the $\theta_i$ are the parameters / weights parameterizing the space of linear function mapping from $\mathcal{X}$ to $\mathcal{Y}$. which $x \in \mathcal{X}$ and $h_\theta(x) \in \mathcal{Y}$.

- To simplify our notation, we have $$h(x) = \sum_{i=0}^d \theta_i x_i = \theta^Tx$$, which we view both $\theta$ and $x$ as [[vector]]. 

---
## Step 2: Fitting the curve (R1)

- Minimize [[Loss function|cost]] function: $$J(\theta) = {1 \over 2}\sum_{i=1}^n(h_\theta(x^{(i)})-y^{(i)})^2$$
- A list of possible algorithms to do that, such as:
	- [[Least mean squares (LMS) algorithm]]





---
## Reference
1. [[(Course) CS229 Machine learning]]