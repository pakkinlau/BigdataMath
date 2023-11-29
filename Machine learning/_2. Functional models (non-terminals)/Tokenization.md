---
alias: [tokenize, token]
---

- Definition:
	- Tokenization used in [[natural language processing]] refers to the process of breaking down a text or a sequence of characters into smaller units called tokens. These tokens can be words, phrases, sentences, or even individual characters, depending on the level of granularity required for a particular NLP task.
- Types:
	- Text segmentation
	- Word tokenization:
		- Use case: sentiment analysis, machine translation, text classification
		- Consideration: Be aware that word tokenization may not be perfect for languages with no spaces between words (e.g., Chinese, Japanese) or for tasks where subword analysis is important.
	- Sentence tokenization:
		- Use case: text summarization, machine translation, named entity recognition
		- Consideration: Sentences can vary in length and complexity, so effective sentence tokenization can be crucial for understanding the context.
	- Character tokenization

- What is a token?
	- A token is an instance of a sequence of characters in some particular [[document]] that are grouped together as a useful semantic unit for processing. (R3)

- Possible package:
	- Stanza:
		- When presented [[raw text]], [[Stanza]] tokenize it and group tokens into sentences as the first step of processing. (R1)
		- [[Stanza]] combines [[Tokenization]] and [[sentence segmentation]] from [[raw text]] into a single module. (R1)


---
## Reference
1. [[(Paper) Qi, P., Zhang, Y., Zhang, Y., Bolton, J., & Manning, C. (2020). Sta n z a -- A Python Natural Language Processing Toolkit for Many Human Languages.]]
2. Tokenex blog: https://www.tokenex.com/blog/ab-what-is-nlp-natural-language-processing-tokenization#:~:text=Tokenization%20is%20used%20in%20natural,into%20understandable%20parts%20(words).
3. Stanford NLP group's blog: https://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html