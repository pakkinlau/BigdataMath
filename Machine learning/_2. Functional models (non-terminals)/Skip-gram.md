- 25-9-2022: created

- N-grams: 
	- A fundamental concept in NLP
	- a language model assigns the probability to a sequence of words in a way that more likely sequences receive higher probabilities. 
	- eg: "I have a pen" has a higher chance than "I am a pen".

- [[Co-occurrence]] matrix of a bi-gram model
![[Pasted image 20220830195731.png]]

- Application
	- Speech recognition
	- Spell correction
	- Augmentative communication

- Types
	- Unigram: {I, am, happy, because, learning}
	- Bigram:{I am, am happy, happy because}
	- N-grams: all variation of N are all considered. 

- Probability
	- Bigram: 
		- function C: counts occurence
		- Sequence probability: $P(y|x) = {C(x y) \over \sum_w C(x w)} = {C(x y) \over C(x)}$
			- eg: Corpus: "I am happy because I am learning"
			- $P(am|I)={C(I am) \over C(I)} = {2 \over 2} = 1$
			- $P(happy|I)={C(I happy) \over C(I)} = {0 \over 2} = 0$
	- N-gram:
		- Sequence probability: $P(w_N|w_1^{N-1}) = {C(w_1^{N-1} w_N) \over C(w_1^{N-1})}$
		- $C(w_1^{N-1}w_N) = C(w_1^N)$
