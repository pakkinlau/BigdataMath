---
category:[]
alias:[softmax regression]
tags:[]
---

- 23-10-2022 14:34: created

- Softmax regression
	- While [[Logistic]] produces label in binary: $y^{(i)} \in\{0,1\}$, Softmax regression is useful when we are interested in multi-class classification, so label $y$ can take on $K$ different values i.e. $y^{(i)} \in \{1,2,...,K\}$, where $K$ is the number of classes. (R1)
	- Settings: 
		- [[activation]] function: $t = exp(Z^{[t]})$
	- Recall, in [[Logistic]], we have: $$a_1 = g(z) = {1 \over {1+e^{-z}}}$$, $$a_2 = 1 - a_1$$
---
- Softmax function
	- That is a totally different [[activation]] than [[Logistic]], converts a vector of K real numbers into a probability distribution of K possible outcomes. 
	- It is a [[Generalization]] of the logistic function to multiple dimensions, and used in multinomial logistic regression. 
	- for each single outcome, we use a different [[activation]] function $\sigma: R^K \rightarrow (0,1)^K$  is defined when $K \geq 1$
	- $$\sigma(z) = {e^{z_i} \over \sum_{j=1}^K e^{z_j}}$$ for $i=1, \dots, K$ and $z=(z_1, \dots, z_K) \in R^K$.
	- such that $$p(y^{(i)}=k|x^{(i)}=\theta)={exp(\theta^{(k)T}x^{(i)}) \over {\sum_{j=1}^K}(exp(\theta^{(j)T})x^{(i)}}$$
	- 


	- Therefore, for softmax we have $$\hat y=\begin{pmatrix} p(y=1|x;\theta) \\ p(y=1|x;\theta) \\ \vdots \\ p(y=k|x;\theta) \end{pmatrix}={1 \over {\sum_{j=1}^K}exp(\theta^{(j)T}x)}\begin{pmatrix}exp(\theta^{(1)T}x \\ exp(\theta^{(2)T}x \\ \vdots \\ exp(\theta^{(K)T}x\end{pmatrix}$$

---
## [[Training]] softmax

- Full softmax
	- Brute force, calculates for all classes
- Candidate sampling
	- Calculates for all the possible [[label]]s, but only for a random sample of negatives. 
---
## Reference

1. [[(Course) Coursea machine learning specialization Course 1 Neural networks and deep learning, and and course 2 Improving Deep Neural Networks Hyperparameter Tuning, Regularization and Optimization]]
2. Deep learning, Stanford blog: http://deeplearning.stanford.edu/tutorial/supervised/SoftmaxRegression/
3. [[(Course) google developers - machine learning courses]]