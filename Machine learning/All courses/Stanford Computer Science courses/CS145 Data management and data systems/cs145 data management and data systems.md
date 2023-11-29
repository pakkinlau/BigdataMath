1234

---
# Ch1 Introduction

### System primer

- Figure: IO systems hierarchical structure
![[Pasted image 20230614205145.png|300]]

### IO blocks:
- What is it?
	- IO blocks refer to the allocation and organization of data 
	- It is fundamental units of storage in digital systems, particularly in field-programmable gate arrays, and application-specific integrated circuits.
- Why block structure can improves performance
	- 1. Parallelism
		- ach block can be independently designed, implemented, and optimized. This parallelism allows for better utilization of available resources and can lead to improved overall system performance.
	- 2. Modularity and reusability
		- Each block can represent a self-contained unit with well-defined interfaces. This modular design allows for easier maintenance, debugging, and testing. 
	- 3. Design partitioning 
		- Breaking a system into blocks facilitates design partitioning, where different blocks can be assigned to different teams or designers. This division of labor can lead to more efficient development and optimization of each block.
	- 4. Hierarchical abstraction
		- Block structures enable hierarchical abstraction, which simplifies the design process. Complex systems can be decomposed into hierarchies of blocks, with higher-level blocks representing larger functionalities and lower-level blocks representing more detailed operations. 
	- 5. Scalability
		- Block structures facilitate scalability by allowing the system to grow and evolve. New blocks can be added or existing blocks can be modified without affecting the entire system. 
	- 6. Design optimization 
		- Blocks can be individually optimized to achieve the best performance for their specific functionality. By focusing on optimizing each block separately, designers can leverage specialized techniques and algorithms to achieve superior performance. 
- Why it is efficient:
	- Proximity to external devices
	- Dedicated circuitry
	- Reduced logic utilization
	- Improved timing and performance
	- Simplicity and flexibility

- Figure: IO blocks for efficiency
	- Data
	- Partition into IO blocks
	- TO store 1GB data, we partition the data, and store in IO blocks
![[Pasted image 20230614205207.png|300]]




- Figure: Basic system numbers
	- Why are they different speed?
		- 1. Digital (SSDs and RAM) versus analog (HDD seeks)
		- 2. Distance from CPU
![[Pasted image 20230614212913.png|400]]

### IO cost model
- Access latency
	- Time to access block's start location
- Scan throughout
	- Speed to run + copy data to RAM
- Estimating the reading speed 
	- `Total time to read data = accessLatency * M  + DataSize / ScanThroughput`
		- `m` = number of non-contiguous blocks
		- access latency = the time it takes for the storage system to locate and retrieve the requested data. 
		- scan through put = the speed at which the storage system can transfer data from the storage medium to the reading device
		- data size = Data Size refers to the total amount of data that needs to be read from the storage system
	- This equation, however, does not account the specific structure of the data or the access pattern required to traverse the structure. 
		- Algorithms used to access the data
		- Caching mechanism
		- Hardware optimization

### Data size
- Example: database
	- 4 columns (`int32`, `char100`, `char200`, `char700` $\rightarrow$ 4+100+200+700 per row)
	- 20 row = 1004 x 20 = 20080 bytes 
	- This data size is fixed, as database assumed to be dense array?

### Cost estimation on storage and computation in cloud
![[Pasted image 20230614221133.png]]

---
# Ch2-3 SQL 

- Simple DB == spreadsheets

### Data model
- Types:
	- Network model
	- Object-oriented model
	- Entity-relationship model
	- Document model
	- Columnar model
	- Key-value model
	- Semantic model
	- Relational model
	- Hierarchical model

---

### Relational model
- a conceptual framework for organizing and representing data in a relational database management system (RDBMS). 
- It was introduced by E.F. Codd in 1970 and has since become the most widely used data model for managing structured data.
	- Relation / table: a multiset of rows, with columns
	- Schema: The table name, its columns, and their types

### Hierarchical model (aka JSON-like trees)


### Semantic model
- a representation of data that focuses on the meaning and relationships between different data elements. It is designed to capture the underlying semantics or semantics of the data, which relates to the interpretation and understanding of the data within a specific domain or context.
- Breakdowns:
	- In a semantic model, data elements are typically represented as entities, which are objects or concepts with distinct attributes that define their properties. 
	- Relationships between entities are defined through associations, which describe how entities are connected or related to each other. 
		- These associations can represent various types of relationships such as inheritance, composition, or aggregation.
	- Additionally, a semantic model often includes constraints and rules that govern the behavior and integrity of the data. 
		- These constraints can enforce data validation, define data dependencies, or specify business rules that need to be followed.



### SQL
- It is a standard language for querying and manipulating data
- It is a very high level programming language
	- This work because it is optimized well.


### SQL operations
- SFW query:
	- Select `<attribute>` FROM `<one or more relatuons>` WHERE `<condition>`
- Selection
- Projection
- Like:
	- Simple string pattern matching (`LIKE` keyword associating with `%...%`)
		- `SELECT * FROM Products WHERE PName LIKE '%...%'`
- DISTINCT:
	- Eliminating duplicates
- ORBER BY:
	- sorting the results

- Figure: notation of input schema and output schema
![[Pasted image 20230614221922.png|400]]

### SQL features
- Keys:
	- A key is a minimal subset of columns that acts as a unique identifier for tuples in a relation

### Data independence
- Logical data independence
	- Can we add a new column or attribute without rewriting the application?
		- Yes, logical data independence. 
- Physical data independence
	- Should you care which disks are the data stored on?
		- No. Physical data independence
		- Which we query a database, we don't have to specifies which disk we are querying. When we put the database somewhere, the database would take care of itself about the way of accessing the memory addresses.

### Multi-table queries
- I should learn this deeply, because graph database queries are the extreme of such operations -- which navigate multiple nodes with foreign key pointers. 
- Foreign key constraints
- Joins basics
- Joins - SQL semantics

### Other SQL features
- NULLS
- JOINs
- Aggregations and group by

### Multiset
- A multiset is an unordered list (a set with multiple duplicate instances allowed)

- Figure: multiset
![[Pasted image 20230618052149.png]]

- Figure: semantics of JOINs
![[Pasted image 20230618052120.png]]
![[Pasted image 20230618052249.png]]

### Grouping and aggregation
- Keywords:
	- Group by
	- Having
- General form of grouping and aggregation
	- `select S from R1, ... ,Rn where C1 group by a1, ... , ak having c2`

### Common table expressions

### SET operator

### Nested queries
- Output of one query can be input to another query, we call it nesting. 
- How?
	- 1. Common table expressions (CTEs)
	- 2. Sub-queries offer another tool
	- 3. Trade-offs: read blog on CTE vs sub-queries

### Sub-queries

- Figure
![[Pasted image 20230618053003.png|700]]



### Equivalent queries
- Can write different SQL queries to solve same problem



---
# Ch4 SQL advanced (How does SQL works, optimizing the SFW RA plan, relational algebra)


### How SQL works?
- Steps of SQL execute querying:
	- SQL query
		- a declarative query from user
	- Relational algebra (RA) plan
		- translate to relational algebra expression 
	- Optimized RA plan
		- find logical equivalent but more cost-efficient RA expression
	- Execution
		- execute each operator of the optimized plan

- Figure:
	- A representation of the workflow of a SQL query
![[Pasted image 20230620230416.png]]

### Relational algebra
- Five basic operation
	- Selection ($\sigma$)　
		- (aka, row filtering)
		-  The selection operator filters tuples from a relation based on a specified condition. It retrieves all tuples that satisfy the given predicate. 
			- For example, σ(age > 30)(Employees) selects all tuples from the "Employees" relation where the age is greater than 30.
	- Projection ($\Pi$)
		- (aka, column filtering)
		- The projection operator selects specific attributes (columns) from a relation, discarding the rest. It returns a new relation with only the specified attributes.
		- It is a multiset operation, which means duplicate elements are allowed, and their frequency is reserved. 
			- For example, π(name, age)(Employees) retrieves a new relation with only the "name" and "age" attributes from the "Employees" relation.
			- It just simply cut a slice vertically, the frequency of the data is preserved, eg, "Alice, Bob, Alice"
	- Cartesian product ($\times$)
		- the Cartesian product is an operation that combines two relations to form a new relation by pairing each tuple from the first relation with every tuple from the second relation.
		- The result is a relation that contains all possible combinations of tuples from the two input relations.
		- eg1: Tablet representation of 2 relations
			- $R(A,B) \times S(C,D) = T(A,B,C,D)$ 
			- Cardinality of $R$ = 2, cardinality of $S$ = 2
			- The resulting relation $T$ will have a cardinality equal to the product of the cardinalities of $R$ and $S$ $= 2 \times 2 = 4$. 
		- eg2: CROSS-JOIN
			- Table 1: (1, 'apple'), (2, 'banana')
			- Table 2: ('red', 10), ('green', 20)
			- Table 1 JOIN Table 2
				- (1, 'apple', 'red', 10), (1, 'apple', 'green', 20) (2, 'banana', 'red', 10) (2, 'banana', 'green', 20)
				- Each tuple from Table 1 is paired with every tuple from table 2, resulting in a new relation with all possible combinations. 
	- Union ($\bigcup$)
		- The union operator combines two relations with the same schema, returning a new relation that contains all tuples from both relations, removing duplicates. 
		- The relations must have the same attributes. 
			- For example, R ∪ S returns a relation that contains all tuples present in both R and S.
	- Difference ($-$)
		- The set difference operator subtracts tuples of one relation from another relation, producing a new relation with tuples that exist in the first relation but not in the second. The relations must have the same schema. For example, R - S returns a relation with tuples that are present in R but not in S.
- Derived or auxiliary operator
	- Intersection ($\bigcap$)
		- The intersection operator returns a new relation that contains only the tuples that are common to both input relations, removing duplicates. Again, the relations must have the same schema. For example, R ∩ S returns a relation with tuples that exist in both R and S.
	- Joins ($\Join$)
		- The join operator combines tuples from two relations based on a common attribute (or set of attributes) and returns a new relation. There are different types of joins, including inner join, left join, right join, and full outer join. The result of a join is determined by the matching condition specified. For example, R ⨝ S on the attribute "ID" returns a relation with tuples that have matching values for the "ID" attribute in both R and S.
		- Examples:
			- Inner join
				- It results a bigger table, which we need to specifies which columns in one table is equal to which columns in another table. 
				- https://www.w3schools.com/sql/sql_join_inner.asp
			- Left Join, Right Join, Full outer join
				- They returns all rows of records in table 1 / table 2 / table 1+2, no matter the condition of ON clause is fulfilled or not. 
				- Application:
					- 1. Analyzing data gap - identify missing or incomplete data by examining NULL values in LEFT / RIGHT / FULL OUTER join.
						- eg: `SELECT * FROM tableA LEFT JOIN tableB ON ... WHERE primary key of tableB is NULL;`
					- 2. Retaining unmatched records / combining data from multiple source
					- 3. Flexible query design / avoid data loss:
						- OUTER JONS provide flexibility in query design as 
			- Cross join
	- Renaming ($\rho$)
		- The rename operator is used to change the name of attributes or relations in a given relation. It returns a new relation with the same tuples but with updated names. For example, ρ(`newName/oldName`)(R) changes the attribute name "`oldName`" to "`newName`" in relation R.
	- Natural join ($*$)
		- Compare with cross join:
			- A natural join combines rows based on matching column names, whereas a cross join combines every row from one table with every row from another table without any condition.
		- The natural join operator combines tuples from two relations based on matching attributes and returns a new relation. 
		- It automatically matches the attributes with the same name in both relations. For example, R ∗ S returns a relation with tuples that have matching values in attributes with the same name in both R and S.



## RA Plan (Relational algebra plan)
- The sequence 
	- Bottom-up tree traversal is the order of operation execution.
	- That is how we interpret the RA plan

- Figure: converting SFW query to RA
![[Pasted image 20230618053346.png]]

### Logical optimization of Relational algebra plan
- Rules:
	-  Selection Pushdown: 
		- Push down selection operations as early as possible in the query plan to reduce the amount of data processed. This involves applying selection predicates before expensive operations such as joins or aggregations.
	- Projection Pushdown: 
		- Push down projection operations to minimize the amount of data transmitted through the system. Eliminate unnecessary columns early in the plan to reduce I/O and memory requirements.
	- Join Ordering: 
		- Consider different join orderings to determine the most efficient sequence. Use techniques like cost-based optimization or dynamic programming to estimate the cost of different join orders and choose the optimal one.
	- Join Algorithms: 
		- Choose the appropriate join algorithm based on the characteristics of the tables being joined. Common algorithms include nested loop joins, hash joins, and merge joins. The choice depends on factors such as table sizes, available memory, and indexing.
	- Indexing: 
		- Utilize appropriate indexes on the tables to speed up data access. Indexes can significantly improve query performance, especially for large tables. Create and maintain indexes on columns frequently used in selection, join, and sorting operations.
	- Aggregate Pushdown: 
		- Push down aggregation operations as early as possible to reduce the amount of data to be processed. This can involve applying aggregation functions on smaller subsets of data before joining or filtering.
	- Subquery Optimization: 
		- Optimize subqueries by rewriting them into more efficient forms, such as using joins or derived tables. This reduces the overall complexity of the query plan and improves performance.
	- Materialized Views: 
		- Identify opportunities to create materialized views, which are precomputed and stored query results. Materialized views can speed up query execution by avoiding expensive computations, especially for complex and frequently executed queries.
	- Statistics and Cost Estimation: 
		- Maintain up-to-date statistics about the data distribution and cardinality of tables. Accurate statistics help the query optimizer estimate the cost of different query plans and make informed decisions about optimization techniques.

### Rules in relational algebra that speeding up the query execution cost
- 1. Push down projection as early as possible:
	- By applying selections early, unnecessary columns can be filtered out.
- 2. Selection pushdown: 
	- By applying selections early, unnecessary rows can be filtered out.
- 3. Join commutativity: 
	- This rule states that the order of joins does not affect the result, so the query optimizer can reorder joins to select the most efficient join order. Reordering joins can minimized the intermediate result size and improve performance. 
- 4. Projection elimination
	- If a projection operation is followed immediately by another projection operation that includes all the attributes of the first projection, the optimizer can eliminate the redundant projection operation. This rule helps reduce unnecessary processing and improve query performance.
- 5. Cartesian Product Elimination: 
	- If a join condition is a tautology (always true), the optimizer can eliminate the join operation and perform a Cartesian product. This rule can be applied when join conditions involve constant values or attributes that have a functional dependency.
		- Constant value: `talbe1.attribute = 10`
		- Functional dependency: `table1.attr1 = table1.attr2 + 5`
	- By eliminating the join operation and using a Cartesian product, the optimizer can avoid unnecessary comparisons and simplify the query plan, potentially improving performance. 
- 6. Indexing
	- The query optimizer can utilize indexes on tables to speed up query execution. 
	- By selecting appropriate indexes and using index access methods such as B-tree or hash indexes, the optimizer can efficiently retrieve the required data without scanning the entire table.
- 7. Cost-based optimization
	- This approach involves estimating the cost of different query plans and selecting the plan with the lowest estimated cost. 
	- The optimizer considers factors like data distribution, available indexes, join selectivity, and system resources to determine the optimal query execution plan.
	- Steps:
		- 1 Query parsing and transformation
			- first parses and transforms the query into an internal representation, typically a query tree or a query graph. This representation captures the logical structure of the query.
		- 2 Plan generation
			- The optimizer generates multiple alternative execution plans for the query. These plans represent different ways of executing the same query, such as different join orders, access methods, and join algorithms.
		- 3 Cost estimation
			- For each generated plan, the optimizer estimates the cost of executing that plan. The cost is usually measured in terms of time or resource usage, such as CPU cycles, I/O operations, or network traffic. The cost estimation is based on statistics about the database objects, such as table sizes, index selectivity, and distribution of data values.
		- 4 Plan comparison and selection
		- 5 Plan execution
- 8. Join decomposition:
	- When a query involves multiple joins, the optimizer can decompose complex joins into a series of simpler joins. This decomposition can create smaller intermediate results and enable the optimizer to choose more efficient join strategies.
	- Steps:
		- 1. Join order generation
		- 2. Cost estimation
		- 3. Cost comparison, and join strategy selection 
	- How the cost is reduced
		- 1. Intermediate result size reduction
		- 2. Join strategy optimization
		- 3. Parallel execution opportunities
- 9. Semi-Join and Anti-Join: 
	- If a join operation is followed by a selection on one of the participating tables, the optimizer can use a semi-join or anti-join strategy. 
	- A semi-join returns only the attributes from the left table that satisfy the selection condition, while an anti-join returns only the attributes that do not satisfy the condition. These strategies reduce the size of intermediate results and improve performance.
	- How the cost is reduced
		- By using a semi-join, the optimizer reduces the size of the intermediate result, as it retains only the relevant rows from the left table. 
- 10. Union Decomposition: 
	- If a query involves a union operation, the optimizer can decompose it into smaller subqueries that can be executed independently. By decomposing the union, the optimizer can parallelize the execution and optimize each subquery separately.
- 11. Materialization: 
	- The optimizer can choose to materialize intermediate results in temporary tables or indexes. 
	- Materialization involves storing intermediate results of a query in temporary tables or indexes. Instead of recalculating the same intermediate result multiple times within a query, the optimizer chooses to store it temporarily and reuse it as needed. 
	- How the cost is reduced:
		- Materialization can be beneficial when the same intermediate result is required multiple times in a query or when the intermediate result is expensive to compute. By storing the intermediate result, the optimizer avoids redundant computations and improves query performance.
	- How materialization works in practice
		- 1. Identification
		- 2. Temporary storage
		- 3. Computation and storage
		- 4. Reuse and optimization
		- 5. Cleanup
- 12. Aggregate Pushdown: 
	- Similar to projection pushdown, aggregate pushdown involves pushing aggregate operations (e.g., SUM, AVG, MAX) as early as possible in the query plan. By performing aggregates early, the optimizer can reduce the amount of data that needs to be processed in subsequent operations.
- 13. Subquery Optimization: 
	- The optimizer can optimize subqueries within a larger query. This may involve rewriting subqueries to more efficient forms or applying other optimization techniques specific to subqueries, such as subquery unnesting or subquery materialization.
	- Example:
		- Subquery unnesting
		- Subquery materialization
		- Subquery rewriting
		- Subquery predicate pushdown
		- Subquery aggregation
		- Subquery caching
- 14. Parallel Execution: 
	- In a multi-core or distributed environment, the optimizer can parallelize query execution by dividing the workload among multiple processing units. Parallel execution can significantly improve performance for queries that involve large datasets or complex operations.


- Figure: How we interpret a RA plan 
![[Pasted image 20230618053439.png]]


---
# Ch5 Scaling a database, indexing, IO model

### DB buffer
- A buffer is a part of physical memory used to store intermediate data between disk and processes
- DB maintains its own buffer
	- DB knows more about access patterns
	- Recovery and logging require ability to flush to disk
	- Buffer manager handles page replacement policies
- DBs typically set RAM page size equals to IO block size (eg: 64MBs). In this case, we will use page IO block, disk block interchangeably.

- Figure
![[Pasted image 20230618060938.png]]

### Data layout
- Row stores
	- Data is stored and retrieved row by row.
	- Advantages:
		- Row stores are generally well-suited for transactional systems where the entire row of data is frequently accessed or updated. They work efficiently when there is a need to retrieve or modify complete records.
		- Row stores are more suitable for transactional systems where the focus is on quickly accessing and modifying complete records.
- Column stores:
	- In a column store, the data is stored and retrieved column by column. Instead of storing all the columns of a row together, column stores store each column separately, grouping the values together. 
	- Advantages:
		- Column stores are particularly useful when there is a need to analyze or aggregate specific columns of data across multiple rows. 
		- They excel in scenarios where queries involve aggregations, filtering, or selecting a subset of columns from a large dataset.
		- Column stores generally provide better performance for analytical workloads and data warehousing scenarios where complex queries involving large volumes of data are common.
- example:
	- google index of web pages
		- URL: 100 bytes
		- pageRank: 8 bytes
		- Language: 4 bytes
		- Number of visitors: 4 bytes
		- HTML: 2 MBs * 5 versions
	- overall sized 10MBs per URL, stored in row format. 
	- Use case:
		- Hours to run query over 1 billion URLs.
			- Row based layout: processing 10MB *  1 billion URLs.
			- Column based layout: only need page rank (8 bytes) + `NumVisits` (4 bytes), that means only process (4+8) bytes * 1 billions URLs (~1 millions time faster)
		- Core idea: analytical queries usually focus on a few columns
		- In Google's index of web pages: 
			- column stores might be employed for analyzing and processing search query data, 
			- while row stores could be used to efficiently store and retrieve individual web page records with their associated metadata. 

- Figure: data layout
![[Pasted image 20230618061116.png]]

### Indexing
- Why study indexes?
	- Fundamental unit for DB performance
	- Core indexing ideas have become stand-alone systems
		- eg search in google
		- data blobs in noSQL, key-value stores
		- embedded join processing
- Kinds of indexes
	- Strings, integers
	- Time series, GPS traces, genomes, video sequences
	- Equality vs similarity, ranges, subsequences
	- Composites of above
- Types of indexes:
	- Primary: a set of columns that has no duplicates elements. 
	- Secondary: may have duplicates
	- Advanced: build across rows, across tables 
- Definition of indexes
	- Maps search keys to sets of rows in table
		- provides efficient lookup and retrieval by search key value
		- Key operations - lookup, insert, delete


### Organizing data and indices (big scale)
- Hashing, sorting solves "all" known data scale problems
	- Boost with a few patterns -- cache, parallelize, pre-fetch
	- Hashing
		- `hash(key) --> value`
		- eg: `hash("Apple") --> 5348`
	- Sorting
		- BucketSort, QuickSort, MergeSort


- Figure: Recall of hashing
![[Pasted image 20230618063547.png|400]]

### Hashing ideas for scale
- Multiple hash functions
- Locality sensitive hash functions (for k-dimensional data)
	- Special class of hash functions to keep spread 'local'

### Multiple hash function


### Locality sensitive hash functions (for k-dimensional data)


### External merge algorithm 
- The external merge algorithm is a technique used to sort data that is too large to fit entirely in memory. It is often employed when the size of the data exceeds the available RAM or when the data is stored on disk.
- The algorithm works by dividing the data into manageable chunks that can fit into memory. It then sorts each chunk in memory using an efficient in-memory sorting algorithm, such as quicksort or mergesort. Once the chunks are sorted, they are written back to disk.
- The external merge algorithm is efficient because it minimizes the number of disk accesses by keeping as much data as possible in memory during the sorting and merging phases. It is widely used in scenarios where the data is too large to fit in memory, such as sorting large databases or processing massive log files.
- Scenario:
	- How to sort 10TB files with 1GB of RAM?
	- How to search over 1 trillion items in <1 seconds, with index?
- Step-by-step breakdown of the external merge algorithm:
	- 1 Divide the input data into smaller chunks that can fit into memory. 
		- The size of the chunks depends on the available memory and the size of the data.
	- 2 Sort each chunk in memory using an in-memory sorting algorithm. 
		- This can be done using quicksort, mergesort, or any other efficient sorting algorithm.
	- 3 Write the sorted chunks back to disk. 
		- Each chunk is written to a separate temporary file.
	- 4 In the merge phase, read a fixed number of chunks (or blocks) from the temporary files into memory. This number depends on the available memory.
	- 5 Perform a merge operation on the chunks in memory. 
		- This can be done using a priority queue, where the smallest element from each chunk is selected and written to the output file. The merged data is then written to a new temporary file.
	- 6 Repeat steps 4 and 5 until all the chunks have been merged. 
		- If there are still chunks remaining on disk, read the next set of chunks into memory and continue the merge process.
	- 7 Once all the chunks have been merged, you will have a single sorted output file.

### External merge sort algorithm


### Calculating IO cost
- IO cost of sorting N pages = $2N(log_B \frac{N}{2B}) + 2N$

### Repacking - example optimiztion

---
# Ch6 Sorting, building indices 

- Index types
	- Hash tables
		- IO-aware hashing
	- B-trees
		- Very good for range queries, sorted data
		- Some old databases only implemeneted B-trees
		- We will look at a variant called B+ trees 


### IO aware
- For big files (bigger than RAM), we need efficient data structures that work with HDD/SSD IO systems.
	- An IO aware algorithm (and data structure)

### How to build indices
- How is data organized?
	- Is data in row or column store?
	- Is data sorted or not?
- How do we organize search values?


### How do we store index?
- Idea: index is just a table (rows/columns)
	- Store in pages
	- Persist on disk
	- Page into RAM buffer

### B+ trees
- Idea:
	- Search trees that are IO-aware
		- Store each tree-node in 1 page
		- Balanced, height adjusted tree
		- Make leaves into a linked list, for range queries
- Basics:
	- Exact search
	- Range queries
- Design and cost
	- How many search values per page?
	- How many levels in tree?
		- High fanout = lower IO
- Clustered indexes
	- An index is clustered if the underlying data is ordered in the same way as the index's data entries. 
	- For exact search, no difference between clustered or not-clustered. 
	- For range search, over R values, A random IO cost ~10ms. For R = 100k records, difference would be 10ms and 17min. 

- Summary of the chapter
	- Algorithms and some optimizations for sorting larger-than-memory files
		- An IO aware algorithm 
	- Create indexes over tables in order to support fast (exact and range) search and insertion over multiple search keys
	- B+ trees are one index data structures which support very fast exact and range search and insertion via high fanout. 
		- Clustered and non-clustered makes a big differences too. 

- Q: What is the index size for amazon's product catalog?

---
# Ch7-8 B+ Trees, query optimization

- Review relational algebra
- Nested loop join versus 
	- block nested loop join
	- index nested loop join
	- sort-merge join
- Hash join
- HashPartion joins
---
# Ch9 Guest lecture

---
# Ch10 Systems design 

- What statistics can I keep to optimize?
	- eg: selectivity of columns, values
- Histogram
	- A set of value range, and the frequencies of values in those buckets
	- How to choose the bucket
		- Equi-width and equi-depth
	- High frequency values are very important
	- Fundamental tradeoffs
		- Want high resolution
		- Want low space
	- Maintaining histograms
	- Compressed histograms


![[Pasted image 20230618075136.png]]

---
# Ch11 Exam review

---
# Ch12-15 Transactions


---
# Ch 16-17 ER model and design theory

- Start with relational schema
- Find functional dependencies (FD)
	- as constraints
- Use these to design a better schema

- Table decomposition
- Conceptual design
	- For a mega table
		- Search for bad dependencies
		- If any, keep decompsoing the tables into sub-tables until no more bad dependencies
		- When done, the database schema is normalized
- Inferring FDs
	- Armstrong's rules
		- Split/combine
		- Reduction
		- Transitivity

---



