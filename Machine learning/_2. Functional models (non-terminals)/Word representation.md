---
alias: [word embedding, word vector, semantic vector space]
---

- 25-9-2022: created

- superset:
	- [[representation]]
	- [[vector]]

- subset:
	- [[GloVe]]
	- [[Global matrix factorization methods]]
		- [[latent semantic analysis (LSA)]]
	- [[Local context window methods]]
		- [[Skip-gram]]

- In [[natural language processing|NLP]], words are mapped to some representation that could be computed. Words cannot be directly analyzed by the computer. (my writing)

- Attributes
	- 1. [[Use of statistical information]]
		- [[Global matrix factorization methods]] perform well on this, but perform poorly on word [[analogy]] tasks (R1)
	- 2. [[analogy]] tasks
		- [[Local context window methods]] perform better on [[analogy]] tasks, but poorly utilize the statistics of the corpus, since they train on separate local context windows, instead of on global co-occurrence counts. 

- Characteristics 
	- 1. Those representations should be fully converted the document from one format, to another format. And also remain exchangeability between different word representations. (My writing)
	- 2.  To make it easier to process, [[graph]] is a reasonable format. But there will be possibly [[Loss of information]]. And [[Loss of information]] makes those models perform relatively poorly on word analogy task, indicating a sub-optimal vector space structure. (R1)
	- 3. A good word representation should be able to perform [[analogy]] tasks
	- 4. More and more word representation models are decoupled from the [[downstream tasks|downstream task]]

- Types of weight in NLP tasks:
	- Weight of Word Embedding
	- Weight of Attention
	- Positional Encoding Weights
	- Feedforward Neural Network Weights
	- Layer Normalization Weights
	- Classifier Weights
	- Masking Weights

---
## The following description is missing reference

- Distributional semantics: "a word's meaning is given by the words that frequently appear close by"
- We build a dense vector for each word, so that we can compare similarity of each word that appears in similar contexts. eg: the word "banking" represents by 1 x 8 matrix. 


---
## Reference

1. [[(Paper) Pennington, J., Socher, R., & Manning, C. (2014). GloVe Global Vectors for Word Representation]]

- 12-10-2022: created

- [[cross-lingual]] sentence embedding (R1)
	- Useful for [[clustering]], [[retrieval]], modular use of textual [[representation|representation]]. (R1)
	- Most [[Embedding]] models corporate large [[Transformer]] models, using large pretrained [[language]] models is not well explored. 


---
## Reference
1. [[(Paper) Feng, F., Yang, Y., Cer, D., Arivazhagan, N., Wang, W., & Ai, G. (2020). Language-agnostic BERT Sentence Embedding.]]