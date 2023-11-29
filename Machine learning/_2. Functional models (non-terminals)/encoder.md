---
category: []
alias: [encode]
tags: []
---

- 12-10-2022: created

- superset:
	- [[Encoder decoder model]]

- What is encoder?
	- 1. Changing the format.
		- Encoding means to convert data into a required format. 
	- 2. Composed of RNN
		- Encoder is a unit in neural network that performs encoding. This structure allows the model to understand context and temporal dependencies of the sequence.
	- 3. [[Compress]] data into low dimensional vectors
		- 

- Formalism of encoder: ^3874f7
	- $\text{ENC:}V \ \rightarrow R^d$, that maps nodes to vector embedding $z_i \in R^d$ (where $z_i$ corresponds to the embeddinf for node $v_i \in V$)

- dual-encoder model (R1)
	- demonstrated as an effective approach for learning bilingual sentence embeddings (Guo et al., 2018; Yang et al., 2019a). 
- [[Encoder decoder model]]
	- Tasks
		- eg: a game Pictionary (in which players look at a word, draw it on a paper, then pass to another player to guess.)
			- a sequence of words in Spanish into a 2D vector, this 2D vector is also known as hidden state.

![[Pasted image 20221031001756.png]]
- Fig: Eigenface (R2)
	- represent any new faces in terms of sums of these computed eigenfaces, instead of the intensity values of each pixel in the image, we can represent a face using 7 or 8 numbers, instead of hundreds. ([[Dimensionality reduction]])
---
## Reference
1. [[(Paper) Feng, F., Yang, Y., Cer, D., Arivazhagan, N., Wang, W., & Ai, G. (2020). Language-agnostic BERT Sentence Embedding.]]
2. [[computational neuroscience]]: coursera week 2