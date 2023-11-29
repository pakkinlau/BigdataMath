- 17-10-2022: created


- subset:
	- [[Dependency parsing]]


- Dependency versus [[Syntactic]]: 
	- In dependency-based approaches to syntax, the structure of a sentence is described in terms of a set of binary relations that hold between the words in a sentence. Larger notions of constituency are not directly encoded in dependency analyses.
	- Formalisms, phrasal constituents and phrase-structure rules do not play a direct role.
	- Instead, the syntactic structure of a sentence is described solely in terms of the words (or lemmas) in a sentence, and an associated set of directed binary grammatical relations that hold among the words. 

- Typed dependency structure
	- Relations -- directed, labeled arcs from heads to dependents. 
	- The labels are drawn from a fixed inventory of grammatical relations.
	- Root rode
		- Marks the root of the tree, the head of the entire structure. 

- Advantage
	- 1. Their ability to deal with languages that are morphologically rich and have a relatively free word order.
		- eg: word order in Czech can be much more flexible than in English.
	- 2. A phrase-structure grammar would need a separate rule for each possible place in the [[parse tree]] where such an adverbial phrase could occur. A dependency-based approach would just have one link type representing this particular adverbial relations. 