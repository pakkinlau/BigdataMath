---
alias: [MWT]
---

- 12-10-2022: created

- Superset:
	- [[NLP tasks]]

- Dependency:
	- [[Tokenization]]

- Definition:
	- Multi-word token expansion refers to a technique in natural language processing (NLP) where multi-word expressions or phrases are treated as single tokens or units during text analysis. Instead of breaking down these expressions into individual words, they are preserved as a single entity, which can be beneficial for various NLP tasks.
	- Some languages requires MWT. That means, each token can be expanded into multiple syntactic words. This process is helpful for these language when performing later tasks such as [[part of speech]], [[Morphological feature|Morphological feature tagging]] ,[[Dependency parsing]], [[Lemmatization]]. (R2)
- Benefits:
	- Preservation of Meaning: 
		- Multi-word token expansion helps preserve the semantic meaning and context of multi-word expressions. This is especially important for tasks like sentiment analysis, machine translation, and entity recognition, where the meaning of the expression can change when individual words are separated.
	- Efficient Processing: 
		- Treating multi-word expressions as single tokens can improve the efficiency of NLP models, as it reduces the vocabulary size and the complexity of tokenization.
- Challenges:
	- Ambiguity: 
		- Some multi-word expressions can be ambiguous, and determining the correct tokenization can be challenging. For example, "I saw her duck" could be interpreted as "I saw her (pet) duck" or "I saw (her) duck (down quickly)."
	- Data Size: 
		- Maintaining a comprehensive list of multi-word expressions can be resource-intensive, as it requires a large dataset to cover all possible variations and languages.

---

- How to achieve?
- Whitespace Tokenization:
	- The simplest method is to tokenize text based on whitespace. This would split multi-word tokens into individual words based on spaces or other whitespace characters. While simple, it may not handle all cases correctly, especially when dealing with languages or data where words are not always separated by spaces.
- Dictionary-Based Expansion:
	- Create a dictionary or a list of multi-word tokens and their corresponding expansions. When you encounter a multi-word token, you can look it up in the dictionary and replace it with its constituent words.
- Regular Expressions:
	- Use regular expressions to identify and split multi-word tokens based on patterns. For example, you can define regex patterns that match common multi-word expressions and split them accordingly.
- N-gram Models:
	- Train an N-gram language model on a large corpus of text. When you encounter a multi-word token, you can use the language model to predict the most likely way to split it into constituent words based on the probabilities of word sequences.
- Statistical Methods:
	- Utilize statistical techniques such as Maximum Entropy or Conditional Random Fields (CRF) to learn tokenization patterns from labeled data. These models can learn to recognize and split multi-word tokens based on the context in which they appear.
- Rule-Based Systems:
	- Develop a set of rules or heuristics to identify and split multi-word tokens. These rules can be based on linguistic patterns or domain-specific knowledge.
- [[Dependency Parsing]]:
	- Dependency parsers can be used to analyze the grammatical structure of sentences. They can help identify multi-word tokens and their relationships with other words in the sentence, which can be used to split them into constituent words.
- [[frequency lexicon]]
- [[machine learning]]
	- neural [[sequence-to-sequence model]]



---

- Existing tools:
	- [[Stanza]]
		- For new, [[Stanza]] only perform MWT for French, German and Spanish.
	- [[spaCy]]
	- [[NLTK]]
	- Multi Word Token Expansion is the process of splitting [[Tokenization|token]] into syntactic words which are used by [[downstream tasks|downstream task]] such as [[part of speech]] and [[Dependency parsing]]. 



- Because MWT is for some languages only, therefore there is no Chinese or English examples of MWT. 

![[Pasted image 20221012120442.png]]
- Figure: predict MWT jointly with [[Tokenization]] because this task is context-sensitive in some languages. (R1)

---
## Reference
1. [[(Paper) Qi, P., Zhang, Y., Zhang, Y., Bolton, J., & Manning, C. (2020). Sta n z a -- A Python Natural Language Processing Toolkit for Many Human Languages.]]
2. Trankit, documentation: https://trankit.readthedocs.io/_/downloads/en/latest/pdf/