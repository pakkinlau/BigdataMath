- Week 1 Natural lanugage

- PostgreSQL index types
	- Forward indexes
		- B-Tree
			- The default for many applications, automatically balanced as it grows
		- BRIN
			- Block range index - smaller /faster if data is mostly sorted
		- Hash
			- Quick lookup of long key strings
	- Inverted indexes related
		- GIN
			- Generalized inverted indexes - multiple values in a column
			- GIN indexes are the preferred text search index type.
			- Advantages:
				- Exact matches, efficient on lookup/search
			- Disadvantages:
				- Can be costly when inserting or updating data, because every new word is inserted somewhere in the index and can get large.
		- GiST
			- Generalized search tree
			- Hashing is used to reduce the size of and cost to update the GiST. 
			- A GiST index is lossy, meaning that the index might produce false matches, and it is necessary to check the actual table row to eliminate such false matches. 
			- There are performance / storage tradeoffs between GIN and GiST. 
		- SP-GiST
			- Space partitioned generalized search tree

- Forward indexes
	- You give the index a logical key and it tells you where to find the row that contains the key. (B-Tree, BRIN, Hash)
- Inverted indexes
	- You give the index a string (query) and the index gives you a list of all the rows that match the query. (GIN, GiST)

- Google search
	- Step 1: crawl - retrieve documents, parse them and create an inverted index
	- Step 2: search - take keywords, find the documents with the words then rank them and present results

---
- Inverted indexes of Natural Language - stemming and stop words
	- stop word and stemming
- 
