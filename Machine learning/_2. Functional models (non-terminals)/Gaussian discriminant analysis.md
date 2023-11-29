- 26-9-2022: created

---
## Result:

![[Pasted image 20220926142329.png]]
- Figure: Shown in the figure are the training set, as well as the contours of the two Gaussian distributions that have been fit to the data in each of teh two classes. 

---

- Suppose $x \in R^n$, drop the $x_0 = 1$.
- Assume $p(x|y)$ is distributed gaussian. (eg: size of tumor is distributed gaussian.)
	- [[Multivariate Gaussian]]
- The model is:
	- y ~ Bernoulli($\phi$). Related: [[Bernoulli distribution]]
	- $x|y=0 \sim N(\mu_0,\sigma)$
	- $x|y=1 \sim N(\mu_1,\sigma)$

- Write out the distribution, we have:
![[Pasted image 20220926132952.png]]

- So the parameter of our model are $\phi$ , $\sigma$, $\mu_0$ and $\mu_1$.
- The log-likelihood of the data is given by: $$l(\phi, \mu_0, \mu_1, \sigma) = log \prod_{i=1}^n p(x^{(i)},y^{(i)};\phi,\mu_0,\mu_1,\sigma) = log \prod_{i=1}^n p(x^{(i)}|y^{(i)};\phi,\mu_0,\mu_1,\sigma)p(y^{(i)};\phi)$$
- By maximizing $l$ with respect to the parameters, we find that: 
![[Pasted image 20220926142314.png]]