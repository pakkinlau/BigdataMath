- 21-10-2022: created

- This paper is published in 2014.
- Learning vector space representation  [[representation|representation]]

- Abstract
	- 1. Goal of [[representation]] is capturing fine-grained [[semantics|semantic]] and [[Syntactic]] regularities using [[vector]] arithmetic. But the or origin of these regularities have remain opaque.
		- analyze and make explicit the model properties needed for such "regularities" to emerge in word vectors.
	- 2. End-product: Log-bilinear regression model that combines the advantages of two major model families in the literature
		- Global [[Matrix factorization]]
		- [[Local context window methods]] method
	- 3. The model produces a vector space with meaningful sub-structure, as evidenced by its [[performance]] on a recent model [[analogy]] [[tasks|task]]. It also outperfor4ms related models in [[similarity]] tasks and [[named entity recognition]].
	- Achieving [[State-of-the-art]] performance.

- [[NLP tasks]]

- [[log-bilinear]]

- [[Word representation]]
	- They should be able to model [[analogy]] tasks, which [[Global matrix factorization methods]] cannot perform good results. And [[Local context window methods]] are perform poorly on [[Use of statistical information]].

- [[GloVe]]
	- word vector learning should be with ratios of co-occurrence probabilities rather than the probabilities themselves. 
	- $$F(w_i,w_j,\tilde{w}_k)={P_{ik} \over P_{jk}}$$
	- F: Relationship between words? F may depend on some as-of-yet unspecified parameters.
	- $w \in R^d$ are word vectors
	- $\tilde{w} \in R^d$ are separate word vectors whose roles will be discussed in Section 4.2
	- $P_{ik}$: Co-occurrence probability

	- We would like F to encode the information present the ratio in the word vector space.

- Drafting the GloVe representation:
- 1. 
	- The most natural way to encode the information in the word vector space is with vector difference. 
	- To avoid obfuscate the linear structure we are trying to capture, we take the dot product of the argument which prevents F from mixing the vector dimensions in undesirable way.
	- $$F((w_i - w_j)^T \tilde{w}_k) = {P_{ik} \over P_{jk}}$$

2. 
	- Word-word co-occurrence matrices, the distinction between a word and a context word is arbitrary and we are free to exchange the two roles. 
	-  Equation in step one is not [[Invariant, shift-invariant, time-invariant|invariant]], however, the symmetry can be restored in two steps.
		- Require F be a homomorphism between groups $(R,+)$ and $(R_{>0}, \times)$ 
	- $$F((w_i - w_j)^T \tilde{w}_k) = { F(w_i^T \tilde{w}_k)\over F(w_j^T \tilde{w}_k)}$$, which $$F(w_i^T \tilde{w}_k) = P_{ik} = {X_{ik} \over X_i}$$, the solution is $w_i^T \tilde{w}_k = log(P_{ik}) = log(X_{ik}) - log(P_{i})$

3. 
	- We note that equation solution in (2) would exhibit the exchange symmetry if not for the $log(X_i)$ on the right hand side.
	- The term is independent of k so it can be absorbed into a bias $\tilde{b}_k$ for $\tilde{w}_k$ restores the symmetry.
	- $$w_i^T \tilde{w}_k + b_i + \tilde{b}_k = log(X_{ik})$$, which is a drastic simplification over equation (1)
4. 
	- but it is still ill-defined since the logarithm diverges whenever its argument is zero.
	-  One resolution to this issue is to include an additive shift in the logarithm, $log(X_{ik}) → log(1 + X_{ik})$, which maintains the sparsity of X while avoiding the divergences.
	- The idea of factorizing the log of the co-occurrence matrix is closely related to [[latent semantic analysis (LSA)|LSA]] and we will see the resulting model as a baseline in our experiments.
5. We propose a new weighted least squares regression model that address these problems: $$J = \sum_{i,j=1}^V f(X_{ij})(w_i^T \tilde{w}_j + b_i + \tilde{b}_j - logX_{ij})^2$$, where $V$ is the size of the vocabulary. 
	- The weighting function should obey the following properties:
	- $f(0)=0$
	- $f(x)$ should be non-decreasing so that rare co-occurrences are not overweighted.
	- $f(x)$ should be relatively small for large values of $x$, so that frequent co-occurrences are not overweighted. 

- 6. Researchers found the following function work well can be parametrized as $$f(x) = \begin{cases} (x/x_{max})^\alpha \tag{if x < x.max} \\ 1 \tag{otherwise} \end{cases}$$
$$f(x) = \begin{cases*} (x/x_{\text{max}})^\alpha & if $x < x_{\text{max}}$ \\ 1 & otherwise. \end{cases*}$$


---
## Relationship to other models

- All [[Unsupervised learning|unsupervised]] methods for learning word vectors are ultimately based on [[co-occurrence]] statistics of a corpus, there should be commonalities between the models. 
- 


---

## In-text mainpoint

1. How to make [[semantics|semantic]] and [[Syntactic]] regularities emerges from [[Word representation]].


(The text pdf is in below)
![[Pennington, J, Socher, R & Manning, C. 2014. GloVe Global Vectors for Word Representation. Association for Computational Linguistics. httpsaclantho.pdf]]

![[(Paper) Pennington, J., Socher, R., & Manning, C. (2014). GloVe Global Vectors for Word Representation (pp. 1532–1543). Association for Computational Linguistics.pdf]]