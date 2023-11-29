---
aliases: [LDA]
---
- 31-8-2022: created

- Definition
	- Latent Dirichlet Allocation (LDA): A generalization of the probabilistic [[latent]] semantic analysis model. LDA assumes each [[document]] is a mixture of topics. And each topic is a mixture of words.
	- The basic idea behind LDA is that documents are probabilistic mixtures of topics, and each topic is a distribution over words. The model assumes that there are latent (hidden) variables that generate the observed data (words in documents). These latent variables are the topic assignments for each word in each document and the topic distributions themselves.
- High level overview of how LDA works:

**Part 1: Data Preprocessing**
**Inputs:**
- Corpus: 
	- A collection of text documents (e.g., a set of news articles).
	- A collection of documents is represented as a bag-of-words (BoW) model, where the order of words is disregarded, and each document is represented as a sparse vector of word frequencies.
- Stopwords list: A set of common words to be ignored during analysis (e.g., "the," "and," "in," etc.).
**Outputs:**
- Processed corpus: Text data with stopwords removed and possibly other preprocessing steps like lowercasing, stemming, or lemmatization.

**Part 2: Training the LDA Model**
**Goal**:
Given a collection of documents, the goal of LDA is to infer the hidden topic assignments and the model parameters (document-topic and topic-word distributions) that are most likely to have generated the observed data.
**Model Assumptions**:
- LDA assumes that documents are generated in a two-step process: a. Each document is a mixture of topics, and for each document, there is a distribution over topics. b. Each word in a document is drawn from one of the topics present in the document. The topic for each word is chosen based on the topic distribution of the document.
**Inputs:**
- Processed corpus: The preprocessed text data obtained in Part 1.
- Number of topics (K): A parameter specifying the number of topics to be extracted.
**Outputs:**
- Trained LDA model: A statistical model that has learned topic distributions for the given corpus.

**Part 3: Inference - Document Topic Allocation**
**Inputs:**
- Trained LDA model: The model obtained in Part 2.
- New document: A piece of text for which topic allocation is required.
**Outputs:**
- Topic distribution: The probability distribution of topics for the new document.

**Part 4: Inference - Word Topic Allocation**
**Gibbs Sampling (Inference Algorithm)**:
	    - LDA uses Gibbs sampling as an approximate inference algorithm to estimate the posterior distribution of the hidden variables given the observed data. Gibbs sampling is an iterative process that updates the topic assignments of words in the documents based on their current topic assignments and the topic distributions.
**Inputs:**
- Trained LDA model: The model obtained in Part 2.
- New word: A word for which topic allocation is required.
**Outputs:**
- Topic distribution: The probability distribution of topics for the new word.

**Part 5: Evaluating the LDA Model**
**Inputs:**
- Trained LDA model: The model obtained in Part 2.
- Evaluation corpus: A separate set of documents used to evaluate the model's performance.
**Outputs:**
- Model performance metrics: Measures such as perplexity, coherence score, or topic coherence that assess how well the model performs on the evaluation data.


---
- Step 1: Data preprocessing
![[Pasted image 20230728041419.png]]
![[Pasted image 20230728041556.png]]

- Step 2: Training the LDA Model
![[Pasted image 20230728043508.png]]
![[Pasted image 20230728042049.png]]

- Step 3: Inference - Document Topic Allocation
![[Pasted image 20230728042200.png]]
![[Pasted image 20230728042307.png]]

- Step 4: Inference - Word Topic Allocation
![[Pasted image 20230728042649.png]]
![[Pasted image 20230728042856.png]]

- Step 5: Evaluating the LDA Model
![[Pasted image 20230728043020.png]]
![[Pasted image 20230728043134.png]]


---
- Parameters in the paper
	- $\alpha$,$\beta$: parameter for LDA estimation
	- $z_n$: A set of topic z
	- $w_n$: A set of word w
	- $\theta$: A joint distribution of topic mixture
	- $p(\theta,z,w)$: the reproduced article, given a set of topics and a set of words, that is determined by the given parameters,

![[Pasted image 20220831194943.png]]
![[Pasted image 20220831194951.png]]
![[Pasted image 20220831195001.png]]
![[Pasted image 20220831195009.png]]


- 1. Each point has a distribution of topic possibility. Each article has a mixed distribution of topics: 0.07 science, 0.03 politics, 0.9 sports.
- 2. We can do it in reverse. We have Science: 0.4 galaxy, 0.4 planet, 0.1 ball, 0.1 referendum.
- 3. LDA produces documents by moving the dots in each prism. 
