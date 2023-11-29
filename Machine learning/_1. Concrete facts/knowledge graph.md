---
alias: [KG, knowledge graphs]
---

-7-10-2022: created

- superset: 
	- [[graph]]
- subset: 
	- [[node embedding]]
	- [[Knowledge graph completion]]

- What is knowledge graph?
	- Components:
		- It can be think of "built by triples"? It has source node, relation type and destination node. 
		- Popular built: by [[Resource description framework|RDF]]
	- In [[knowledge]] [[representation]] and [[reasoning]], knowledge graph is a knowledge base that uses a graph-structured data model or topology to integrate data. Knowledge graphs are often used to store interlinked descriptions of entities – objects, events, situations or abstract concepts – while also encoding the semantics underlying the used terminology (wiki)
	- It is [[Heterogeneous graph]].
	- It can be handled by [[Graph Convolutional Networks]], [[Graph Attentional Network]]
- Why knowledge graphs adopt RDF triples
	- Path dependencies:
		- RDF is an established standard, 
	- Flexibility:
		- RDF is flexible and extensible data modal
	- Expressivity:
		- Allows for the representation of complex relationships between entities. 
	- Querying:
		- RDF provides a powerful and efficient querying mechanism -- SPARQL, which allows users to retrieve and manipulate data in a structured and precise way. 
		- Why SPARQL is good:
			- eg: RDF triple `?person rdf:type foaf:Person`
			- Versatility: 
				- SELECT, CONSTRUCT, ASK, DESCRIBE
	- Interoperability
- Properties:
	- 1. Database-like functionalities
		- In one hand, knowledge graphs are often used as a database paradigm for representing structured data and its relationship.
		- Provides a database paradigm in knowledge learning. For example, google displays a "knowledge panel" aside the search results page.
		- Amazon, eBay etc use knowledge graphs to improve their product recommendations.
	- 2. As a framework for knowledge learning and discovery
		- Supports information retrieval, natural language processing, machine learning and reasoning
		- By representing knowledge as a network of interconnected entities and relationships, those intelligent systems can perform question answering, search and decision making.
	- 3. Facilitate knowledge discovery by the integration and analysis of data from multiple sources. 
	- 4. Enhancing deductive reasoning
		- [[deductive inference]]: Giving an object fulfills some characteristics, then the statement is true. 
		- `Statement + {char1,2,...,n} --> Statement = True`
		- Say Manager John works in Accounting department, and employee Jane works in the Finance department. Then we combine information from multiple source, to draw relationship between different data points. 
	- 5. Enhancing inductive reasoning
		- `{Char 1,2,...,n} --generates--> statement`
		- Inductive = drawing general conclusion based on specific examples or observation.
		- Knowledge graphs can support inductive reasoning by providing a large set of interconnected data points that can be used to identify patterns, and make generalizations.
		- As the knowledge graph scale up, more nodes connected to one node. It can be challenging to perform inductive reasoning over knowledge graphs. 
			- 1. Use visualization to identify patterns and connections within the knowledge graph
			- 2. Use machine learning algorithms and other computational techniques to help identify patterns and connections within the knowledge graphs. 
				- Unsupervised ML over knowledge graph
					- Cluster similar data points together.
						- K-means that partitions data into k clusters based on similarity. Group data points based on RDF information -- types, properties, relationships with other data points. 
					- Association rule mining
						- Association rule mining is a technique for identifying frequent patterns, correlations, and relationships in data. In the context of a knowledge graph, association rule mining could be used to identify common patterns and relationships between different data points, even if they don't have any explicit labels.
	- 5b. Abductive reasoning (conditional reasoning)
		- Abductive = educated guess or hypothesis based on incomplete information. KG provides a rich set of related information that can be used to develop and test hypotheses.
		- Necessity versus sufficiency
		- Necessity: A person who had COVID-19 might in high body temperature
		- Sufficiency: A person who has COVID-19 would yield positive result in COVID-19 test.
		- When some objects fulfils the description partially, you doubt that guy also has COVID-19.
		- Abductive reasoning also requires the agent knows completely about the symptoms of COVID-19. 
		- By using knowledge graph to analyze information and draw connections between different pieces of data, agent can make more informed decisions. 
	- 6. Enhancing analogical reasoning
		- By providing a large set of interconnected data points, a knowledge graph can help users to identify similarities and analogies between different pieces of information. This can be particularly useful for problem-solving, decision-making, and creative thinking.
			- For example, a knowledge graph might contain information about different products, including their features, specifications, and customer reviews. By comparing and analyzing this information, a user might identify analogies between different products that could be useful for designing new products or improving existing ones.
			- Analogical reasoning typically involves identifying similarities between different objects or situations and then using those similarities to draw conclusions or generate new ideas.
			- To identify similarities, you need to have a way of categorizing and organizing information. A knowledge graph can be a useful tool for this, as it provides a structured and interconnected view of information that can help users to identify patterns and make connections between different pieces of information.
			- Once you've identified similarities, you can then go one level up in abstraction to generalize the characteristics of the group of objects. This involves identifying common features or attributes that are shared by the objects in the group and using them to create a more abstract concept or idea.
	- 7. Enhancing causal reasoning
		- KG can facilitate causal reasoning by representing relationships between different entities and events in a structured and interconnected way. By identifying and analyzing these relationships, users can gain insights into how different factors contribute to specific outcomes or events.
		- For example, a knowledge graph might contain information about the causes and effects of different medical conditions, including risk factors, symptoms, and treatment options. By analyzing this information, a user might be able to identify causal relationships between different factors and develop a deeper understanding of the condition.
	- 8. Facilitating probabilistic reasoning
		- By assigning probabilities to different outcomes or events. Knowledge graphs can support probabilistic reasoning by representing uncertain or probabilistic relationships between different pieces of information in a structured and interconnected manner.
	- 9. Facilitating spatial reasoning
		- Knowledge graphs can support spatial reasoning by representing spatial relationships between different objects in a structured and interconnected manner.
		- For example, a knowledge graph might contain information about the layout of a building, including the location of different rooms, doors, and windows. By analyzing this information, a user might be able to visualize the building in their mind and navigate through it mentally.
	- 10. Temporal reasoning
	- 11. Social reasoning
	- 12. Emotional reasoning




---
## Reference

1. [[(Course) CS224W - Machine learning with graphs (stanford)]]
2. AIOverloads Youtube video: https://www.youtube.com/watch?v=wJQQFUcHO5U
3. [[(Video) From Structured Text to Knowledge Graphs -- Creating RDF Triples From Published Scholarly Data, Bob Kasenchak]]
4. ChatGPT
