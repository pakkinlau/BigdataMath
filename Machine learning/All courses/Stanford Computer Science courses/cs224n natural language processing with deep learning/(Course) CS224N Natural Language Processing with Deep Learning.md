- Learning goals
	- the foundations of the effective modern methods for deep learning applied to NLP
	- A big picture of understanding of human languages and the difficulties in understanding and producing them via computers
	- An understanding of and ability to build systems (in PyTorch) for some of the major problems in NLP. 
		- Word meaning, dependency parsing, machine translation, question answering

---
# Lecture 1

### Word meaning
- many approaches
	- Words as discrete symbols
		- problems with words as discrete symbols
	- Commonest linguistic way of thinking of meaning: signifier(symbol)$\iff$ signified(idea or thing)
		- wordNet a thesaurus containing lists of synonym sets and hypernyms
		- Problems
			- A useful resource, but missing nuance
			- Subjective
			- Requires human labor to create and adapt
	- Represent words by their context
		- Distributional semantics, a word's meaning is given by teh words that frequently appear close-by.

### Word vector
- We build dense vector for each word, chosen so that it is similar to vectors of words that appear in similar contexts, measuring similarity as the vector dot product. 


### Word2vec
- A framework for learning word vectors
- Idea:
	- Word2vec maximizes objective function by putting similar words nearby in space 
	- ...
	- ...
- Objective function
	- Likelihood: $L(\theta) = \prod_{t=1}^T \prod_{-m \leq j \leq m} P(w_{t+j} | w_t ; \theta)$
	- Objective function $J(\theta)$ is the average negative log likelihood
		- $J(\theta) = - \frac{1}{T}logL(\theta) = - \frac{1}{T} \sum_{t=1}^T \sum_{-m \leq j \leq m} log P(w_{t+j} |w_t; \theta)$
		- Minimizing objective function $\iff$ Maximizing predictive accuracy
	- Prediction function
		- $P(o|c) = \frac{exp(u_o^T v_c)}{\sum_{w \in V} exp(u_w^T v_c)}$
- Training of model -  optimize value of parameters to minimize loss
	- Recall: $\theta$ represents all the model parameters, in one long vector
	- Derive: 
		- See slide L1, p33-35
- Gradient descent

---
# Lecture 2

- Capture the essence of word meaning more effectively by counting

### Bag of words model
- The model makes the same prediction at each position
- We want a model that gives reasonably high probability estimate to all words that occur in the context

### Skip-gram model with negative sampling
- ...
- The normalization term is 
- Main idea
	- Train binary logistic regressions to differentiate a true pair (center word and a word in its context window) versus several noise pairs (the center word paired with a random word)
- Word2vec algorithm family
	- Why two vectors? 
		- Easier optimization, average both at the end
		- Two model variants
			- Skip-grams (SG)
			- Continuous bag of words (CBOW)
	- Loss functions for training
		- Naive softmax
		- More optimized variants like hierarchical SoftMax
		- Negative sampling
	- Overall objective function
		- $J(\theta) = \frac{1}{T} \sum_{t=1}^T J_t (\theta)$
		- $J_t(\theta) = log \sigma (u_0^T v_c) + \sum_{i=1}^k E_{j~P(w)} [log \sigma(-u_j^Tv_c)]$
		- Logistic / sigmoid functions

- Why not capture co-occurrence counts directly?

### Co-occurrence vectors
- simple count co-occurrence vectors
	- ...
	- ...
- low-dimensional vectors
	- ...
	- ...

### GloVe
- Encoding meaning components in vector differences
- ...
- ...
- ...


### Evaluation of word vectors
- Related to: general evaluation in NLP -- intrinsic versus extrinsic
- Intrinsic
	- Evaluation on a specific / intermediate subtask
	- Fast to compute
	- Helps to understand that system
	- Not clear if really helpful unless correlation to real task is established
	- eg:
		- 1. Intrinsic word vector evaluation
			- $d = arg\ max \frac{(x_b - x_a + x_c)^T x_i}{||x_b - x_a + x_c||}$
		- 2. Meaning similarity
		- 3. Correlation evaluation
- Extrinsic
	- Evaluation on a real task
	- Can take a long time to compute accuracy
	- Unclear if the subsystem is the problem or its interaction or other subsystem
	- If replacing exactly one subsystem with another improves accuracy --> Winning
	- eg:
		- named entity recognition (where good word vectors should help directly)

### Word senses
- most words have lots of meaning
	- eg:
		- pike has at least 9 distinct meanings
- solution:
	- improving word representations via global context and multiple word prototypes
		- Idea: cluster word windows around words, retrain with each word assigned to multiple different clusters banks.
		- Linear algebraic structure of word sesnse
			- different senses of word reside in a lienar superposition (weighted sum) in standard word embeddings like word2vec.
			- $v_{pike} = \alpha_1 v_{pike_1} + \alpha_2 v_{pike_2} + \alpha_3 v_{pike_3}$
			- where $\alpha_1 = \frac{f_1}{f_1 + f_2 + f_3}$, for frequency $f$
	- surprising result
		- because of ideas from sparse coding, you can actually separate out the sense (providing they are relatively common)

### Named entity recognition (NER)
- Approach 1: Deep learning classification task
	- The task:
		- Find and classify names in text, by labeling word tokens.
- Approach 2: Window classification using binary logistic classifier
	- Train logistic classifier on hand-labeled data to classify center word for each class based on a concatenation of word vectors in a window
- Classification review and notation
	- Supervised learning - we have a training dataset consisting of samples: $\{ x_i, y_i\}_{i=1}^N$
		- $x_i$ are inputs
			- words (indices or vectors), sentences, documents
		- $y_i$ are labels
			- labels are objects we try to predict
				- classes - sentiments, named entities, buy-sell decision
				- other words
				- multi-word sequences

- Figure:
	- PER: person's name
	- LOC: Location
	- Date: Date
![[Pasted image 20230623114953.png|600]]

### Neural classification

### Softmax classifier


### Neural networks

### Neural computation

---
# Lecture 3 Neural nets

---
# Lecture 4 Dependency parsing and syntactic structure


- PS:
	- No much time spent on this lecture!!! 
	- Not completely covered!


- Two views of linguistic structure
	- [[Constituency parsing|Constituent]]
	- [[dependency]]

### 4 methods of dependency parsing
- Dynamic programming
- Graph algorithms
- Constraint satisfaction
- Transition-based parsing / deterministic dependency parsing


### Conventional feature representation

### Neural dependency parser model architecture
- Why do we gain from a neural dependency parser?
	- Indicator features revisited
- Winnings
	- 1. Distributed representations
	- 2. Deep learning classifiers are non-linear classifiers

### Graph-based dependency parser


---
# Lecture 5 Language models and recurrent neural networks

### NLP task: language modeling (LM)


### Recurrent neural networks
- ...
- Problems with RNNs
- Recap on RNNs / LMs 

---
# Lecture 6 - LSTM RNNs and Neural machine translation

### Vanishing gradient
- ...
- ...
- Effect of vanishing gradient on RNN-LM
- Why is exploding gradient a problem?

### Long short-term memory RNNs (LSTMs)
- ...
- ...
- ...
- 

### Bi-directional RNNs


### Multi-layers RNNs


### Machine translation (MT)

### Neural machine translation (NMT)
- Why sequence-to-sequence is versatile?
	- ...
	- ...
- Training a neural machine translation system
- Advantages
- Disadvantages
- 

---
# Lecture 7 NMT and final projects


### Multi-layer deep encoder-decoder machine translation net


- figure:
![[Pasted image 20230629071815.png]]

### Greedy decoding
- we generate the target sentence by taking argmax on each step on the decoder. 
- problems with greedy decoding

### Exhaustive search decoding
- Ideally, we want to find a length $T$ translation $y$ that maximizes
	- $P(y|x) = P(y_1|x) P(y_2|y_1,x) P(y_3|y_1, y_2,x), \dots, P(y_T|y_1, y_2,\dots, y_{T-1}x)$
	- $P(y|x)= \prod_{t=1}^T P(y_t |y_1, \dots, y_{t-1}, x)$
- We could try computing all possible sequence $y$
	- This means that on each step $t$ of the decoder, we are tracking $V^t$ possible partial translation, where $V$ is vocab size. 
	- This $O(V^T)$ complexity is far too expensive. 
- problems:
	- if it is one way greedy algorithm, greedy decoding has no way to undo decision.
	- it it is collectively greedy algorithm, the cost is very expensive. 
- figure:
![[Pasted image 20230629073105.png|400]]

### Beam search decoding
- Core idea:
	- On each step of decoder, keep track of the $k$ most probable partial translations (which we call hypotheses)
		- $k$ is the beam size 
	- A hypothesis $y_1, \dots, y_t$ has a score which is its log probability:
	- $score(y_1, \dots, y_t) = log P_{LM}(y_1, \dots, y_t | x) = \sum_{i=1}^t log P_{LM}(y_i |y_1, \dots, y_{i-1},x)$
		- Scores are all negative, and higher score is better
		- We search for high-scoring hypotheses, tracking top $k$ on each step.
	- Problem: longer hypotheses have lower scores
	- Fix: Normalize by length.
		- Use this to select top one instead - $\frac{1}{t} \sum_{i=1}^t log P_{LM}(y_i |y_1, \dots, y_{i-1},x)$
	- Steps:
		- Step 0 - choosing parameter
			- say $k$ is the beam size, which determines the number of candidate sequence to consider in each step.
		- Step 1 - generate the first word prediction
			- Select the top-k predictions where k is the beam width, with the highest probabilities as the initial candidate sequences. 
		- Step 2 - expanding candidate sequences. 
			- For each chosen candidate  sequence, generate next word prediction using the language model, combine candidate sequence with each predicted word, to create new extended sequence.
			- Calculate the score or probability of each extended sequence, using the product of their individual word probabilities.
			- Sort and select the top $k$ 
		- Step N - repeating the process
		- Step Last - When a hypotheses produces `<END>`, the hypothesis is complete.
- It is not guaranteed to find optimal solution, but much more efficient than exhaustive search.

### SMT (Statistical machine translation) versus NMT (Neural machine translation)
- Better performance
	- More fluent
	- Better use of context
	- Better use of phrase similarities
- A single neural network to be optimized end-to-end
	- No subcomponents to be individually optimized
- Requires much less human engineering effort
	- No feature engineering


### Evaluate: how do we evaluate machine translation?
- BLEU (Bilingual evaluation understudy)
	- Compares the machine-written translation to one or several human-written translations and computes a similarity score, based on
		- geometric mean of n-gram precision (usually for 1,2,3 and 4-grams)
		- plus a penalty for too-short system translations
	- BLEU is useful but imperfect
		- There are many valid ways to translate a sentence, So luck factors plays a role in the score of the evaluation, because it has low n-gram overlap with the human translation.
		- So a good translation can get a poor BLEU score because it has low n-gram overlap with the human translation

- Figure: performance comparsion
	- The y-axis is the BLEU score.
![[Pasted image 20230629075856.png]]

### Attention
...
- The bottleneck problem (in seq2seq model)
	- It refers to the limitation imposed by the bottleneck layer, which compresses the input information into a fixed-length vector called "context vector" or "thought vector". The bottleneck is typically an LSTM or GRU layer that encodes the input sequence into a fixed-length representation before decoding it into the output sequence. 
	- The issue is that if forces the model to compress all the information from the input sequence into a fixed length vector. As a result, the model may struggle to capture and retain all the necessary information, particularly for long input sequence or where there is a significant amount of information that needs to be preserved.
	- This compression of information can lead to loss of details and context, which can negatively impact the performance of the model. The model may have difficulty in accurately generating the desired output sequence, especially if the input sequence is complex or contains long-range dependencies.
	- To mitigate the bottleneck problem, researchers have explored various techniques such as using attention mechanisms to allow the model to focus on different parts of the input sequence selectively. Attention mechanisms enable the model to allocate more attention to relevant parts of the input sequence, which helps to address the information loss caused by the fixed-length bottleneck vector.
	- Additionally, alternative architectures like Transformer models have been developed to address the bottleneck problem more effectively. Transformers rely heavily on attention mechanisms and do not have a fixed-length bottleneck layer, allowing them to capture long-range dependencies and handle larger input sequences more efficiently.
- Attention provides a solution to the bottleneck problem
- Idea:
	- On each step of the decoder, use direct connention to the encoder to focus on a particular part of the source sequence. 
- Attention variants
	- ...
	- ...
	- ...
	- 


### Sequence-to-sequence with attention

- Figure:
![[Pasted image 20230629080911.png|400]]

---

# Lecture 8  Self-attention and transformers

- From recurrence (RNN) to attention-based NLP models

- Issues with recurrent models
	- 1. Linear interaction distance
	- 2. Lack of parallelizability

- Attention  as soft, averaging lookup table
	- ...
	- ...

- self-attention - hypothetical example
	- keys, queries, values from the same sequence
	- barriers and solutions for self-attention as a building blocks

- fixing the self-attention problem
	- approach 1 - sequence order
		- position representation vectors learned from scratch
	- approach 2 - adding nonlinearities in self-attention

- masking the future in self-attention

### Transformer model
- ...
- Great results with transformers
	- ...
- Drawbacks
- Variants of transformers
- Great results with transformers

### Multi-head attention


### Transformer encoder-decoder

### Cross-attention

---
# Lecture 9 - Pretraining

### subword modeling
- consider there is word structure that is make up by subwords. 
- many language exhibits complex morphology, or word structure to communicate word sense. 
- Sometimes we can grasp the word sense from the subwords
- Types:
	- Variations: 
		- taaaasty
	- Misspellings:
		- laern
	- Novel items:
		- transformerify

### Byte-pair encoding algorithm
- It is a simple, effective strategy for defining a subword vocabulary
	- Steps
		- 1. Start with a vocabulary containing only characters and `<eow>` symbol.
		- 2. Using a corpus of text, find the most common adjacent characters `"a,b"`; add `"ab"` as a subword. 
		- 3. Replace instances of the character pair with the new subword; repeat until desired vocab size. 
	- Common words end up being a part of the subword vocabulary, while rarer words are split into components.
		- In the worst case, words are split into as many subwords as they have characters. 

- Figure
![[Pasted image 20230629092351.png]]

### The pretraining THEN finetuning paradigm
- It improves NLP applications by serving as parameter initialization. 
- Consider, provide parameters $\hat \theta$ by approximating $\underset{\theta}{min} L_{pretrain}(\theta)$
	- Which can be considered as the pretraining loss
	- This process is known as unsupervised learning, because the model doesn't have access to explicit labels, or human annotations. The goal of pretraining is to enable the model to capture general language patterns, grammar, and semantic relationships from vast amount of text it is exposed to.
- Then, finetuning approximates $\underset{\theta}{min} L_{pretrain}(\theta)$, starting at $\hat \theta$
	- Which can be described as "the finetuning loss"
- The pretraining may matter, because stochastic gradient descent sticks (relatively) close to $\hat \theta$ during finetuning. 
	- So maybe the finetuning local minima near $\hat \theta$ tend to generalize well
	- Or maybe the gradients of finetuning loss near $\hat \theta$ propagate nicely

- Figure
	- Pre-training: 
		- Pretrain involves lots of text. The model learn general things.
	- Fine-tuning: 
		- Fine-tuning on your tasks involve not many labels. Adapting the model to the task.
![[Pasted image 20230630190101.png]]


### Motivating model pretraining from word embeddings
- Backgrounds:
	- Word meaning and context:
		- "You shall know a word by the company it keeps" (KR Firth 1957)
	- Pretrained word embedding:
		- Circa 2017: Start with pretrained word embeddings (no context)
		- Learn how to incorporate context in an LSTM or Transformer while training on the task. 
- Some issues of language models:
	- The training data we have for our downstream task (like question answering) must be sufficient to teach all contextual aspects of language. 
	- Most of the parameters in our network are randomly initialized. 
- Modern NLP
	- Almost all parameters in NLP networks are initialized via pretraining.
- What is pretraining a language model, anyways?
	- Word meaning of "pre-training"
		- The term "pretraining" can be a bit misleading because it suggests that it is a preliminary or preparatory step before the actual training. In the context of language models, pretraining is the primary learning process where the model acquires its initial language understanding.
		  - It is called "pretraining" because it is often followed by a subsequent phase called "fine-tuning" or "task-specific training".
	- It refers to the initial phase of training, where the model is exposed to a large corpus of text data, to learn the statistical patterns and linguistic structures of the language.
	- The large corpus data could including:
		- Books
		- Articles
		- Websites
		- Other textual sources 
	- Pretraining is typically performed using unsupervised learning, where the model doesn't require explicit human-labeled annotations. 
	- The pretrained language model can then be fine-tuned on specific downstream tasks, such as text classification, sentiment analysis, question answering, or language translation. We will talk about fine-tuning in another thread.
- Benefits of pretraining a language model:
	- 1. It can improves NLP applications by serving as parameter initialization.
	- 2. General language understanding:
		- Pretraining exposes the model to a vast amount of diverse text data, allowing it to learn grammar, syntax and semantic patterns from various sources. 
		- As a result, the model gains a broad understanding of language, including context, nuances, and common usage.
	- 3. Transfer learning
		- Pretraining enables the model to learn useful representations of language that can be transferred to downstream tasks. 
		- These pretrained models serve as a starting point for fine-tuning on specific tasks, reducing the need for extensive task-specific training data and computational resources. 

- Gap filling 
	- Pretraining methods hide parts of the input from the model, and train the model to reconstruct those parts. 
	- This is exceptionally effective at building
		- create strong representations of language
		- Parameter initializations for strong NLP models
		- Probability distributions over languages that we can sample from


- Figure:
![[Pasted image 20230629092728.png]]
![[Pasted image 20230629092957.png]]


### Model pretraining 3 ways
- We classify the pretraining methods, for 3 types of language models

- encoders
	- Encoders gets bidirectional context - can condition to future - thus they cannot be trained easily.
	- How do we train them to build strong representations?
	- Idea:
		- Replace some fraction of words in the input with a special `[mask]` token, predict those words. 
			- Only add loss terms from words that are "masked out". If $\tilde x$ is the masked version of $x$, we are learning $p_{\theta}(x| \tilde x)$, called masked LM.
	- Example:
		- BERT
			- Devlin et al proposed Masked LM objective and released the weights of a pretrained transformer, a model they labeled BERT. 
			- Details
				- Training:
					- Predict a random 15% of (sub)word tokens
						- Replace input word with `[mask]` 80% of the time
						- Replace input word with a random token 10% of the time
						- Leave input word unchanged 10% of the time (but still predict it)
					- Why? Does not let the model get complacent and not build strong representation of non-masked words. 
				- Specs:
					- BERT-base: 12 layers, 768 dim hidden states, 12 attention heads, 110 million parameters. 
					- BERT-large: 24 layers, 1024 dim hidden states, 16 attention heads, 340 million parameters. 
				- Dateset:
					- BooksCorpus (800 million words)
					- English wikipedia (2500 million words)
			- Pretraining
				- It is expensive and impractical on a single GPU
					- BERT was pretrained with 64 TPU chips for a total of 4 days.
			- Finetuning
				- Finetuning is practical and common on a single GPU
					- "Pretrain once, finetune many times"


- Fine-tuned BERT
	- BERT was massively popular and hugely versatile. Finetuning BERT led to new state-of-the-art results on a broad range of tasks. 
	- Types:
		- QQP
			- Quora question pairs
		- QNLI
			- natural language inference over question and answering data
		- SST-2
			- sentiment analysis
		- CoLA
			- corpus of linguistic acceptability
		- STS-B
			- semantic textual similarity
		- MRPC
			- microsoft paraphrase corpus
		- RTC
			- a small natural language inference corpus

- Figure:
	- Embeddings of the BERT model. 
		- Token embeddings
			- BERT uses WordPiece tokenization, which breaks down words into subword units to handle out-of-vocabulary (OOV) words and improve generalization.
			- Each token is associated with an initial token embedding, which is a fixed-size vector that captures the semantic and contextual information of the token.
		- Segment embeddings
			- Segment embeddings are used in BERT to distinguish between different segments or sentences within a given text. 
			- BERT has the ability to process pairs of sentences, such as in the case of sentence classification or question-answering tasks. 
			- To differentiate between the segments, BERT assigns a unique segment embedding to each token based on its original segment or sentence. This allows the model to understand the relationship and dependencies between different segments of text.
		- Position embeddings 
			- Position embeddings in BERT provide information about the position or order of the tokens within the input sequence. Since transformers do not inherently capture sequential information, position embeddings are necessary to convey the positional encoding to the model. 
			- BERT incorporates position embeddings by assigning a unique position embedding vector to each token, indicating its position in the input sequence. 
![[Pasted image 20230630172023.png]]

- Limitations of pretrained encoder
	- If your task invovles generating sequneces, consider using a pretrained decoder; BERT and other pretrained encoder don't naturally lead to nice autoregressive (1-word-at-a-time) generation.
- Figure:
![[Pasted image 20230630173850.png]]






- interlude
	- what do you think pretraining is teaching?
- very large models and in-context learning


![[Pasted image 20230629095835.png]]


- Figure:
	- What are the equations about?
	- Figure 3a
		- Encoder
	- Figure 3b
		- Encoder-decoder
	- Figure 3c
		- Decoder
			- $h_1, \cdots , h_T$: the [[hidden state]]
			- $w_1, \cdot, w_T$: the input words/ sub-words
			- $y \sim Ah_t + b$: 
				- It is a linear layer at the end of the neural network, that generate the final prediction.
				- Let's say we are training the decoder to predict the sentiment.
				- You train not just the linear layer here, but actually back propagate the gradients all the way through the entire pretrained network, and fine tune all of those parameters. 
				- So it is not just training the linear layer, but the whole neural network's parameters. 
![[Pasted image 20230630182559.png]]
![[Pasted image 20230630182551.png]]
![[Pasted image 20230630183347.png]]
### pretrained word embeddings
- Circa 2017 
	- Start with pretrained word embeddings (no context)
	- Learn how to incorporate context in an LSTM or transformer while training on the task
- Some issues
	- The training data we have for our downstream task must be sufficient to teach all contextual aspects of language.
	- Most of the parameters in our networks are randomly initialized

### Pretraining through language modeling


### Stochastic gradient descent and pretrain / finetune




### Full fine-tuning
- Background 
	- Typical pre-training:
		- During pre-training, the model learns to predict the next word in a sentence or reconstruct masked-out words based on the context of the surrounding words. This process helps the model learn semantic and syntactic relationships between words, as well as general knowledge about language.
	- However, pre-training above is not sufficient for many NLP tasks, as the model lacks task-specific information.
	- Fine-tuning involves training the pre-trained model on a smaller labeled dataset that is specific to the task at hand. 
- Definition:
	- Full fine-tuning refers to the practice of fine-tuning the entire pre-trained model on the task-specific dataset. 
	- In this process, all the parameters of the model are updated during the fine-tuning phase. 
- Dataset:
	- The labeled dataset typically contains examples with input-output pairs, where the input is a textual input, such as a sentence, and the output is the desired prediction, such as sentiment classification or question-answering.
- Advantages:
	-  allows the model to adapt to the task-specific data and make predictions that are more relevant to the given task.
- Disadvantages:
	- It can be computationally expensive and requires a significant amount of labeled data. However, it often leads to better performance compared to using the pre-trained model as-is or using other transfer learning techniques where only a portion of the model is fine-tuned. 


### Parameter-efficient finetuning / light weight finetuning
- Definition
	- It refers to a technique used to adapt a pre-trained deep learning model to a new task or domain while minimizing the number of parameters that need to be updated or modified. 
- When to use it:
- Advantages:
	- This approach is particularly useful when computational resources or labeled data are limited.
- Disadvantages:
	- Performance is not good as full finetuning.

### Low-rank adaptation - of - parameter-efficient finetuning
- The low-rank adaptation refers to a specific approach to parameter-efficient fine-tuning. 
- In this technique, the weights of the pre-trained model are decomposed into low-rank matrices. 
- Low-rank matrices have a compact representation and can capture the essential information in the original weights. By applying low-rank adaptation, the number of parameters needed to represent the model can be significantly reduced.
- The process of low-rank adaptation of parameter-efficient fine-tuning involves decomposing the pre-trained model's weights into low-rank matrices, updating only a subset of these low-rank matrices during fine-tuning, and reassembling the updated matrices to obtain the adapted model. 
- This approach allows for efficient fine-tuning with reduced memory and computational requirements while preserving the performance of the original pre-trained model.



### Prefix-tuning
- Background
	- Traditional fine-tuning methods typically involve training a pre-trained language model on a specific downstream task by providing it with input-output pairs. 
	- However, these methods have limitations when it comes to generating coherent and contextually appropriate responses. In many cases, the model tends to generate generic or nonsensical completions, lacking a clear understanding of the input context.
- Definition
	- It is a technique to improve the performance of language models. 
	- fine-tune a pre-trained language model by conditioning it on a specific prefix or context during the fine-tuning process.
	- Prefix tuning aims to address this issue by conditioning the model on a specific prefix or context during fine-tuning. 
- Method
	- Instead of training the model on complete input-output pairs, the training data consists of partial sequences where the prefix is given, and the model is tasked with generating the rest of the sequence. This helps the model focus on generating completions that are consistent with the provided prefix.
	- By conditioning the model on a prefix, it encourages the language model to better understand the context and generate more relevant and coherent responses. The prefix can be a few words, a sentence, or even a paragraph, depending on the desired level of context.


### Prompt tuning
- Definition
	- It refers to the process of refining and optimizing the initial instruction or prompt provided to a language model like ChatGPT in order to achieve better results or specific outcomes. 
	- By modifying the prompt, you can guide the model's behavior, tone, or style, and steer it towards producing more accurate or relevant responses. It allows you to fine-tune the model's output to align with your specific needs or objectives.
- Process:
	- The process of prompt tuning often involves several iterations. You start with an initial prompt and evaluate the model's responses. Based on the results, you make adjustments to the prompt by adding or modifying instructions, changing the format, or specifying the desired output. After each iteration, you assess the model's performance and iterate again if necessary until you achieve the desired outcome.


---
- encoder-decoder
	- Good parts of decoders and encoders?
	- What is the best way to pretrain them?
	- How to train?
		- Span corruption
			- Replace different-length spans from the input with unique placeholders; decode out the spans that were removed. 
	- Example:
		  T5

---


- decoders
	- Languages models, that is what we have seen so far.
	- Nice to generate from; can't condition on future words
	- Example:
		- GPT



### Generative pretrained transformer (GPT)
- 2018's GPT was a big success in pretraining a decoder. 
- Specs:
	- 12 layers
	- 117M parameters
	- 768-dimensional hidden states
	- 3072 dimensional feed-forward hidden layers
	- [[Byte-pair encoding]] (BPE) with 40000 merges
- Dataset
	- over 7000 unique books
		- Contains long spans of contiguous text, for learning long-distance dependencies.
- Example task: natural language inference (NLI)
	- NLI including Label pairs of sentence as entailing / contradictory / neutral
	- To train GPT for NLI, you would use a labeled dataset consisting of pairs of sentences and their corresponding labels. 
	- The input representation for each pair of sentences would be constructed by concatenating them together with special tokens
		- Say, we have 2 sentence: `SentA` and `SentB`
		- When training, we have: `[Start]` `SentA` `[Delim]` `SentB` `[Extract]`
	- during training, updating parameters to minimize the loss.

- Q: Would the whole model lose its capability to make sense of semantic meaning?
- A: We keep the pretrained parameters fixed for the initial layers. Only the additional task-specific layers are trained during the fine-tuning. This allows the model to adapt its representations and predictions to the specific task, while retaining the general semantic knowledge captured during pretraining. 

- Scaling efficiency - how do we best use our compute


---
# Lecture 10 - Neural language generation

### Natural language generation


- Categories of NLG tasks
	- Ordered by "open-endedness"
		- Machine translation
		- Summarization
		- Task-driven dialog
		- Chitchat dialog
		- Story generation

- Text generation model
	- In autoregressive text generation models, 
		- at each time step $t$, our model takes in a sequence of tokens as input $\{y\}_{<t}$ and outputs a new token $\hat y_t$. 
		- For model $f(\cdot)$ and vocab $V$, we get scores $S = f(\{ y_{<t}\}, \theta) \in \mathbb{R}^V$, 
		- and probability would be $P(y_t | \{ y_{<t}\}) = \frac{exp(S_w)}{\sum_{w' \in V} exp(S_{w'})}$
- Trained one token at a time by maximum likelihood
	- Trained to maximize the likelihood of the next token $y_t^*$ given preceding words $\{y^*\}_{<t}$ , $L = - \sum_{t=1}^T log(P(y_t^* | \{y\}_{<t})$.
		- This is a classification task at each time step trying to predict the actual word $y_t^*$ in the training data.
		- Doing this is often called teacher forcing,
- Inference (= decoding) in NLG
	- In the context of NLG, inference is often synonymous with decoding.
	- And the process of inference refers to generating meaningful and coherent natural language output based on a given input or prompt. 
	- $\hat y_t = g(P(y_t| \{ y_{<t}\}))$
	- $g(\cdot)$ is your decoding algorithm
	- This process involves selecting the most likely token at each step based on the model's internal state and the previously generated tokens. 
		- Greedy algorithm
			- i.e. $\hat y_t = \underset{w \in V}{argmax}P(y_t = w | y_{<t})$
		- Beam search
			- 

- For non-open-ended tasks, 
	- we typically use encoder-decoder system, where this autoregressive model serves as the decoder, and we would have another bidirectional encoder for encoding the inputs.
	- encoder:
		- used to process the input data and encode it into a meaningful representation. The encoder is typically bidirectional model that takes into account the contextual information from both past and future inputs. 
		- It processes the input sequence and produces a fixed-length vector or a sequence of vectors that encapsulates the input information.
	- decoder:
		- an autoregressive model is employed as the decoder
		- it takes the encoded input representation from the encoder and generates thew output sequence step by step, usually in an autoregressive manner.
		- It predicts the next token of the output sequence conditioned on the previously generated elements.
		- Decoder typically uses attention mechanisms to focus on different parts of the input representation while generating the output.

- For open-ended tasks,
	- This autoregressive generation model is often the only component.




---
# Lecture 11 - Prompting, instruction finetuning and RLHF

- from language models to assistants 
	- zero-shot (ZS) and few-shot (FS) in-context learning
	- instruction finetuning
	- reinforcement learning from human feedback (RLHF)

---
### Class 1: zero-shot (ZS) and few-shot (FS) in-context learning
- Advantages:
	- No finetuning needed, prompt engineering (eg Chain of thoughts) can improve performance
- Disadvantages:
	- Limits to what you can fit in context
		- Due to the limited exposure to examples or the absence of specific training data, there is a constraint on the amount of information the model can grasp and utilize.
		- This limitation can affect the model's performance.
	- Complex tasks will probably need gradient steps
		- Gradient steps refers to the iterative updates made to the model's parameters during the training process using techniques such as backpropagation.
		- Complex tasks often involves intricate patterns, relationships, or dependencies that require more nuanced adjustments to the model's parameters.

### Emergent abilities from large language models
- It refers to the unexpected or novel capabilities can arise from the use of advanced language models, such as GPT-3.5.
	- Beyond their primary purpose of language generation, they have shown the potential for exhibiting additional skills and capabilities.
		- Creative writing
		- Translation
		- Information retrieval
		- Coding assistance
- If you ask some novel questions to the language model, it could generate some reasonable, or even correct answers back. 

### Emergent zero-shot learning
- It refers to the ability to do many tasks with no examples, and no gradient updates. 
- It refers to the ability of large language models to learn and perform tasks without specific training on that particular task.
	- eg: answering questions that has never encountered before. 
		- that is because the model has learned general patterns and knowledge about animals during training, allowing it to make reasonable inferences and predictions about new animal species. 
- real life examples:
	- GPT-2 beats SoTA on language modeling benchmarks with no task-specific fine-tuning

### Emergent few-show learning / In-context learning
- It means "specify a task by simply prepending examples of the task before your example". Also called in-context learning, to stress that no gradient updated are performed when learning a new task.
- How it works?
	- When we providing examples in the prompt, it update the gradient of the LLM, as such, it can improve the accuracy of the result. 

### Emergent few-shot learning is proportional to the model size
- Few-shot learning is an emergent property of model scale

### Limitations of prompting for harder tasks
- Some tasks even seem too hard for even large LMs to learn through prompting. Especially tasks involving richer, multi-step reasoning.

![[Pasted image 20230629191249.png]]

![[Pasted image 20230629191330.png]]


### Chain-of-thought prompting
- It refers to a technique in NLP, to generate coherent and contextually relevant text by conditioning the model's output on a given input or prompt. 
- Goal:
	- guide the model's generation process in a specific direction and encourage it to follow a logical chain of thought.
- Process:
	- When using chain of thought prompting, a user typically provides an initial prompt or instruction that sets the context or topic for the generated text. 
	- The model then uses this prompt as a starting point and attempts to build upon it, creating a coherent continuation that follows a logical flow of ideas. 
	- By maintaining a chain of thought, the model can produce text that is more relevant and consistent with the given context.

- Figure:
![[Pasted image 20230630123336.png|400]]

- Figure:
	- Few-shot CoT (chain of thoughts) prompting has the highest accuracy in the question answering process. 
![[Pasted image 20230630123616.png|500]]

---
### Instruction finetuning
- Recall: the pretraining / finetuning paradigm
	- Pretraining can improve NLP applications, by serving as parameter initialization
		- Lots of text, learn general things
- Steps
	- 1. Dataset preparation - Collect example of `(instruction, output)` pairs across many tasks and finetune an LM.
		- A dataset is created containing example dialogues or conversations that demonstrate the desired behavior. Each dialogue typically consists of an instruction or prompt given to the model and the corresponding model-generated response.
	- 2. Annotation:
		- The dataset is annotated to provide explicit instruction or guidance for the model. This can involve highlighting specific parts of the instruction that the model should pay attention to or indicating desired properties of the generated response.
	- 3. Model training:
		- The base language model, such as GPT-3.5, is fine-tuned using the annotated dataset. During fine-tuning, the model is optimized to generate responses that adhere to the given instructions or guidelines. 
		- This process involves updating the model's parameters to minimize the discrepancy between the generated response and the desired response specified in the dataset.
	- 4. Fine-tuning Objective: 
		- The fine-tuning process typically involves defining a specific objective or loss function that quantifies how well the model follows the instructions. This objective guides the optimization process by assigning higher scores to responses that align well with the desired behavior.
	- 5. Fine-tuning Iteration: 
		- The model is trained iteratively using the annotated dataset. In each iteration, the model's parameters are adjusted based on the defined objective, and the process continues until the desired level of performance is achieved or convergence is reached.
	- 6. Evaluate on unseen tasks
		- The fine-tuned model is evaluated to measure its performance and ensure that it produces responses aligned with the instructions. This evaluation can involve comparing the model-generated responses to human-generated responses or using other metrics specific to the task at hand.
- Discuss on its usefulness
	- Advantages
		- Simple and straight forward
			- Instruction fine-tuning allows for a more focused and targeted approach to improving a language model's performance. By providing explicit instructions, the model can be trained to understand and generate responses that align with the desired task or domain.
		- Generalize to unseen data. 
			- By training the model with diverse examples and instructions, it can learn patterns, concepts, and problem-solving strategies that are applicable to a wide range of similar tasks. 
			- This enables the model to provide accurate and relevant responses even when faced with previously unseen inputs.
	- Disadvantages
		- Expensive to collect ground-truth data for tasks
			- Tasks like open-ended creative generation have no right answer.
		- Mismatch between LM objectives and human preferences
			- Language modeling penalizes all token-level mistakes equally, but some errors are worse than others. 

---
### Reinforcement learning from human feedback (RLHF)
- Advantages:
	- Directly model preferences (cf. language modeling), generalize beyond labeled data
- Disadvantages:
	- RL is very tricky to get right
	- Human preferences are unreliable
		- Reward hacking is a common problem in RL
		- Chatbots are rewarded to produce responses that seem authoritative and helpful, regardless of truth.
		- Models of human preferences can be even more unreliable.


- Optimizing language models for human preference
	- Let's say we were training a LM model on some tasks (eg: summarization). For each LM sample $s$, imagine we had a way to obtain a human reward of that summary: $R(s) \in \mathbb{R}$.
		- say, for $s_1$ , $R(s_1) = 8$
	- Now we want to maximize the expected reward of samples from our LM:
		- $\mathbb{E}_{\hat S \sim p_{\theta}(s)} [R(\hat s)]$
			- $p_{\theta}(s)$ represents the probability distribution of samples (denoted by $s$) generated by a language model (LM) with parameters $\theta$.
			- $\hat S$ is the collection of summaries
			- $\hat S \sim p_{\theta}(s)$ means: the random variable $\hat S$ that follows the probability distribution $p_{\theta}(s)$. In other words, $\hat S$ is a sample or realization drawn from the distribution $p_{\theta}(s)$.
			- $R(\cdot)$ refers to the value or outcome of the reward function $R(\hat s)$ applied to a particular summary $\hat s$. 
			- $[R(\hat s)]$ represents the reward obtained for a specific example or summary $\hat s$ generated by the language model. 
	- Now tries to change our LM parameters $\theta$ to maximize $\mathbb{E}_{\hat S \sim p_{\theta}(s)} [R(\hat s)]$
		- $\theta_{t+1}:= \theta_t + \alpha \nabla_{\theta_t}\mathbb{E}_{\hat S \sim p_{\theta}(s)} [R(\hat s)]$
		- Policy gradient method in RL give us tools for estimating and optimizing this objective. 

### A very brief introduction to policy gradient / reinforcement learning
- Deviations:
	- Below

![[Pasted image 20230630133128.png]]
![[Pasted image 20230630132216.png]]


- Limitations of RL approach of finetuning:
	- 1. Human-in-the-loop is expensive
		- Solution - instead of directly asking humans for preferences, model their preferences as a separate NLP problem. (Reward model)
	- 2. Human judgments are noisy and mis-calibrated
		- Instead of asking for direct ratings, ask for pairwise comparisons, which can be more reliable. 

- Figure: single reward asking, versus, pairwise comparisions
![[Pasted image 20230630134133.png|300]]


### Reward model
- This is a separate NLP problem that tries to offset the cost of human-in-the-loop cycle,
- Use NLP model tries to predict the preference of humans. 

![[Pasted image 20230630134343.png]]
![[Pasted image 20230630134141.png]]


### Reinforcement with human feedbacks (RLHF)
- We have everything we need:
	- A pretrained (possibly instruction-finetuned) LM $p^{ST}(s)$
	- A reward model $RM_{\phi}(s)$ that produces scalar rewards for LM outputs, trained on a dataset of human comparisons
	- A method for optimizing LM parameters towards an arbitrary reward function.
- Now to do RLHF:
	- Initialize a copt of the model $p_{\theta}^{RL}(s)$, with parameter $\theta$ we would like to optimize
	- Optimize the following reward with RL:
		- $R(s) = RM_{\phi}(s) - \beta log( \frac{p_{\theta}^{RL}(s)}{p^{PT}(s)})$
			- Pay a price when $p_{\theta}^{RL}(s)$ > $p^{PT}(s)$

- Figure: the preformence of RLHF
![[Pasted image 20230630134833.png]]

### InstructGPT 
- sclaing up RLHF, to 30k tasks.

---
# Lecture 12 - Question answering

---
# Lecture 13 - ConvNets, Tree recursive neural networks

---
# Lecture 14 Insights between NLP and linguistics

---
# Lecture 15 Code generation

---
# Lecture 16 Multimodal deep learning, with an NLP focus

---
# Lecture 17 Coreference resolution

---
# Lecture 18 Model analysis and explanation

---
# Lecture 19 - Model interpretations 


