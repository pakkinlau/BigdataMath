- 26-9-2022: created

- Related: [[Receptive field]]

---
### General information
- Characteristics of receptive fields of units in deep CNNs.
	- 1. Anywhere outside the receptive field of a unit does not affect the value of that unit. 
	- 2. Not all pixels in a receptive field contribute equally to an output unit's response.
	- 3. Pixels at the center of a receptive field have a much larger impact on an output. (central pixel can propagate information to the output through many different paths, while the pixels in the outer area have very few paths to propagate its impact.)
	- 4. Distribution of impact within a receptive field on the output -- In many case, it distributes as a Gaussian. 
	- 5. Effective receptive field, only occupies a fraction of the theoretical receptive field, since Gaussian distribution generally decay quickly from the center.
- The receptive field size is a crucial issue in many visual tasks (eg: semantic image segmentation, stereo and optical flow estimation) , as the output must respond to large enough areas in the image to capture inforation about large objects.
- Way to increase receptive field size
	- 1. Stack more layers to make the network deeper, which increases the receptive field size linearly by theory, as each extra layer increases the receptive field size by teh kernel size.
	- 2. Sub-sampling: Increases the receptive field size multiplicatively.
		- VGG and residual network use these techniques.
- Introduce the notion of an effective receptive field in several architecture designs
- Introduce the effect of nonlinear activations, dropout, sub-sampling and skip connection
- Suggestions for ways to address its tendency to be too small
---
## Detail information

- 1. Mathematically characterize how much each pixel in a receptive field can impact the output of a unit $n$ layer up the network
	- pixel: $(i,j)$, with their center at $(0,0)$. 
		- $x_{i,j}^p$ denote the $(i,j)$th pixel on the $p$th layer. 
		- $y_{i,j}=x_{i,j}^n$ as the output on the $n$th layer.
	- Impact: ${\partial y_{0,0}} / {\partial x_{i,j}^0}$
		- From back-propagation: 
			- By chain rule, $${\partial l \over \partial x_{i,j}^0}= {\sum_{i',j'} {\partial l \over \partial_{y_{i',j'}}}}{\partial_{y_{i',j'}} \over \partial x_{i,j}^0}$$
			- Init:
				- Set $\partial l / \partial y_{0,0} = 1$ and $\partial l / \partial y_{i,j}=0, \forall i \neq  0 \lor j \neq 0$.
				- Propagate theis gradient from there back down the network.
		- factors
			- 1. Weights of the network
			- 2. Input-dependent


![[Luo, W., Li, Y., Urtasun, R., & Zemel, R. (2016). Understanding the Effective Receptive Field in Deep Convolutional Neural Networks.pdf]]