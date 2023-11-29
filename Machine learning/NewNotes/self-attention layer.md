- Related: [[attention]]

- Definition:
	- It is a key building block in models like [[Transformer]], which have achieved remarkable success in various NLP tasks.
- Key component:
	- Vectors
		- Common characteristics:
			- The vectors are derived by applying a linear transformation to the token's embedding using a trainable weight matrix specific to the value operation.
		- Types
			- (Note: the actual equation for determining each vector might differs. Need to be verified. )
			- Query vector
				- The query vector is a learned representation of a token that seeks to understand the relationship between that token and other tokens in the input sequence. 
				- For each token in the input sequence, a query vector is derived through a linear transformation of the token's embedding. This transformation is typically achieved using a trainable weight matrix specific to the query operation.
				- Mathematical representation:
					- $q = W_q * x$, where $W_q$ is the trainable weight matrix for the query operation. 
			- Key vector
				- The key vector is another learned representation of a token that acts as a unique identifier for that token. It helps in capturing the importance of different tokens concerning a particular query. 
				- Similar to the query vector, the key vector is derived by applying a linear transformation to the token's embedding using a trainable weight matrix specific to the key operation.
				- Mathematical representation:
					- $k = W_k * x$, where $W_k$ is the trainable weight matrix for the key operation. 
			- Value vector
				- The value vector is the final learned representation of a token that stores information about that token. It does not have any specific role in the attention mechanism but is used later in the process to calculate the weighted sum of the values based on the attention scores. Similar to the query and key vectors, the value vector is derived by applying a linear transformation to the token's embedding using a trainable weight matrix specific to the value operation.
				- Mathematical representation:
					- $k = W_v * x$, where $W_v$ is the trainable weight matrix for the value operation. 
		- These are learned linear transformations of the input embedding. 
	- Attention scores
		- The attention score quantifies the similarity between the query vector and the key vector for each token in the sequence. It measures how much the current token should "pay attention" to other tokens. This is often computed using a dot product or other similarity measures followed by a softmax operation to obtain normalized attention weights.
		- Computation:
			- Input: Q, K vector
			- Raw attention score S: $S = Q * K^T$, where $S$ is a $n \times n$ matrix, $K^T$ is the transpose matrix of the vector $K$. 
			- Scale the dimensionality: $S_{\text{scaled}} = S / {\sqrt(d)}$
			- Apply softmax function: `A = softmax(S_scaled, axis = -1)`, where $A$ is now $m \times m$ matrix.
	- Weighted sums (The final output) (represent as "context vector")
		- The final step is to compute a weighted sum of the value vectors using the attention scores. 
		- This weighted sum represents the context vector, which captures the importance of different tokens in the input sequence relative to the current token.
- The final output vector:
	- 1. It is context-aware
		- It is a combination of multiple vector, and the value of vector during combination depends on the context. 
		- The final output vector from the self-attention layer is not a one-to-one mapping like word embeddings. In the context of the self-attention mechanism in a Transformer model, the final output vector is typically a weighted sum of the Value vectors, and it is calculated based on the attention scores obtained from the dot product of the Query and Key vectors.
		- Compare:
			- Word embeddings are fixed, independent, pre-trained vectors that map each unique word in the vocabulary to a specific vector representation.
	- 2. It is dynamic: 
		- The output of the self-attention layer is context-dependent and varies depending on the input sequence.
		- Compare:
			- In word embedding, For a given word in the input sequence, the corresponding word embedding is retrieved, and it remains unchanged throughout the model's processing.

- Why it can be context-aware?
	- 1. Attention score:
		- The self-attention mechanism calculates attention scores by performing a dot product between the Query vector and the Key vector for each position in the input sequence.
		- These attention scores represent the relevance or similarity between the Query and Key vectors, indicating how important each element in the Value vector is to the corresponding element in the Query vector.
		- After obtaining the attention scores, they are normalized using the softmax function, resulting in attention weights that represent the relative importance of each element in the Value vector for the current position.
	- 2. Weighted sum
		- This weighted sum ensures that the model emphasizes more relevant elements in the input sequence while downplaying less important ones, allowing it to focus on the contextually relevant parts of the sequence.
	- 3. Information flow
		- The self-attention mechanism allows information to flow between all positions in the input sequence, regardless of their distance from each other.
		- The attention scores can capture long-range dependencies in the data, allowing the model to establish connections between elements that are further apart in the sequence.
		- This information flow enables the model to understand the context in which each element appears and facilitates the learning of complex patterns and relationships within the sequence.
	- 4. Multiple layers or self-attention
		- Transformer models typically stack multiple layers of self-attention to capture different levels of context and dependencies in the input sequence.
		- Each layer refines the representation of the input by incorporating more context and considering the interactions between different parts of the sequence.
		- This multi-layered approach enhances the context-awareness of the model, enabling it to make more informed decisions based on the relationships across the entire sequence.

- How multiple stack of transformers can cooperate to each others?


- while the model is using a very similar equation to computer Q,K,V vector from g x, (such as `q = W_q * x` and `k = W_k * x`)why Q,K,V could represent different thing?


---
- Steps of how a self-attention layer works:
1. **Input Preparation**:
    - The self-attention layer takes three input vectors: Query, Key, and Value vectors. These vectors are typically derived from the input sequence, and they play different roles in the attention mechanism.
    - For the purpose of the UML sequence diagram, you can represent the Query, Key, and Value vectors as labeled arrows or labeled objects with their respective values.
2. **Calculate Attention Scores**:
    - The attention scores are calculated by computing the dot product between the Query and Key vectors. These scores represent the relevance or similarity between each element in the Query vector and all elements in the Key vector.
    - To illustrate this part, you can draw labeled arrows from each element of the Query vector to all elements of the Key vector, with the values of the attention scores written next to the arrows.
3. **Attention Weighting**:
    - The attention scores are normalized using the softmax function to obtain attention weights. These weights indicate how much each element in the Value vector should be attended to or weighted in the final output.
    - To visualize this step, you can draw labeled arrows from each element of the Value vector to a summed output object, and label these arrows with the corresponding attention weights.
4. **Weighted Sum**:
    - The final output vector is obtained by taking the weighted sum of the Value vector, where the weights are the attention scores obtained in the previous step.
    - For this part, you can draw an arrow from the summed output object to the final output object, labeled as "Weighted Sum," and indicate that it represents the final output of the self-attention layer.

- Detailed:
- Step 1: 
	- Self-attention input
![[Pasted image 20230728014834.png]]
![[Pasted image 20230728015130.png]]

- Step 2: Calculate Attention Scores
![[Pasted image 20230728020029.png]]

- Step 3: 
![[Pasted image 20230728020304.png]]

- Step 4:
![[Pasted image 20230728020445.png]]


---
