---
category: []
alias: [message]
tags: []
---

- 02-11-2022 03:54: created

- What is Message computation?
	- In [[Graph Convolutional Networks|GCN]], the "message"  is a very vague notion related to the embeddings of nodes. 
	- The most simple case
		- In [[message passing]], people might just simply assume [[homophily]] and pass node characteristics as the message to neighbors. Then for a unlabeled nodes, it aggregates all messages from its neighbor, to conclude its prediction.
	- In a general GNN framework: (R1)
		- The message passed into [[LSTM]]() or GRU() which enables the [[neural network]] to keep hidden states longer, which enable itself to process n-hops computation graph as a sequential data.
- Steps:
	- Each node will create a message, which will be sent to other nodes later.
	- $m_u^{(l)}=MSG^{(l)}(h_u^{(l-1)})$
	- MES() could be [[LSTM]](), LRU() etc. 



---
## Reference

1. [[(Course) CS224W - Machine learning with graphs (stanford)]]