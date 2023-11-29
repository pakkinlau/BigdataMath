---
category: []
alias: []
tags :[]
---

- 25-10-2022 15:55: created

- What is Encoder decoder model?
	- 1. [[Compress]]ing information
		- The steps involves a higher-[[dimensionality|dimensional]] input [[feature]], the [[encoder]] maps the feature into a lower-[[dimensionality|dimensional]] embeddings, and then [[Decoder]] extracts user-specified information from the higher-dimensional embeddings.
	- Jointly [[optimization|optimizing]] the encoder and decoder, the system learns to compress information about graph structure into low-dimensional embedding space. 
	- Components:
		- [[encoder]]
		- Hidden state
		- [[Decoder]]

![[Pasted image 20221025155606.png]]
- Fig: Encoder decoder for translation problems (R1)


![[Pasted image 20221027005021.png]]
- Fig: Encoder decoder for graph representation learning
	- encoder: 
		- node's position, its local neighborhood structure, and/or its attributes.
	- decoder: 
		- its local graph neighborhood from embedding (eg: the identity of its neighbor)
		- a classification associated with it (eg: a community label)

---
## Reference

1. Nechu BM's medium blog: https://towardsdatascience.com/what-is-an-encoder-decoder-model-86b3d57c5e1a#:~:text=To%20decode%20means%20to%20convert,output%20sequence%2C%20the%20English%20sentence.