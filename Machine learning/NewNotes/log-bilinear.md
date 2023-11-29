---
alias: [LBL]
---

- 22-10-2022: created

- subset: (R2)
	- vLBL
	- ivLBL

- Log-bilinear (LBL) model is perhaps the simplest neural language model. (R1)
- Given the previous context word $\{ w_1, \dots, w_{n-1}\}$, the LBL first predict the representation for the next word $w_n$  by linear combining the context word: $$\tilde{r} = \sum_{i=1}^{n-1}C_ir_{w_i}$$ (R1), where $r_w$ is the real-valued vector representing word $w$. (R1)
	- Q: How to determine $C_i$?

- Then the distribution for the next word is computed based on the similarity between the predicted distribution and the representations of all words in the vocabulary:  (R1)
- Recall [[softmax]]: $$\sigma(z) = {e^{z_i} \over \sum_{j=1}^K e^{z_j}}$$
- In the setting of log-bilinear model, we have $$P(w_n=w|w_{1:n-1})={exp(\tilde{r}^\top r_w) \over {\sum_j exp(\tilde{r}^\top r_j)}}$$, which 
	- The linear regression function is $\tilde{r}^T r_w$, which $\tilde{r}^T$ combined the word embedding of the first $j$ pervious "context" words, and the embedding of the last word $r_w$.
	- The activation function is [[softmax]].
	- , where we can see the [[activation]] function is [[softmax]].
- Why it is called [[bilinear]]? (R1)
	- $\tilde{r}$ is the combination of the previous word embeddings
	- $r_w$ is the [[Embedding]] of word $w$.
	- The multiplication of them $\tilde{r}^\top r_w$ is called bilinear map. As such, there only exists one embedding look-up table. 
- [[Logistic]]
- [[softmax]]



---
## Reference

1. Nan Jiang's blog: https://jiangnanhugo.github.io/blog/log-bilinear-model
2. [[(Paper) Pennington, J., Socher, R., & Manning, C. (2014). GloVe Global Vectors for Word Representation]]