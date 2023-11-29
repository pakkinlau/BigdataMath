- 12-10-2022: created

- _Stemming_ usually refers to a crude heuristic process that chops off the ends of words in the hope of achieving this goal correctly most of the time, and often includes the removal of derivational affixes. (R1)

- Most common algorithm for stemming
	- Porter's algorithm



![[Pasted image 20221012141143.png]]
- Figure: Porter's algorithm consists of 5 phases of word reductions, applied sequentially. Within each phase there are various conventions to select rules, such as selecting the rule from each rule group that applies to the longest suffix. In the first phase, this convention is used with the following rule group (R1) 



---
## Reference

1. Stanford NLP group: https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html