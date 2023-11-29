---
alias: [parts of speech, POS]
---

- 12-10-2022: created

- subset:
	-[[ Universal POS]] (upos): 
	- [[Treebank-specific POS]] (xpos)
	- [[Morphological feature]]
	- [[part of speech tagging]]

- Dependency:
	- [[Tokenization]]
	- [[Multi-word token expansion|MWT]]

- For each word in a sentence, [[Stanza]] assigns it a [[part of speech]], and analyzes its universal [[Morphological feature]] (UFeats, e.g., singular/plural, 1st/2nd/3rd person, etc.). (R1)

- To predict POS and [[Morphological feature|UFeat]], we adopt bidirection [[LSTM]] as the basic architecture. 

---
## Reference
1. [[(Paper) Qi, P., Zhang, Y., Zhang, Y., Bolton, J., & Manning, C. (2020). Sta n z a -- A Python Natural Language Processing Toolkit for Many Human Languages.]]