- 26-9-2022: created

- This algorithm is for [[Unsupervised learning]]. 
- It is an iterative method to find (local) maximum likelihood or maximum posteriori estimates of parameters in statistical models., where the model depends on unobserved [[latent]] variables.

![[Pasted image 20220926231710.png]]![[Pasted image 20220926231649.png]]


---
- we have a set of training data $\{x^{(1)},\dots, x^{(n)} \}$. Since  we are in the unsupervised learning setting, these points do not come with any labels.
- goal: model the data by specifying a joint distribution $p(x^{(i)},z^{(i)}) = p(x^{(i)}|z^{(i)})p(z^{(i)})$.
	- $z^{(i)} \sim Multinomial(\phi)$ -- which is a generalization of binomial distribution. 
	- $x^{(i)}|z^{(i)} =j \sim N(\mu_j,\Sigma_j)$.
- $z^{(i)}$ are called [[latent]] random variables
- TO estimate the model, we write down the likelihood of our data: $$(\phi,\mu,\Sigma)=\sum_{i=1}^n logp(x^{(i)};\phi,\mu,\Sigma)=\sum_{i=1}^n log\sum_{z^{(i)}=1}^k p(x^{(i)}|z^{(i)};\mu,\Sigma)p(z^{(i)};\phi)$$

..... And More (view cs229 book)


---
## Reference
- [[(Course) CS229 Machine learning]]
- wikipedia
