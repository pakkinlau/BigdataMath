---
category: []
alias: []
tags: []
---

- 27-10-2022 02:27: created

- What is Low-rank approximation?
	- We’re aware that deep neural networks tend to be over-parametrized, with a lot of similarity—or redundancy—occurring between different layers and/or channels. 
		- For example, image a above shows filters of a convolutional layer learned for an image segmentation task, many of which look nearly the same. (R1)
	- Intuitively, we get the sense that if an element of a matrix can be computed using others that are present, there is some redundancy of information occurring in the matrix. 
	- Effect
		- Compressing layers in this way reduces the network’s memory footprint as well as the computational complexity of convolutional operations and can yield significant speedups.

![[Pasted image 20221027023217.png]]
- Fig: example 1 -- the third column can be calculated by first two columns, thus there are some redundancy in between data.

![[Pasted image 20221027023308.png]]
![[Pasted image 20221027023317.png]]
![[Pasted image 20221027023312.png]]
- Fig 2: Example of low-rank approximation
	- The goal is to reduce the computational complexity with a linear combination of lower rank M filters where M<N, based on the assumption that there is redundancy between the N filters. 
	- say, we could found the data column can be "factorized" or "decomposed", that is, determined by the value of another column. 
	- By imposing separability of the M basis filters and adding a layer to approximate the N output channels of the original convolution operation from the compressed basis.
	- This look more complex, it is actually a more computationally efficient operation if M is made to be sufficiently small.
	- They achieve 4.5x speedup of a [[shallow]] network

---
## Reference

1. Hannah Peterson's medium blog: https://medium.com/gsi-technology/an-overview-of-model-compression-techniques-for-deep-learning-in-space-3fd8d4ce84e5