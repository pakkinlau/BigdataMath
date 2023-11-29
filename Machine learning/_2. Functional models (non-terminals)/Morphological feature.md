---
alias: [UFeat, Morphological feature tagging, UFeat]
---

- 12-10-2022: created

- superset: 
	- [[Morphology]] 
	- [[morphological analysis]]


- [[Morphological feature]] and [[Universal POS]], [[Treebank-specific POS]] are jointly performed by the `POSProcessor` in [[Stanza]], and can be invoked with the name `pos`.
- UFeats are the extension of the core [[part of speech|POS]] categories. These features listed here distinguish additional lexical and grammatical properties of words, which is not covered by the core [[part of speech|POS]] tags. 

- UFeats
	- Universal morphological feature
	- e.g., singular/plural, 1st/2nd/3rd person, etc.). 


---
## Types of UFeats

![[Pasted image 20221013190722.png]]
- Figure: Around 100 kinds of UFeats. (R1)

---
## Example output of UFeats analysis

![[Pasted image 20221013191358.png]]
- Figure: from my stanza getting started pack.


----
## Reference:

1. UD Organization: https://universaldependencies.org/u/feat/index.html