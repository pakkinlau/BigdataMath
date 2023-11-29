- 16-8-2022: created

- [[Application of scholarship]]

- This page is specialized to store up the information from this course. For the bigger picture, I keep them in [[____ALL models (machine learning)]]

- [[L1.1 of CS224W (Introduction)]]
---
# Section 1 : The generalized content summary of cs224w slides

(Remark: The index should be related to week number. )

- Important formulas:
	- 1.1 Heterogeneous [[graph]] $G(N,T,R,E)$
		- Sized m adjacency matrix and $A_{ij}=1$ if there is a link between node $i$ and $j$.
		- (V/X) directed
		- (V/X) weighted
		- (V/X) ranked
		- (V/X) typed
		- (V/X) self-edge
		- (V/X) properties that depending on the neighboring structure 
	- 2.1 [[Loss function|loss function]] $L(y,f(z_u,z_v))$
	- 2.2 Node features: 
		- 2.2.1 Characterize the structure and position of a node in the network
			- Node degree
			- Centrality
				- Eigenvector centrality
					- node $v$ is important if surrounded by imported neighboring nodes $u \in N(v)$
					- $c_v = \frac{1}{\lambda} \sum_{u \in N(v)} c_u$, where $\lambda$ is normalization constant, will turn out to be the largest eigenvalue of $A$. 
					- Rewrite it in the matrix form: $\lambda c = Ac$.
						- $A$ is adjacency matrix
						- $A_{uv} = 1$ if $u \in N(v)$
				- Betweenness centrality
					- $c_v = \frac{1}{\sum_{u \neq v}\text{shortest path length between u and v}}$
				- Closeness centrality
					- $e_v = \frac{\text{number of (edges among neighboring ndoes)}}{\begin{pmatrix} k_v \\ 2 \end{pmatrix}} \in [ 0,1]$
			- Clustering coefficient
			- Graphlet degree vector
		- 2.2.2 Color refinement: $c^{(k+1)}(v)=HASH(\{c^{(i)}(u),\{c^{(k)}(u) \} , \forall u \in N(u)\})$, which $c^{(k+1)}(v)$ summarizes the structure of $K+1$ hop neighborhood.
	- 2.3 Edge features: a. Counting neighbors that 2 node shares b. Local overlap measures. c. Global overlap (random walk) measures
	- 2.4 Graph: Graphlets, Kernels $\phi(.)$ that calculates similarity: $K(G,G')$,  and it can be factorized, such that $K(G,G')=h_G^Th_G$.
	- 3.1 Encoders $f$ and embeddings $z$
		- [[encoder]]
		- a. Node Embedding that maps $f:u \rightarrow R^d :f(u) = z_u$.
		- b. Edge embeddings
		- c. Graph embeddings: $z_G = \sum_{v \in G}z_v$
	- 3.2 Feature decoder $g(z_v) \rightarrow \hat Y$
	- 3.3 $similarity(u,v)$ for loss function 
	- 4.1 Representation of embeddings
		- a. One-hot vector: $z=Zv$
		- b. Matrix factorization: $z_vz_u = A$
	- 4.2 Random walk log likelihood objective: $obj=max \sum_{u \in V} logP(N_R(u)|z_u)$
	- 5.1 Message passing: Feature prediction. Base classifier: $\phi_1(f_v)$, Relational classifier: $\phi_2(f_v,z_v)$.
	- 6 GNNs
	- 6.1 Revision of ANNs
		- 6.1.1 MLP: $x^{(l+1)}=\sigma(W_lx^{(l)}+b^l)$,
	- 6.2 GCN
		- 6.2.1 $0^{th}$ layer: $h_v^0=x_v$ and $B_kh_v^{(k)}$. B is the neuron weightings.
		- 6.2.2 $1^{st}$ layer: $h_v^{1} = \sigma(W_0\sum_{u \in N(v)}{h_u^{(0)} \over |N(v)|})$, which $|N(v)|$: Total number of of previous layer neighborhood node.
			- AGG() could be mean(), max() or avg().
			- MES() could be LSTM(), LRU() etc. 
		- 6.2.3 ${k+1}^{th}$ layer: $h_v^{(k+1)}=\sigma(W_k\sum_{u \in N(v)}{h_u^{(k)} \over |N(v)|} + B_kh_v^{(k)})$
		- 6.2.4 Final node embedding: $z_v = h_v^{(K)}$
	- 6.3 Matrix formulation 
		- Important, but skip it by now.
	- 6.4 Attention mechanism
	- 6.5 Unsupervised training: $L = \sum_{z_u,z_v}CE(y_{u,v},DEC(z_u,z_v))$, where $y_{u,v}=1$ when $u$ and $v$ are similar.
	- 6.6 Supervised learning $L= \sum_{v \in V}y_vlog(\sigma(z_v^T \theta))+(1-y_v)log(1-\sigma(z_v^T\theta))$, where $y_v$ is node class label
	- 6.7 Inductive capability: Aggregation parameters $B_k$ and Updating parameter $W_k$ are shared between compute trees. So that the trained algorithm are capable of reason/predict unseen graph/node/link. 
	- 6.8 GNNs subsume CNNs: the similarity in their formula. 
	- 6.9 GNNs versus transformers. 
	- 8 Graph augmentation
		- 1-hop neighbor: Adjacent matrix = $A$, 2-hop neighbor: Adjacent matrix = $A+A^2$.
		- Why constant node feature better than  one-hot node feature:
			- Less expressive, but simpler to generalize new node in inductive learning, lower computational cost, and more applicable to any graph use cases. 
		- Receiver operating cost (ROC)
	- 7. GNN stacking 
		- 7.1.1 Message: $m_u^{(l0)}=MSG^{(l)}(h_u^{(l-1)})$. $MSG(.)$ converts the prior layer message such that the message is capable of multi-set classification. (eg: $m_u^{(l)})=W^{(l)}h_u^{(l-1)}$.
		- 7.1.2 Aggregation $h_v^{(l)}=AGG^{(l)}(\{m_u^{(l)}, u \in N(v)\})$. $AGG(.)$ could be SUM(), Mean(), Max() aggregator. But information from node $v$ itself could get lost. 
		- 7.1.3 Aggregating itself inside the AGG() function: $h_v^{(l)}=CONCAT(AGG(\{m_u^{(l)}, u \in N(v)\}), m_v^{(l)})$.
		- 7.1.4 Non-linearity: Pack up in the final computation. $\sigma$: $ReLU$, $Sigmoid$, etc. 
		- 7.1.5 1-layer of GCN: $h_v^{(l)}=\sigma(\sum_{u \in N(v)} W^{(l)}{h_u^{(l-1) \over |N(v)|}})$. $W^{(l)}$ performs the message conversion, and the summation performs the aggregation. 
		- 7.1.6 GrphSAGE uses CONCAT())
		- 7.1.7 Different aggregation function: 
			- Aggregation: $Agg() = \sum$.
			- Pool: $Agg() = Mean(\{ MLP(h_u^{(l-1)}, \forall u \in N(v)\})$.
		- 7.1.8 Attention mechanism: 
			- Prerequsite: All the nodes are colored with a set of node/link features.(Written by me, is it true????)
			- 7.1.8.1 Attention weight: $e_{vu}=a(W^{(l)} h_u^{(l-1)},W^{(l)}h_v^{(l-1)})$, $a()$ is attention function that produce $e_{vu}$ that indicates the importance of $u$'s message. 
			- 7.1.8.2 Normalized attention weight: $\sum_{u \in N(v)} \alpha_{vu} =1$ and $\alpha_{vu}={exp(e_{vu}) \over \sum_{k \in N(v)} exp(e_{vk})}$
			- 7.1.8.3 Put it back to GNN layer and expand that , we have: $\sigma(\alpha_{AB}W^{(l)}h_B^{(l-1)}+\alpha_{AC}W^{(l)}h_C^{(l-1)}+\alpha_{AD}W^{(l)}h_D^{(l-1)}+\dots)$
			- 7.1.8.4 Multi-head attention
			- 7.1.8.5 Batch normalization
			- 7.1.8.6 Dropout 
			- 7.1.8.7 Stacking GNN layers and receptive fields.
			- 7.1.8.8 Skip connection
	- 7.2 Expressive power of a shallow GNN.
		- a. Increase parameters within each GNN layer, eg: 3-layer MLP within a box.
		- b. Add layers that do not pass messages (eg: Add MLP layers before and after GNN layers)
		- c. Add skip connections in GNNs (4 slides)
	- 8.1 Node level prediction: $\hat {y_v} = Head_{node}(h_v^{(L)})=W^{(H)}h_v^{(L)}$, for $\{h_v^{(L)} \in R^d, \forall v \in G\}$, with $Head_{node} = W^{(H)}$.
	- 8.2 Edge level prediction: $\hat {y_{uv}}=Head_{edge}(h_u^{(L)},h_v^{(L)})$. With $Head_{edge}$ could be concatenation + linear, or dot-product method that's similar to word vector space relations.
	- 8.3 Graph level prediction: 
		- Global pooling: $\hat {y_{uv}}=Head_{graph}(h_v^{(L)} \in R^d, \forall v \in G)$, and $Head_{graph}$ is similar to $Agg()$ in a GNN layer. 
		- Hierarchical global pooling
	- 8.4 Prediction effectiveness: Transductive > Inductive > Deductive, due to there are resolution loss from the generalization of inductive reasoning. 
	- 9 Expressiveness of a graph neural network
		- Most expressive GNNs are producing injective neighborhood aggregation function over multi-sets. Examples of multi-set are a set of ball, Y,B,B, for example. $f$ works out element-wise conversion (one-hot vector or constant node feature or others), and $\phi$ produces decision boundary for the neuron.
		- Infective: $f: X \rightarrow Y$ if it maps different elements into different outputs. 
	- 9.1 Injective multi-set function $\phi(\sum_{x \in S}f(x))$, which $\phi$ and $f$ are some non-linear function.
	- 9.2 Universal approximation theorem: 1-layer MLP with sufficiently-large hidden dimensionality and approximate non-linearity can approximate any continuous function to an arbitrary accuracy. In practice, MLP hidden dimensionality of 100 to 500 is sufficient.
	- 9.3 Graph isomorphism network (2019): $MLP_{\phi}(\sum_{x \in S} MLP_{f}(x))$.
	  10 Knowledge graphs
	- 10 Heterogeneous graphs
	- 10.0.1 Decoder for multi-relational embeddings (from GRL book): $DEC(u, \tau,v)=z_u^TR_\tau z_v$. (which $\tau \in R$ and $R$ is the set of relation type.) -- termed RESCAL by Nickel et all in 2011.
	- 10.0.2 Loss function: $\sum_{u \in V} \sum_{v \in V} \sum_{\tau \in R}||DEC(u,\tau,v)-A[u,\tau,v]||^2$, where $A \in R^{|V| \times |R| \times |V|}$ is the adjacency tensor for the multi-relational graph. If we want to optimize it, we would be performing tensor factorization. 
	- 10.1 Relational GCN (RGCN), node class prediction: 
		- $h_v^{(l+1)} = \sigma \sum_{r \in R} \sum_{u \in N_v^r}{1 \over c_{c,r}}W_v^{(l)}h_u^{(l)}+W_0^{(l)}h_v^{(l)}$, which $c_{v,r} =|N_v^r|$ (node degree of the relation).
	  - Recall 6.2.3 ${k+1}^{th}$ layer: $h_v^{(k+1)}=\sigma(W_k\sum_{u \in N(v)}{h_u^{(k)} \over |N(v)|} + B_kh_v^{(k)})$
	  - Message: 
		  - Each neighbor of a given relation: $m_{u,r}^{(l)}= {1 \over c_{v,r}}W_r^{(l)}h_{u}^{(l)}$.
		  - Self-loop: $m_{v}^{(l)}= W_0^{(l)}h_{v}^{(l)}$
	  - Aggregation (sum all messages):
		  - $h_v^{(l+1)}=\sigma(sum(\{m_{u,r}^{(l)}, u \in N(v)\} \lor \{m_v^{(l)}\}))$.
	  - RGN: Scalability
		  - Each relation has L matrices: $W_r^{(1)},W_r^{(2),\dots,W_r^{(L)}}$
		  - The size of each $W_r^{(l)}$ is $d^{(l+1)} \times d^{(l)}$, because relations are linking two entities. 
  - 10.2 Improves scalability
	  - 10.2.1: Block diagonal matrices: By limiting the interactions of nodes, dimensions reduces from $d^{(l+1)} \times d^{(l)}$ to $B \times {d^{(l+1)} \over B} \times {d^{(l)} \over B}$.
	  - 10.2.2: Basis / dictionary learning: represent the matrix of each relation as a linear combination of basis transformations:  $W_r = \sum_{b=1}^B a_{rb}V_b$,
  - 10.3 Relational GCN (RGCN), link class prediction
	  - 10.3.1: Find a pair of nodes as "training supervision edge" that going to be predicted, and "training message edge" that are going to send message to the training. 
	  - 10.3.2: To prepare the training, we use final layer node embeddings $h_v$ and 

![[Pasted image 20220921174232.png]]
- For W10: Figure: summary of some popular decoders used for multi-relational data (from p.42 of GRL book). 

---

- W1:
	- Why GNNs are different than other ANNs (GNNs are the generalized version of CNNs (small + large area message passing) and RNNs (self + neighbors message passing)) 
	- Graph representation learning 
		- (Heterogeneous G(N,T,R,E): Node(Type), Relation( Type)))
		- Adjacency matrix and adjacency list
		- Choice of edge attributes: (Y/N)directed, (Y/N)weighted, (Y/N)ranked, (Y/N)Type, (Y/N)Sign, (Y/N) Properties depending on the structure of the rest of the graph, (Y/N) Self-edge, (Y/N) Multigraph, (Y/N)Disconnected graph
	- Self-supervised learning 

- W2: 
	- Pipeline of graph learning
		- Step 1: train an ML model
			- Random forest, SVM, neural network
			- Connecting embeddings to node/link/graph to tune the embeddings. 
			- During the iteration (adding examples (SGD) + learning rate) of learning, embedding spaces would slowly change its own value to mimic the similarity value of all pairs of nodes in the graph. 
			- Loss function: $L(y,f(z_u,z_v))$. 
		- Step 2: apply the model
			- Obtain a tuned embeddings from a graph. And then inputs a new node/link/graph, predict its feature. 
	- Design of **effective feature** over graphs (What is effective?)
		- (W3) Effective
			- (W3) 1. GRL automatically learns the feature
			- (W3) 2. Efficient **task-independent** feature learning (how to achieve it?)
		- [[Node features, node statistics]]
		- [[Edge or relations or links level features]]
		- [[Graph level features (requires further study)]]
	- Pros and cons of hand-designed features
	- Objective function (What is it?)

- W3:
	- Goal of node embeddings
		- Graph position and structure of their local graph neighborhood.
		- Optimized embeddings in vector space reflect the relative position of the nodes in the original graph. 
	- Downside of manmade features in node/link/graph level
	- Graph with $ENC(v)$: embeddings, embeddings with $DEC(z_v)$: $similarity(u,v)$.
	- Different methods of embedding
		- Shallow (one-hot vector) encoding ($z=Zv$): 
			- simple but effective?
		- Random walk embeddings: (random walk of depth of K, how high the chance two nodes are co-occurring in the same path.)
			- Expressivity: Flexible stochastic definition incorporates both local and higher-order neighborhood information. 
			- Efficiency: Attention window on depth K -- No need to consider all node pairs when training 
	- Unsupervised feature learning
		- Nearby nodes definition: $N_R(u)$ -- neighborhood of $u$ obtained by some random walk strategy $R$. 
		- The goal is to learn mapping $f:u \rightarrow R^d:f(u)=z_u$ that maximize log-likelihood objective $obj=max \sum_{u i\in V} logP(N_R(u)|z_u)$ (Same idea as n-gram models of creating word vectors for words). In layman words, the goal of learn embedding vector space of a node that are predictive of its neighborhood nodes.
		  - In graph representation learning, neighborhood = relevant 
		- Equivalently, for the learning process,  $L = \sum_{u \in V} \sum_{v \in N_R(u)}-log(P(v|z_u))$. Notice -log(0.9) = 0.04, -log(0.2) = 0.70. As -log(x) approaches zero, the objective approaches 100%. 
	- Node similarity
		- Goal: Measure a set of coordinates of a node so that some aspect of the network structure is preserved. 
		- Choices:
			- 1. Self-supervised / unsupervised (no augments feed into it)
			- 2. (V/X) Augment with node/link/graph labels 
			- 3. (V/X) Augment with node features (graphlets and graph structure)
	- Techniques 
		- Negative sampling
		- Stochastic gradient decent
	- [[(library) node2vec]]
		- Biased second order random walk
		- Searching strategies: BFS, DFS
	- Embedding entire graph:
		- 1. $z_G = \sum_{v \in G}z_v$
		- 2. Introducing virtual node
		- 3. Anonymous walk embeddings (???)
		- 4. Hierarchical embeddings (Week 8)

- W4: Node importance
	- Node importance with random walk (page rank algorithm)
		- PageRank
			- Flow model, stochastic adjacency matrix M, rank vector r.
		- Personalized page Rank (PPR)
			- 
		- Random walk with restarts
	- Obtain node embeddings with matrix factorization (MF)
		- Different than one-hot vector method $z=Zv$, now uses $z_vz_u=A$.
		- Node embeddings based on random walks can be expressed as matrix factorization
	- View other node embeddings as MF
	- Application: websites as uni-directed graph.

- W5: Message passing
	- Semi-supervised node classification 
---

# Section 2: Detailed notes

### Lecture 1: 

- Why graphs?
	- Graphs are general language for describing and analyzing entities with relations / interactions. 
	- Complex domains have a rich relational structure, represented as a relational graph. By explicitly modeling relationships, we achieve better performance. 
	- [[Example types of graphs of data]]
- Why GNN are different than other ANNs
	- Graphs are much harder to process because they are more complex.
		1. Graphs topology/structure are "complex" mathematically, and it has arbitrary size
		2. Absence of reference points: 
			- Modern deep learning toolbox is designed for simple sequences and grids.
			- No spatial locality as in graphs (2D grids) or as in text (1D grid). But in networks, there is no reference point or any notions of spatial locality. 
		3. Absence of fixed node ordering 
			- There is no fixed node ordering that allow us to do deep learning.
		4. Dynamic (keep updating) nature
			- Often these networks are dynamic and have multi-model features. 
- An attempt: N layer graph convolution
	- With N layer convolution, we could get predictions of :
		- node labels
		- new links
		- generated graphs, subgraphs
		- property of a given molecule
- Research interest: 
	- ICLR keyword growth 2018-2020: GNN is the most trending area. 
- Pipeline of Graph learning
	- 1. Raw data
	- 2. Graph data (produced without feature engineering) (representation learning that automatically learn the features instead)
	- 3. Learning algorithms
	- 4. Model that works on the downstream prediction tasks
- [[Toolbox for cs224w GNN learning ]]
- Representation learning versus "feature engineering"
- Graph ML tasks
	- CS224W - Cases of different level of tasks
		- Node classification
		- Link prediction
		- Graph classification
		- Clustering
		- Graph generation
		- Graph evolution
- Choice of graph representation
	- 1. Heterogeneous systems G(N, E, R, T)
		- Objects with node type N,  Node type T
		- Interactions with relation types E, Relation R
		- Levels of abstraction: 
			- Solid object (specific person) --> Abstract object (a Chinese) --> Node type (A human)
			- Concrete Relationship --> Abstract relationship
	- Choice of proper network representation of a given domain, determines our ability to use networks successfully. 
	- 2. Adjacency matrix
		- M x M sized and $A_{ij}$ = 1 if there is a link to node $i$ to node $j$. M is the total number of unique node. $A_{ij}$ =0 otherwise.
		- [[Sparse graphs ]]
	- 3. Bipartite graphs (authors to papers, actors to movies)
		- [[Folded bipartite graphs]]
	- 4. Adjacency list (large and sparse network)
- Choice of edge attributes
	- 1. Undirected versus directed
		- Collaborations, friendships on facebook
		- Phone calls, following on twitter
	- 2. Weight (eg: frequency of communication)
		- $A_{ij}$  can allow any value that is outside of  $(1,0)$ .
	- 3. Ranking (eg: best friend, second best friend)
	- 4. Type (friend, relative, co-worker)
	- 5. Sign (Friend/foe, trust/distrust)
	- 6. Properties depending on the structure of the rest of the graph: (number of common friend)
	- 7. Self-edge(undirected)
		- Diagonal blocks of the adjacency matrix$A_{ii}$ could be non-zero now.
	- 8. Multigraph(undirected)
		-  $A_{ij}$  can allow any value that is outside of  $(1,0)$ .
	- 9. Connected and disconnected graph
		- Strongly connected (two ways) and weakly connected (disregard edge directions)
		- SCC (Strongly connected components)

![[Pasted image 20220915153642.png]]
- Figure: The pipeline of graph learning. Human-involved features

![[Pasted image 20220915153549.png]]
- Figure: Each node are represented as "d-dimensional embeddings".

---
### Lecture 2 
- Graph ML pipeline
	1. Train an ML model
		- Random forest, SVM, neural network etc.
		- Connecting embeddings to node/link/graph features to tune the embeddings. 
	2. Apply the model
		- Given a new node/link/graph, extracting features from different levels, and then make predictions. 
- Feature design
	- Using **effective features** over graphs is the key to achieving good model performance.
	- Traditional: Hand-designed features.
- Objective function
	- Node/edge level prediction: 
		- Given $G = (V,E)$, which V/E are vertices/edges. We learn a function that could have embeddings R ( $f: V/E \rightarrow R$.) such that with $R$ we can predict features for a new node / edge.
- (Effective) features for graph representation learning
	- [[Node features]], [[Node-level statistics]]
		- Node level prediction: labels of nodes
		- Features: node degree, node centrality, clustering coefficient, graphlets.
	- [[Edge features]]
	- [[Edge or relations or links level features]]:  
		- Link level prediction: new links / missing links at random (remove a random set of links and aim to predict them), growing links over time. 
		- At test time, node pairs (with no existing links) are ranked, and top K node pairs are predicted.
		- Features: 
			- Proximity (distance-based) features, local/global neighborhood overlap
	- [[Graph level features (requires further study) ]]
		- Prediction:
		- Features: 
			- Graph feature vector 
				- Bag-of-nodes/bag-of-word, graphlets and path-based methods.
			- Kernel methods: design kernels instead of feature vectors
				- Weisfeiler-Lehman kernel, Graphlet kernel

![[Pasted image 20220915162250.png]]
- Figure: $x_N$ represents the embedding for a specific node/link/graph. $y_N$ represent a feature of a node/link/graph. Each embedding $x_i$ could serve a prediction task for its feature $y_i$. 

![[Pasted image 20220915161611.png]]
- Figure: traditional ML pipeline. 
- Traditionally ML uses hand-designed features. But that is not scalable so we won't use that. We use embeddings instead. We need to collect a certain number of sample to create effective embeddings.

---
### Lecture 3 Node embedding

- Goal of node embeddings:
	- Summarize their graph position and the structure of their local graph neighborhood. 
	- In other words, we want to project nodes into a latent space, where geometric relations in this latent space correspond to relationships (edges) in the original graph or network.
	- These embeddings are optimized so that distances in the embedding space reflect the relative positions of the nodes in the original graph.

- In GNN, we at all cost trying to avoid manmade features in node/edge/graph level. 
- Graph representation learning 
	- GRL automatically learns the feature, alleviates the need to do feature engineering every single time. 
	- Goal: efficient task-independent feature learning for machine learning with graphs.
	- Embedding spaces would slowly change its own value to mimic the similarity values of all pairs of nodes in the graph. 
	- Flow: 
		- Node/Links/Graphs feature, (with labels, or graph structure) --> Encoder ENC(v) --> Embeddings $z_v$ --> $DEC(z_v)$ --> $similarity(u,v)$ score -->Loss function  $L(y,f(z_u,z_v))$.
	- Components
		- Encoder: 
			- Maps from nodes to embeddings to get $z_v$.
			- $ENC(v) = z_v$, which $z_v$ is a d-dimensional embedding.
		- "Shallow" encoding (simplest)
			- The simplest version encoder ("one-hot vector" with a embedding lookup matrix): 
				- It is just an embedding lookup. $z_v = Zv$ , which Z is a matrix each column is a node embedding. v is an one-hot indicator vector, each zeroes except a one in column indicating node v. 
				- If the graph has |V| nodes, and we assume each single node has a d-dimension embedding.  Then the lookup table Z has $d \times |V|$ dimension, i.e. $Z \in R^{d \times |V|}$. 
				- One-hot vector is multipled into the Z, and then the a 1 x d sized strip of data is selected from Z. That brings us back the embeddings for the node.
		- Similarity function: 
			- It works on vector space, that map to the relationship in the original network.
		- Decoder:
			- DEC() maps from embeddings to the similarity score, and the similarity score can be defined without the embeddings. 
			- Decoder DEC() candidate: Inner product / dot product between node embeddings. 

![[Pasted image 20220915232049.png]]
- Figure: 2D embeddings (after PCA) of nodes of the Zachary's Karate Club network.

![[Pasted image 20220915232212.png]]
- Figure: The bridge between the graph and the embedding space, that outlines the representation learning model. 

---


- Node similarity:
	- Intuition:
		- 1. Are A and B node linked? 2. Are A and B node share neighbors? 3. Are A and B node have similar "structural roles"?
		- The goal is to directly measure a set of coordinates of a node so that some aspect of the network structure is preserved.
		- The embeddings are "task independent". They are not trained for a specific task.
	- Choices: 
		- Unsupervised / self-supervised
		- Utilize / not-utilize node labels
		- Utilize / not-utilize node features (graphlets / graph structure)
		- The goal is to directly measure a set of coordinates of a node so that some aspect of the network structure is preserved.
	- In W3, we introduce node similarity based on:
		- From graph: Random walks / Node proximity
			- Question: How about learning edges, graphs?
		- From embeddings: Matrix factorization: $A=similarity(z_u,z_v)=z_v^Tz_u$
			- Question: How about label is unavailable and we need to have unsupervised learning?


- $N_R(u)$ / $N$: 
	- Neighborhood of u obtained by some random walk strategy R.

- Random-walk embeddings (Graph node similarity)
	- Definition: Given a graph and a starting point, we select a neighbor of it at random. 
	- Random walk on the graph = The sequence of points visited
	- Similarity $z_u^Tz_v$ = probability that u and v co-occur on a random walk over the graph.
		- eg: u and v is a neighbor, u has 4 connectivity. then the similarity of u and v > 0.25. The shortest path brings up 0.25. and it could also be possible that other sideways could link up u and v.
	- Why random walks
		- 1. Expressivity: Flexible stochastic definition of node similarity that incorporates both local and higher-order neighborhood information. (express as: if from u visit v with high prob, u and v are similar.)
		- 2. Efficiency: Do not need to consider all node pairs when training, only need to consider pairs that co-occur on random walks.

- Unsupervised feature learning
	- Idea: 
		- Find embedding of nodes in d-dimensional space preserves similarity. --> Learn node embeddings such that nearby nodes are close together in the network.
		- Goal: Learn a mapping function f that $f:u \rightarrow R^d : f(u):z_u$,
	- Prob. representation of u visit v: $P(v|z_u)$
		- Intuition: Optimize embedding $z_u$ to maximize the likelihood of random walk co-occurrences. 
		- Running "short fixed-length" random walks starting from each node on the graph. 
		- Log-likelihood objective (???):
			- $$max_f \sum_{u \in V}logP(N_R(u)|z_u)$$, which $N_R(u)$ is the neighborhood of node u by strategy R.
			- For each node u collect $N_R(u)$, the multiset of modes visited on random walks starting from u.
			- equivalently, the similarity for 2 graphs: $$L = \sum_{u \in V} \sum_{v \in N_{R(u)}} -log(P(v|Z_u))$$, which the first sigma sums over all nodes u, and the second sigma sums over nodes v seen on random walks starting from u, and the log(x) term predict probability of a single u and v co-occurring on a random walk.
		- Parameterize $P(v|z_u)$ using softmax: $P(v|z_u)={exp(z_u^Tz_v) \over {\sum_{n \in V}ex(z_u^Tz_n)}}$. We want node $v$ to be most similar to node $u$. Intuition: $\sum_{i}exp(x_i)$ close to $max_i exp(x_i)$.
		- Put all together, $$L = \sum_{u \in V} \sum_{v \in N_{R(u)}} -log({exp(z_u^Tz_v) \over {\sum_{n \in V}ex(z_u^Tz_n)}})$$
	- But doing this is expensive. Nested sum over nodes gives $O(|V|^2)$.
	- Computation techniques:
		- 1. Negative sampling
			- Breaking down the idea:
				- a. negative = in NLP, negative sampling means choosing the wrong context word that speed up the training. 
				- b. sampling = take random samples over all candidates. 
			- Instead of normalizing w.r.t. all nodes, just normalize against k random "random samples" $n_i$.
			- $log({exp(z_u^Tz_v) \over {\sum_{n \in V}ex(z_u^Tz_n)}})$ could be approximate to $log(\sigma(z_u^Tz_v))-\sum_{i=1}^k log(\sigma(z_u^Tz_{n_i}))$,$n_i$~$P_v$, which $\sigma$ is chosen to be sigmoid function. and $n_i$ is random distribution over nodes. 
		- Stochastic gradient descent (SGD): Instead of evaluating gradients over all examples, evaluate if for each individual training example.

- Node2vec:
	- Embed nodes with similar network neighborhoods closer in the feature space. 
	- Observation: Flexible notion of network neighborhood leads to rich node embeddings. 
	- Develop biased second order random walk R to generate network neighborhood of node u.
	- Two classic strategies:
		- BFS: Local microscopic view
		- DFS: Global microscopic view
	- Biased random walk:

- Embedding entire graphs
	- Approach 1 (Simplest): $$z_G= \sum_{v \in G}z_v$$
	- Approach 2: Introduce a virtual node to represent the graph and run a standard graph embedding technique.
	- Approach 3: Anonymous walk embeddings
	- Approach 4: Hierarchical embeddings (week 8)

![[Pasted image 20220916012231.png]]
- Figure: node2vec algorithm

![[Pasted image 20220916012649.png]]
- Figure: Hierarchial embeddings

---
### Week 4 - page rank (aka google algorithm)
- Websites as a [[directed]] (because hyperlinks is one directional) graph (Broder et al. 2000)
- All web pages are not equally important.
- Link analysis
- [[Page rank algorithm]] solves $r=Mr$ where $r$ can be viewed as both the principle eigenvector of M and as the stationary distribution of a random walk over the graph.
- Random walk with restarts and presonalized [[Page rank algorithm]].
	- Goal: proximity on graph 
	- A [[bipartite]] graph representing user and item interaction. --what items should we recommend to a user who interacts with item Q?
	- Intuition: [[Clustering]] matching -- If item P and Q are interacted by similar user, then we recommend P when user interacts with Q. 

- [[Matrix factorization]] for [[node embedding]]
	- For an edge, $z_v^Tz_u=A_{u,v}$. Which is the $(u,v)$ entry of the graph.
	- Recall  [[Adjacency matrix]] represents the connection between different nodes. 
	- We fill in each of it into the [[adjacency matrix]] of the graph. We get $Z^TZ=A$.
	- [[objective]]: minimize $|A-Z^TZ|$, 
		- The goal to approximate A with $Z^TZ$. So it is similar to factorize A.
	- Deepwalk has a more complex node similarity definition:$$log(vol(G)({1 \over T}\sum_{r=1}^T(D^{-1}A)^rD^{-1})-logb$$, which volume of graph $vol(G)=\sum_i \sum_j A_{i,j}$, context window size $T=N_R(u)$, $r$ is the power of normalized adjacency matrix. and $logb$ is the number of negative samples, and diagonal matrix D is $D_{u,u} = deg(u)$.
	- Refer to the paper for more details: "Network Embedding as Matrix Factorization: Unifying DeepWalk, LINE, PTE, and node2vec, WSDM 18".

- Limitations
	- 1. Cannot obtains embeddings for nodes not in the training set
	- 2. Cannot capture structural similarity --> Deepwalk and node2vec  do not capture structural similarity.
	- 3. Cannot utilize node, edge and graph features. (eg: protein properties in a protein-protein interaction graph) --> Solution: GNN

---
### Lecture 5 - message passing 

- Given a network with labels on some nodes, how do we assign labels to all other labels to all other nodes?
	- eg: some nodes and fraudsters and some are trusted, in a social network. How do you find other good or bad guys. (L3 technique: node feature and prediction (node classification) with node level embeddings)
- Intuition: 
	- Correlations (dependencies) exist in networks. In other words, similar nodes are connected. 
		- eg: homophily (similar individual characteristics leads to social connections) 
		- eg: influence social connections leads to similar individual characteristics) 
	- Collective classification: assigning labels to all nodes in a network together.
- Leverage node correlations in networks
	- 1. Guilt-by-associations: if A is connected with B with label X, then A is likely to have label X as well.
	- 2. Classification label of a node v based on: 
		- feature v, 
		- labels of nodes in v's neighborhood 
		- features of nodes in v's neighborhood

- Semi-supervised node classification
	- Given labels of some nodes, predict labels of unlabeled nodes.

- Three techniques
	- Relational classification
	- Iterative classification
	- Correct & smooth

- Relational classification (???)
	- Idea: propagate node labels across the network
	- For labeled node v, initialize label $Y_v$ with ground-truth label $Y_v^*$. For unlabeled nodes, initialize $Y_v$ = 0.5. 
	- Update all nodes in a random order until convergence or certain iterations is reached.
	- Update formula for each node v and label c (eg: 0 or 1): $$P(Y_v=c)={1 \over { \sum_{(u,v) \in E} A_{v,u}}} \sum_{(v,u) \in E} A_{v,u}P(Y_u=c) $$, which $A_{u,v} = z_v^Tz_u$ is the similarity of two nodes. $P(Y_u =C)$ represent the label of v's neighbor, which could be 1 or 0 if it has labelled. It is 0.5 if it is not labelled.  

![[Pasted image 20220916031427.png]]
- Figure: first iteration of relational classification that update the label for node 3, by referring to its neighbor's label.


- Iterative classification
	- Relational classifier does not use "node attributes"
	- Iterative classification: classify node v based on its attributes $f_v$ as well as label $z_v$ of neighbor set $N_v$.
	- Given $f_v$: feature vector for node v, and some nodes v are labeled with $Y_v$, and labels $z_v$, predict label of unlabeled nodes with two classifiers
		- 1. Base classifier:  $\phi_1(f_v)$: predict node label $Y_v$, based on node feature vector $f_v$. 
		- 2. Relational classifier: $\phi_2(f_v,z_v)$: predict label $Y_v$, based on node feature vector $f_v$ and $z_v$ (summary of labels of $v$'s neighbors).
	- Computing $z_v$ (summary of labels of v's neighbors)
		- $z_v$ = vector that captures labels around node $v$.
			- Histogram of the number of each label in $N_v$.
			- Most common label in $N_v$
			- Number of different labels in $N_v$.
	- Architecture of iterative classifiers
		- 1. Train base and relational classifier
		- 2. Iterate till convergence
			- $\phi_1$ --> update labels $Y_v$ --> compute $z_v$ --> predict labels with $\phi_2$ --> update labels $Y_v$.
	- Example: web page classifications
		- Input: graph of webpages
		- Node: webpage
		- Edge: hyperlink between webpages
		- Node features: webpage description
		- Task: predict the topic of the webpage


- Correct and smooth
	- 2021 release model 
	- Recent state-of-the-art collective classification method
	- Setting: A partially labeled graph and features over nodes
	- Base predictor: It can by a simple linear model / multi-layer-perception (MLP) over node features
	- Soft labels (class probabilities)
	- 3-step procedures:
		- 1. Train base predictor
		- 2. Given a trained base predictor to predict soft labels of all nodes, to obtain soft labels for all the nodes, and we expect soft labels to be decently accurate. 
		- 3. C&S uses the 2 step process to post-process the predictions using graph structure to obtain the final predictions of all nodes. 
			- Correct step: expect errors in the base prediction to be positively correlated along edges in the graph
			- Smooth step: the predicted soft labels may not be smooth over the graph. 

- Diffusion matrix $\tilde A$ 

---
### Week 6 - GNN(1) 

![[Pasted image 20220916034022.png]]
- Figure: The illustration of GNN. Node embeddings are located closely that is representing the node/link/graph feature similarity of the node in the graph.


- Recall: Shallow encoders
	- Limitations:
		- 1. O(|V|) parameters are needed: No sharing of parameters between nodes. Every node has its own unique embeddings. (We will see how GNN/GCN solves this problem )
		- 2. Inherently transductive: cannot generate embeddings for nodes that are not seen during training (We will see how GNN/GCN solves this problem )
		- 3. Do not incorporate node features: nodes in many graphs have features that we can and should leverage.  (We will see how GNN/GCN solves this problem )
	- Deep graph encoder
		- Step 1: Graph convolution
		- Step 2: Activation function
		- Step 3: Regularization (eg: dropout)
		- Step 4: Loop step 1 to 3 once again.

---
- Permutation invariance
	- We need to design a GNN model that would produce a prediction result that won't be affected by the ordering of node/edge data. 
	- Idea:
		- Design GNN that are premutation invariant / equivariant by "passing and aggregating information from neighbors".
		- Passing information across the graph the compute node features. 


![[Pasted image 20220916173658.png]]
- Figure: The problem of  input ordering in the calculation of the prediction output. (After N times of 2-ways propagation. )

- Neighborhood aggregation: Passing neighborhood information to the node. 
![[Pasted image 20220916174242.png]]
![[Pasted image 20220916175112.png]]
- Figure: Step 1: Determine node computation graph by BFS and return all nodes that within arbitrary depth. Step 2: Propagate and transform information back to the node. Step 3: Every node defines a computation graph based on its neighborhood. Step 4: Determine the activation function for each layer in these computation graph.

- First two layers: 

![[Pasted image 20220916182627.png]]
- 0th layer (node itself): 
	- $$h_v^0=x_v$$
- 1st layer:
	- The NN look at its own value, also look at the value of nodes that is depth=1 away from itself.
	- Value of the center node: $$B_kh_v^{(k)}$$
	- Value of the neighbor node that is depth =1 away: $$\sigma(W_0\sum_{u \in N(v)}{h_u^{(0)} \over |N(v)|})$$, which $|N(v)|$: Total number of of previous layer neighborhood node. (Integer)
	- Adding them up, we obtain: $$h_v^1=\sigma(W_0\sum_{u \in N(v)}{h_u^{(0)} \over |N(v)|} + B_0h_v^{(0)})$$
	- Total number of hidden unit: $1$
2nd layer (k=2):
- We can observe there is a recursive pattern in receiving information from the graph.
- The formula becomes: $$h_v^2=\sigma(W_1\sum_{u \in N(v)}{h_u^{(1)} \over |N(v)|} + B_1h_v^{(1)})$$
- Total number of hidden unit: $|N(v)|+1$
	- $|N(v)|$ : (each prior layer has 1 neuron
	- $1$ : (for the current layer)
- 3rd layer:
	- Total number of hidden unit: $|N_2(v)| (|(N_1(v)|+1)+1$
	- If each layer has same number of neighbor, the number of hidden unit: $N^2+N+1$
- $k+1$ layer:
	- $$h_v^{(k+1)}=\sigma(W_k\sum_{u \in N(v)}{h_u^{(k)} \over |N(v)|} + B_kh_v^{(k)})$$
- Final node embedding:
	- $$z_v = h_v^{(K)}$$
---
- Matrix formulation
	- Concerning: $W_k\sum_{u \in N(v)}{h_u^{(k)} \over |N(v)|}$. How to compute $W_kh_u^{(k)}$ efficiently.
	- Idea: many aggregations can be performed efficiently by (sparse) matrix operations
	- Setup:
		- $H^{(k)}=[h_1^{(k)} \dots h_{|V|}^{(k)}]^{T}$
		- Recall: $z_v^Tz_u=A_{u,v}$, which $z_i$ are node embeddings, $A_{i,j}$ is similarity matrix. 
		- $\sum_{u \in N(v)}{h_u^{(k)}}=A_{v,:}H^{(k)}$
		- Diagonal matrix $D_{v,v}=Deg(v)=|N(v)|$
		- Inverse of D also diagonal thus: $D_{v,v}^{-1}=1/|N(v)|$
		- Therefore we obtain: $\sum_{u \in N(v)}{h_u^{(k)} \over |N(v)|}=H^{(k+1)}=D^{-1}AH^{(k)}$
		- Rewriting the updating function, we have: $$H^{(k+1)}=\sigma(\tilde AH^{(k)}W_k^T+H^{(k)}B_k^T)$$, where $\tilde A = D^{-1}A$

---
- Transferring / Inductive capability
	- The same aggregation parameters are shared for all nodes (Why?)
		- The number of model parameters is sublinear in $|V|$ and we can generalize to unseen nodes (why?)

![[Pasted image 20220917043825.png]]
![[Pasted image 20220917044055.png]]
- Figure: We can make prediction for the node we never trained on.  (Why?)


---
- GNNs subsume CNNs
	- CNN can be seen as a special GNN with fixed neighbor size and ordering.
		- The size of the filter is pre-defined for a CNN.
		- The advantage of GNN is it processes arbitrary graphs with different degrees for each node.
		- Switching the order of pixels will leads to different outputs. 



- GNNs and transformers
	- Transformer is one of the most popular architectures that achieves great performance in many sequence modeling tasks.
		- Self-attention: Every token attends to all the other tokens/words via matrix calculation.
		- Transformer layer can be seen as a special GNN that runs on a fully-connected word graph.

---
- GNN framework summary
	- 1. Message
	- 2. Aggregation
	- 3. Layer connectivity
	- 4. Graph augmentation
	- 5. Learning objective

![[Pasted image 20220917045314.png]]
- Figure: Summary of GNN framework

---
### Week 7


- A single layer of GNN:
	- Idea:
		- Compress a set of vectors into a single vector
	- 2 steps: 
		- Message: 
			- Each node will create a message, which will be sent to other nodes later.
			- $m_u^{(l)}=MSG^{(l)}(h_u^{(l-1)})$
		- Aggregation:
			- Each node will aggregate the message from node's neighbors.
			- $h_v^{(l)}=AGG^{(l)}(\{m_u^{(l)}, u \in N(v) \})$
			- $AGG()$ could be sum(), mean(), or max() aggregator.
			- Issue:
				- Information from node $v$ itself could get lost. $h_v^{(l)}$ does not directly depend on $h_v^{(l-1)}$  --> 
			- Solution: 
				- 1. Include $h_v^{(l-1)}$ when computing $h_v^{(l)}$.This idea is similar to RNN. And the problem of this kind of design is, this will exponentially increase the cost of computation. 
				- 2. Include the message from center node itself. This idea is also very similar to RNN which is ingesting one text per neuron in some text processing NN.
	- Nonlinearity (activation): 
		- Adds expressiveness. Candidates are sigmoid, ReLU, etc.
		- Can be added to message or aggregation.
	- Different instantiations under this perspective
	- GCN, GraphSAGE, GAT,...

- GraphSAGE (slide 476, Week 7):
	- LSTM: $$AGG = LSTM([h_u^{(l-1)}, \forall i \in \pi(N(v))])$$, which $LSTM()$ reshuffle neighbors. 
	- Pool: max() or max() to transform neighbor vectors
	- L2 normalization
	- Graph attention:
		- Idea:
			- Not all node's neighbors are equally important. Attention is inspired by cognitive attention. 
			- The NN should devote more computing power on that small but important part of the data. 
			- Uses storage capacity for the exchange of computing speed. 
		- $$h_v^{(l)}=\sigma \sum_{u \in N(v)} \alpha_{vu}W^{(l)}h_u^{(l-1)}$$, which $\alpha_{vu}$ is the attention weight. In GCN / GraphSAGE, $\alpha_{vu} = {1 \over |N(v)|}$
		- Attention coefficient $e_{vu}=a(W^{(l)} h_u^{(l-1)},W^{(l)}h_v^{(l-1)})$ across pairs of nodes $u,v$ based on their messages.
			- Normalize $e_{vu}$, we have $\alpha_{vu}$: 
			- $$\sum_{u \in N(v)} \alpha_{vu} =1$$. $$\alpha_{vu}={exp(e_{vu}) \over \sum_{k \in N(v)} exp(e_{vk})}$$
		- Weighted sum based on the final attention weight: And $\alpha_{vu}$ is a vector. Expand it we get back $h_A^{(l)}$ = $\sigma(\alpha_{AB}W^{(l)}h_B^{(l-1)}+\alpha_{AC}W^{(l)}h_C^{(l-1)}+\alpha_{AD}W^{(l)}h_D^{(l-1)})$.
		- Question: 
			- If Wk and Bk are shared, how alpha(attention) works assign attention correctly?

![[Pasted image 20220917052111.png]]
- Figure: Illustration of graph / node attention 

- Benefits of attention mechanism
	- 1. Computationally efficient
	- 2. Storage efficient: Spare matrix operations do not require more than $O(V+E)$ entries to be stored. 
	- 3. Localized: Only attends over local network neighborhoods
	- 4. Inductive capability: edge-wise mechanism, it does not depend on the global graph structure. 

- GNN layer in practice (slide 489)
	- Deep learning modules can be incorporated into a GNN layer:
		- BatchNorm: stabilize neural networks training
		- Dropout: regularize a neural net to prevent overfitting
		- Activation (non-linearity)
		- Attention/Gating
		- More

- Skip connections
	- Worth learning 

---
- Stacking layers
	- GNN suffers from the "over-smoothing problem": All the node embeddings converge to the same value. 
	- Why over-smoothing happen?
		- Receptive field: the set of nodes that determine the embedding of a node of interest. 
		- Shared neighbors quickly grows when we increase the number of hops. 

- Receptive field
![[Pasted image 20220917052850.png]]
- Figure: Illustrating the growing overlapping neighbor
---
Week 8: Graph augmentation

- Graph augmentation
	- Idea: 
		- 1. Before week 8, We assume raw input graph is not computational graph, but we are going to break this assumption. 
			- Problem: The input graphs most probably leaks features
				- Graph structure: 
					- if the graph is too sparse --> inefficient message passing (information depends on depth and neighbors)
					- if the graph is too dense --> message passing is too costly (why???)
					- if the graph is too large --> the graph cannot fit the computational graph into a GPU.
		- 2. Stacking too many GNN layers --> GNNs suffers from the over-smoothing problem, and all the node embeddings converge to the same value. (It is the same as the vanishing problem in Deep neural network.)

		- Augmentation:
			- If lacks feature --> Feature augmentation
				- Why we need feature augmentation
					- 1. Input graph does not have node features
						- (Solution: "Standard" labelling techniques)
					- 2. Certain structures are hard to learn by GNN (eg: cycle count feature, eg: node in a triangle that's cycle with length = 3, cannot differentiate with another node in a rectangle, that's cycle with length = 4, and also a cycle with infinite length).
						- (Solution: use cycle count as augmented node features.)
						- Other commonly used augmented features:
							- Node degrees
							- Clustering coefficient
							- PageRank
							- Centrality

			- Further discussion of other augmentations for sparse graph: 
				- 1. Adding virtual edges (1 hop --> 2 hops): 
					- "Adding, changing and augmenting the underlying graph structure". To do this, we add virtual edges and virtual nodes. 
					- Connecting 2-hop neighbors, so the adjacent matrix increases from $A$ to $A+A^2$.
						- eg: Author-paper Bipartite network. Rather than think of author/paper separately as a 1-hop adjacent matrix, we can use  see whether where is co-author relationship between two authors by taking 2 hops. 
						- That might bring another problem (too dense), we will discuss how to fix it later.
				- 2. Adding virtual nodes
					- The virtual node will connect to all the nodes in the graph.
					- Let's say there is two nodes actually relevant, but they are 10 hops away.
					- With a virtual node that connect to all the nodes, the message passing will be efficient with less deeper network. 
			- Further discussion of other augmentations for dense graph: 
				- 1. (Randomly) sample a node's neighborhood for message passing
					- Aggregating message from $10^7$+ nodes can be very expensive. 
					- At the time we gain computation efficiency, the trade-off is you kind of lose some of the expressive power, due to the potential loss of information. 
			- Predictions:
				- Node level prediction: 
					- we have d-dim node embedding $\{h_v^{(L)} \in R^d, \forall v \in G\}$, and suppose we want to make k-way prediction that classify among k categories. 
					- $\hat {y_v} = Head_{node}(h_v^{(L)})=W^{(H)}h_v^{(L)}$. With $Head_{node} = W^{(H)}$, we map node embeddings from embeddings to y hat, so that we can compute the loss. 
				- Edge level predictions:
					- Using pairs of node embeddigns
					- $\hat {y_{uv}}=Head_{edge}(h_u^{(L)},h_v^{(L)})$.
					- $Head_{edge}$ options:
						- 1. Concatenation + linear: 
							- $\hat {y_{uv}}=Linear(Concat(h_u^{(L)},h_v^{(L)}))$, the linear() will map 2D-dimensional embeddings to k-dim embeddings. 
							- $Concat()$: putting elements into a list, or dictionary, for example. 
						- 2. Dot product
							- $\hat {y_{uv}} = (h_u^{(L)})^Th_v^{(L)}$. This only applies to 1-way prediction (eg: link prediction, predict the existence of an edge.)
							- Similar to multi-head attention, 
				- Graph level prediction:
					- 1. Global pooling 
						- $\hat {y_{uv}}=Head_{graph}(h_v^{(L)} \in R^d, \forall v \in G)$
						- $Head_{graph}$ is similar to $Agg()$ in a GNN layer. 
							- Global mean pooling, global max pooling and global sum pooling are describing different $Head_{graph}$ functions. 
					- 2. Hierarchical global pooling
						- Do the same action by smaller batches, obtain a set of pooling results, and then apply the same action to that set of pooling results, to obtain the final y hat.
						- Issue of global pooling: prediction of two different graph could have the same y hat after each graph takes summation on all nodes. Which makes it can't differentiate 2 graphs.
						- By hierarchical pooling, we don't aggregate everything together at the same time. 
						- DiffPool idea:
							- Graphs tends to have community structure. Detect community first, and then we aggregate communities, and then this create a super-node, and then use that super-node to aggregate super-community super-node..

			
			- If some structure are hard to learn by GNN --> Feature augmentation
				- eg: cycle count feature

				- Standard:
					- 1. Assign constant values to nodes
					- 2. Assign unique IDs to nodes 


![[Pasted image 20220917053835.png]]
- Figure: Comparing constant node value, versus one-hot node. How we can learn from 1 dimensional feature, by the way?

![[Pasted image 20220920160545.png]]
- Figure: Receiver operating characteristic (ROC) curve that captures the tradeoff in TPR and FPR as the classification threshold is varied for a binary classifier.
	- Source: https://www.wikiwand.com/en/Receiver_operating_characteristic

---
- Week 8 - Training the GNN
- Prediction head: Choosing the head function for predicting y hat. 
- Evaluation metrics: RMSE or MAE.
- Split / random split data into train /validation / test set. 
	- Deductive learning: (For completeness) The problem has been solved, and there are set of rules, and the answer is obtained with a 100% accuracy using those rules. 

	- Inductive setting (Generalizing rules): train/valid/test set data are on different graph. It tries to fit a general rule from a set of observed instances, then use that model to predict the unknown.
	- Difference:
		- 1. Encountered? While transductive learning label unlabeled points which we have already encountered, inductive learning train the model and label unlabeled points which we have never encountered.
		- 2. Transductive learning does not build a predictive model. If new unlabelled points are encountered, we will have to re-run the algorithm. Inductive model is a predictive model, it could initially built model to predict new unlabelled points. 
		- 3. Inductive learning has less computational cost than transductive learning. 
	- Shortcoming of inductive learning:
		- 1. The error in decision boundary: if a "nearest neighbor" approach is used, points closer to the border may be in wrong color.
		- 2. If we have more information, such as connectivity, 
	- When to use inductive learning:
		- Problem which cannot be solved deductively
		- Problems in which no human expertise is available 
		- Humans can complete the task, but it is difficult for a computer
		- Problems where the desired function is frequently changing.
		- Problems where each user requires a unique function.

	- Transductive setting (Reasoning from observed, specific training cases to specific test cases.): train/valid/test set data are on the same graph
		- Transduction = Reasoning from observed, specific (training) cases to specific (test) cases. 
		- Vladimir Vapnik (PhD in statistics): When solving a problem of interest, do not solve a more general problem as an intermediate step, try to get the answer that you really need but not a more general one. 
		- Transduction was introduced by Vladimir Vapnik in 1990s, induction requires solving a more general problem  (inferring a function) before solving a more specific problem.
		- The predictions of the transductive model are not achievable by any inductive model.
			- eg: binary classification. A large set of test inputs may help in finding the clusters, thus providing useful information about the classification labels. The same predictions would not be obtainable from a model which induces a function based only on the training cases.
			- eg: Transductive suppert vector machine (TSVM).
		- Why transduction could be more accurate than inductive learning:
			- Route 1: Examples -->Induction to get approximating functions --> Deduction using that function to perform prediction.
			- Route 2: Examples --> Use transduction to preform prediction. 



![[Pasted image 20220920070846.png]]
- Figure

---
- Week 9
	- How expressive are GNNs?
		- Expressive power  = ability to distinguish different graph structures 
			- 1. Distinguish node/link/graph features
			- 2. Distinguish local neighborhood structures
		- Use computational graph to distinguish different node's local neighborhood structure
			- Computational graph lay down the data flow in one dimension. 
			- Computational graphs are identical to "rooted subtree structures" around each node. 
				- eg (with figure): When a GNN aggregates neighboring node embeddings, GNN only sees node features, not IDs.  a GNN will generate the same embedding for node 1 and 2 because their computational graphs are the same, and node features (color) are identical.
			- Injection property
				- Most expressive GNN should map subtrees to the node embeddings injectively
				- Function $f:X \rightarrow Y$ is injective if it maps different elements into different outputs.
				- Observation: Subtrees of the same depth can be recursively characterized from the leaf nodes to the root nodes. If each step of GNN's aggregation can fully retain the neighboring information, the generated node embeddings can distinguish different rooted subtrees. 
				- In other words, most expressive GNN would use an injective neighbor aggregation function at each step. 
	-  How to design a maximally expressive GNN model
		- Expressive power of GNNs can be characterized by that of neighbor aggregation functions they use. 

![[Pasted image 20220920173817.png]]
- Figure: Computational graph of 2 nodes in the same graph. GNN only sees node features, not IDs. 

---



![[Pasted image 20220916041159.png]]
- Figure: GNN consist of multiple permutation equivariant function. Naive MLP approaches doesn't apply these permutation invariant functions on the dataset. Different ordering of data would produce hugely different prediction results. 


---
- GCN 

![[Pasted image 20220916034551.png]]
- Figure: Illustration of Convolution GNN layers. 




- Tasks for (Convolution) GNNs
	- Node classification
	- Link prediction
	- Community detection
	- Network similarity

- Breakdown the pipeline of Basic ANN ML (review the basics)
	- Inputs: 
		- vectors of real numbers, sequences (natural language), matrices (images), graphs (potentially with node and edge features)
	- Task: optimization problem: $min_\theta L(y, f(x))$,
		- $\theta$: a set of parameters we optimize
		- Backpropagation etc
	- MLP: MLP NN consists of at least 3 layers, input layer, output layer and a hidden layer.


- Graph deep learning 
	- Local network neighborhoods
		- Describe aggregation strategies
		- Define computation graphs
	- Stacking multiple layers
		- Describe the model, parameters and training
		- How to fit the model
		- Simple example for unsupervised and supervised training
	- Setting
		- V: vertex set
		- A: adjacency matrix (assume binary)
		- $X \in R^{m \times|V|}$: matrix of node features. (what is m?)
		- v: a node in V
		- $N(v)$: the set of neighbors of v
		- example of node features:
			- 1. social networks: user profiles, user image
			- 2. biological networks: gene expression profiles, gene functional information
		- Naive approach:
			- Join adjacency matrix and features, and feed them into a deep neural net.
			- Issue:
				- $O(|V|)$ parameters
				- Not applicable to graphs of different sizes
				- Sensitive to node ordering
		- Convolutional approach
			- Problems:  
				1. No fixed notion of locality: 
					- Not similar to image, for graphs, there is no fixed notion of locality or sliding window on the graph. And graph is permutation invariant. 
				2. Permutation invariance
					- Definition: the order of the numbering should not change the prediction result.
					- Graph does not have a canonical order of the nodes
					- Consider we learn a permutation invariant function that gives $f(A_1, X_1)$ = $f(A_2, X_2)$, which A is adjacency matrix and X is node feature matrix for the node.

- GCN
	- Idea: Node's neighborhood defines a computation graph
	- Techniques
		- Determine node computation graph
		- Propagate and transform information
	- Idea: Aggregate neighbors
		- Generate node embeddings based on local network neighborhoods

![[Pasted image 20220916042618.png]]
![[Pasted image 20220916042652.png]]
![[Pasted image 20220916042731.png]]
![[Pasted image 20220916042744.png]]
![[Pasted image 20220916042756.png]]


---



- Given that we have adjacency matrix $\tilde A$ for the graph, then 

- 1. Node embedding $H^{(k+1)}$: 
	- $H^{(k+1)}= \sigma(\tilde AH^{(k)}W^{(k+1)})$
- 2. Message passing in a very generic form: 
	- $h_u^{(k+1)}=UPDATE^{(k)}(h_u^{(k)},AGGREGATE^{(k)}(\{h_v^{(k)}, \forall v \in N(n)\})$, where h is node features / embeddings, k is the number of hops. 
	- The aggregate function is not restrictive. A simple lump sum function is also viable.
	- The update function would be linear regression. That will be shown in the next section. 
- 3. "self-supervised" process: 
	- $h_u^{(k+1)} = \sigma(W_{self}^{(k+1)}h_u^{k}+W_{neigh}^{(k+1)}\sum_{v \in N(u)}h_v^{(k)})$
	- $W_{neigh}^{(k+1)}$ is a matrix which brings back the weighting to all of the embeddings of its neighbors.
- 4. Collapse the two matrices into a single weight matrices for equation 3.
	- $H^{(k+1)}=\sigma((A+I)H^{(k)}W^{(k+1)})$
	- This reduces message passing to relatively simple matrix multiplication. 
	- Not familiar with how to go from eqn 3 to eqn 4.
	- Eqn 4 is very similar to eqn 1.
	- $\tilde A = (D+I)^{-1 \over 2}(I+A)(D+I)^{-1 \over 2}$

- Development and application of GNN models is a new and active area of research. 

---
![[Pasted image 20220819172630.png]]
- 2-step message passing
	- 1. You have a target node and its neighbor node information (those nodes)
	- 2. You took all the information from those nodes, and aggregate it in some ways 
	- 3. Update the representation of node A based on the message that you calculate inside of this aggregation function.

- How to train a GNN? (Slide 419)
	- Input: node embedding $z_v$
	- Loss: minimize the loss between node label $y$ and node embedding $z_v$.
	- Unsupervised learning: No node label available, and use graph structure as the supervision.
- unsupervised training
	- $L = \sum_{z_u,z_v}CE(y_{u,v},DEC(z_u,z_v))$, where $y_{u,v}=1$ when $u$ and $v$ are similar.
		- $CE()$ is the cross entropy (Slide 371, Lecture 6). $CE(y,f(x))=-\sum_{i=1}^C(y_ilogf(x)_i)$
		- $DEC()$ is the **decoder** such as inner product. (Lecture 4)
			- If $DEC()$ is "inner product", then it will be $z_uz_v$, which takes in embeddings, and outputs similarity score. 
- supervised learning
	- $L= \sum_{v \in V}y_vlog(\sigma(z_v^T \theta))+(1-y_v)log(1-\sigma(z_v^T\theta))$, where $y_v$ is node class label

- Inductive capability:
	- The same aggregation parameters $W_k$ and $B_k$ are shared for all nodes, such that the number of model parameters is sublinear in $|V|$ and we can generalize to unseen nodes. 

![[Pasted image 20220921062859.png]]
- Figure: shared parameter.

---
- Week 10: Heterogeneous Graph, Knowledge graph
	- Recall 
		- heterogeneous G = (V,E,T,R), where V: node with node type, E, Edges with relation types, R: Relation type, T: Node type
		- For a single GNN layer, Message passing from l-1 layer to l layer, and aggregation from neighbors. 
	- Relational GCN:
		- What if the graph has multiple relation type?
		- Use different neural network weights for different relation types. i.e. W1 for r1, W2 for r2, W3 for r3 etc. In the learning process, The loss will be lower if each relation type is going closer to their zone. 


---

## Important concept 1: Word embeddings, network embeddings 
- Why embedding?
	- 1. Representing the data / text / network into graphs, representing the graphs into adjacency matrix. 
		- Map nodes to d-dimensional embeddings, such that "similar nodes in the network are embedded close together"
	- 2. Convert sparse vectors into dense vectors
		- There would be a lot of spaces of the matrix storing zeros.
			- The analogy would be "a book that had only a single word on each page." They are hard to comprehend and inefficient use of paper.
			- Same issue with using sparse vectors for ML tasks
	- 3. Tools: TransE/TransR/DistMult
		- Utilizes of lists of triples: head,relation,tail
		- Produces embeddings such that minimizes the distance between the source and destination of the relation.


----

- Motifs
	- Occur in real-world networks with frequencies significantly higher than randomly generated networks.

- Graph mining
	- source: https://towardsdatascience.com/understanding-graph-mining-e713183a64f3
	- You knows how to get from point A to point B. Using the shortest period of time to buy what you need.
	- Similarly, graph mining uses features to see how a set of observations are related from a user facing similarity signal.
	- Two types of graphs
		- Natural graphs (eg: social graphs, roadway graphs etc)
		- Similarity graphs: measure the similarity distance between nodes. (a blob of metadata shares the blob structure via graph representation)
	- And each of these types of graph we can classify:
		- Simple homogeneous with one type of node and edge
		- Complex heterogeneous with multiple types of nodes, multiple types of edges. These can be directed or undirected. 

- Why graphs important?
	- Graphs abstract" local information" and extract useful "global information" from data. 
		- such as
			- uncovering clusters of data points
			- providing distance measures for otherwise intangible concepts.

- Graphs are data types flexible
	- By embedding and combining multiple types of features: textual (Jaccard similarity), visual (image similarities), and other semantic attributes.

![[Pasted image 20220817012755.png]]
- Graphs are scalable
	- Graph sampling is used to seek subgraphs on receptive fields. 
- eg: GNNs with Cora (google colaboratory)

---
- Wikispeedia:
	- 6 degrees of separations tell us that every wikipages are standing away from each another by at most six degrees. 
	- This is a online "game" that let people tries to reach certain wikipage, starting from a wikipage that is totally irrelevant with it. 
		- Human strategy is discussed in 2012: https://cs.stanford.edu/~jure/pubs/wayfinding-www12.pdf
		- keywords: human factors, information networks, human computation.
		- "We find that human wayfinding, while mostly very efficient, differs from shortest paths in characteristic ways: the median human game path is only one click longer than the median optimal solution".
			- This is affected by the structure of the information network. If the degree distribution 
		- "Human: navigate through high-degree hubs in the early phase, while their search is guided by content features thereafter"
		- "Observe a trade-off between simplicity and efficiency: conceptually simple solutions are more common but tend to be less efficient than more complex ones."
		- Design a model and an efficient learning algorithm. That model can be applied in intelligent browsing interfaces. 
		- Candidate models
			- Human Markov model
			- Binomial logistic model
			- Learning-to-rank model
		- Features for learning
			- Likelihood of the likelihood feature vector $\vec f(u_i,u_{i+1},t$
			- $TF-IDF(u_{i+1},t)$
			- $deg(u_{i+1})$
			- Indicator $SPL(u_{i+1},t) > SPL(u_{i},t)$

- Analytic perspective: 

- There is tradeoff between topical relatedness of concepts and the underlying network structure that tells us insights about the methods used by efficient information seekers. 
	- There are safe wayfinding strategies but inefficient.
	- On the other hand, by trying to find only the shortest path, the searcher might get lost more easily.

- Pragmatic perspective:

- "trails" an information seeker has navigated can provide useful information to the seeker. 
- One useful direction is to predict what piece of information the information seeker is trying to locate.
- Another is in automatically detecting if the user has gotten lost. 

- What we want:
	- applications in improving the design of information spaces (15), more intuitive and navigate link structures (8), and new intelligent information navigation systems (16).

- Players have no knowledge of the global network structure but rely solely on the local information they see on each page. 
	- The outgoing links connecting the current articles to its neighbors, and on their expectations about which articles are likely to be interlinked. 

---
- Week 10 Knowledge graph
- Relational GCN
	- Each relation has L matrices, and the rapid number of parameter growth with respect to relations. 
	- Node class prediction 
		- RGCN uses the representation of the final layer - if we predict the class of node A from k classes, take the final layer (prediction head): $h_A^{(L)} \in R^k$, each item in $h_A^{(L)}$ represents the probability of that class.
	- Link class prediction
		- RGCN: In a heterogeneous graph, the homogeneous graphs formed by every single relation also have the 4 splits. 
		- Link prediction loss, with negative sampling: $l = -log(\sigma(f_{r_3}(h_E,h_A))-log(1-\sigma(f_{r_3})h_E,h_B)))$
		- eg: 
			- Step 1:  $(E, r_3, A)$ is training supervision edge, then all the other edges are training message edges. What we want to train is the training supervision edge? And message passing edges are the edges that are going to deliver information to that edge, to predict the likelihood of that edge. 
			- Step 2: Use RGCN to score $(E,r_3,A)$. Take the final layer of $E$ and $A$: $h_E^{(L)}\in R^d$ and $h_A^{(L)}$ $\in R^d$.
			- Step 3: Relation-specific score function $f_r:R^d \times R^d \rightarrow R$. One example, $f_{r_1}(h_E,h_A)=h_E^TW_{r_1}h_A,W_{r_1} \in R^{d \times d}$, we have a transformation matrix between 2 embeddings, and then dot-product between them, then predict it is relation type $r_1$ between that two nodes. 
			- Step 4: Create a negative edge. Negative edges means the connection between two nodes that is not existed before, not in the set of either training supervision edge, or training message edges. Adding these by perturbing the supervision edge $(E,r_3,B)$, corrupt the tail of $(E,r_3,A)$, eg: $(E,r_3,B)$, $(E,r_3,D)$.
			- Step 5: Use RGCN to score negative edges, eg: $(E,r_3,B)$, $(E,r_3,D)$.
			- Step 6: Optimize a standard cross entropy loss by (a) maximize the score of training supervision edge and (b) minimize the score of negative edge. 
			- Step 7: Validate the performance of our model. Link another non-existent edge eg: $(E,r_3,D)$ as "validation edge", and uses the rest of the prior "training supervision edge" + "existing graph, "training message edge" to predict the validation edge. By message propagation, score the value of the validation edge.
	- Two methods to regulate the weight $W_r^{(l)}$.
		- Use diagonal matrices
		- Use basis/dictionary learning 
	- Regulate weights:
		- 1. Block diagonal matrices or partitioned matrix: 
			- Block matrix or partitioned matrix
				- It is a matrix that is interpreted as having been broken into sections called blocks or submatrices. 
			- Block diagonal matrix
				- Block matrix with only diagonal parts are non-zeros. 
				- The size of each $W_r^{(l)}$ is $d^{(l+1)} \times d^{(l)}$.
				- with B low-dimensional matrices, then the number of parameter reduces from $d^{(l+1)} \times d^{(l)}$ to $B \times {d^{(l+1)} \over B} \times {d^{(l)} \over B}$, by limiting the behavior of the neuron, that only nearby neurons / dimensions can interacts through W. 
		- 2. Basis / dictionary learning
			- The idea, I guess, should came from the factorization. It breaks down relations into a number of combination of basic relations.
			- Share weights across different relations. 
			- Represent the matrix of each relation as a linear combination of basis transformations: $W_r = \sum_{b=1}^B a_{rb}V_b$, which B is a set of scalar. 
				- where $V_b$ is the basis matrices that shared across all relations
				- $a_{rb}$ is the importance weight of matrix $V_b$.
			- Q: If all relations share the same weight, why it would be useful?
	- eg: entity/node classification
		- Goal: predict the label of a given node. 

- Knowledge graphs
	- Publicly available KGs: Freebase, wikidata, dbpedia, yago, nell.
	- Characteristics: 1. Massive - millions of nodes and edges 2. Incomplete: many true edges are missing. 

- KL complete task
	- For a given (head, relation), we predict missing tails.
	- Properties
		- In KGs, edges are represented as triples (h,r,t).
	- In vector space, the goal is the embedding of (h,r) should b close to the embedding of t.
		- Q: how to embed (h,r)?
		- Q: how to define closeness?

- Relation patterns
	- Symmetric (antisummetric) relations: $r(h,t) \Rightarrow r(t,h)$, $(r(h,t)) \Rightarrow \neg r(t,h))$, $\forall h,t$.
		- ¬: latex = `\neg`, Logical not. 
		- eg: family, roommate = symmetric, hypernym are antisymmetric
	- Inverse relations: $r_2(h,t) \Rightarrow r_1(t,h)$
		- eg: advisor and advisee
	- Composition (transitive) relations: $r_1(x,y) \land r_2(y,z) \Rightarrow r_3(x,z)$, $\forall x,y,z$.
		- Q: composition and transitive is not the same thing?
		- eg: my mother's husband is my father
	- 1-to-N relations: $r(h,t_1),r(h,t_2),\dots,r(h,t_n)$ are all True. 
		- eg: r is "Student of".

- TransE model (Translating embeddings for modeling multi-relational data) (A Bordes, N Usunier et al, 2013)
	- TransE is a method for modeling multi-relational data. This is the first work of the translation model series. The basic idea is making the sum of head vector and relation vector as close as possible with the tail vector. 
	- Trans: Translation.
	- E: Embeddings.
	- Algorithm: For a triple $(h,r,t)$, $h,r,t \in R^d$, $h+r$ close to $t$ if the given scoring function is true, else $h+r$ is far away from $t$.  Scoring function $f_r(h,t) = -d = -||h+r-t||$.
	- Loss function: $L(h,r,t) = max(0, d_{pos}, d_{neg} + margin)$.
	- Relationships in TransE:
		- Symmetric: X TransE cannot model symmetric relations -- eg: $h+r=t$ holds, then $t+r=h$ do not holds anymore. 
		- Antisymmetrix:$h+r = t$ , but $t+r \neq h$, thus V.
		- Inverse: We can set $r_1 \neq r_2$, thus V. 
		- Composition (Transitive) relations: $r_3 = r_1 + r_2$, this V.
		- 1-to-N relations; $t_1$ and $t_2$ will map to the same vector, although they are different entities. (a) $t_1 = h+r = t_2$, (b) $t_1 = t_2$, (a) and (b) are contradictory.
	

- TransR model (Learning Entity and Relation Embeddings for Knowledge Graph Completion) (Y Lim, Z Liu et al, 2015)
	- TransE models translation of any relation in the same embedding space. Can we design a new space for each relation and do translation in relation-specific space?
	- TransR model entities as vectors in the entity space $R^d$ and model each relation a vector in relation space $r \in R^k$ with $M_r \in R^{k \times d}$ as the projection matrix. It also means  the dimension for G: d could be different than G': k. Say we have $h$ and $h$ for 2 entities in space of entities. In the space of relation, they are denoted as $h_\perp = M_r h$ and $t_\perp = M_rt$.
	- Scoring function: $f_r(h,t)= -||h\perp + r - t_\perp||$.
	- Relations:
		- It is the most expressive among all models, but the dimension of the model is also the largest. 
		- Symmetric: $r=0$, $M_rh = M_rt=t_\perp$, V
		- 

- 3. DistMult model:
	- New idea: bilinear modeling.
	- DistMult: entities and relations using vectors in $R^k$.
	- Scoring function: $f_r(h,t) = <h,r,t> = \sum_i h_i r_i t_i$, $h,r,t \in R^k$.

![[Pasted image 20220922045126.png]]
- Figure: expressiveness of all models.

---
- Week 11: Reasoning in KG using embeddings

- Tasks in KG reasoning:
	- It is not KG completion
	- Answer complex queries by multi-hop reasoning (1 hop = depth-one neighbor from the node)
	- Generalize one-hop queries to path queries by adding more relations on the path.

- Properties:
	- Due to KG incompleteness, one is not able to identify all the answer entities.
		- My Q: Is that any information loss from such text to graph conversion? Can I perform such query task without any loss of information?
		- That is the tradeoff of the [[representation]]. If we don't represent them as a graph, we cannot 



- Goal: Perform multi-hop reasoning over KGs.
- KG completion versus one-hop query:
	- KG completion: is link $(h,r,t)$ in the KG?
	- One-hop query: is $t$ an anser to query $(h,r)$?
- Query types:
	- One-hop queries: A->B: What adverse event is caused by Fulvestrant?
	- Path queries (Generalized one-hop queries): A->B->C: What protein is associated with the adverse event caused by Fulvestrant?
	- Conjunctive queries: A->C and B->C: What is the drug that treats breast cancer and caused headache?
- Path queries
	- An n-hop path query q can be represented by $q = (v_a,(r_1,\dots,r_n))$, which $v_a$ is an anchor entity.
	- In complete graph, it is easy, just traverse the grapg. 
		- eg: "What proteins are associated with adverse events cased by Fulvestrant" -- Query (e;Fulvestrant, (r: causes, r:assoc))
		- 1. Start from anchor node
		- 2. Traverse the KG by the relation "causes", we reach a list of 1-hop entities L. 
		- 3. Start from each element in L, we transverse associated-relation arrow, to get a list of 1-hop entities L2. That is the answer. 
	- KGs are incomplete and unknown.
		- Many relations between entities are missing or are incomplete. 
			- 1. Missing answers. 
	- Can we first do KG completion and then traverse the completed KG?
		- No. The completed KG is a dense graph. And more $(h,r,t)$ triples will have some non-zero probability. Time complexity of traversing a dense KG is exponential as a function of the path length $L:O(d_{max}^L)$.
- Existing methods:
	- Answering multi-hop queries
		- Path queries
		- Conjunctive queries
	- Query2box

- Predictive queries
	- Answer arbitrary queries while implicitly imputing for the missing information
	- i.e. generalization of the link prediction task

---
- Book: 
	- Orienterring in an information landscape: how information seekers get from here to there (VL O'Day and R Jeffries, 1993)
	- Pragmatic evaluation of folksonomies (D. Helic et al, 2011)
	- Integrating browsing and searching on the Web. (C.Olston, 2003)

---