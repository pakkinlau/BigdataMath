---
category: []
alias: []
tags: []
---

- 25-10-2022 15:51: created

---
- Definition:
	- It refers to a mechanism or technique that allows models to focus on specific parts of the input data that are deemed most relevant for the task at hand. Attention mechanisms have become a crucial component in various machine learning models, especially in natural language processing (NLP) and computer vision tasks.
	- introduced in the context of sequence-to-sequence models, specifically in machine translation tasks, to improve the alignment between input and output sequences.
- Advantage:
	- Computational efficient
		-  Instead of the traditional approach of using fixed-length representations like RNNs or LSTMs, attention mechanisms enable the model to weigh different parts of the input sequence dynamically while generating the output.

- How attention models facilitate the discovery of pattern knowledge:
	- Steps:
		- Selective focus:
			- This focus enables the model to concentrate on important patterns, relationships or dependencies.
		- Long-range dependencies / Efficient computation:
			- Traditional neural network may struggle to capture long-range dependencies effectively. 
			- Attention models address this issue by learning to associate distant elements in the input sequence, even if they are separated by a large number of steps or tokens.
			- Instead of processing the entire sequence at once, attention models can selectively attend to relevant parts, reducing the computational burden.
		- Pattern recognition
			- It can recognize recurring patterns or motifs within the data
			- These patterns may not be explicitly encoded in the input representation but can emerge as a result of the attention mechanism's learning process.
		- Interpretable representation
		- Adaptability
			- It can adapt their attention patterns dynamically based on the input and the task. 

- NLP Model
	- Transformer: 
		- The Transformer architecture, introduced in the paper "Attention is All You Need," utilizes self-attention mechanisms to compute contextual embeddings for words in a sentence. This allows the model to capture long-range dependencies and better understand the context of each word based on the entire sentence.
	- BERT (Bidirectional Encoder Representations from Transformers): 
		- BERT employs a multi-layer, multi-head self-attention mechanism that enables bidirectional processing of the input text, leading to state-of-the-art performance in various NLP tasks like question answering, text classification, and named entity recognition.
	- GPT (Generative Pre-trained Transformer) models: 
		- Models like GPT-2 and GPT-3 use the Transformer architecture with attention mechanisms for language generation tasks, demonstrating impressive capabilities in natural language understanding and generation.
- Computer vision models:
	- Spatial Attention: 
		- This type of attention is used to highlight different regions of an image based on their importance to the task. It allows the model to "pay attention" to the relevant parts of the image when making predictions.
	- Channel Attention: 
		- Channel attention is used to emphasize or suppress specific channels or feature maps in a convolutional neural network (CNN) to capture more relevant features.

- Figure:
	- The process of preparing a attention-based model.
	- The detail of "attention-based model" refer to [[self-attention layer]]
![[Pasted image 20230727042412.png]]

- Figure
![[Pasted image 20230727045914.png]]

---
- Obtaining attention weight for each token from a language model

```python
import torch
from transformers import BertTokenizer, BertModel

def extract_attention_weights(input_text, model_name='bert-base-uncased'):
    # Load the BERT model and tokenizer
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertModel.from_pretrained(model_name)

    # Tokenize the input text
    input_ids = torch.tensor([tokenizer.encode(input_text, add_special_tokens=True)])

    # Get the model's attention masks and attention weights
    with torch.no_grad():
        model.eval()
        outputs = model(input_ids)
        attention_masks = outputs[2]  # Attention masks for each layer
        attention_weights = torch.stack(attention_masks, dim=0).squeeze(1)  # Stack and remove the batch dimension

    return attention_weights

if __name__ == "__main__":
    input_text = "The quick brown fox jumps."
    model_name = 'bert-base-uncased'

    attention_weights = extract_attention_weights(input_text, model_name)

    # Print the attention weights for each layer and head
    for layer_idx, layer in enumerate(attention_weights):
        print(f"Layer {layer_idx + 1}:")
        for head_idx, head in enumerate(layer):
            print(f"Head {head_idx + 1}: {head.tolist()}")
        print("\n")

```

- Figure: sequence diagram
![[Pasted image 20230727051234.png]]

- Figure: class diagram
![[Pasted image 20230727051427.png]]

---
## Reference

1. 