---
category: []
alias: []
tags :[]
---

- 26-9-2022: created

- What is Decoder?
	- To decode means to convert a coded message into intelligible language. 
	- Analogy:
		- A Pictionary game, a person get a word, and draw it as a picture. That is encoding. The second picture guess the word from the picture. That is decoding. 
	- In machine learning model, the role of decoder will be to convert the 2D vector into the output sequence, the English sentence.
	- Structure:
		- It is built with RNN layers and a dense layer to predict the English word. 

- Formalism of decoder: ^58bb6d
	- $\text{DEC:}R^d \times R^d \rightarrow R^+$, that maps pairs of node embeddings to a real-valued node similarity measure, which quantifies the similarity of the two nodes in the original graph. $R^+$ usually means the set of all strictly positive numbers. 

- Lect4, [[(Course) CS224W - Machine learning with graphs (stanford)]]
	- [[dot product]] decoder with node similarity defined by the edge connectivity is equivalent to matrix factorization of A.

---
## Reference

1. Nechu's medium blog: https://towardsdatascience.com/what-is-an-encoder-decoder-model-86b3d57c5e1a#:~:text=To%20decode%20means%20to%20convert,output%20sequence%2C%20the%20English%20sentence.