---
category: []
alias: []
tags: []
---

- 27-10-2022 01:33: created

- What is Pruning?
	- Pruning involves removing connections between neurons or entire neurons, channels, or filters from a trained network, which is done by zeroing out values in its weights matrix or removing groups of weights entirely (R1)
		- for example, to prune a single connection from a network, one weight is set to zero in a weights matrix, and to prune a neuron, all values of a column in a matrix are set to zero. 
	- Motivation
		- The motivation behind pruning is that networks tend to be over-parametrized, with multiple features encoding nearly the same information.
	- unstructured pruning involves removing individual weights or neurons, while structured pruning involves removing entire channels or filters.

- Tradeoff:
	- Between network performance and size.
	- Parametrize a drop bound which define a maximum allowed drop in performance between the original and pruned model.

- Effect
	- By replacing connections or neurons with zeros in a weights matrix
	- unstructured pruning
		- It increases the [[Sparse|sparsity]] of the network, i.e. its proportion of zero to non-zero weights.
		- No decrease in classification accuracy.
	- structured pruning
		- It does not result in weight matrices with problematic sparse connectivity.
		- It involves removing the entire blocks of weights within given weight matrices. 

![[Pasted image 20221027015048.png]]
- Fig: Unstructured pruning (R1)

![[Pasted image 20221027015207.png]]
- Fig: three types of structured pruning

![[Pasted image 20221027015448.png]]
- Fig: Pruning saved size versus accuracy drop.

- Pruning criteria
	- 1. Han et al. 2015 --  
		- First, a predetermined “quality parameter” is multiplied by the standard deviation of a layer’s weights to calculate the threshold value and weights with magnitudes below the threshold are zeroed.
		- After all layers are pruned, the model is retrained so that the remaining weights can adjust to compensate for those that were removed, and the process is repeated for several iterations.
		- Researcher prune four different model architecture with MNIST dataset


---
## Reference

1. Hannah Peterson's medium blog: https://medium.com/gsi-technology/an-overview-of-model-compression-techniques-for-deep-learning-in-space-3fd8d4ce84e5