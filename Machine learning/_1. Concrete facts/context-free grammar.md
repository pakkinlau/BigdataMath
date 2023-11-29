- 16-10-2022: created

- subset: 
	- context-free grammar
	- context-free

---
### Context-free grammar


- What is context-free grammar?
	- It is the most widely used formal system for modeling constituent structure in English and other natural languages. (R1)
	- it consists a set of rules / productions, each of which expresses the way that symbols of the languages can be grouped and ordered together, and a [[lexicon]] of words and symbols. (R1)

- Characteristics
	- 1. CFGs can be hierarchically embedded. (R1)
	- 2. CFGs are be thought of a generator, and --> arrow as "rewrite the symbol on the left with the string on symbols on the right". (R1)
	- 3. Most of the time CFGs are expressed together with the [[lexicon]] together. 


![[Pasted image 20221016182024.png]]
- Figure: Showing some context-free rules. The arrow is an ordered list of one or more terminals are non-terminals. To the left of the arrow is a single non-terminal symbol expressing some [[clustering|cluster]] or [[Generalization]]..


![[Pasted image 20221016175741.png]]
- Figure: An example demonstrating CFG. And this process is visualized by a [[parse tree]]. 
	- This graph shows: 1. CFGs could be hierarchically embedded. 
	- 

![[Pasted image 20221016182938.png]]
- Figure: 12.2 gives a sample lexicon (from some corpus in some database). 12.3 summarizes the grammar rules for the 12.2's corpus, probably extracted from the article. "|" indicate that a non-terminal has alternate possible expansion. 12.4

- Grammar equivalence and normal form
	- A formal language is defined as a set of strings of words. This suggests that we could ask if two grammars are equivalent by asking if they generate the same set of strings.
	- In fact, it is possible to have two distinct context-free grammars generate the same language.
	- Types:
		- Strong (grammer) equivalence:
			- The generate same set of strings AND if they assign the same phrase structure to each sentence (allowing merely for renaming of non-terminal symbols. )
		- Weak (grammer) equivalence:
			- The generate same set of strings BUT NOT assign the same phrase structure to each sentence.

---
### Formal definition of context-free grammar

- See [[derivation]]. 


---
## Reference

1. [[Speech and language processing - Daniel Jurafsky (Stanford university).pdf]]