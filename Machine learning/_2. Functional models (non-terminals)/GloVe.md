- 30-8-2022: created

- What is Glove?
	- GloVe word embeddings are vector [[representation]] of words. These word embeddings will be used to create vectors for our sentences. (R2)




- Is it pre-trained?
- What is the feature of these vector?


- 


---


---
## The following terms don't have any reference pointers. 

- GloVe vector
	- Count based vs direct prediction
	- Connecting A: linear algebraic methods (eg: PCA, COALS) with B: neural updating methods (eg: skipgrams, CBOW). 
		- A: Fast training. Efficient usage of statistics. Primarily used to capture word similarity. It is disproportionate importance given to large couuts.
		- B: Scales with corpus size. Inefficient usage of statistics. Generate improved performnace on other tasks. Can capture complex patterns beyond word similarity.
	- Insights: Ratios of co-occurrence probabilities can encode meaning components.
		  eg: $P(x|ice)$, $x = solid$, --> Get a larger number. than P(x|ice) x = gas. The ratio of these two probability will be obviously bigger than 1. if x is not relevant to these two things. The P will approach 1.
	- $X_{ij}$: the number of times i appears in context j.
	- Some words appears very often, like "this", "is", "of", "a",...... we often call them stop words. 
	- Some words like "Durion", we still want to take into account. 
	- Cost:
		- $\sum_{i=1}^{10000}\sum_{j=1}^{10000}f(X_{ij})(\theta_i^Te_j+b_i-b_j'-logX_{ij})^2$
			- $\theta_t^T$:feature weights
			- $X_{ij}$: co-occurence matrix
			- $f(X_{ij})$: extra weighting term. It is 0 if $X_{ij}=0$. Also, $0 \times log0=0$.


---
## Reference

1. [[(Paper) Pennington, J., Socher, R., & Manning, C. (2014). GloVe Global Vectors for Word Representation]]
2. Vidhya's text summarization blog: https://www.analyticsvidhya.com/blog/2018/11/introduction-text-summarization-textrank-python/