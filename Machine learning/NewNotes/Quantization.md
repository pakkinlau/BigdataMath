---
category: []
alias: []
tags: []
---

- 27-10-2022 01:55: created

- What is Quantization?
	- While [[pruning]] [[Compress]] [[model]] by reducing the number of weights, quantization consists of decreasing the size of the weights that are there.
	- Quantization in general is the process of mapping values from a large set to values in a smaller set, meaning that the output consists of a smaller range of possible values than the input, ideally without losing too much information in the process. 

- Color quantization
	- [[gray level|gray scale]] is an example of it.
	- To turn a 24-bit image into an 8-bit image, the image must go through a process called color quantization. 
		- The simplest form of quantization is to simply assign 3 bits to red, 3 bits to green and 2 bits to blue, as the human eye is less sensitive to blue light. This creates a so called 3-3-2 8-bit color image

![[Pasted image 20221027015659.png]]
- Fig: 8-bit image versus 1-bit image. "We aren't able to detect much difference between the first four images."(R1)

![[Pasted image 20221027021205.png]]
- Fig: mechanism of quantizing. Approx. to nearest number. (R1)


---
## Reference

1. Hannah Peterson's medium blog: https://medium.com/gsi-technology/an-overview-of-model-compression-techniques-for-deep-learning-in-space-3fd8d4ce84e5