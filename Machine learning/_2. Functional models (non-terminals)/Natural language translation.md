- 25-9-2022: created

---
- From deeplearningAI (): 
	- Week 4: Machine translation
	- Locality sensitive hashing
	- Overview of translation
		- 1. Find someone who knows both languages to start making a list. We need both list of English word and French word equivalents. Keep the rows lined up. 
		- 2. Machine calculate word embeddings (word vectors) associated with English, and word embeddings (word vectors) associated with French. 
		- 3. Retrieve English word embedding of a particular English word (eg: cat: embedding: `[1,0,1]`)
		- 4. Find some ways to translate that English word embedding into word embedding that has the meaning in the French word vector space. (eg: Cat in French: `[2,3,2]`)
		- 5. Take the transformed word vector and search for word vectors and the candidate French word vector space that are most similar to it. 
	- We define transformation matrix and denote it as $R$. So we have $XR = Y$. We minimize the distance between XR and Y, in order to get R.
	- The nice thing is, you can just collect a subset of translation, to find your transformation matrix. And it works well, the model can be used to translate words that are not part of your original training set. 
---

---
