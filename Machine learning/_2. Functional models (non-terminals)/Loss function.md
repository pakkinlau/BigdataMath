---
alias: [cost function, cost, loss, loss function]
---

- 25-9-2022: created

- Related:
	- [[objective|objective function]]

- What is loss function?
	- 

- List of cost functions:
	- In general, if we don't specify which loss function we use, we express loss function as: $J(\theta)= {1\over n} {\sum_{i=1}^n} {L(y^{(i)},h_\theta(x^{(i)}))}$, which loss function is on the right side, and [[Cross entropy]] is on the left side. 
	- Mean squared Error (MSE) 
		- If the downstream task is a regression problem , we will use: ${\sum_{i=1}^n}L(y^{(i)},h_\theta(x^{(i)})) = {\sum_{i=1}^n(y^{(i)}-h_\theta(x^{(i)}))^2}$
		- $J(\theta)= {1\over n} {\sum_{i=1}^n(y^{(i)}-h_\theta(x^{(i)}))^2}$
		- difference between ground truth and the model's prediction, square it, and average it out across the whole dataset. 
	- Mean absolute error (MAE)
		- $MAE= {1\over n} {\sum_{i=1}^n|y^{(i)}-h_\theta(x^{(i)})|}$
	- Self-supervision: 
		- 1. Pretrain: Average of self-supervised loss on a single datapoint $x^{(i)}$:
			- $L_{pre}(\theta)={1 \over n}\sum_{i=1}^n l_{pre}(\theta,x^{(i)})$, and inout embeddings $\phi_\theta(x), \phi_\theta(x) \in R^m$.
			- $l_{pre}$ comes from the data point $x^{(i)}$ itlsef. 
		- 2. Adaptation: Using SGD to train $w$ (on the downstream task loss to predict the task label)
			- Linear probe approach:
				- $\underset{w \in R^m}{min} {1 \over {n_{task}}} \sum_{i=1}^{n_{task}} l_{task} (y_{task}^{(i)}, w^T \phi_{\hat \theta} (x_{task}^{(i)}))$
			- Finetuning algorithm
				- $\underset{w, \theta}{min} {1 \over {n_{task}}} \sum_{i=1}^{n_{task}} l_{task} (y_{task}^{(i)}, w^T \phi_{ \theta} (x_{task}^{(i)}))$
	- Huber loss
		- ![[Pasted image 20220927100914.png]]


---

- Discuss the test error versus train error: [[Generalization]]

---
- Problems
1. [[Overfitting]]: It predicts accurately in training dataset, but failed terribly in the test dataset. 


- Application: 
	- In [[Discriminative learning algorithms]]: 
		- [[supervised learning]] and [[Unsupervised learning]]

- Problem: 
	- [[Loss of information]]
	- [[Overfitting]]

- Related: [[Generalization]]

---
- Related: [[Cross entropy]]
- Logistic loss function: $L(f(w,b),yi) = -log(f(w,b))$, if $yi = 1$, $L(f(w,b),yi) = -log(1-f(w,b))$ if $yi = 0$.
---

- Loss function in [[Natural language translation]] problem: 
	-  $Loss =||XR-Y||_F$, SGD: $g = {d \over dR}Loss$, Update: $R_{new} =R_{old}- \alpha g$



