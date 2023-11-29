# Goal of the course
- 


# Lecture 1: Introduction, mapReduce, Spark

- To extract the knowledge data needs to be:
	- Stored [[cs107 computer organization and systems]]
	- Managed [[cs145 data management and data systems]]
	- Analyzed: This course
- Emphasis in CS246 on algorithms that scale -- parallelization often essential
- Data mining methods:
	- Descriptive methods
		- Find human-interpretable patterns that describe the data (eg: clustering)
	- Predictive methods
		- Use some variables to predict unknown or future values of other variables. (eg: recommender systems)

- Figure: data mining / machine learning pipeline
![[Pasted image 20230619212913.png]]

### Multiple aspects of the class
- High dimensional data: 
	- locality sensitive hashing, clustering, dimensionality reduction
- Graph data: 
	- page rank, simRank, GNN, spam detection
- Infinite data: 
	- filtering data streams, web advertising, queries on streams
- Machine learning: 
	- learning embeddings, decision trees, experimentations
- Apps: 
	- recommendation systems, association rules, duplicate document detection


# Large scale computing
- How do you distribute computation?
- Issues: 
	- Machine fail:
		- One server may stay up 3 years
		- If you have 1000 servers, expect to lose 1 per day.
		- With 1M machines 1000 machines fail everyday.
	- Copying data over a network takes time:
		- Bring computation to data
		- Store files multiple times for reliability
		- Spark / Hadoop address these problems
			- Storage infrastructure - file system
			- Programming model:
				- MapReduce
				- Spark
	- If nodes fail, how to store data persistently?
		- Distributed file system
		- Typical usage pattern
			- Huge files
			- Data is rarely updated in place
			- Reads and appends are common

### Distributed file system
- Chuck servers
	- File is split into contiguous chucks
	- Typically each chunk is 16 - 64 MB
	- Each chunk replicated (usually 2x or 3x)
	- Try to keep replicas in different racks 
- Master node
	- aka name node in Hadoop's HDFS
	- stores metadata about where files are stored
	- master nodes are typically more robust to hardware failure and run critical cluster services. 
- Client library for file access
	- Talks to master to find chunk servers
	- Connects directly to chunk servers to access data
- Reliable distributed file system
	- Data kept in chunks spread across machines
	- Each chunk replicated on different machines
	- Seamless recovery from disk or machine failure


### MapReduce
- MapReduce is a style of programming designed for
	- Easy parallel programming
	- Invisible management of hardware and software failures
	- Easy management of very large scale data
- It has several implementations, including Hadoop, Spark, Flink, and the original Google implementation just called MapReduce. 
- Steps of MapReduce
	- Map
		- Apply a user-written map function to each input element
		- The output of the map function is a set of 0,1 or more key-value pairs
	- Group by key
		- Sort and shuffle
		- System sorts all the key-value pairs by key, and outputs key-(list of value) pairs
	- Reduce
		- User-written reduce function is applied to each-(list of values)
- Environment
	- Takes care of 
		- Partitioning the input data
		- Scheduling the program's execution across a set of machines
		- Performing the group by key step, in practice this is the bottleneck
		- Handling machine failures
		- Managing required inter-machine communications
- Dealing with failures:
	- Map worker failure
	- Reduce worker failure
- Limitations of MapReduce
	- It is inefficient for problems where random (or irregular) access to data is required
		- Graphs
		- Interdependent data
			- Machine learning
			- Comparisons of many pairs of items

### Cost measures for algorithms
- Breakdown
	- Communication cost:
		- Total IO of all processes
	- Elapsed communication cost:
		- max of IO along any path
	- (Elapsed) computation cost:
		- Analogous, but count only running time of processes
- Cost of map-reduce join
	- Total communication cost: $O(|R| + |S| + |R \Join S|)$
	- Elapsed communication cost: $O(S)$

- Figure: map reduce pattern
![[Pasted image 20230619214637.png]]
![[Pasted image 20230619214716.png]]
![[Pasted image 20230619214730.png]]


### Spark - extends MapReduce
- Problem with mapReduce
	- Incurs substantial overheads due to data replication, disk IO and serialization
- 2 limitations of MapReduce:
	- Difficulty of programming directly in MapReduce
	- Performance bottlenecks, or batch not fitting the use cases. 
- Feature:
	- Expressive computing system, not limited to the map-reduce model
	- Additions to MapReduce model:
		- Fast data sharing
		- General execution graphs (DAGs)
		- Richer functions that just map and reduce
	- Compatible with Hadoop
	- Key idea: Resilient distributed dataset (RDD)
	- Higher-level APIs:
		- DataFrames and Datasets:

### DataFrame:
- Unlike an RDD, data organized into named columns
- Imposes a structure onto a distributed collection of data, allowing higher-level abstraction

### Dataset:
- Extension of DataFrame API which provides type-safe, object-oriented programming interface


### Data-flow systems
- Generalize MapReudce in two ways:
	- 1. Allow any number of tasks/ranks
	- 2. Allow functions other than Map and Reduce

### Resilient distributed dataset (RDD)
- partitioned collection of records
	- generalizes key-value pairs
- spread across the cluster, read-only
- caching dataset in memory
- RDDs can be created from Hadoop, or by transforming other RDDs
- RDDs are best suited for applicaitons that applu the same operation to all elements of a dataset

- Figure: representation of RDDs.
![[Pasted image 20230619215521.png]]

### Spark RDD operations
- Transformations
	- Build RDDs through deterministic operations on other RDDs
		- Functions includes:
			- map
			- filter
			- join
			- union
			- intersection
			- distinct
- Actions
	- Return value or export data
	- Functions includes
		- count
		- collect
		- reduce
		- save
	- Actions can be applied to RDDs, actions force calculations and return values

- Figure: Task scheduler - general DAGs
![[Pasted image 20230619215717.png]]

- Figure: Data analytics software stack
	- Spark SQL
	- Spark streaming
	- MLlib
	- GraphX
![[Pasted image 20230619215144.png]]

- Problems suited for MapReduce
	- Working on a large web corpus, look at the metadata file
	- Link analysis and graph processing
	- Machine learning algorithms 
	- Statistical machine translation
		- Need to count number of times every 5-words sequence occurs in a large corpus of documents

### Map-reduce join


- Figure: map-reduce join example
![[Pasted image 20230619220701.png]]


---
# Lecture 2: Frequent itemset mining

- Background
	- Typically, data is kept in flat files rather than in a database systems
		- Stored on disk, busket-by-basket
		- Baskets are small but we have many buskets and many items
- Computational model
	- The true cost of mining disk-resident data is usually the number of disk IOs.
	- We measure the cost by the number of passes an algorithm makes over the data.
- Main memory bottleneck
	- For many frequent-itemset algorithms, main-memory is the critical resource
- Finding frequent pairs
	- The hardest problem often turns out to be finding the frequent pairs of items $\{ i_1, i_2\}$
		- Freq pairs are commons, frequent triples are rare
			- Probability of being frequent drops exponentially with size.
	- Lets first concentrate on pairs, then extend to larger sets.
- Algorithm
	- Naive approach
		- counting the occurrences of each pair, with nested loop
			- generates its $n_b ( n_b - 1) / 2$ pairs by two nested loops
- Counting methods
	- Method 1. Using a methods
	- Method 2. Keep a table of triples, `[i,j,c]`, which $c$ is the occurence.
- Comparing 2 methods
	- Method 1
		- 4 bytes per pair
		- $n(n-1)/2 \implies O(n^2)$
	- Method 2
		- 12 bytes per occurring pair

- Algorithm for the problem
	- A-priori algorithm
	- PCY algorithm

---
# Lecture 3-4: Locality-sensitive hashing

- [[Jaccard similarity]]

- Finding similar items
	- Applications - similar documents
	- Shingling
		- Convert documents, emails etc to sets
	- [[Minhashing]]:
	- Locality-sensitive hashing
		- Focus on pairs of signatures likely to be similar


- Figure: the big picture of finding similar documents
![[Pasted image 20230619231831.png]]


[[Shingling]]


- Figure: column similarity
![[Pasted image 20230619232726.png|300]]

### Minhashing
- Jaccard similarity
	- $Sim(C_1, C_2) = \frac{|C_1 \bigcap C_2|}{|C_1 \bigcup C_2 |}$
- From sets to Boolean matrices
	- Rows = elements of the universal set
	- Columns = sets
	- 1 in row $e$ of that set if and only if $e$ is a member of that set, else $0$.
- What is minhashing
	- Permute the rows, thought experiment, not real
- minhash function
	- For this permutation, $h(C)$ = the number of the first row in which column $C$ has 1. 
- Apply, to all columns, several randomly chosen permutations to create a signature for each column.
- Result is a signature matrix
	- columns = sets
	- rows = minhash values, in order for that column
- Similarity for signatures
	- The similarity of signatures is the fraction of the minhash functions in which they agree. 
	- Thus, the expected similarity of two signatures equals the Jaccard similarity of the columns or sets that the signatures represent.

- Figure: minhashing
![[Pasted image 20230619233626.png|300]]

### Locality-sensitive hashing (LSH)
- Application
	- Entity resolution
	- Similar news articles
	- Distance measures
		- Triangle inequality
		- Euclidean distance
		- Cosine distance
		- Jaccard distance
		- Edit distance
	- An LSH family for cosine distance
		- Random hyperplane sketches (signatures)
	- LSH families of hash functions
		- Definition
		- Combing hash functions
		- Making steep S-curves



---
# Lecture 5: Clustering

### Clustering
- Problems:
	- Clustering in high dimensions are hard
		- Almost all pairs of points are very far from each other --> the curse of dimensionality.
- Applicastion:
	- Galaxies
	- Music CDs
		- Music can be divided into categories, and customers prefer a few genres. 
			- Represent a CD by a set of customers who bought it
				- Space of all CDs....
				- Find topic:
					- Represent a document by a vector
					- Documents with similar sets of words may be about the same topic
			- Similar CDs have similar sets of customers, and vice versa
- Clustering strategies
	- Hierarchical 
	- Point assignment
	- Euclidean or non-Euclidean space
	- In-memory clustering versus large-data clustering

### Hierarchical clustering

### k-means clustering

### BFR algorithm

### CURE algorithm






---
# Lecture 6: Dimensionality reduction

### Singular value reduction

### CUR decomposition



---
# Lecture 7-8: Recommender systems

- Figure: performance of various methods
	- Netflix prize
	- The winner of netflix prize adopted such methods
![[Pasted image 20230620002124.png]]
![[Pasted image 20230620002432.png]]
- Types of recommendations
	- Non-personalized
		- Editorial and hard curated
		- Simple aggregates
	- Personalized recommendations
		- Tailored to individual user
		- Amazon, Netflix, Youtube ... 

### Content-based recommender systems

### Collaborative filtering


### Latent factor model
- finding the latent factor
- The effect of regularization 


---
# Lecture 9: Page rank


---
# Lecture 10: Extensions of PageRank to Recommendations and Spam

---
# Lecture 11: Community detection in graphs

---
# Lecture 12: Graph representation learning


---
# Lecture 13: Graph Neural Network


---
# Lecture 14: Learning embeddings


---
# Lecture 15: Decision trees


---
# Lecture 16: Mining data streams

---

# Lecture 17: Matrix sketching


---
# Lecture 18: Computational advertising


---
# Lecture 19: Optimizing submodular functions 

