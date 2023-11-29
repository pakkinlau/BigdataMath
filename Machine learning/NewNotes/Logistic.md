---
category:[]
alias:[logistic regression]
tags:[]
---

- 23-10-2022 13:45: created

- superset:
	- [[regression]]

- In [[classification]] problems, if we want to predict take on only a small number of discrete values, eg, binary classification in which $y$ can take on only two values, $0$ and $1$. (R1)

- Formulation: $$h_\theta(x) = g(\theta^Tx)={1 \over {1+e^{-(\theta ^Tx)}}}$$, where $g(z) = {1 \over {1+e^{-z}}}$ is called logistic function or the sigmoid function.

---
## Sigmoid function / logistic function


![[Pasted image 20221023135332.png]]
- Derivative of $g(z)$ is $g(z)(1-g(z))$. (R1)
	- So how do we fit $\theta$ for it?
- Assumption
	- Based on P(all events) = 1, and only 2 possible events, we have a pair of probabilities: 
		- $P(y=1|x;\theta) = h_\theta(x)$ (chosen)
		- $P(y=0|x;\theta) = 1-h_\theta(x)$ (from $P(y=0|x;\theta) + P(y=1|x;\theta) = 1$)
	- Or more compactly, $$p(y|x;\theta)=(h_\theta(x)^y(1-h_\theta(x))^{1-y}$$

---
## Training

- Assuming $n$ training examples were generated independently, we can write down the likelihood of the parameters as:
$$L(\theta)=p(\vec{y}|X;\theta)=\prod_{i=1}^n p(y^{(i)}|x^{(i)};\theta) = \prod_{i=1}^n (h_\theta(x)^{y^{(i)}}(1-h_\theta(x))^{1-{y^{(i)}}}$$
- Log likelihood would be: $$l(\theta) = logL(\theta) = \sum_{i=1}^n {y^{(i)}}log(h_\theta(x)) + {(1-y^{(i)})}log(1-h_\theta(x))$$
- Derivatives to derive the [[Stochastic gradient descent]]: $${\partial l(\theta) \over \partial \theta_j} = (y-h_\theta(x))x_j$$

---
## Reference

1. [[(Course) CS229 Machine learning]]