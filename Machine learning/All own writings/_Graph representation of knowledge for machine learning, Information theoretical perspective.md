---
category: []
alias: []
tags: []
---

- 28-10-2022 16:34: created

- [[Compress]]

- 30-10-2022:
	- "The connected path" represents how much representation we need, to get to the destination we want to get. "Bits" is an amount of information. (R1)

- Abstract
	- 1a. Existing knowledge graph completion techniques are far from complete and are growing at rapid pace. 
		- Six unresolved [[_All challenges|challenges]] to future progress of knowledge graphs. (1) Consistent theoretical frameworks, benchmarks and precise goal of graph representation learning, (2) Scalability, (3) Decoding higher-order motifs, (4) Model dynamic, temporal graphs, (5) Reasoning about large sets of candidate subgraph, (6) Improving interpretability. (R2)
	- 1b. No straightforward way to encode the high-dimensional non-Euclidean information about the graph structure into a feature vector. (R2)
		- Review 3 families of model for [[Knowledge graph completion]], [[node embedding|Knowledge graph embedding]]
		- In this paper, we will try to explore some alternatives of storing the edge types into nodes, tries to explore whether this method could train the [[knowledge graph]] effectively.
	- 1c. Current dominant knowledge graph models are overspent relation types, which is computational expensive and also disconnected from how human perceive knowledge. (my writing)
		- Review a list of graph representational learning frameworks 
		- Discuss the computational cost of different models. 
	- 1d. The implicit goal of the field is to service a specific set of classification benchmark, such benchmark does not connected within machine learning and data mining communities. (R2)
		- In this paper, the goal of graph representation learning is to generate coherent knowledge articles.

---
- Why graphs?
	- 1. Structured data which allow computers to process it. 
	- 2. Mathematically it is the most compact form?


---
## Hints / Insights that show 3Os is possible

- 1. Noun verb ratio
- 2. Compositional semantic parsing
	- Question: could compositional relationship and 1-to-N relationship could be parsed directly from the source.
- 3. Relational database
	- The schema of database is actually about 1-to-N etc and association etc.
- 4. Any supports of [[natural language processing|NLP]]?
	- How to represent 3Os in a single line? just like RDF --- 
		- Reading is relaxing
		- Tom reads books
		- ...
- 5. How 3Os model fits 4 types of relations 
	- Symmetric relations: 
		- $r(h,t) \Rightarrow r(t,h)$
		- eg, roommate, family
	- Antisymmetric relations, 
		- $r(h,t) \Rightarrow r(t,h)$
		- eg: "is divisible by"
	- 1-to-N relations
		- $r(h,t_1),r(h,t_2), \dots, r(h,t_n)$ are all true.
		- eg: $r$ is "Students Of"
	- Inverse relations
		- $r_2(h,t) = r_1(t,h)$
		- eg: Advisor and advisee
	- Composition relations
		- $r_1(x,y) \land r_2(y,z) \Rightarrow r_3(x,z), \forall x,y,z$
		- eg: my mother's husband is my father

![[Pasted image 20221101024451.png]]
- Fig: Noun verb ratio.
	- Source: R3

---
## Pipeline of old model

- 1. Collect RDF triples (those are first created by human users) (In reality, we don't have RDF triples )
- 2. Use those triples to connect a graph and run KGC algorithms.


---
## Pipeline of the new model

- 1. Treat entities and relationships as the same thing.
- 2. Collect their possible types (words like `convolution` and `parsing` -- could be verb or noun)
- 3. But things are going to be connected each others --- 
	- First stage: we use association between entity. 
- 4. Run vector representation of each of them once. (What is the loss function?) (Like word vector?)
- 5. 

---
## Roundup some related technical notes

1. [[machine learning]]
	1. [[Loss function]], [[Gradient descent]], [[Unsupervised learning]]
	2. [[feature learning|representation learning]], [[autoencoder]]
	3. [[Graph Convolutional Networks|GCN]]
		1. [[Message computation]]
		2. [[message passing]]
		3. [[directed]]
		4. [[Receptive field]]
		5. [[Heterogeneous graph]]
	4. [[Relational Graph Convolutional Networks]]
		1. [[Edge features]]
	5. [[knowledge graph]]
	6. [[scalable machine learning]]
2. [[Embedding]]
	1. [[Resource description framework|RDF]]
	2. [[GloVe]]
	3. [[Trans series models]]
		1. [[dimensionality#^eae603]], [[dimensionality reduction]]
	4. [[natural language processing|NLP]]
		1. [[co-occurrence]]
		2. [[semantic understanding]]
		3. [[parsing]]
		4. [[ambiguity]]
	5. [[Kernel space]]
	6. [[latent]]
	7. [[Matrix factorization]]
3. [[category theory]]
4. [[first order logic]]
5. [[computational cost]]
	1. [[Big-O notation]]
	2. [[asymptotic complexity]]
6. [[Performance]]
	1. [[State-of-the-art]]
	2. [[Compositionality]]



---
## Reference

1. [[(Paper) Information Theory-- A Tutorial Introduction]]
2. [[(Paper) Representation learning on graphs -- Methods and applications]]
3. https://www.researchgate.net/publication/301607770_Nounverb_Ratio_in_L1_Japanese_L1_English_and_L2_English_A_Corpus-based_Study



- Symmetric relations: 
	- $r(h,t) \Rightarrow r(t,h)$
	- eg, roommate, family
- Antisymmetric relations, 
	- $r(h,t) \Rightarrow \lnot r(t,h)$
	- eg: "is divisible by"
- 1-to-N relations
	- $r(h,t_1),r(h,t_2), \dots, r(h,t_n)$ are all true.
	- eg: $r$ is "Students Of"
- Inverse relations
	- $r_2(h,t) = r_1(t,h)$
	- eg: Advisor and advisee
- Composition relations
	- $r_1(x,y) \land r_2(y,z) \Rightarrow r_3(x,z), \forall x,y,z$
	- eg: my mother's husband is my father