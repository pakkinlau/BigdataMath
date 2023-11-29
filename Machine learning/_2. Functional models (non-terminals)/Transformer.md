- 28-7-2023
---
- Constrast:
	- [[]]

---

- Definition 
	- introducing the self-attention mechanism and parallel processing, enabling it to efficiently process and generate sequential data, such as language sequences.
- Technical design:
	- a stack of [[self-attention layer]]s and [[feed-forward]] neural networks without relying on sequential computations like traditional recurrent neural networks.

---
- input: data
- output: refined data

---

- Role: 
	- massaging the data to make it easier to be consumed by the later devices / end-user.
- Key features:
	- 1. Feature extractors
		- extract relevant features from the input data, highlighting important patterns or characteristics.
	- 2. Dimensionality reducers
		- Techniques such as PCA, SVD
		- helping to manage high-dimensional data and eliminate irrelevant information.
	- 3. Data cleaners
		- Transformers can also perform data cleaning tasks, removing noise, outliers, or errors from the input data.
	- 4. Cooperative nature of transformers: 
		- Transformers can cooperate with each other since their input and output data types remain the same. This allows multiple transformers to be combined in a pipeline
		- They can be freely added or removed without affecting the overall system because the datatype remains unchanged.



---
- Why transformer allow parallel computation?
	- In transformer, the self-attention model is performing in a context-aware representation, each element (word/token) in the input sequence interacts with all other elements to determine its context-aware representation. This interaction is performed through weighted summation, where attention weights are calculated based on the relationships between elements. 
		- It can be parallelized because the attention scores for each element are computed independently of the other elements. 
		- The attention weight for a given element depends only on the embeddings of all elements in the input sequence, which can be processed concurrently in parallel hardware like GPUs.
	- Importantly, the calculation of attention weights can be done in parallel for all elements in the sequence, allowing the model to attend to all elements at the same time.
- Why RNN cannot be running in parallel?
	- At each time step, the model takes an input element and its hidden state from the previous step to compute the output and the updated hidden state for the current step.
	- This inherently sequential nature of RNNs creates a dependency chain, which makes parallel computation impossible. 
- Why attention is so good?
	- Relationship extraction
		- The self-attention mechanism computes attention weights for each element in the input sequence by taking into account its relationships with all other elements in the same sequence. These attention weights determine the importance of each element when computing its context-aware representation. 
	- Parallel
		- By attending to all elements in parallel, the transformer model can process the entire sequence at once, making it highly efficient and enabling it to capture long-range dependencies more effectively than RNNs.
		- This parallel processing capability is one of the key reasons behind the transformer's success in natural language processing tasks and other sequence-to-sequence tasks. It allows transformers to handle longer sequences and capture complex dependencies between elements more efficiently, leading to better performance on a wide range of tasks, including machine translation, language modeling, text generation, and more.




---

- 25-9-2022: created

### Old Note: Need review!!

- 3d. Transformer
	- Related structure:
		- This kind of structure is similar to GRUs, LSTMs. But transformer eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between inputs and outputs. 
	- Performance
		- This model scored 41 in BLEU after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. 
	- Mitigation of problems
		- 1. Loss of information
			- Passing information forward through an extended series of recurrent connections leads to a loss of relevant information and to difficulties in training
		- 2. Inhibiting parallel computational resources. 
			- Most attention mechanisms use recurrent neural networks, this limits their usefulness for transfer learning, because sequential nature of RNN the hidden units$h_t$ feeds in a sequence of hidden states as a function of previous hidden state $h_{t-1}$, which precludes parallelization within training examples. That becomes critical at longer sequence lengths, as memory constraints limit batching across examples. 
		- Factorization tricks for LSTM networks (Kuchaiev, 2017)
		- Outrageously large neural networks: the sparsely-gated mixture-of-experts-layer (Shazeer et al., 2017)
	- Architecture
		- 1. An input sequence mapped into a sequence of continuous representation to the decoder. The decoder generates an output sequence of symbols one element at a time. At each step the model is auto-regressive, consuming the previously generated symbols as additional input when generating the next.
		- 2. Stacks of network layers consisting of simple linear layers, feedforward networks, and custom connections around them.
		- 3. The key innovation of transformer is the use of self-attention layers. 
			- Self-attention allows a network to directly extract and use information from arbitrary large context without the need to pass it through intermediate recurrent connections as in RNNs.
	- Transformer architecture achieves the relations of two signals with arbitrary positions in input or output with a constant number of operations. It is also the first model that relied entirely on self-attention for the computation of representations of inputs or outputs without using sequence-aligned recurrent networks or convolutions. 
