---
alias: [KGC]
---

- 28-9-2022: created

- superset:
	-[[ knowledge graph]]

- Historical progress
	- While before 2010s, the work treating representing graph structure as "pre-processing" work, and using hand-engineered statistics to extract structural information. (R4). 2010s, representation learning approaches treat "graph structure representation"  as machine learning task itself, using a data-driven approach to learn embeddings that encode graph structure.

- Current progress of knowledge graph completion: 
	- ![[Knowledge graph challenge#^50697e]]
- Goal:
	- Resolve incompleteness
		- While hand-engineered [[knowledge graph]] are assumed incomplete, the task of KGC is to complete the structure (nodes and edges) of knowledge graph by predicting the missing entities or relationships in knowledge graph and mining unknown facts. (R1) (R2)
	- Factoid question answering (my writing)
		- Considered as low-difficulty level of factoid question answering, such as, predicting tail nodes, given the relationship and head entity. (?, capitalOf, China) or predict the relationship between two nodes. 
	- Knowledge graph reasoning 

- Data model
	- [[Resource description framework|RDF]] (which I consider it as outdated, but the industry still dominantly using it to construct knowledge graph.)

- Model setting: (R3)
	- Vector representation:
		- For each entity and relation present in the knowledge graph a continuous vector representation $(h,r,t), h,t \in R^d, r \in R^k$, where $d$ is the embedding dimension for the entities, and $k$ for the relations.
	- Scoring function: 
		- The scoring function of a given model: $f_r(h,t)$ and measures the distance of the embedding of the head from the embedding of tail given the embedding of the relation. It quantifies the plausibility of the embedded representation of a given fact.  


- Descriptors of KGC models
	- Score function
	- Memory complexity
	- Constrains / Regularization
	- Characteristics 
	- Defects / Improvements

---
## Classification of KGC

- 1. Open versus closed
	- Open environment (dynamic) knowledge graph completion (R1)
		- Most of the current research focuses on knowledge graph completion in closed environment.
		- Probabilistic database theory -- the knowledge graph completion model in open environment provides a method to predict external entities and weakly connected entities.
		- Most [[knowledge graph|KG]] are constantly updated and expanded through linking external entities to [[adapt]] to the explosive growth of information.
		- Relatively difficult to establish a connection between the local knowledge graph and the outside world, due the the wide range of alternative knowledge.
	- Closed environment (static) knowledge (R1)
		- Applicable to the domain knowledge graph with small scale and slow update.
		- Does not make full use of external data for missing completion, resulting in insufficient information and strong limitation in usage. 
	- Dynamic updating (R1)
		- Data model layer
		- Data layer or adopting active learning strategies
- 2. Traditional KGC versus Deep representation learning
	- Infers the hidden information in knowledge graph
	- Traditional: (In my article, I should say "Deep could avoid hand-engineered features thus we don't focus on this....")
		- Rule-based reasoning method
			-  rely on a large number of effective and accurate rules and statistical features. 
			- Example:
				- OWL2RL (Semantic network inference rule)
				- KGRL (Knowledge graph completion model)
		- Probability graph model method
		- Graph-based and translation model-based multi-hop inference model
	- Deep representation
		- Main problem:
			- 1. Calculation efficiency
			- 2. Data [[Sparse|sparsity]]: ![[Sparse#^ef4955]]
			- thus, [[knowledge representation]] aims to express [[semantics|semantic]] information such as entities and relationships as dense low-dimensional real value vectors in a continuous vector space.
		- Main paradigm: (R1) 
			- 1) Represent relationships and entities in a continuous space
			- 2) Define the score function $f_r(h,t)$ to judge the probability of the establishment of triples $(h,r,t)$. The main difference between models lies in the difference of the score function.
			- 3) Learn the representation of entities and relationships, and solve the optimization problem of maximizing the rationality of visible facts. 
		- Translation model based method (R1)
			- It is the most representative classical method in knowledge representation learning
			- Relation patterns:
				- Symmetric (antisymmetric) relations
				- Inverse relations
				- Composition (transitive) relations
				- 1-to-N relations
			- [[Word2vec]]
			- [[Trans series models]]
		- Semantic matching model based method (R1)
			- Semantic matching model uses the score function based on semantic similarity to mine the potential semantic association between entities and relationships, by embedding the representation of entities and relationships in the vector space.
				- Score function
					- Intuition: can be viewed as [[Cosine product|cosine similarity]] between $h$, $r$ and $t$, where $h \cdot r$ defined as $\sum_i h_i \cdot r_i$.
				- $f_r(h,t) = \langle h,r,t \rangle = \sum_i h_i \cdot r_i \cdot t_i$ (R5)
				- $h,r,t \in R^k$ (R5)
			- It can obtain the possibility of new facts, so as to predict the new knowledge and complete the knowledge graph.
			- Models based on [[bilinear]] model:
				- Relations after [[bilinear]] transformation is used to describe the semantic connection between entity and relation, and to capture various interactions between data. 
				- KG is characteriszed by the correlation between multiple interconnected nodes, such as entity attribute categories and other hidden semantic information. 
				- Famous model
					- RESCAL
					- DistMult
		- Network representation learning method
		- Neural network model based method

![[Pasted image 20221101022710.png]]
- Fig: (R1)
	- h and t represents head and tail
	- The score function captures the underlying relationships between pairs of head-tail entities that are only in the same dimension. $f_r(h,t)$ is similarity function of $h$ and $t$.
	- 

![[Pasted image 20220921174232.png]]
- Fig: from (R5)

![[Pasted image 20221101021130.png]]
- Fig: Translation model performance
	- From (R1)

![[Pasted image 20221101021146.png]]
- Fig: Semantic matching model
	- From (R1)



---
### 3 main families of model (R3) 
- Tensor decomposition models
	- Uses a multi-dimensional matrix to represent a knowledge graph, that is partially knowable due to the gaps of the knowledge graph describing a particular domain thoroughly. 
	- These models use a "three-way" (3D) tensor, which is then factorized into low-dimensional vectors that are the entities and relations embeddings. 
	- it only records only the existence or the absence of a relation between entities. 
	- Characteristics
		-  It is simple structure
		- No need to know a "priori" the network structure
		- The class of embedding model lights, and easy to train even if they suffer from high-dimensional and sparsity of data. 

- [[Bilinear]] model
	- This family of models uses a linear equation to embed the connection between the entities through a relation.
	- The embedded [[representation]] of the relations is a bidimensional matrix. 
	- These models use the single fats to compute the embedded representation, and ignore the other associations to the same entity or relation. 
	- Types:
		- DistMult
		- ComplEx
		- ANALOGY
		- SImplE

- Non-bilinear model
	- Type
		- HolE
		- TuckER


- Geometric models
	- These models encodes the relations as a geometric transformation between the head and tail of a fact. To compute the embedding of the tail, it is necessary to apply a transformation $\tau$ to the head embedding, and a distance function $\delta$ is used to measure the goodness of the embedding or to score the reliability of the fact: $$f_r(h,t)=\delta(\tau(h,r),t)$$
	- Geometric models are similar to the tensor decomposition mdoel, but the main difference between the two is that they have to preserve the applicability of the transformation $\tau$ in the geometric space in which it is defined. 

- Pure transformation models
	- This class of model is inspired by the idea of translation invariance introduced in word2vec. 
	- A pure translation model relies on the fact tat the embedding vector of the entities are close to each other "after applying a proper relational translation in the geometric space," in which they are defined.
	- In other words, given a fact, when the embedding of head is added to the embedding of relation, the expected result should be the embedding of the tail.  (eg: H+R = T)
	- The closeness of the entity embedding is given by some distance measure and quantifies the reliability of a fact. 
	- Types:
		- TransE
		- TransH
		- TransR
		- TransD
		- TransA

- Translational models with additional embeddings
	- Associate additional information to each element in the knowledge graph and their common representation facts. 
	- Each entity and relation can be enriched with text descriptions, weights, constraints, and others in order to improve the overall description of the domain with a knowledge graph.
	- During the embedding of the knowledge graph, this information can be used to learn specialized embeddings for these characteristics together with the usual embedded representation of entities and relations, with the cost of learning a more significant number of vectors.
	- Types
		- TransE
		- CrossE

- Roto(Rotation-like)-translational models
	- TorusE
	- RotatE


- Deep learning models 
	- This family uses deep learning to learn patterns from the knowledge graph that are the input data.
	- These models have the generality to distinguish the type of entity and relation, temporal information, path information, underlay structured information
	- These models and resolve the limitations of distancebased and semantic-matching-based models in representing all the features of a knowledge graph
	- The use of deep learning for knowledge graph embedding has shown good predictive [[performance]] even if they are more expensive in the training phase, angry of data, and often required a pre-trained embedding representation of knowledge graph coming from a different embedding model.
	- Types
		- Convolutional neural networks
			- This family of models, instead of using fully connected layers, employs one or more convolutional layers that convolve the input data applying a low-dimensional filter capable of embedding complex structures with few parameters by learning nonlinear features.
			- Types:
				- ConvE
				- ConvR
				- ConvKB
		- Capsule neural networks
			- This family of models uses capsule neural networks to create a more stable representation that is able to recognize a feature in the input without losing spatial information.
			- The network is composed of convolutional layers, but they are organized in capsules, and the overall result of a capsule is sent to a higher-capsule decided by a dynamic process routine.
			- Types:
				- CapsE
		- Recurrent neural network
			- The advantage of this architecture is to memorize a sequence of fact, rather than just elaborate single events
			- Type
				- RSN


---
## Reference:

1. [[(Paper) Chen, Z., Wang, Y., Zhao, B., Cheng, J., Zhao, X., & Duan, Z. (2020). Knowledge Graph Completion, A Review. _IEEE Access_, _8_, 192435–192456]]
2. [[(Paper) Shi, B., & Weninger, T. (2018). Open-World Knowledge Graph Completion. _Proceedings of the AAAI Conference on Artificial Intelligence_, _32_(1).]]
3. [[(Wikipedia) Knowledge graph embedding]]
4. [[(Paper) Representation learning on graphs -- Methods and applications]]
5. [[(Course) CS224W - Machine learning with graphs (stanford)]]


