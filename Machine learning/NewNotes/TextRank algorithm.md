- superset:
	- [[algorithm]]

- TextRank versus [[Page rank algorithm]] 
	- [[Page rank algorithm]] inspired Textrank. 

- Category:
	- Extractive text summarization method
	- Unsupervised

- History:
	- Peter Luhn (late 1950s) "Automatic creation of literature abstracts" - used features as word frequency and phrase frequency to extract important sentences from the text for summarization purposes.
	- Edmundson (late 1960s) Use methods the presence of cue words, words used in the title appearing in the text, and the location of sentences, to extract significant sentences for text summarization. 

- Steps:
	- 1. Split the article into individual sentences
	- 2. Find vector representation (word embeddings) for each and every sentence
	- 3. Similarities between sentence vectors are then calculated and stored in a matrix
	- 4. Similarity matrix is converted into a graph, with sentences as vertices, and similarity scores as edges, for sentence rank calculation.
	- 5. A certain number of top-ranked sentences form the final summary.

---
## Reference

1. Vidhya's blog: https://www.analyticsvidhya.com/blog/2018/11/introduction-text-summarization-textrank-python/