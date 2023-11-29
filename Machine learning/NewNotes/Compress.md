---
category: []
alias: [compression, compressing, data compression]
tags: []
---

- 27-10-2022 00:56: created

- Related:
	- [[Loss of information]]

- What is Compress?
	- By compressing the input data, we hopes for getting useful embedding, reducing the number of the parameter by representing the model more effectively. 
	- In [[information theory]],
		- data compression, source coding, or bit-rate reduction is the process of encoding information using fewer bits than the original representation. Any particular compression is either lossy or lossless. 
			- [[Lossless]] compression reduces bits by identifying and eliminating statistical redundancy. No [[Loss of information]] in lossless compression. 
	- Logically, compression is a [[encoder|encode]] process which inherits the characteristics of [[Inductive]] inference. 
	- We can see this notion appears in many place in [[machine learning]]. 
		- eg: [[Encoder decoder model]], encoders compress input feature to be low [[dimensionality|dimensional]] vector, and then decoder use those low dimensional vectors to predict a higher dimension output value.
		- eg: [[neural network]], a layer of NN consumes N values input to produce 1 value output.
		- eg: [[autoencoder]]: "Add a bottleneck in the network, where there the network is narrower at the middle that it is on the inputs and the outputs. --> It is forced to [[compress]] the data down into meaningful [[representation]] "
		- eg: [[principal component analysis]]:
	- [[encoder]]: ![[encoder#^3874f7]]
	- [[decoder]]: ![[Decoder#^58bb6d]]
	- Heavily researched methods for achieving compressed models: (R1)
		- [[Pruning]]
		- Quantization
		- Low-rank approximation and sparsity
		- Knowledge distillation
		- Neural architecture search (NAS)
	- These low-dimensional embeddings can be viewed as [[encoder|encode]]ing , projecting, nodes into a [[latent]] space, where geometric relation in this latent space correspond to interaction in the original graph.

- Problems that compress can fix:
	- By replacing connections or neurons with zeros in a weights matrix, unstructured pruning increases the [[Sparse|sparsity]] of the network, i.e. its proportion of zero to non-zero weights.
	- Pruned networks can take up much less memory than their dense counterparts. 
		- [[Pruning]]
		- [[Quantization]]
		- [[Low-rank approximation]]

- The design of data compression schemes involves trade-offs among:
	- The degree of compression
	- The amount of distortion introduced
	- The computational resources required to compress and decompress the data. 

- How far we can compress?
	- As far as the further compression would not cause more [[Loss of information]]. (my writing)
	- 

---
## Reference

1. Hannah Peterson's medium blog: https://medium.com/gsi-technology/an-overview-of-model-compression-techniques-for-deep-learning-in-space-3fd8d4ce84e5