---
category: []
alias: []
tags: []
---

- 01-11-2022 00:42: created

- What is Word2vec?
	- 2013 Mikolov et al. 
	- The proposed translation [[Invariant, shift-invariant, time-invariant|invariant]] phenomenon of word vector

1. start with random word vectors, iterate through each word in the wole corpus, try to predict surrounding words using word vectors. Through preduction, update word vector of each (center) word. 
2. the dot-product of two words represent how likely those two words appears at the same time.

---
## Reference

1. 