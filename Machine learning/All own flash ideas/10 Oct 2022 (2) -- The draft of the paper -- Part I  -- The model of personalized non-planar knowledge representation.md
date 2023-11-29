- 10-10-2022: created

- Raising a concern for the whole paper:
	- Q: Is RDF triple an optimal way for constructing a knowledge graph? My intuition is No.
		- 1. Knowledge graph is a kind of network that bridge relationships between "concept". And RDF triple omits a lot of possible information when it is missing those "verb-Noun transition". 
			- eg: The ambiguity of the sentence "The goal is to optimize this mapping so that..." would be converted into `Is-a(Goal, Optimize mapping)`,  `Goal(Optimize, mapping)`.
			- eg: `Embedding` could be possibly a noun, or a verb (eg: `embedding` method)

- Problem:
	- The quantity of node types and edge types could be similar, and both of them could be expanded infinitely. 

- [[Performance]]
	- What is a good model?
		- A new branch model (If that is solving one problem that other model is also trying to solve.) should maintaining the performance of old models, and improving some other kind of aspects. 
		- But if a new model that solves a new problem don't have such requirements.

- Sections
	- 1. [[representation|representation]] Knowledge representation, Wayfinding, BFS/DFS, difficult concepts, heuristics, and quantifying what is a fast knowledge gathering process
	- 2. Roles of learners, teachers adding values to the knowledge structure
		- To shorten the number of steps jumping over each node. 
	- 3. [[knowledge graph]] technologies, [[Graph neural networks]], and their underlying paradigms
		- [[Unsupervised learning]] suppose the training data are also containing ground truth values thus it can be trained. So each of the full documents are equally important.  
		- The pipeline of creating [[knowledge graph]] from textual [[Data|data]]
			- From neo4j:
				- 1. [[Coreference resolution]]
				- 2. [[named entity recognition]]
				- 3. Datatype extractions 
				- 4. Relationship extractions (This step could be wrong!)
				- 5. Scale up those datatypes, relationships and entities to form up knowledges. 
		- Most researchers of [[Graph neural networks|GNNs]] assume the network of knowledge is a single big network 
	- 4. My proposing way to improve the knowledge structure
		- (a) Knowledge is incompressable
		- (b) Each [[document]] is a ground-truth value that we won't delete them in the process of learning. 
		- (c) The central GNN would be type
	- 5. Experiment setting:
		- (a) In each learning session we take a sampling 20 documents 
	- 6. [[25 Aug 2022 Problems of the current knowledge structure]]

- The difficulty of training with the framework of current [[knowledge graph]]
	- curse of dimensionality

- 6. My own model
	- a. Due to the fact that [[Resource description framework|RDF]] raises a lot of computational problems, for example   ###High dimensionality### raises the cost of training dramatically at the time we put more entities into the knowledge graph.
		- We restraint the flexibility of heterogeneous graph, we have such changing to the model:
			- 1. Relationships:
				- a. Reducing the number of possible types of edges.
					- from infinite labelled edges, to some mathematical relationships, like superset, subset (from same entity type
				- b. 
			- 2. Entities: 
				- (A) Subsets:
					- Allowing entities creating a tree of child entities. 
				- Distinct entity types: facts, functional models, qualities and attributes, problem patterns, implementations. 
				- Their formal definition (like how linguists define "formal language" in the [[(Book) Speech and language processing - Daniel Jurafsky (Stanford university)]] chapter 12.)
				- (B) Negations of qualities / entities
					- If such positive/negative entity pair could be detected, the map would be much smaller and effective. 
			- 3. [[downstream tasks|downstream task]] relationships: (Facts --> Models -->  Qualities and attributes) --> Problem pattern --> implementations
				- a set of fact/models can be connected to the same typed node. That is called abstraction
				- a set of facts/models can be connected to the different typed node. That node most likely be qualities and attributes.
			- 4. Regular micro-graph patterns
				- Like there always have attribute difference between two elements on the same set of fact-typed or model-typed similar nodes. 
				- Inference to the superset types: such as, if multiple "models" typed nodes points to one node + that node is listing out a list of similar models, then that node is likely an abstraction of those nodes, or that's an attribute/quality typed node.
				- More generally speaking, it is possible to create a set of 2D matrix for a set of element in the same set, that differentiate each element. 
					- eg: [[Word representation]] has elements [[Global matrix factorization methods]], and [[Global matrix factorization methods]] has element [[latent semantic analysis (LSA)]] and 
		- The role of neural network:
			- 1. Put entities into the right categories. 
			- 2. Generate abstract relations between entities. 


- Problems:
	- 23/10/2022
		- eg: "Instead of comparing manually-combined [[feature]] [[Data|data]], you can reduce the feature data to [[representation]] called embeddings." --> That is highly related to the entity [[dimensionality reduction]]. How to related them automatically?