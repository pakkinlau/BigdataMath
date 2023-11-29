---
alias: [self-supervision, self-supervised]
---


- 26-9-2022: created

- This leads to a paradigm shoft with the rise of models such as:
	- [[BERT]] GPT-3.
- These models are called "foundational models" by Bommasani et al.

- For NLP, [[Foundational model]], and Graph neural networks, they are all looking for a self-supervised model. 

- As long as a ML model is just learning [[co-occurrence]] of the sequences it is exposed to, then it coutns as a foundation model by definition (Ref1)


- Relations to [[Unsupervised learning]]
- Self-supervised learning is a machine learning approach where the model trains itself by leveraging one part of the data to predict the other part and generate labels accurately. 
- Instead of finding high-level patterns for [[clustering]], self-supervised learning attempts to still solve tasks that are traditionally targeted by [[supervised learning]] (e.g., image classification) without any labelings available.(Medium)

---

- Pretraining and adaptation:
	- 2 phases: 
		- 1. Pretraining (or simply training) 
			- Pretrain a large model on a massive unlabeled dataset (eg: billions of unlabeled images)
			- Average of each self-supervised loss on a single datapoint: 
				- $\{x^{(1)}, x^{(2)}, \dots, x^{(n)} \}$  that consists of $n$ examples in $R^d$.
				- Let $\phi_\theta$ be the "embedding or features" of the sample X of the model, that maps the input X to some m-dimensional represnetation $\phi_\theta(x), \phi_\theta(x) \in R^m$.
				- $L_{pre}(\theta)={1 \over n}\sum_{i=1}^n l_{pre}(\theta,x^{(i)})$,  $l_{pre}$ comes from the data point $x^{(i)}$ itlsef. 
		- 2. Adaptation
			- Adapt the pretrained model to a downstream task (eg: detecting cancer from scan images. These downstream tasks are aften prediction tasks with limited or even no labeled data.)
			- usually have a labeled dataset $\{  (x_{task}^{(1)}, y_{task}^{(1)}) , \dots, (x_{task}^{(n_{task})}, y_{task}^{(n_{task})})  \}$ with $n_{task}$ examples.
			- The adaptation model uses pretrained parameter $\hat \theta$, (hat denotes it is a prediction from the model), adapt to downstream task, that outputs a variant of $\hat \theta$ that solves the downstream task. 
			- Prediction on adaptation model:  $w^T \phi_{\hat \theta}(x_{task}^{(i)})$, where $w \in R^m$  is the difference between pretrain case and adaptation case, which is a parameter to be learned, and $\hat \theta$ is exactlly the pretrained model provides. 
			- 2 approaches: 
				- 1. Linear probe approach:
					- Using SGD to train $w$ (on the downstream task loss to predict the task label), to obtain a value of $w$ minimizing the prediction error: 
					- $\underset{w \in R^m}{min} {1 \over {n_{task}}} \sum_{i=1}^{n_{task}} l_{task} (y_{task}^{(i)}, w^T \phi_{\hat \theta} (x_{task}^{(i)}))$.
				- 2. Finetuning algorithm
					- It further finetunes the pretrained model $\hat \theta$.
					- $\underset{w, \theta}{min} {1 \over {n_{task}}} \sum_{i=1}^{n_{task}} l_{task} (y_{task}^{(i)}, w^T \phi_{ \theta} (x_{task}^{(i)}))$, 
						- with init: 
							- $w \leftarrow$ random vector, 
							- $\theta \leftarrow \hat \theta$.
			- If it is a regession problem 
		- Three kinds of adaptation learning 
			- When $n_{task}=0$, it is called "zero-shot learning" - the downstream task doesn't have any labeled examples.
			- When $n_{task} < 50$, the setting is called "few-shot learning".
			- It is very common to have a larger $n_{task}$ on th eorder of ranging from 100+ to 100k+.
	- The intuition is, the pretrained models learn "good represenations" that capture intrinsic semantic structure / information about the data; the adaptation phase customizes the model to a particular downstream task (eg: retrieving the information specific to it.)




---
## Reference
- [[(Paper) On the Opportunities and Risks of Foundation Models (Bommasani et. al, 2021)]]