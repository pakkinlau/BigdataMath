- 11-10-2022: created

- [[language-agnostic]]
- [[NLP models]]

- systematically investigate methods for learning multilingual sentence embeddings by combining the best methods for learning monolingual and cross-lingual representations including: [[masked language modeling]] (MLM), [[translation language modeling]] (TLM) (Conneau and Lample, 2019), [[dual encoder translation ranking]] (Guo et al., 2018), and additive margin softmax (Yang et al., 2019a). 

- [[feature]]


- [[performance]]:
	- With a pre-trained multilingual language model: reduce 80% data required to achieve good performance. 
	- Arhieves 83.7% [[bi-text retrieval]]

---
## session 1

![[Pasted image 20221012162612.png|300x200]]
- Figure: Dual encoder model with [[BERT]] based encoding modules. 

- While existing [[cross-lingual]] sentence embedding, using large pretrained language models is not well explored. 

- [[encoder]] are trained directly on translation pairs (Artetxe and Schwenk, 2019b; Guo et al., 2018; Yang et al., 2019a), or on translation pairs combined with monolingual inputresponse prediction (Chidambaram et al., 2019; Yang et al., 2019b).



![[(Paper) Feng, F., Yang, Y., Cer, D., Arivazhagan, N., Wang, W., & Ai, G. (2020). Language-agnostic BERT Sentence Embedding..pdf]]