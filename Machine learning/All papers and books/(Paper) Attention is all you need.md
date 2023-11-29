- 18-4-2023: created

- Transformer is the first sequence transduction model based entirely on attention, replacing the recurrent layers mostly commonly used in encoder-decoder architectures with multi-headed self-attention. 
- Can be applied to tasks, to data outside text (eg: video, image)
- Model: `github.com/tensorflow/tensor2tensor`

---
### Preprocessing

- Input embedding
	- Gives each word a number
		- Method 1: One-hot vector (dictionary)
		- Method 2: Input word embedding
			- Similar words should have similar vector

- Positional encoding
	- Why it matters? Importance of position
		- "The Avengers defeated Thanos" versus "Thanos defeated the Avengers"
	- How we add information of order?
		- In this paper, coauthors try to put that information with 
			1. current word embedding
			2. new vector that contains information on position of each word. 
		-  Checklist of positional encoding
			- 1. Output a unique encoding for each time-step 
			- 2. Consistent distance between any two-time steps
			- 3. Should generalize to longer sentences, without any efforts. 
			- 4. Deterministic, which means its values should be bounded. 
		- Possible design
			- Assign position encoding to each time-step linearly. 
			- Issue: 
				- The embedding could be huge
				- The model will be confronted problems when they encounter a sentence which is longer than those sentence in training. 
			- eg: 
				- 4.2, 4.76, 4.69
				- 1,2,3
			- Assign embedding such that embedding would in between 0 and 1.
				- Issue: 
					- Non-deterministics: create the inability to determine how many words are present within a given range. 
					- Non-consistent: The time-step-delta does not have a consistent meaning across sentences. 
			- Method 3: Create a d-dimensional vector that contains information about a specific position in a sentence. 
				- Because word has 512 dimension in the model. Positional embedding will also be 512 dimension?
				- To fill the elements, of the vectors, authors used $sin(x)$ for even dimensions, and $cos(x)$ for odd dimensions. 
					- $PE_{(pos,2i)} = sin(\frac{pos}{10000^{2i/d_{modle}}})$
					- $PE_{(pos,2i+1)} = cos(\frac{pos}{10000^{2i/d_{modle}}})$
					- $\vec p_t = \begin{bmatrix}  sin(\omega_1,t) \\ cos(\omega_1,t) \\ sin(\omega_2,t) \\ cos(\omega_2,t) \\ \vdots \\ sin(\omega_{d/2},t) \\ cos(\omega_{d/2},t) \end{bmatrix}_{d \times 1}$, where $\omega_k = \frac{1}{1000^{\frac{2k}{d}}}$
				- The authors chose this function because they hypothesized it would allow the model to attend by relative position. 
				- Amirhossein Kazemmnejad's blog post on the topic is good:
					- https://kazemnejad.com/blog/transformer_architecture_positional_encoding/

- Figure:
	- How RNN consider order 
![[Pasted image 20230419011810.png|400]]

---
- Self attention
	- eg: "The animal didn't cross the street because it was too tired".
	- It is easy for us to infer, but it is more difficult for an algorithm to do so.
	- self-attention of the algorithm would put part of its attention to "the animal", and baked a representation of it into the encoding of "it".
	- Key idea: using different copies of the same input. 
		- So their multiplication has same dimension as the embedding vector. 
		- The data can be square or non-square. The authors chose these matrices in a way that the 52 dimensional embedding was converted to three 64 dimensional embeddings, after matrix multiplication.
			- In transformer model, why input embeddings has 512 dimensions, while Queries, keys and values has 64 dimensions for each?
		- 3 copies, Q, K, V embeddings
			- Q,K,V are used to compute attention weights, which determine the importance or relevance of different tokens in the input sequence for a given query.
			- The queries allow the model to express what information it is looking for, the keys help determine which tokens are relevant for a given query, and the values provide the actual information associated with the tokens.
		- Attention weight
			- Attention weight is used to weight the values in $V$. 
			- Computation:
				- Taking the dot product between queries and keys, followed by a softmax operation to normalize the weights. 
		- Weighted value
			- Values are weighted by attention function calculated by Q and K. 
			- The weighted values are summed up to obtain the output of the self-attention mechanism.

   - Query embeddings $Q$
				- Representation: 
					- represent the tokens in the input sequence in a transformed space
				- How to obtain:
					- They are obtained by multiplying the input embeddings by a learnable weight matrix. 
				- Dimensions:
					-  The dimensionality of queries is typically lower than the input embeddings to reduce computational costs.
			- Keys embeddings $K$
				- Representation:
					- represent the tokens in the input sequence in the same transformed space as the queries.
				- How to obtain
					- Same as Q
				- Dimension:
					- Same as Q
			- Values embeddings $V$
				- Represents:
					- The values are embeddings that provide the actual information associated with the tokens in the input sequence. 
				- How to obtain
					- Same as Q, K
				- Dimensions
					- Same as Q, K
		- Use $Q$ and $K$ to calculate "score"

- [[Gradient descent]]

- Figure: How does self attention work?
	- Source: the illustrated transformer https://jalammar.github.io/illustrated-transformer/
	- eg of self-attention
		- In the image, First word is "thinking". $q_1 \times k_1 = 112$. 
		- Score each word of the input sentence against this word. 
		- As we encode a word at a specific location, the score decides how much attention to place on other parts of the input sentence. 
		- Divide the score by  $\sqrt{d_k}$ ( in paper $d_k$ is 64, so $\sqrt{d_k} = 8$) such that  
		- Softmax normalize the score, so they are all positive and add up to 1. 
			- This softmax determines how much each word will be expressed at this position. 
			- Sometimes it is more meaningful to attend to another word that is relevant to the current word. 
		- Value vectors come into play. Multiply each vector with its corresponding softmax score. The goal is preserve the values of the words we want to focus, while fading out irrelevant words, by multiplying them, by multiplying them with very small numbers. 
		- The last step is to sum up the weighted value vectors. 
			- This produces the output of the self-attention layer for the first word. 
			- That vector will be send to the feed-forward neural network
![[Pasted image 20230419020909.png|400]]

- Having parameter number that is power of 2 
	- computational efficiency and hardware considerations:
		- Many deep learning frameworks and hardware accelerators are optimized for tensor operations that involve dimensions that are powers of 2. For example, when performing matrix multiplication or convolution, using dimensions that are powers of 2 can result in more efficient computation due to hardware optimizations like vectorization, parallelization, and memory alignment.

- feed-forward neural network

- Multi-head attention


---
- Batch normalization

![[Pasted image 20230418144328.png]]
- Batch normalization versus layer normalization
- 1. Scope of normalization
- 2. Training dynamics
- 3. Applicability
- 4. Robustness
- 5. Parameterization
- 6. Input dependencies
