---
alias: [Constituent, syntactic parsing]
---

- 13-10-2022: cteated

- superset:
	- [[NLP tasks]]
	- [[Syntactic|Constituent]]

- Dependencies:
	- [[Tokenization]]
	- [[part of speech|POS]]

- What is constituency?
	- [[parse tree]]s accessible a `Sentence`'s constituency  property. (R1)
	-  Syntactic [[Constituency parsing]] is the idea that groups of words can be behave as single units, or constituents. Part of developing a grammar involves building an inventory of the constituents in the language. (R2)
		- eg: noun phrase in English
	- The idea is picking out the constituents from sentences. 

- What is constituency parsing?
	- A constituency [[parse tree]] displays the [[syntactic]] structure of a sentence using [[context-free grammar]]. Unlike [[Dependency parsing]] which relies on dependency grammar. 


- What are the constituents from the sentences?
	- First encountering
		- Noun phrase NP
		- Verb phrase VP

- Constituency grammars
	- [[context-free grammar]]
	- [[parse tree]]
	- [[treebank]]

- Syntactic movement
	- The way to split a long-run sentence to be two smaller [[parse tree]]. (R2)

- The problem of constituent parsing
	- Ambiguity
		- [[part of speech|POS]] ambiguity and [[part of speech|POS]] disambiguation
			- (ch8 of R1 book)
		- structural ambiguity:
			- It occurs when the grammar can assign more than one parse to a sentence.
			- example: [[Constituency parsing#^d84d85]]
		- attachment ambiguity:
			- A constituent can be attached to the [[parse tree]] at more than one place.\
		- coordination ambiguity:
			- phrases can be conjoined by a conjunction like and, with more than one possible combinations. 


- CKY parsing / dynamic programming approach
	- It employs "bottom-up parsing" and dynamic programming (wiki)
	- Efficiency
		- The importance of the CYK algorithm stems from its high efficiency. The worst case running time is $O(n^3)$, where n is the length of the parsed string. Related: [[Big-O notation]]
		- This makes it one of the most efficient parsing algorithm in terms of worst-case [[asymptotic complexity]].
	- Dynamic programming use a table of partial parses to efficiently parse ambiguous sentences. 
	- But it doesn't tell us which parse is the correct one.
	- Layout:
		- For a sentence of length n, we will work with the upper-triangular portion of an $(n+1)^2$ matrix. each cell $(i,j)$ in this matrix contains the set of non-terminals that represent all the constituents that span positions $i$ through $j$ of the input. 
		- eg: `0 book 1 that 2 flight 3`
		- These gaps are often called fenceposts.
		- Each non-terminal entry in our table has two daughters in the parse, there must be a position in the input k, where it can be split into two parts such that $i < k < j$.

![[Pasted image 20221017000101.png]]
![[Pasted image 20221017000319.png]]
![[Pasted image 20221017000509.png]]
![[Pasted image 20221017000524.png]]
- fig: CKY represent "Book the flight through Houston"
	- First 2 image: 1-word constituent
		- Rows: contains the [[part of speech|POS]] for each word in the input.
		- Book (noun / verb) --> Book (noun / verb / nominal / VP), noun automatically a nominal due to CNF conversion. verbs are automatically VP as well,
	- Third image: 2-word constituent
		- To determine that, we find out whether there are any production rule that generate other kind of [[part of speech|POS]]

- CKY parsing
	- The above model is a recognizer, not a parser. 
	- To turn it into a parser capable of returning all possible parses for a given input, we can make two simple changes to the algorithm: 
		- 1. augment the entries in the table so that each non-terminal is paired with pointers to the table entries from which it was derived. 

- Span-based neural constituency parsing / or neural CKY
	- Train a neural classifier to assign a score to each constituent, and then use a modified version of CKY to combine these constituent score to find the best-scoring [[parse tree]].




![[Pasted image 20221016225159.png]] ^d84d85
- Fig: structural ambiguity


---
## Reference
1. [[Stanza]] documentation: https://stanfordnlp.github.io/stanza/pipeline.html#build-pipeline-from-a-config-dictionary
2. [[(Book) Speech and language processing - Daniel Jurafsky (Stanford university)]]

- 16-10-2022: created

- superset:
	- [[Syntactic]]

- The problem of mapping from a string of words to its [[parse tree]], which contains [[context-free grammar]] and [[lexicon]] is called [[Syntactic parsing]].