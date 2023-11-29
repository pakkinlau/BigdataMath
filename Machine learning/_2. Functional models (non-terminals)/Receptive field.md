- 26-9-2022: created

- Applied: GNNs and CNNs 

- Receptive field: 
	- It is the set of nodes that determine the embedding of a node of interest. It is how many hops away from the center of interest. 

- CNN properties (from Luo's paper):
	- 1. Anywhere outside the receptive field of a unit does not affect the value of that unit. 
	- 2. Not all pixels in a receptive field contribute equally to an output unit's response.
	- 3. Pixels at the center of a receptive field have a much larger impact on an output. (central pixel can propagate information to the output through many different paths, while the pixels in the outer area have very few paths to propagate its impact.)
	- 4. Distribution of impact within a receptive field on the output, in many case, distributes as a Gaussian. 
	- 5. Effective receptive field, only occupies a fraction of the theoretical receptive field, since Gaussian distribution generally decay quickly from the center.

- GNN Properties:
	- 1. Shared neighbors: The shared neighbors quickly grows when we increase the number of hops (number of GNN layers)

![[Pasted image 20220926063836.png]]
- Figure: Receptive field, Week 7, page 61 of [[(Course) CS224W - Machine learning with graphs (stanford)]]


---

## Reference

- [[(Paper) Luo, W., Li, Y., Urtasun, R., & Zemel, R. (2016). Understanding the Effective Receptive Field in Deep Convolutional Neural Networks]]