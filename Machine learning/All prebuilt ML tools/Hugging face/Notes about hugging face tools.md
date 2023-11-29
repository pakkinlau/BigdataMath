https://huggingface.co/learn/nlp-course/chapter2/4?fw=pt

### NLP tools
- Tools 
	- Feature extraction
	- Zero-shot classification
	- NER
	- Question answering
	- Text generation
	- Translation
	- Summarization
	- Fill-mask
	- Sentiment analysis
- History of transformers
	- GPT-like
	- BERT-like
	- BART/T5-like
- Transformers are language models
	- Trained on large amounts of raw texts
	- Self-supervised learning is a type of training in which the objective is automatically computed from the inputs of the model.
	- These model develops a statistical understanding of the language it has been trained on, but it is not very useful for practical tasks. 
- Transfer learning
	- To make base model useful, it have to go through transfer learning.
	- eg:
		- masked  language modeling: 
			- The model predicts a masked word in the sentence. 
	- performance:
		- training a task from scratch would got 68% accuracy, while fine-tuning a pretrained model could get 81% accuracy. 

- Figure: the flow of transfer learning
![[Pasted image 20230627182236.png|400]]

### General architecture of transformer
- Types:
	- Encoder (left) only model
	- Decoder (right) only model
	- Encoder decoder model / sequence-to-sequence model
- Layers
	- Attention layers
		- eg: a word by itself has a meaning, but that meaning is deeply affected by the context, which can be any other word / words before or after the word being studied.
- Architecture:
	- "Architecture" means the skeleton of the model
	- Originally designed for translation
	- Encoder receives inputs in one language
	- Decoder  receives the same sentences in the desired target language. 
	- Attention layer can be used in both encoder and decoder. 
- Checkpoints
	- These are the weights that will be loaded
- Model:
	- This is an umbrellas that isn't precise as last two.

### Encoder models
...
- Encoder generates a representation of the whole sentence, which is perfectly suited for a task like classification.

### Decoder models
...
- Decoder models are perfectly suited for text generation from a prompt.


### Sequence-to-sequence model
...
- Seq2seq are better suited for tasks where you want to generate sentences in relation to the input sentences, not a given prompt.
	- Examples: Summarizing text


### Transfer learning
...



