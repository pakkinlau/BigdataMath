[[Concepts about vault design 2]]





---
# Prototype

- Structural equation models
- Category theory representations model  
- Metadata-Dataview models 
	- Use some script to extract meaning from the content to populate metadata. Metadata represent a list of questions / prompts that would regularly concerning about that concept. 

---

# Conceptual design







---
# Technical design



---
# Difficulties of making this product

### Forming collections: Every objects could living in multiple classes of collections
- Sept 2022 
- Like a "square" in geometry, it could belongs to "rectangle", "parallelogram" , "shape", "a shape with right angle", "four-sided shape" etc. Unlike programming, one objects always following one class definition. 
- Maybe we can form a tree like universal dependency tree, to gather these abstract collections types. 

### One demonstration could be related to various concepts
- Sept 2022
- Draft solution: just classify that demonstration as "demonstration", and then link that demonstration to many concepts / sequence. 

### The link between entities
- The process of writing text to the notes is "writer dependent", which means the content is retrieved by the brain of the author. 
- But author won't be able to store the entities of the vault, so he might not realize he 

### One word can have multiple meaning in different context (easy to solve)






---
# Discuss how alternate notes can facilitate thinking










### Abstract thinking in learning
- 11 Feb 2023
- Knowledge mostly exists in the edges(connections) between entities.
- To learn edges well, human learns patterns of these massive number of edges. 
- "Pattern extraction + pattern dictionarying + pattern application" as a way of abstract thinking
	- In human language studies, we have a set of entities that is describing how people enhance its own expression by some formulas. Overall, learning the discovered patterns is a more effective way of learning knowledge. 
	- In learning human language, we have:
		- 1. Learn the annotation / labels for the smallest components
			- a. Grammatical annotation of single word: Noun
			- b. Small categories of words: Animals, Temperature etc.
		- 2. Discover some patterns from the corpus, directly. 
			- Say you want to speak like How famous person, like, Obama. You collect a lot of corpus from him.
			- You find the pattern within the corpus. Pattern searching only possible if the list of "basic pattern" is already inside the agent.  (This step is important)
				- For human, it is easy to discover new patterns from old patterns they have already got.  (This step is important)

### Scalability of knowledge: could a language expand itself?
- Instead of creating a set of tools, we create a set of rules, that enable the users to define their own tools by a set of operations. 
- How to came from:
	- Inspired "Growing a language", a smaller language that could stick for the users. But that small language would be unable to fit the need of the user very quickly. Similarly, if the tutorial session / the skills is limited to a specific kind of task, the student will be harder to transfer the skill to other field.  

### Dependence of prior knowledge
- Human interpret the concepts by associating the existing knowledge they have. That is the way human can consume less words, but still can more or less predict what the speaker is trying to deliver. 
	- Knowledge has certain aspect that are transferable. That is why reading a certain amount of knowledge could helps the readers to understand another field of knowledge. 

### Decomposition quadratically decrease the complexity of the problem
- By reducing the size of a block of words, we tend to make that block of words easier to understand. 
- From software design principle: 
	- as the size of problem increase, the difficulty of it will quadratically increase.

### Creativity and knowledge creation 
- 11 Feb 2023
- Most of the important paradigm shifts in science, or great humors from multi-media, are coming from experimentations of connecting different kinds of relationships to the entities in the context. 
- Other factors:
	- Creativity? Imagination? Intuition?
		- Can we oversimplify them as "solely to pattern recognition and random triggers"?
- Example
	- Person who are having higher intelligence in art, humor, math sense, are those who are not only could sum up the pattern from repeated event, but also coming up with hypothesis and to verify it. 
		- A humor person would tries to move attention to an angle that is unreasonable, then tries to verify it very soon.
		- A scientist would tries to make hypothesis that's something not merely exists. 


###  Diversity of note format 

- There should be at least 2 kinds of notes format. (a) Flexible notes. (b) Concept extracts notes.
- These notes has more value when they are connected to other types of notes.
	- The smaller the collection is, the faster the search will be, and easier to retrieve information from the database.
	- However, we could not simply delete all records from the raw source of information because most of the time many associating records are trying to demonstrate / making sense of how a concept is valid. So giving examples are always value added. 
- To enable connectivity between notes, we enforce objects creations, and object means there are rules that guiding the creation of higher level notes. 


### Category theory
- 1-10-2022:
	- It is possible to follow [[category theory|category theory]] to organize the folder ordering of notes. 
		- 1. Since programming is a kind of thing that [[category theory|category theory]] capable to analyze, we have:
			- Some obvious functional notes like [[Decoder]], [[GloVe]]
		- 2. Observed there are more than 1 type of category in the notes. 
			- Some are not included in the category of "machine learning programming". EG: GloVe could be an object in machine learning programming script, but "Loss of information" would not be an object in a machine learning programmign script.

### Categories: 
- Written in (13-11-2022)
	- 1. All notes should have a template which forms up the abstract characteristics of each note type.
	- 2. There are some pre-defined ordering between different note types. 
		- There are some guiding function that guides the information extraction process from the former type to the latter type. 
			- This idea comes from category theory.
			- The step of generating extracts from the original article copies, should have a routine process that guiding the attention of the agent. 
		- Providing structure is costly, but it reduces entropy of the article. 
			- While classifying which sentence is a topic sentence, in a language examination, and is a NLP tasks in machine learning. Keep using and following templates would adds up more dimensions/features to our production, which facilitates our content coverage (writing) and information retrieval (reading) efficiency. 

### Dimensionality of information?
- 2 Oct 2022
- This part is written in early stage, which is doubtful for now. 
- Each level is a superset of the next item?
	- Library ( = a set of books, papers")
	- Paper  ( = a set of reasonings. with a categorization of "Subject / theme")
	- Reasonings ( = a set of relations and entities pairs / proposition + implications, with a categorization of "Arguments / Lemma")
	- Relations and entities ( = a set of nodes, with a categorization of "node type" + a set of links, with a categorization of "link type")
		- Metadata (eg: author, date) co-exists with the smallest entities-relation pairs. 
	- Discussion of the above structure
		- We take Library > paper as an example. 
		- 1. Each level,  each objects (eg libraries, books) would have a specific purpose (eg: geotechnical library: = a collection of books
		- 2. but each objects would have its own discreteness, and they differentiate themselves with a categorization header,  and we can use these headers to sort out some order for the set of object. 
		- 3. The upper level domain provides a "context" for each lower level domain.

### Context
- Oct 2022?
![[thumbnail - Copy.jpg|500]]
- Fig: Most of the articles that is written by some authors. 

---
# Technical features about knowledge-retaining 

### Neck
- I think there should be a type of metadata that explains why certain edge/node is related to the context / concern, that enforce relevance of the content. 
- Example:
	- Goal of this page is to write down the concepts about designing good vault
	- Then this section is about technical features about the design.
	- Then there is an object "Extra-linguistic entity" inside that section. 

### Extra-linguistic entity
- From NLP perspective, we know "most words are just symbols for an extra-linguistic entity", which means words are signifier that maps to a signified idea / thing. 
	- The vocabulary we have is always less than the total amount of facts (or, extra-linguistic entity) we have in the reality. 
	- example: Chimpanzee learns 100 hand signs as his language, which is his vocabulary. He later expands his expressions by combining/borrowing words that has the similar image/pronunciation. 
- The objective concept model is not creating a model for meta-language. Languages are just signs that trying to make a narrower view of those concepts. Combining views from more people the views then there is a chance the views could be more complete. 
	- The way of thinking about the model is, imagining languages and speech is just a narrower view of the relationship of entities. 
	- Language means the set of words, plus the rules that interpreting the combinations of words. . Hand language / signs / text / voice are the signature of the expression. 

---


### Software Layout
- 30-9-2022: modifed
![[Pasted image 20220930030853.png]]
- Figure: the structure of the note right now. 

![[Pasted image 20220930030524.png]]
- Figure: The workflow of the Obsidian right not. 


### Hyperparameters while learning
- 6/4/2023
- As a human learner, deliberately recognize the number of possible options or concepts to be learned, can be beneficial for human learners.
	- It is like change the hyperparameter
	- having an understanding of the number of possible options or concepts to be learned can be beneficial for human learners as well.
	- By understanding the scope and complexity of a learning task, learners can adjust their learning strategies and allocate their time and resources more efficiently.
	- Having an awareness of the number of possible options or concepts can also help learners identify and prioritize the most important information to learn, rather than getting bogged down in details that may not be as relevant or useful.

### Constraints are information
^7a8db8
- 5/4/2023
- If we enforce limitations on the data formats, the usefulness of that object increase. 
 - Information theory
	 - Measures the amount of uncertainty or randomness in a system.
	 - In the context of alphabets and language, entropy is a measure of the unpredictability or complexity of a message. The entropy of a message is directly related to the number of possible sequences of symbols that could convey the same information.
	 - While Chinese words contains the most variety within a character, which means it could provides the most amount of content by Chinese language. But, in computer environment, Chinese cannot be typed easily with keyboard. So eventually English becomes the prominent language for programming.  
	 - In general, length of message and amount of information is a tradeoff. To convey more information, a message typically needs to be longer
- Example 1:
	- Data formats (Plain text, images requires a more complex processing algorithms), Gene expression (For proper cellular differentiation and function ), Grammar (Reduce ambiguity, because meaning could be context-dependent, and sometimes adherence to strict grammar rules)
- Example 2:
	- Combinatorics of alphabets:
		- By analyzing the frequency of certain letters or combinations of letters, we can gain insights into the language, style and authorship of the text.
		 - The properties of the alphabet can be used to encode or decode messages.
- Example 3:
	- Rules of languages
		- The rules of languages enable us to use a smaller collection of vocabulary to deliver what we meant. With more rules are using, the language are said to be more mature. 
			- The rules of languages includes
				- Types of words (word form): That expand the applicability of a single word to represent an action / noun / adjective etc. 
				- Fixed word-type sequence in a sentence: That rule is like a decoder of word forms. Sort the meanings of the sentence back from the numerous combinations it is possibly be. 
- Application: 
	- Rules of concepts 
		- The rules of language and the rules of concepts should be totally different. Because their mission is different. The mission for the rules of language is to deliver the correct description. The mission for the rules of concepts is to deliver correct understanding. 
			- Obviously there are a branch of language expression that is obviously 'orthogonal' to the delivery of the understanding of concepts. 
		- Example: rules in mathematics

### (Data-)Structure helps reading, too
- Oct 2022?
	- How structure could helps reading?
		- 1. Traditional perspective: Putting headings at every block of words, could helps the readers to decide whether the following content is useful for him. That brings the speed of reading to the question of "searching tree" problem. Each node is a table of headings.
		- 2. Computational perspective: Certain data structure is needed for a computer to query the information to answer certain question for a reader. 
	- Demonstration (Traditional perspective):
		- Fig 1: An article. With paragraphs. Full stops. Headings. Which expects the reader would pays attention to read every lines.
		- Fig 1B: Learnt from university lecture notes, putting concepts into 3x3 tablet. 
		- Fig 2: point form. But each heading is still a very long sentence. Each heading summarizes the content of its underlying block of sentences. That helps the reader to decide whether it is fitting their need and read it. 
		- Fig 3: Entity based content extraction
![[Pasted image 20230104122221.png|250]]![[Pasted image 20230104190621.png|250]]
![[Pasted image 20230104121006.png|250]]![[Pasted image 20230104121439.png|250]]


### Averaging the appearing frequency of our categories
- Inspired by "neuroscience" / "cross entropy", a good language should encode different types of things in average portion, such that we will get the best Shannon information from the data. 

### Consistency when encoding/decoding notes
- Continue [[#^7a8db8|Constraints are information (above)]]
- Successful communication involves high quality encoding and high quality decoding. 
- While the medium of "natural language plain text articles" provides a wide design space for the writer to put any symbols to the table, which means they can encode their message with any dialects they want. 


### 5 Main kinds of knowledge
- 5/4/2023
- If we are using entity-based note taking method, there are at least 3 kinds of knowledge for an entity existing:
	- 1. Compositional knowledge:
		- The object would have its meaning if it is adhere to some provided context.
		- Other terminology: 
			- Contextual knowledge, semantic knowledge, conceptual knowledge
	- 2. Functional knowledge:
		- How objects could interacts with other objects
		- Other terminology:
			- Relational knowledge, procedural knowledge, interactivity knowledge
	- 3. Relative attribute knowledge:
		- Attribute of an object only exist when it is comparable to other relatable objects. 
		- Other terminology:
			- Comparative knowledge, relational attribute knowledge, contextual attribute knowledge


### Information content from symbols 
- 9 Apr 2023
- "Length - Information" trade-off
	- In general, there is a tradeoff between the amount of information conveyed in a message and the length of the message.
	- Information density
		- This tradeoff is captured by the concept of information density, which is the amount of information conveyed per unit of length or space. For example, consider two messages that convey the same information, but one message is twice as long as the other. The shorter message has a higher information density, since it conveys the same information in a smaller amount of space.
- Content prediction:
	- Say I am putting the concepts from [[Course 1 of 4, Introduction to TensorFlow for Artificial Intelligence, Machine Learning, and Deep Learning]] into separate entity notes. 
	- I might write the content for each entity individually. But that would lose the context meaning of the course designer. The concepts in the same section should be closely correlated to each others. 
	- Computationally, Say
		- C: context node
		- E: entity node
		- Then when writing E, we shall infer the meaning of E by inferring E-->C-->E, and then mention each other E that is close to that E .

### (Added to version 2) Node-centered note-taking (28 July 2023 comment: This is wrong! the pinnacle of  learning is "pattern learning") 
- Currently, note taking software like obsidian and notion still using hyperlinks to link up pages. So that users could make entity-based notes with these software.
- Advantage:
	- Intuitive
- Disadvantage:
	- However, the knowledge is mostly in the connection between entities and not within the entity itself, so this approach may not capture the full complexity of the relationships between different notes.

### (Added to version 2) Edge-centered note-taking / learning (28 July 2023 comment: This is wrong! the pinnacle of  learning is "pattern learning") 
^4ac320
- Written in April 2023
- Examples of edge-centered note-taking
	- Mind-mapping
	- Concept-mapping: 
		- High school teachers don't teaches us that the important information from that map is from the linkages between items, not items itself.
	- Graph-based note-taking: 
		- uses a graph database to store notes as nodes and relationships as edges. 
		- Graph-based note-taking is particularly useful for capturing the complexity of relationships between notes.
- 9 Apr 2023
	- While entity-based writing could retain the information more effectively than plain notes writing. Most of the knowledge actually exists in between interactions between entities. 
	- In machine learning, the connections between neurons in a neural network are crucial for the network's ability to learn and perform tasks. 
	- During training, the weight of those connections between entities are adjusted 
- 8 Apr 2023
	- Extending this concepts
		- We can also do this checking to a level of "each sentence".
		- Say, each sentence should whether have:
			- Kind A -  belongings of entity 
				- (i.e. that sentence would be an attribute / description of some entities)
			- Kind B -  Itself is the topic sentence of discussing one entity
				- (i.e. that sentence triggers us to create an entity, or link that block of content to existing entity content.)

### Missing link detection
- Continues [[#^4ac320|Edge-centered note-taking (above)]]. 
- When populating the vault, a satisfactory rate of conversion rate of links, is important indicator
- Currently, software like obsidian and notion still using hyperlinks to link up pages. 

### Effective information organization
- Examples:
	- 1. Use hierarchical structure
	- 2. Apply dimensionality reduction techniques
	- 3. Implement indexing (address of data)
	- 4. Use compression techniques
	- 5. Apply chunking / padding
- Detailed article:
	- Query: locate the records satisfying the condition
	- Data structure:
		- 1. Indexes
		- 2. B-trees
		- 3. Hash-tables
		- 4. Trees
		- 5. Arrays and lists
	- Detail article: 
		- [[2 March 2023 - ways to organize information such that a NLP model could retrieve information effectively and consume less memory]]


### Creating a new way of working on knowledge
- Sept 2022?
- I am proposing a way of working effectively: Splitting out the definition of class objects as 30 ~ 40% of workloads.
- All kinds of production: 
	- We are too relying on our brain to create something from scratch. 
	- A better way to produce something is by looking at some previous work. We copy the framework of it, and then changes some values of it. But that is a narrow way that could solve limited tasks. What we want is to expand the capabilities. 

### Query and query-related data structure



### Robust NN against noises and outliners 
- 6/4/2023
- Prone to noise:
	- Neural network structures with a large number of parameters
		- They are more prone to overfitting and may be more sensitive to noise and outliers in the data. This is because they have the capacity to memorize the training data, including the noise and outliers, instead of learning the underlying patterns in the data.
	- Deep neural networks:
		- the gradient signal can become very weak or vanish in the deeper layers, making it difficult to update the parameters correctly.

- Robust structure
	- Convolutional Neural Networks (CNNs)
		- Parameter sharing
			- the same set of parameters is used to process different parts of the input, which enables the network to learn local features that are robust to variations in the input
		- Pooling layers
			- Down-sample the feature maps produced by the convolutional layers. This reduces the sensitivity of the network to small variations in the input 
		- Regularization
			-  CNNs often use regularization techniques such as dropout or weight decay to prevent overfitting and improve the generalization capability of the network. 
		- Transfer learning
			- CNNs can be pretrained on large datasets such as ImageNet, which enables them to learn a set of general features that can be applied to a wide range of tasks. 
	- Recurrent Neural Networks (RNNs)
		- Varying length:
			- . Unlike feedforward neural networks that take fixed-size inputs and produce fixed-size outputs, RNNs can take inputs of varying lengths and produce outputs of varying lengths. This makes RNNs well-suited for handling noisy or outlier data that may be present in the sequence.
		- Recurrent architecture
			- the output of a previous time step is fed back as input to the current time step. This allows the network to maintain an internal state or memory of previous inputs, which can help it to handle noise and outliers in the data.
		- Long-term dependencies
			- RNNs can learn long-term dependencies in the sequence, which can help to improve the generalization capability of the network.
	- Adversarial training
	- Residual network

### Composite objects that is built upon concept extracts
- Sept 2022?
- Flexible notes
	- It could be the immediate printout that produces from an author to let the reader understand something, or some 
	- The flow of the flexible notes should follows the materials the note is referring to. 
	- Trade-off between the amount of "context". More of them are likely to increase the clarity, less of them would make it more effective in knowledge databasing for expertise learners.
		- The objectives of these sources are solely making sense of handful, likely 2~3 concepts, with around 1000 words. 
		- These copies of writings are very helpful for readers to make sense of a new concept to them. But we cannot hide the unnecessary "known fact" to the readers with more expertise 
- Concept extracts
	- Concepts are all only valid when they are connected to (a) Flexible notes. Trimming out the context, concepts would loss the meaning of itself.
	- It is computationally accessible, which means the data model is query-ready. 
	- CRUD rule of database. 
	- It is a processed product, which should be more structurally defined
	- These concept extracts should be connected to (a) flexible notes, because Knowledge become knowledge when the author provides content around the concept. And every author would express their understanding by just one perspective. 
	- Application:
		- Effective horizontal thinking
			- eg: combining horizontal + vertical: 
				- "Word-document matrix" versus "context-windows co-occurrence matrix", they are both 2D table matrix. Which is "better"? The sideway searching requires horizontal thinking. The feature extraction and comparison requires vertical thinking. 
		- Effective vertical thinking
- Model / problem-pattern / library / comparisons etc is a more predefined note type. 
- There are multiple facets of knowledge. RDF / entities won't be sufficient to model knowledge effectively. 

### Database improvements
- 29/3/2023
- Ways to improve database performance
	- Query optimization techniques
		- Finding the most efficient way to execute a given database query
		- The goal is to minimize the time it takes to execute a query, while maximizing the utilization of system resources such as CPI, memory and disk I/O.
		- General methods:
			- 1. Indexing: 
				- Quickly locate the rows that match a given query. 
			- 2. Partitioning: 
				- Dividing a large table into smaller, more manageable pieces called partitions. 
			- 3. Caching: 
				- Storing frequently accessed data in memory so that it can be quickly retrieved. 
				- Access memory is in nano-second, and access disk is in the speed on mini-second.
			- 4. Query rewriting:
				- Transforming a complex query into a simpler, more efficient query that produces the same results. By eliminating unnecessary joins and subqueries, or reordering the execution of certain parts of the query. 
			- 5. Parallel execution:
				- Breaking a query into smaller parts and executing those parts simultaneously.
			- 6. Materialized views:
				- Precomputed tables that stores the results of a query. That help to reduce query execution time by eliminating the need to execute the query every time data is requested. 
			- 7. Statistics
				- Database systems use statistics to estimate the cost of executing a query. 
			- 8. Join optimization
				- Use the optimal join algorithm and join order
				- Minimize the amount of data that needs to be processed and improve performance. 
	- Indexing methods (locating)
		- Creates a data structure that helps in faster data retrieval.
		- Indexing = Creating an index on one or more columns of a database table. 
		- An index stores a copy of a portion of the data from a database table, in a separate data structure, to make it easier and faster to retrieve data from the table.
		- 1. Faster data retrieval:
			- It allows database systems to retrieve data from a table more quickly.
		- 2. Reduced disk I/O:
			- Reduce the amount of disk I/O that is required to access data in a table. 
			- Index provides a more direct path to the data that is being requested.
		- 3. Improved query performance:
			- When queries are executed against a table that has an index, the database engine can use the index to quickly locate the data that is required by the query. 
		- 4. Faster sorting
			- Indexing can improve the performance of sorting operations. Sorted index can be worked out more efficiently.
		- 5. Improved concurrency
			- Reducing the amount of time a table is locked when data is being accessed or modified. 
	- Data compression algorithms
		- 1. Reduced disk space usage
			- Additional storage space could slow down database operations
		- 2. Faster data access
			- Compressed data can be read and write to disk more quickly than uncompressed data, as it takes up less space and requires fewer I/O operations. 
			- So data retrieval, updates and backups would be faster.
		- 3. Improved memory usage
			- As it requires less memory to store and manipulates. 
		- 4. Lower network bandwidth usage
			- Reduce the amount of data that needs to be transferred over a network.
- Ways to improve performance of machine learning:
	- 1. Feature engineering
		- Selecting and transforming the input variables to create a more informative representation of the data for the machine learning algorithm.
	- 2. Model selection and tuning
		- Choosing right model for a particular problem and tuning its hyperparameters can significantly improves performance.
	- 3. Ensemble method
		- Combining multiple machine learning models to improve predictive accuracy
	- 4. Data augmentation
		- Creating new training examples by manipulating or generating additional data. 
	- 5. Transfer learning
		- Reusing knowledge gained from one machine learning task to improve performance on a different task.
	- 6. Hardware acceleration
		- Using specialized hardware speed up training and inference time.
	- 7. Distributed computing
		- Distributing inference workload across multiple machines. 
- Venn diagram for the above examples:

### Templating
 - 22-12-2022:  ^a9f269
	- Every events in life, every notes, projects etc are repeated process that's like cutting cookies with tools. There will be benefits to create "structural typing" for each of them. 
	- For notes:
		- 1. Each notes should follows an architype. And all notes should belongs to a collection. 
		- 2. The collection would facilitate discovery of the notes, which could provide a higher speed retrieval than relying on the search bar. 
	- For materials inside the note:
		- 1. Some repeated parts should be also taken out and design some architypes for them. Such as coding example templates. 

### Kinds of knowledge-container (Distinct space for nodes)
- While we have 2 kinds of notes now
	- Kind A:
		- detailed course notes, which provides context; and 
	- Kind B:
		- abstract entity-based notes, which speeding up the reasoning. 

### Connection between kind A and kind B notes  (Edges)
- There is lack of a tracking log that helps the users to know the status of the content in contextual notes is linked to certain abstract notes. 
- Say, each section in the kind A notes we also would have a status section which notify the user whether that section is connected to some abstract notes.

### Metadata
- 9 April 2023
- Example functionalities:
	- Markup the status in between kind-A notes and kind-B notes. 

### Computational accessibility
- Oct 2022?
- 1. Connections
	- The vault and the network of the collection of notes. 
		- The value of grouping notes belonging to some collections is because it could shape up the behaviors of some repeated objects. In such way, comparing become possible. 
	- Tags and labels
		- Tags and labels are the pointers that indicating some notes is belonging to certain collections. 
		- An effective single note page should be labeled and tagged so the computer program would interacts with it far more easier.  
- 2. Allow join/split/merge?
	- A database should not accounting the same record more than once. Thus an effective knowledge base should supports splitting and joining the attributes/content from multiple notes. A more complicated concept, such as "Bayes inference", requiring some basic probability concepts, so the notes of "Bayes inference" should JOIN the content from basic probability concept notes, instead of writing those repeated ideas there. 
	- So the very first rule of creating notes is: normalize/split the notes as far as we can. 
- 3. Categories / Structuring of templates?
	- By structured, that leaves us a design space on how to artfully locate the information in such way speeding up the search without losing the completeness of information. 
	- Everything becomes an object when they belongs to some class definition. And class definition provide structure to objects of that class. 
- 4. Named entities
	- A structured notes should focus its attention to the smallest unit of concern -- the object itself.
	- Based on the grasp of the network of objects, we might be able to answer more sophisticated questions, like comparing objects, generating better articles from the notes and extracts we already have in the database etc. 
- 5. Primary keys?
- 6. Bridging to extracts / context 
	- Concepts shouldn't be existing by themselves but supported by handout extracts. 
	- Making sense to the human readers who is the beginner to the field of the concept. 


---

# Views about knowledge existing in between natural language


### Rebus (phonetic loan) characters
- The same word could be adopted by many fields to express their own individual ideas, thus therefore natural language contains ambiguity in many cases. 
	- example: 
		- a. some words like "independent" has a lot of different meanings, and that depends on the context. 
		- b. In encyclopedias online, we saw that they organize named entities with: `Cao Cao/ <SHAcode>` in Baidu encyclopedia, `independence_(mathematics)` in Wikipedia to more accurately locate / disambiguate different concepts but using the same word to express it.  

### Needling of meaning
- The meaning of a single word might or might not coming from the context. Natural language words are just a façade of the actual concepts we want to deliver. (Need more development)
	- In most of the case, we are not training the algorithm to be a dictionary learner, but explaining the actual concept of the article. 
	- To make sure the readers could understand the message, we have to provide demonstration. But once we have learnt the concept, we don't need much of those demonstrations anymore. 
- In a flexible notes, we are less likely found needling of meaning. But it personal notes, there are a lot of people going to trim the demonstration part because they have practiced those sequences recently and they think those parts are not important. But after some gap period they cannot understand the notes that is made by themselves because the important memory that already loss from the brain 






---
## Suggestions of the data model for knowledge bases


![[thumbnail - Copy - Copy - Copy.jpg|700]]
- Fig: demonstration of the structure of a vault. 

- The following drawings are demonstrating how the concepts I have mentioned in this article could be applied to the data model of the knowledge base: 

![[thumbnail - Copy - Copy.jpg]]
- Fig: The relationships between concept extracts and articles. 

![[277105710_525046535657178_740020059978335055_n - Copy 1.jpg]]
- Fig: This drawing tries to demonstrate how to convert raw article into higher processed notes, in a low resolution manner. 

![[277105710_525046535657178_740020059978335055_n - Copy - Copy.jpg]]
- Fig: This drawing tries to demonstrate how to extract patterns from the raw source. Typically we cannot extract a generalized problem pattern from the article directly, so we will extract a lot of patterns that could mean the same thing, but there are variations from each of them. Might be it comes from the choice of dialects, choice of some free orderings, choice of words, etc. But they are getting the same inputs, and producing the same output. And they could be the same thing. 

![[277105710_525046535657178_740020059978335055_n - Copy - Copy (2).jpg]]
- Fig: This drawing is demonstrating the process of extracting concepts from raw sources. It is pretty much like how to extract "sequential object" like the prior drawing. 

![[277105710_525046535657178_740020059978335055_n - Copy - Copy (3).jpg]]
- Fig: This drawing summarizing the whole process extracting objects from raw source. The immediate product is "flexible notes" generated by the agent. The fact is all entities we got from a single raw source is just a narrow aspect of a concept. But we still treat them as the same as how we would build a "entity-based note system" because "narrow aspect concept" should be the same class as the "complete aspect concept". 
- The crucial KPI is to capture as much as information, but adding as many as structure to the data. We preserve all "supporting details" of a concept by bringing them to another class of object, that is "problem pattern" / "demonstration" etc. And bridging these examples back to concepts. They will be called only when it is needed. 

---

- As I said, I suggest 30% of the workload of maintaining a knowledge base should be focusing on designing a schema of it.  What is the meaning of designing schema as a main activity?
- Let's assume we are already using the notes system for the vast majority of our works and studies.
- When we construct a knowledge base, the activity of a user would be:
	- 1. Select N row source
	- 2. After learnt and read from those raw source, capture narrow aspect of concepts, sequences
	- 3. Bring and link those puzzles back to the notes system, create a new entity if it is not exist before. 
- When we try to USE the knowledge base, the activity of the user will be:
	- 1. Tries to query a sequence that helps us solve the problem, from the database. Or, tries to retrieve that knowledge from the database
	- 2. If that is not work, tries to build that sequence, or tries to read some raw sources to get those objects.
- As the process iterates many times, we get a collection of concept/sequence data
- Some new tasks emerges:
	- 1. Tidying up the ordering and dependencies of the class / collection / objects that improves the querying that notes. 
	- 2. Editing the class object definition, after seeing there are some commonalities that should be hard-coded into the class object definition. 
	- 3. Review the impact of changing the class object definition, after we have changed the class object definition. 


- 1. The owner of the knowledge base should try his best to use up his KB creation to generate his ideas. And storing records of knowledge. 
- 2. In the process of using the system, always having some compatibility problems. Then the user have to define concept hierarchy tree. 
	- The difficulty of giving an object a class / collection
		- For example, we have "square" as our object. In geometry, it could belongs to "rectangle", "parallelogram" , "shape", "a shape with right angle", "four-sided shape" etc. Unlike programming, one objects always following one class definition. 




![[thumbnail - Copy - Copy - Copy - Copy 2.jpg|700]]
- Fig: the structure of a single note. 

---


- Paradigms
	- 1. Graph-view focus: 
		- a. Considering the implicit meaning extraction concept by [[category theory|category theory]], the meaning of an entity could be revealed by the [[neighbor]] connection of the node, or the graphlet structures of the graph. 
			- We hold an assumption that - All knowledges are expressed in the graph, otherwise they are not exist. Instead of "internal expression", Now we claim that knowledge exists in between the connection. We consider each sentence should have at least two named entity otherwise it won't be able to be appeared in the graph, and the entity that are not shown
	- 2. Named entities: 
		- 1. Subset / superset entity separation: create a subset/superset groups for such thing. So when we switch to our default setting of  "depth = 2 local graph view",  the node could also read the the property of its subset / superset. 
		- 2. Adjective separation:  for example, separate "Latent" and "Latent Dirichlet Allocation", such the sentence that describe the meaning of "Latent" could be shown in the graph. 
		- 3. Abstract of each entity: by enforcing the rule, we can filter many vague expression that does not contain much information at all.
			- eg; "Fuzzy logic is based on the observation that people make decisions based on imprecise and non-numerical information." --> Which refers the subject which some observation, and it is forming a weak relation --- "based on", won't gives a good represenation of the entity. 
			- eg: "Fuzzy logic is a form of [[many-valued logic]] in which the truth value of variables may be any real number between 0 and 1. It is handle the concept of partial truth, like Boolean logic, where the value may range between completely true and completely false." -- which tells a subset / superset relation, and also specifies the location of the entity in that category space. 
	- 3. Structured typed notes ([[Change log of vault design#^a9f269]])
		- 
	- 4. Collections, networking for the set of notes 
		- Because each notes are belonging to at least one collection, then there is a way to discover the note.
		- A network of them would make each notes be more probable to be discovered in a query. This is not something easy to be realized because human readers are familiar with looking up at the content page ONLY. There is no concepts querying tools viral among people. 
		- Some persons have no knowledge about the difference between querying and searching. 
		- To make querying viable, there should be a commonplace in between query tools and the data itself. That is called a schema of the dataset. 
		- Schema should be determined like how we design class objects in programming.
		- Schema should be able to easily inherited from its older versions, so all existing notes will still be valid for the future schema version.  
	- 5. Better context
		- Architypes for some modules in the context elements, such as how to demonstrate, how  to layout the coding examples, how to compare two concepts. 
		- False training -- Providing negative sampling could helps the agent to identify the correct decision boundary much faster. 

## Vault design for the current obsidian note-taking system
- To recap, the flow of information is, 1. Raw source, 2. Flexible notes, that captures the narrow aspects of concepts and sequence. 3. The entity-based note system
- To recap, the most valuable activity for the user is to design the schema that enforce the future data inflow would follow the same pattern to capture information. 
- To recap, (2) flexible notes and (3) the entity-based note system should having the same kind of schema, so that 


- 3 January 2023 added:
	- In flexible notes (which is recording the highlights from the book), I found it is easier to maintain the notes if I have pin the concepts with their entity name. And it the obsidian software, I need to use "###" notations to create headings. And headings will be appeared in the "Outline" of the page. 
	- So we come up: "Heading is the sentence that summarizing the content of the following block"
	- So we come up: "For a good notes, we should have a good system of writing notes such that we could navigate the notes will lesser cost. ". And "Good notes system", it means having headings in hand, those heading could help us decide what will be the page I click on my next trial.
	- And what will be the best kind of heading?
	- If we don't have such organization, we might create multiple sections for the same matters here and there. That would increases the workload for the next stage of moving the knowledge to "more defined" knowledge area. 


## Future tasks

- 1. Building our own query language. 
	- Source: https://www.linkedin.com/pulse/building-your-own-query-language-my-first-career-project-batra/
- 2. Build a good visualization framework like displacy.
- 3. Software design:
	- The software should be able to create entity based on seeing ('###') before the block of text.
	- The software should maintain the notes in two divisions. 
		- 1. Flexible notes that allow the users to provide context, and also following the flow of the materials they are tracing on.
		- 2. Entity notes that each entries have their reference points. 
	- It should be able to suggest merging similar entities even the user is using different names. 

![[Pasted image 20230103185558.png]]
- Fig: the snapshot of the idea of "flexible notes". 
	- That is pretty much everyone can make this kind of notes by themselves. 
	- "Outline" palette: List out the collection of entities defined in the flexible note. 


---

### Appendix: 
- Setting that controlling the graph view of a vault: 
	- Managing functions:
		- `path: -"All own writings" path:-"All papers and books" path:-"All courses", file:-"changelog" file:-"_all facts"`
	- Managing facts:
		- `path: -"All own writings" path:-"All papers and books" path:-"All courses", file:-"changelog" file:-"_func index"`


### Reviewed papers, videos
- Review of data structure for knowledge:
	- [[Resource description framework|1998, RDF]] invented 
	- [[(Paper) Spivak, D. I., & Kent, R. E. (2012). Ologs -- A Categorical Framework for Knowledge Representation. PLoS ONE, 7(1), e24274| Spivak, 2015]] introduces a data structure call [[olog|ologs]] that tries to convert the relationship between knowledge into a graph. However, it failed to become popular because the setting is unable to be run by computer. 
