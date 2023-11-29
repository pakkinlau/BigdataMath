---
alias: [sparsity]
---

Sparse is an adjective that describes the distribution of values.
Sparsity means that most of the elements in the vector are zero. 

- Property of sparsity
	- 1. efficient representation
	- 2. sampling efficiency
	- 3. noise robustness
	- 4. computation efficiency
	- 5. structural information

Sparsity in big data analytics can exist in many objects:
- Solution vector
    - (especially in optimization / norm minimization)
    - For example, in a linear regression problem, the solution vector could represent the coefficients of the regression equation. If most of the coefficients are zeros, the solution vector is sparse, indicating that only a few features have significant impact on the output.
- Input data
    - In a movie recommendation system, the input data could be a user-item interaction matrix where rows represent users and columns represent movies. If most users have only rated a few movies and left the rest unrated, the input data is sparse.
    - In natural language processing, a document-term matrix used for text analysis is typically sparse. Each row represents a document, and columns represent unique words or terms in the entire corpus. Most documents use only a fraction of the vocabulary, resulting in a sparse representation of text data.
    - Another examples: 
	    - Genomic data
	    - Social networks
	    - Collaborative filtering
	    - Text data
	    - Sensor data in IoT
- Output data
    - In natural language processing, generating a sparse output could refer to text summarization. Given a long article, a text summarization model might generate a summary that contains only a fraction of the words from the original article, making the output sparse compared to the input.
    - Another examples:
	    - Document classifications
	    - Anomaly detection
	    - Customer purchase history (not all customer buy a wide range of products)
	    - Biological data analysis (gene expression levels)
	    - Social network analysis (identifying influential nodes or communities)
- Intermediate data representations
    - Image processing - Edge detection
    - Genomics - sparse matrices where rows represent genes and columns represent samples
    - NLP - rows represent documents and columns represent terms, the matrix is often sparse
    - Sensor data detection -  For instance, temperature sensors deployed in a city might only record data in certain locations and at specific times, leading to sparse intermediate data when analyzing temperature patterns.
    - Graph database - In graph databases, the adjacency matrix of a graph can be sparse, especially in large networks. Nodes in a graph might be connected to only a few other nodes

Application
- Recommendation systems
- Text mining 
- Image processing


---

- 21-10-2022: created

- Sparse matrices can come into play when working with embeddings, especially in scenarios where you have a large vocabulary or feature space. A sparse matrix representation is used to save memory and computational resources.
- In this context, the sparse matrix often represents the relationships or co-occurrence statistics between words or features. The rows of the sparse matrix correspond to words or features, and the columns correspond to dimensions in the embedding space.

- [[GloVe]]:
	- GloVe efficiently leverages statistical information on nonzero elements, rather than on the entire sparse matrix. 
- On [[Knowledge graph completion]]: ^ef4955
	- Large-scale knowledge graphs also follow long-tail distribution. The entities and relationships of the long-tail distribution face serious data sparsity problem. 

---
## Reference

1. [[(Paper) Chen, Z., Wang, Y., Zhao, B., Cheng, J., Zhao, X., & Duan, Z. (2020). Knowledge Graph Completion, A Review. _IEEE Access_, _8_, 192435–192456]]