---
alias: [local context window]
---

- 31-8-2022: created

- Superset:
	- [[Word representation]]

- Shallow window aid in making predictions within local context windows. 
	- For example, 
		- Bengio et al. (2003) introduced a model that learns word vector representations as part of a simple neural network architecture for language modeling.(R1)
		- Collobert and Weston (2008) decoupled the word vector training from the downstream training objectives, which paved the way for Collobert et al. (2011) to use the full context of a word for learning the word representations, rather than just the preceding context as is the case with language models
- Window-based method suffer from the disadvantage that they do not operate directly on the [[co-occurrence]] statistics of the corpus. Instead, these models scan context windows across the entire corpus, which fails to take advantages of the vast amount of repetition in the data.

- Examples
	- [[Skip-gram]], continuous bag of words (CBOW)
- characteristics
	- Generate improved [[performance]] on other tasks
	- Cap capcture complex patterns beyond word similarity
	- Sacles with corpus size
	- Inefficient usage of statistics


---
## Reference

- 1. [[(Paper) Pennington, J., Socher, R., & Manning, C. (2014). GloVe Global Vectors for Word Representation]]

