
# Human learning

### Cognitive loading
- Definition:
	- refers to the mental effort and resources required to process information and perform tasks. 
	- Types:
		- Intrinsic Cognitive Load: 
			- Some tasks are naturally more demanding and require more mental effort to be processed and understood. eg: math equation
			- As the knowledge base grows, the cognitive loading for recalling the location of one specific information can increase significantly. 
			- As the number of notes and their relationships increase, it becomes more difficult to remember where a specific piece of information is located.
		- Extraneous cognitive load:
			- This type of load is imposed by the way information is presented or the method of instruction. Poorly designed learning materials, confusing graphics, or unclear explanations can lead to extraneous cognitive load. 
		- Germane Cognitive Load: 
			- This type of load is considered beneficial as it relates to the mental effort required to build and integrate new knowledge or create meaningful connections with prior knowledge. It is associated with deeper learning and understanding.
- Solution to each type of cognitive load:
	- Intrinsic cognitive load
		- Chucking: 
			- Breaking down complex information into smaller, manageable chunks can reduce the intrinsic cognitive load. This allows learners to focus on understanding individual pieces before combining them into a coherent whole.
		- Prior Knowledge Activation: 
			- Relating new information to existing knowledge can facilitate the learning process by reducing the intrinsic cognitive load. 
			- When learners can connect new concepts to what they already know, it becomes easier to understand and remember the new information.
		- Progressive Complexity: 
			- Introducing information in a progressive manner, starting with simpler concepts and gradually increasing the complexity, can help manage cognitive load effectively. It allows learners to build a foundation before tackling more challenging aspects of the subject.
	- Extraneous cognitive load:
		- Clear and Coherent structure: 
			- Providing well-structured and clear instructions can help minimize extraneous cognitive load. Information should be presented in a logical sequence, and the use of multimedia (e.g., visuals, diagrams) should support learning rather than distract from it.

### Productivity on human writing / producing product versus AI
- Reasons human cannot produce detailed articles:
	- 1. Limited knowledge
	- 2. Personal Bias
	- 3. Cognitive Load
	- 4. Writing styles
	- 5. Time constraints

### More concepts: refer to - "Wisdom about memory, writing and searching" in "meta" vault


### Kinds of knowledge
- [[Factual knowledge]]
- [[Pattern knowledge]]


### classification of knowledge in graph theory language perspective 
- Written in 28/7/2023
- Before talking about "what are knowledge", we need to establish some benchmarks of "knowledge usefulness". 
	- Assumption:
		- The structure of knowledge will be discussed later. Now we just think of knowledge is a single black box.
	- The viable benchmark of "knowledge usefulness" would be:
		- 1. The basic benchmark is, how such data improves our understandings, behaviors and decisions. In other words, it assesses the practical utility of knowledge in enhancing our comprehension and guiding our actions.
			- The understanding of language helps us understand a concept
			- The understanding of a concept helps us understand some situation
			- The understanding of a situation manifest the value of such knowledge 
		- 2. The advanced benchmark is, how well the current knowledge can gap-filling to help the agent adapt to the scenario when the information is not complete. This means assessing the knowledge's ability to address uncertainties and provide valuable insights even in the absence of complete data.
			- Combining the factual knowledge (understanding of separate facts), and patterns knowledge (such as -- some events / reasoning is likely / not likely to happen).
- Knowledge are graphs
	- Graph can represent knowledge with the following reasons:
		- Relationship Representation: 
			- Knowledge often involves interconnected entities and concepts with various relationships between them. Graphs can explicitly represent these relationships as edges connecting the corresponding nodes. This allows us to capture not only the entities themselves but also the connections between them, making it easier to comprehend the knowledge.
		- Flexibility: 
			- Graphs can handle a wide range of data types and relationships. Whether the knowledge is hierarchical, networked, causal, associative, or any other form of connection, graphs can accommodate it without requiring a fixed schema or data model.
		- Inference and Reasoning: 
			- Knowledge graphs can support inferencing and reasoning capabilities. By defining semantics and rules within the graph, we can draw logical conclusions and infer new knowledge based on existing connections.
- Say there are 5 kinds of knowledge exist:
	- Factual knowledge: 
		- Hierarchy level 1: Basic node and edge: 
			- "Basic node and edges" are the basic component in language. They are facts, observable phenomenon. We human pick them up in our childhood. 
			- Structural properties of basic nodes and edges:
				- 1-to-1 dictionary: 
					- When using basic nodes and edges, we use words . We coin a word to represent an object, or a relationship. 
				- attributes representation:
					- attributes includes the measurable and not measurable properties of the property. The functionalities of the property.
					- attributes approximate the true meaning of a node / an edge: a node or an edge manifest itself by certain attributes. An agent could correlate an object is something, by looking at what attribute that attribute has. In machine learning, models use some high dimensional embeddings to represent the attributes of each node and edge. 
		- Hierarchy level 2: Granular edges and granular nodes:
			- As we progress in our learning journey, we encounter Granular edges and nodes. These are more complex terms that convey nuanced meanings and ideas. The existence of granular edges and nodes comes from learning from others, or discovering themselves with "pattern knowledge", which will be discussed later. 
			- With some edges and nodes grouping up, some [[emergence]] attributes might comes out. 
				- Real life examples:
					- The properties of water emerges from the properties of water particle. 
					- The properties of a computer program emerges from the properties of simple keyword blocks. 
						- To master Granular edges and nodes, think of them as "functions" and "classes" in programming. When coder defines "functions" and "classes", they want something to happen, and their way to achieving is by combining existing building blocks to make some new properties emerge. And then finally coining new variable name for each of them. Finally these new variables can be used just like how other basic nodes and edges within a line.
			- Innovation (writing it in 16-8-2023): 
				- 
			- It's important to recognize that these complexities can all be expressed in terms of basic nodes and edges, just like a dictionary explains each word's meaning. In the process of grasping complex ideas, the agent usually have to walk through the inner structure of that boundary. Here are some reason why it is useful:
				- Tracing causality and understanding
					- Understanding the micro properties allows us to trace the causal relationships between individual components and the emergent properties of the larger system. It helps identify the specific interactions and processes that lead to the observed behaviors at the macro level.
				- Prediction and control
					- By studying micro properties, we gain insights into how small changes at the individual level can result in significant changes at the macro level. This knowledge enables us to predict the behavior of the larger system under different conditions and potentially control or manipulate its emergent properties.
				- Validation of models
					- Researchers often create models to simulate and understand emergent behaviors. Examining the micro properties helps validate and refine these models to ensure they accurately represent the real-world system.
				- Identifying critical elements
					- In some cases, specific micro properties or components may play a disproportionately significant role in determining the emergent properties of the system. 
				- System design and optimization
					- Studying the micro properties (algorithms, data structures, individual code component) is crucial for designing and optimizing the overall system's performance, efficiency, and stability.
				- Cross-domain insights
					- The study of micro properties and their emergence is a fundamental concept that applies across various disciplines, from physics to biology, computer science, sociology, and beyond. 
			- The usefulness of a granular edge or node depends on how well the creator could clearly state the emergent attributes of that granular object. 
			- "Fuzzy logic": This term describe an agent use the mentality of level 1 to understand level 2 knowledge. As a result, people make decisions based on imprecise and non-numerical information.
			- Structural properties of granular edges and nodes: 
				- Compositions: Each of them consists of multiple edges / nodes
				- Interfaces: 
					- While each of them are composite bodies, an agent cannot use it without creating an interface for those complex ideas. 
					- Real life examples: 
						- Experts in social science rely heavily on coining concepts with a single word. 
						- Experts in science and engineering rely heavily on coining new variables, equations and models to outline a phenomenon. 
	- Pattern knowledge:
		- Hierarchy level 3: Pattern knowledge:
			- While granular edges and nodes can be learned by aggregating the learning experience, the recognition of patterns requires deliberate thinking. 
			- Pattern knowledge enables us to understand complete stories, even when certain facts are hidden or new words are encountered in a sentence: even some words are first-seen from a sentence; we can still use our "sense" to link up a complete story to interpret it. Pattern knowledge allows us to connect dots and interpret information using our intuition and experience.
			- Mastering pattern knowledge enable the person become an effective creator of granular edge and node. 
			- Learning strategy:
				- Engage in activities that promote critical thinking, problem-solving, and creativity. Reading diverse literature, analyzing case studies, and discussing abstract concepts with peers can help strengthen your pattern recognition abilities. 
				- Embrace the beauty of uncertainty and ambiguity, as they offer opportunities for pattern knowledge to emerge.

### Abstract thinking 
- 29 July 2023
- "Abstract thinking" is the way of composing "Granular edges and nodes" to create some new perspective. 
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


### How to learn factual knowledge?
- Concepts:
	- [[Embedding]]
- Edges and nodes
	- To grasp knowledge at this level, immerse yourself in a diverse environment that exposes you to a wide range of basic nodes and edges. 
	- Engage in activities that encourage observation and exploration, such as reading books, participating in experiments, and engaging in discussions with others.
- Granular edges and nodes
	- To master Granular edges and nodes, think of them as "functions" and "classes" in programming. By coining new terms, we can condense communication steps and convey intricate concepts efficiently. 
	- While it may seem overwhelming to learn all the details of each Granular term, rely on pattern knowledge to make informed guesses about their meanings. 
	- Embrace the iterative learning process and expose yourself to diverse examples of Granular knowledge in real-life contexts.

### How to learn pattern knowledge?
- Concepts:
	- [[Attention]], [[Embedding]]
- We need 3 to 4 times higher parameters to learn pattern language. 
	- In popular language models like BERT and GPT, the rough ratio of the number of parameters between the "Weight of Word Embedding" (which represents factual knowledge) and the "Weight of Attention" (which represents pattern knowledge) is about 1-to-3 to 1-to-4. There is four times greater number of parameters in attention layers 
- Why attention need more parameters?
	- This is because the attention mechanisms in these models play a crucial role in capturing contextual relationships and dependencies between words, and thus they require more parameters to perform their function effectively.


### Network effect, sense making and gap-filling mechanism
- 29 Jul 2023
	- [[Network effect]]
- 27 Jul 2023
- Sense making 
	- Intelligence manifest at the times information are missing and the agent is still able to understand the meaning of it. 
	- The step of sense making might be involving 4 steps:
		- 1. Recognize what kind of objects appears in the space.
		- 2. Imagine what are the possible relations / structures between those objects that could have meaningful interpretations.
		- 3. In the process of guessing and fitting which structures is the most probable, the agent would use a structure that has more slots than the number of objects existing in the space. Thus, in most cases, the agent would need to fill in the gaps of the "structure" they are suggesting. 
		- 4. When fill in gaps, they try to put the most frequent occurring concept into the blank and try to make sense of it. That is the source of hallucination.
	- To improve the output of thought quality of the agent. We can:
		- 1. Organize our knowledge base in the way that when the agent tries to gap-filling, he can recall more useful facts.
		- 2. With a good and rich knowledge base, and if it is computational efficient. We can try to depict structure in the knowledge base. 
		- 3. Tries to use the combination of "structure" + "factual data", and try to return back meaningful articles. 
- 6 Feb 2023
	- Learning/successful-training means "You covered up a part of the information of the material, and your system could still predict what it is covered up correctly.".
	- We start off by providing information to the agent. 
	- Then we cover up some information out of the whole content. Then stimulate the neural network to see the pattern.   
	- The result of learning would be: the agent have ways to use the remaining linkage of information of him to produce the correct prediction of missed information. 
- Dec 2022
	- If there are missing pieces existing in a message, human would also tries to fill up the missing information by their pre-trained understanding of the world.
- ![[F0fLEtKpdlhcpSOHkZcmeAJ3Irrbik0dMNiuGjDYrho - Copy.jpg|400]]
- Fig: My demonstration of the cardinality between natural words and extra-linguistic entity (the actual concept)

### Context
- Context refers to the surrounding elements around the main object of communication.
- Usefulness of context
	- In some cases, conversations can be context-sensitive, meaning the interpretation and understanding of the conversation may depend on the context in which it takes place.
- Context and truths
	- In most cases, context does not overlap with the construction of complex ideas.
		- While context can provide a testing environment to showcase the validity of an idea to the audience, a rich-context conversation alone may not be sufficient to teach the audience the true meaning of that idea.
		- Books / articles /  agents need to establish a space to formally list out the components of some complex ideas before they start the conversation because it is time consuming and they assumes the readers can understand those ideas their own. 
- Context and unsupervised learning
	- Agents can learn ideas from the context in which they are presented. But solely learning ideas from conversation without deeply think of "how each ideas are constructed" might cause problems.  
	- If an agent relying solely on accumulated knowledge from context-based communication may lead to a false sense of understanding, especially when dealing with complex ideas.
	- Complex ideas often involve emergent phenomena, and their attributes may change when certain conditions change. Thus, understanding the true essence of complex ideas requires more than just contextual learning.



- Figure: Oct 2022?
![[thumbnail - Copy.jpg|500]]
- Fig: Most of the articles that is written by some authors. 

### Unsupervised learning of human learners
- 6/4/2023
	- Strategies for unsupervised learners:
		- 1. Use prior knowledge or context to help them interpret new information
		- 2. Seek out additional resources or perspectives to gain a broader understanding
		- 3. Engage in reflection and self-assessment to monitor and improve their learning progress
	- [[Unsupervised learning]]

### Active learning
- Active learning is a paradigm in which a learning algorithm iteratively queries an oracle (i.e., an expert or human) to obtain the labels of a carefully selected set of examples. The algorithm uses the labeled examples to improve its performance in subsequent iterations.

### Focus on difficult examples -- is that valuable?
- Valuable (not so):
	- Mostly no, because whole decision progress is an average. If we put too much weights on difficult examples, it makes the rest of decision making neurons for easy examples also moving  around. 
- Not valuable:
	- This is because the difficult examples may not be representative of the general distribution of data, and the model may overfit to these examples and perform poorly on new, unseen data.
	- some difficult examples may be outliers or noise in the data, and incorporating them into the training process may harm the model's performance rather than improve it
- My thought (27 Jul 2023):
	- Difficult example has less frequency to meet them again
	- Difficult example don't implies it involves novel connection. It might involves a bigger knowledge graph chunk. But it can be learned with several easier examples. 
	- The ability of solving hard problems are emergence phenomenon. Smart people don't need to train on a series of hard problems to be smart. Smart people study problems at anything with a more robust approach. They might break down the problem into the smallest size and then merge those facts to come up with their recognition. Elon Musk call it "first principle".

### Two types of neural network components
- I propose we can think of there are two main classes of components in any neural network. 
- [[Transformer]]
- [[Boundary constructor]]



---

# Data handling


### M-to-N relationship among elements
- Written in Sept 2022
- There are a lot of  M-to-N relationship in terms of knowledge base.
	- One demonstration could be related to various concepts
	- One concept could exists in multiple text or documents
	- This complexity in relationships enhances the interconnectedness of knowledge and allows for a richer and more comprehensive understanding of various subjects.
- What if we don't include M-to-N relationship in a database?
	- Limited interconnectedness
		- This could lead to a fragmented representation of knowledge, making it challenging to understand the broader context and connections between various concepts.
	- Reduced Contextual Understanding:
		- Concepts in a knowledge base would exist in isolation, without the ability to understand their contextual relevance or associations with other elements. This could hinder the ability to capture the intricate relationships and dependencies that exist in real-world scenarios.
	- Loss of Richness and Depth: 
		- M-to-N relationships bring richness and depth to a knowledge base by allowing multiple perspectives and connections to be explored. Without this feature, the knowledge base would lack the capacity to provide comprehensive and nuanced insights.
	- Inability to Capture Ambiguity: 
		- By disregarding M-to-N relationships, the knowledge base might struggle to handle ambiguous information effectively. In the real world, many concepts can be interconnected in multiple ways, and not considering these relationships might lead to oversimplified or inaccurate representations.
	- Limited Knowledge Inference: 
		- The ability to infer new knowledge based on existing relationships is an essential aspect of knowledge bases. By omitting M-to-N relationships, the knowledge base may miss out on opportunities for knowledge discovery and inference.
	- Difficulty in Knowledge Expansion: 
		- As new information is added to the knowledge base, the lack of M-to-N relationships might make it harder to integrate and connect the new data with existing knowledge effectively.

### Scalable data structure
- Characteristics:
	- Accessibility
		- Measurable scalability - from the capability of "search queries"  
			- To measure whether a knowledge base is scalable, involves assessing its ability to grow and adapt to increasing demands, both in terms of data volume and user usage. 
			- Real life example
				- A scalable programming language would not include all possible encounters and use cases within its own pre-built interface. Instead, it allow the user to define their own tools by a set of operations by themselves. 
		- Efficient Indexing and Retrieval:
			- This is an extended characteristics when the knowledge base has "search queries" capabilities. 
			- Efficient indexing and retrieval mechanisms are essential for quick access to information
		- Content Categorization and Tagging: 
			- Organizing content with categories and tags can aid in efficient retrieval and improve the user experience.
		- Easy Integration of Media Content: 
			- Support for media content like images, videos, and audio can enrich the knowledge base and cater to different learning styles.
	- Maintenance 
		- Flexible data structure
			- Save up the time of maintaining the content of the knowledge base.
		- Automated Maintenance: 
			- Automation of maintenance tasks, such as data ingestion, updates, backups, and monitoring, helps reduce manual effort and ensures the knowledge base remains up-to-date.
		- Adaptability to New Data Formats: 
			- The knowledge base should be able to handle various data formats, ensuring compatibility with different data sources.
		- Scalability Plan and Roadmap: 
			- A clear scalability plan and development roadmap ensure the knowledge base is prepared for future growth and evolving needs.
- Why designing a scalable communication tool is important?
	- 

- Measurements:
	- Performance testing:
		- Measure response times for various operations (e.g., data retrieval, search queries) under different levels of concurrent usage.
	- Benchmarking:
	- Load testing
		- Simulate heavy user traffic and data access to determine how well the knowledge base handles peak loads.
	- Data size and complexity
		- Assess how the knowledge base handles large and complex datasets. Ensure that it can efficiently store, index, and retrieve data as the volume increases.
	- Hardware and infrastructure
	- Distributed architecture
	- Auto-scaling capacity
	- Redundancy and failover mechanism
	- Monitoring and analytics
		- Ensure that the knowledge base has monitoring and analytics tools to track performance metrics and identify potential scalability issues.
	- Real-world testing
	- Vendor and community feedback
	- Future roadmap
		- Review the development roadmap of the knowledge base platform or software. Look for planned features or improvements that address scalability concerns.
	- Scalability plan
		- Ensure that the knowledge base has a clear scalability plan in place. This plan should outline strategies for handling increased data volume and user traffic in the long term.



- The following strategies can make the personal knowledge base more scalable:
	- 1. Organize information using a consistent structure: 
		- Define a clear taxonomy and hierarchical structure for your knowledge base. Categorize your notes into well-defined topics or themes. This makes it easier to locate and update information because related notes are grouped together.
	- 2. Utilize a semantic tagging system: 
		- Implement a tagging system that allows you to assign relevant keywords or tags to each note. This provides additional flexibility in organizing and searching for information. When adding new notes or updating existing ones, ensure that you assign appropriate tags to maintain consistent and meaningful connections.
	- 3. Create interlinking between notes: 
		- Establish links or references between related notes. By connecting relevant concepts, you can create a network of interconnected knowledge. When updating or creating new notes, make sure to include hyperlinks or references to related notes. This helps maintain the integrity of the knowledge base and facilitates easier navigation.
	- 4. Use a consistent naming convention: 
		- Adopt a consistent naming convention for your notes and files. This convention could include dates, titles, or keywords that reflect the content of each note. By using a standardized naming approach, it becomes easier to locate and update specific notes when needed.
	- 5. Leverage automated tools and technology: 
		- Explore software tools or applications that offer automation and assistance in managing knowledge bases. There are various note-taking applications, personal knowledge management systems, and semantic web technologies available that can help streamline the process of updating and maintaining your knowledge base.
	- 6. Regularly review and update: 
		- Set aside dedicated time for regular review and updating of your knowledge base. This ensures that information remains accurate, relevant, and up to date. By consistently investing time in maintaining your knowledge base, you can avoid the accumulation of outdated or incorrect information that would require significant efforts to rectify later.
	- 7. Foster collaboration and crowdsourcing: 
		- If feasible, consider involving others in contributing to your knowledge base. This could be through collaboration with colleagues, peers, or online communities. By allowing others to contribute, the burden of maintaining and updating the knowledge base can be shared, reducing individual maintenance time costs.

### [[Topic modeling]]


### [[Polysemy]]


### Designing a new data structure for personal knowledge base
- Say initially we have a collection of "entity-based notes", which means each markdown file containing a natural language article that only specifically write about that concept. 

- The middle of fully unstructured "plain text" and fully structured "RDF triple". (written in 27 July 2023)
	- While RDF triples are computationally efficient, but it is not human readable, and text are human readable but not computationally efficient, is there any good way to produce a thing in between?
		- Proposal:
			- Write a entity-based notes. The content is worked based on a series of pre-made prompts. 

- The new data structure has the following aspect:
	- 1. How it is constructed
		- 1. Say each notes would have their own boundary / "community", and we use a "circle" to represent that space. And we can use some script or software to obtain the RDF triple representation of that article. So we have an isolated mini knowledge graph within that "circle".
		- 2. In each "circle" or mini-knowledge graph, there are one node that is the main concern in that community, which is the subject of that "circle". (If that community is not a entity-based notes, then there are not main concern.) 
		- 3. Some obvious relationships (eg: common neighbor node, direct mentioning) would establish some relationships among those previously isolated circle.
		- 4.  each "circle" are the individual unit of "concept" are the first citizen that human reader concern about.
	- 2. Objectives / goals of maintaining a good knowledge base
		- 1. Discovering granular patterns or relations between circle
			- While it is hard to capture relationship between nouns, because the relationship type is restricted to be one of the relationship defined in the schema. With communities of RDF, we can naturally observe some complex behavioral patterns between "concepts". Thus granular patterns or relations could be extracted  from such arrangement.
		- 2. Discovering potential circles within the mass of explanation RDF
			- We might use some technique to detect whether some nodes could be a "main concept" that is not yet determined. 
		- 3. Discover the node / edge type 

- We still keep notes for each entity / notes.
- The goal is to produce a data structure that could ultimately help generate human readable patterns and relationships among objects.
- The outcome would be a new kind of information, and it will be an asset that is helpful for human users to understand something. 
- Rules of finding these relationship / patterns
	- 1. If it is >1 edge away from the subject, then it might be a relationship.
	- 2. Automatic association / composition / aggregation relationship extraction, by referring to specific kinds of edge types and node types.

### Multiple kinds of notes
- Vault:
	- All content of the vault should be converted to RDF triples, so that the computer could compute it more effectively.
- Larger notes:
	- These notes can encompass a larger scope of articles, such as books, videos, papers, etc.
	- They aim to provide context and relationships between entities and concepts.
	- There is a trade-off between the amount of context provided. More context increases clarity, while less context is more effective for knowledge databasing for expertise learners.
	- The objectives of these sources are to make sense of a handful of concepts (around 2-3) within around 1000 words.
	- These notes are useful for readers to understand new concepts, but they should avoid redundant information for expert readers.
- Entity-based notes:
	- Concepts are only valid when connected to Larger notes. Trimming out the context would cause concepts to lose their meaning.

- Figure: the data structure
![[GdtuMVs - Copy.jpg]]

### Predicate groups
- Definition: 
	- In the context of the W3C (World Wide Web Consortium) standards, predicates and predicate groups are terminologies often used in the schema definition languages, such as RDF (Resource Description Framework) for predicates and SHACL (Shapes Constraint Language) for predicate groups. 
	- Predicate groups, in the context of W3C standards like SHACL, allow you to organize related predicates together for more efficient validation and readability of data shapes. SHACL is a language used to define shapes (constraints) for RDF data. A shape describes a set of constraints that resources must adhere to, and predicate groups help categorize these constraints based on their relationship to each other.
	- It captures hierarchies of predicates.  
- Advantages:
	- By grouping related predicates, you can specify validation rules or constraints that apply to multiple predicates simultaneously. This approach promotes reusability and modularity in data shape definitions. F
	- Predicate groups help to simplify the data validation process, making it easier to manage and maintain complex datasets by organizing related predicates together.

- Example:
	- Schema.org
	- `DEpedia`
- Figure: Blueprint of schema.org
![[Pasted image 20230417020537.png|400]]

---
# Computing and machine learning

- [[universal approximation theorem]]
- Memory structure in computer 
	- When making knowledge base should learn the memory structure of computer, to optimize the searching time-cost of our knowledge
	- Properties:
		- 1. Organization and categorization
			- Computer memory relies on hierarchical structures, such as folders and directories, to organize and store data. 
			- By adopting a logical and hierarchical organization system, designers can enhance the accessibility and organization of information for users.
		- 2. Indexing and searching
			- Knowledge base designers can employ indexing methods, such as keyword tagging or metadata, to enable faster and more accurate searching within the knowledge base. 
			- This allows users to find relevant information efficiently, similar to how computers retrieve data based on specific addresses or indices.
		- 3. Data compression and optimization
		- 4. Scalability and extensivity
		- 5. Error handling and redundancy

### [[Missing link detection]]



- Continues [[#^4ac320|Edge-centered note-taking (above)]]. 
- When populating the vault, a satisfactory rate of conversion rate of links, is important indicator
- Currently, software like obsidian and notion still using hyperlinks to link up pages. 


---
# Collaboration

### plug-in
- maybe create a website that allow people embed their own interpretation of the popular access files or video lectures. And people could install a add-on that could show that additional resource if that viewer is installed the browser extension.
- similar thing:
	- catalyzeX