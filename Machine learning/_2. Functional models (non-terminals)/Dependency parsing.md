---
alias: [depparse]
---

- 12-10-2022: created

- superset:
	- [[parsing]]
	- [[NLP tasks]]
	- [[dependency]]

- Dependency:
	- [[Tokenization]]
	- [[Multi-word token expansion|MWT]]
	- [[part of speech|POS]]
	- [[Lemmatization|lemma]]


- What is dependency parsing
	- Dependency parsing is the process of defining the grammatical structure of a sentence by listing each word as a node and displaying links to its dependents.  (R1)
		- While [[Constituency parsing|Constituency parsing]] displays the syntactic structure of a sentence using context-free grammar.
- The dependency parsing module builds a tree structure of words from the input sentence, which represents the syntactic dependency relations between words. (R2)
- The resulting tree representation, [[Universal dependencies|UD]], are useful in many [[downstream tasks|downstream task]].  (R1)

- Dependency grammar in dependency parsing:  (R1)
	- While phrase-structure grammar would need a separate rule for each possible place in the [[parse tree]] where such an adverbial phrase could occur. 
	- Free word order
		- eg: Czech can be much more flexible than in English --> Which produces a lot of rules in [[Constituency parsing]]. 
		- Thus dependency grammars is their ability to deal with languages what are morphologically rich and have a relatively free word order.
		- Thus dependency grammar approach abstracts away from word order information, representing only the information that is necessary for the parse.


![[Pasted image 20221014120254.png]]
- Figure: 
	- LHS --- Dependency parsing tree. 
	- RHS --- Constituency parsing tree.


---
- Dependency relations
	- 1. Traditional linguistics notion of grammatical relation provides the basis for the binary relations that comprise these dependency structures. 
		- These relations consist of a head and a dependent. 
		- The remaining words in the constituents are either direct, or indirect, dependents of their head. 
	- 2. In dependency-based approaches, the head-dependent relationship is made explicit by directly linking heads to the words that are immediately dependent on them, bypassing the need for constituent structures.
	- 3. Apart from "head-dependent" pairs, dependency grammars allow us to further classify the kinds of grammatical relations, or grammatical function.

- In English, both position in a sentence and constituent type are somwhat redundant with the kind of information forund in phrase-structure tree. 

- Linguists have developed taxnomies of relation that go well beyond "familiar notions of subject and object". 
	- From theory to theory, there is enough commonality to develop a computationally usefl standard. 
	- Universal dependencies proejct provides an inventory of dependency relations that are linguistically motivated, computationally useful, and cross-linguistically applicable.

![[Pasted image 20221014122030.png|600x400]]




- Content of chapter X of (R1)
	- Dependency relations
	- Dependency formalisms
	- Dependency treebanks 
	- Transition-based dependency parsing
	- Graph-based dependency parsing


--- 
## Programming implementations 

- [[Stanza]] parses each sentence for its [[Syntactic]] structure, where each word in the sentence is assigned a syntactic head that is either another word in the sentence, or in the case of the root word, an artificial root symbol. 
- Outcome: [[Universal dependencies]] 
- We implement Bi-[[LSTM]] based biaffine neural dependency parser. (Dozat and Manning, 2017)
	- Further augment the model with two linguistically motivated features -- one that predicts the linearaization order of two words in a given language, and other predicts the typical distance in linear order between tehm.
	- We have previously shown that these features significantly improve parsing accuracy (Qi et al, 2018)


---
## Reference
1. [[(Book) Speech and language processing - Daniel Jurafsky (Stanford university)]]
2. Stanza documentation: https://stanfordnlp.github.io/stanza/depparse.html#accessing-syntactic-dependency-information