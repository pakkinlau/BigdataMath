Document similarity analysis is a critical task in various fields including information retrieval, text mining, and natural language processing. Shingling is a widely used technique in document similarity analysis. 

**Shingling** is a process of transforming a document (or any sequence of items) into a set of its constituent subsequences of a given length. These subsequences are often referred to as "shingles" or "n-grams". For instance, if we're working with character-level shingling of length 3 (3-shingles), the string "hello" would be broken down into the following shingles: "hel", "ell", "llo".

Shingling can also be performed at the word level. For example, the sentence "The quick brown fox" could be broken down into the following 2-shingles (or bigrams): "The quick", "quick brown", "brown fox".

The resulting sets of shingles can be used to evaluate the similarity between documents. One common approach is to use Jaccard similarity, which is the size of the intersection of the shingle sets divided by the size of their union. 

Here's the formula for the Jaccard similarity:

```
Jaccard similarity(A, B) = |A ∩ B| / |A ∪ B|
```

Where `A` and `B` are the sets of shingles for two documents.

This approach is particularly efficient for large-scale, high-dimensional data because it allows us to estimate document similarity without directly comparing every element of the documents. Instead, we can compare the smaller, more manageable sets of shingles.

---
- Shingles
	- A "k-shingle" (or "k-gram") for a document is a sequence of k characters that appears in the document. 
		- eg: k=2, doc = abcab, set of 2-shingles = `{ab,bc,ca}`
		- Represents a doc by its set of k-shingles
- Documents that are textually similar will have many shingles in common.
	- Changing a word only affects k-shingels within distance k-1 from the word.
	- Reordering paragraphs only affects the 2k shingles that cross paragraph boundaries.
- Compression options:
	- Want enough possible shingles that most docs do not contain most shingles
		- k = 8~10 shingles is often used in practice.
- Tokens
	- To save space but still make each shingle rare, we can hash them to 4 bytes, called "tokens"
	- Represent a doc by its tokens, that is, the set of hash values of its k-shingles. 
	- Two documents could rarely appear to have shingles in common, when only hash-values were shared. 