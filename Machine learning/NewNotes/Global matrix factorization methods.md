- 21-10-2022: created

- superset:
	- [[Matrix factorization]]

- These methods works poorly on [[analogy]].
- Related: [[Global]]
- Related: [[Matrix factorization]]


---
## What is [[Matrix factorization]]?

![[Matrix factorization]]

---
- How global matrix factorization differs [[Matrix factorization]]?
	- It highlights it is computing in [[Global]] setting. 





- Possible matrices variations: 
	- In [[latent semantic analysis (LSA)|LSA]], the matrices are of "term-document" type, the rows corresponds to words or terms, the columns correspond to different documents in the corpus.
	- In HAL (Hyperspace analogue to language, 1996), uses "Term-term" type
- The pipeline is using [[latent]] scores to model those low-rank features. 
- Problems:
	- These model is thee most frequent words contribute a disproportionate amount to the similarity measure
		- eg: `and` , `the` will have a large effect of their [[similarity]] despite conveying relatively little about their semantic relatedness.




---
## Reference 

1. [[(Paper) Pennington, J., Socher, R., & Manning, C. (2014). GloVe Global Vectors for Word Representation]]