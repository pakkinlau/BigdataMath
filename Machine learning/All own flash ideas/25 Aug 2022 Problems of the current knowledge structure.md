- 25-8-2022: created
- 21-10-2022: created

- Combining similar meaning phrases into the same node: (21-10-2022)
	- eg: when learning NLP, "semantic vector space model". "word vector", "word embeddings".... actually in most of the case meaning the exact same thing. 

---
## The following contents do not have any reference pointers:

- Problem 1:
	- The [[Resource description framework|RDF]] structure only be fully descriptive for factoid data. But for knowledge, the R could be much more important than those two entities. Because in science / technology, most useful concepts are functional, and functions would act as relations that joins entities together. 

- Problem 2: 
	- It is not easy to fully generate back a document by terms and concepts. Some good quotes or special way to convey a meaning. We call it "dialect" here. 

- Problem 3:
	- Many useful attributes does not only relates to one entity. The structure of hyperlink system only effective to deal with tree structure systems. In general, any child nodes could have multiple parent nodes. 

- Problem 4:
	- Concepts does not exists in the word itself
	- Knowledge was built by asking questions, exploring, revising views and asking new questions (Sutton, 1998)
	- eg: The earth is not the center of the universe. --> People know the meaning of earth, universe, center. But the concepts from this statement cannot be described by word vector alone. 

- Problem 5:
	- de Finetti (1990): If we wish to consider exchangeable [[representation]] for documents and words, we need to consider mixture models that captures the exchangeability of both words and documents. 

- Problem 6: 
	- We should be able to label author and date.
	- Most artificial contribution should be on "concepts", instead of entities and attributes. 
---

- Strategy:
	- 1. Try to use "Concept Rc/Ra Concept" method to construct the overall structure of notes.  
		- Rc could be a relation that is made by a concept, or Ra, a relational that is linking to a description.
		- This is trying to resolve problem 1. 
	- 2. Diff(C1,C2) = list(A1,A2,...,An) --> (C1&C2) Ra A1 , (C1&C2) Ra A2 , .... etc
		- Those "difference of set" could be partially resolved adding those differences as "dimension". eg: the [[performance]] difference of "global word vector methods" vs "local windows methods" might be manifested in multiple distinct area. These kinds of comparisons also automatically adds content to the related entity.
		- Because C1 and C2 has common dimensions to compare with, so they should be relatively close distance in vector space (if applicable).
		- This is trying to resolve problem 3. 
		  

---
- Result data structure:
	- Corpus (K) that contain a list of documents (D)
	- 1. A list of documents (D) that is conveying a list of concepts and entities.
	- 2. A list of functional concepts (F) that is a functional unit that manipulates entities. 
	- 3. A list of entities (E) that is described by attributes and terms. 
	- 4. A list of comparisons of E that is described by Attributes (Comp(Ei, Ej) = Ak). A complete list of attibutes provide a vector space that enables the categorization of entities. 
	- 5. A list of attributes that is described by terms (T)

- Result taggings:
	- 1. Tag (author, year of paper) after the important concept.  (Resolving problem 6)

---
- Automated tasks for knowledge machine:
	- 1. Named-entity recognition: 
		- There are certain named-entity recognition technology available. 
	- 2. Attribute level completeness: 
		- Group up all the attributes that is related to recognized entities. 
		- Parsing technique to reduce the sentence to certain meaning
		- Fusion those descriptions from distinct documents. 
	- 3. Entity level completeness: 
		- Given there are similar entities A and B. Entity A has N dimensions, and entity B has N-k dimensions. The systems would automatically query for the remaining k dimensions and gather those information for entity B. 
	- 4. Entity level categorization:
		- Use Diff(Ci, Cj) on vector space to find similar entity groups. 
	- 4. (Harder) Concept/functional level completeness:
		- Explore Latent Semantic Indexing to explore how to extract concepts from an article.

- Content recommendations:
	- Inference: by Bayesian approach: $$p(\theta, z|w, \alpha, \beta)= {p(\theta,z,w|\alpha, \beta) \over p(w| \alpha, \beta)}$$

---
## List of NLP functions

- Preprocessing
	- Tokenization
	- [[Annotation]]
	- Tagging (what is it?)
	- Parsing (what is it?)
	- Feature selection
	- Cluster texts by date/author/discourse context

- Representing meaning of terms ("The meaning of word is its use in the language")
	- 1. [[One-hot vector]]
	- 2. [[Word representation]]
	- 3. [[GloVe]]

- Word vectors characteristics:
	- Polysemy (Deerwester, 1990)
	- Synonymy (Deerwester, 1990)
	- Exchangeability: (Aldous, 1985), (Finetti 1990)

- Matrix design:
	- word vector could contain different meaning, and its meaning is represented by how the matrix is constructed. 
	- Kinds of matrix design
		- word x document: it is a sparse matrix. the shape of the shape will change
		- word x word: generate relative dense word vector. the shape of the matrix is predictable
		- word x discourse context: 
		- word x search proximity
		- adjective x modified noun: collect collocational information 
		- word x dependency rel.

- Problems to avoid
	- 1. NLP could have overfitting problem, when: 
		- Number of parameters in the model grows linearly with the size of the corpus.  
	- 2. The probability should be able to be connected with the documents outside the training set. 

- Word vectors learning models
	- 1. [[Global matrix factorization methods]]
	- 2. [[Local context window methods]]



- Packages
	- [[Word2vec]]

- Reweighting
	- Probabilities
	- length norm
	- [[TF-IDF]] (Salton and McGill, 1983)
	- PMI
	- Positive PMI

 - Vector comparison (for similarity)
	 - Euclidean
	- Cosine
	- Dice
	- Jaccard
	- KL

- Concepts cannot be found in its use of words. Concepts might be found by the use of "attibutes" insteads. 
	- Question-answering techniques --> Entities and their attributes, and a connected mixture of knowledge graphs. 

- Dimensionality reduction strategies 
	- TF-IDF
	- [[Latent semantic indexing (LSI)]]: 
		- Use [[singular value decomposition]] to identify linear subspace in the space of [[TF-IDF]] features
	- [[Latent Dirichlet Allocation (LDA)]]
	- [[Abstracting entity grouping algorithm ]]
	- LSA
	- PCA
	- NNMF

- Generative probabilistic model 
	- Bayerian methods
	- Maximum likelihood methods
	- probabilistic LSI model (Hofmann 1999, which is presented in "Latent Dirichlet Allocation" by Andrew Ng)


- Some commonly used layers:
	- ![[Pasted image 20220906151418.png]]