---
alias: [lemma]
---

- 12-10-2022: created

- Dependency:
	- [[Tokenization]]
	- [[Multi-word token expansion]]
	- [[part of speech|POS]]

- _Lemmatization_ usually refers to doing things properly with the use of a vocabulary and [[Morphological feature]]  of words, normally aiming to remove inflectional endings only and to return the base or dictionary form of a word, which is known as the _lemma_ . (R1)
	- eg: If confronted with the token _saw_, stemming might return just _s_, whereas lemmatization would attempt to return either _see_ or _saw_ depending on whether the use of the token was as a verb or a noun. (R1)

- Doing full [[Morphological feature]]

- The goal of both [[stemming]] and lemmatization is to reduce inflectional forms and sometimes derivationally related forms of a word to a common base form. (R1)
	- eg: 
		- am, are, is --> be
		- car, cars, car's cars' -> car
	- The result of this mappng will be:
		- "the boy's cars are different colors" -> "the boy car be differ color"

- Similar to the multi-word token expander, [[Stanza]] ’s lemmatizer is implemented as an ensemble of a dictionary-based lemmatizer and a neural [[sequence-to-sequence model|seq2seq]] lemmatizer.  (R1)
	- To predict "shortcuts" such as lowercasing and identity copy for robustness on long input sequences such as URLs.

---
## Reference

1. Stanford NLP group: https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html