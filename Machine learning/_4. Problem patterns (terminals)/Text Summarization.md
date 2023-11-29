- 12-10-2022: created

- Text summarization
- Document summarization

- Types: (R2)
	- Extraction-based summarization
		- Rely on extracting several parts, such as phrases, and sentences, from a piece of text and stack them together to create a summary. (R2)
		- Identify the important sentences or phrases from the original text. related: [[TextRank algorithm]]
		- Extract only those from the text.  (R2)
		- Those extracted would be our summary.  (R2)
	- Abstractive summarization
		- Used advanced NLP techniques to generate an entirely new summary. Some part of this summary may not even appear in the original text.  (R2)
	- Domain-specific summarization
	- Query-based summarization
	- Generic summarization


![[Pasted image 20221021213150.png]]
- General steps: (R1)
	- 1. Create a method for extracting the important keys from the original documents
	- 2. Collect text documents with keywords that are favorably labeled. The keys must be compatible with the extraction method specified. One may also build negatively labeled keys to improve accuracy.
	- 3. To produce the text summary, train a binary machine learning classifier.
	- 4. In the test phrase, generate all of the relevant words and phrases and classify them accordingly.

- Algorithms
	- [[sequence-to-sequence model|seq2seq]]

- Advantages: (R1)
	- Effective
	- It functions in any language
	- Productivity is increased

---
## Reference

1. Analytic steps blog: https://www.analyticssteps.com/blogs/what-text-summarization-nlp
2. Vidhya's blog: https://www.analyticsvidhya.com/blog/2019/06/comprehensive-guide-text-summarization-using-deep-learning-python/