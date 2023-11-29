- 26 July 2023: created
---
# Design Direction
- Factual knowledge: 
	- Entity based notes.
		- The vault should use "entity/concept" as a unit of a markdown file. 
		- The advantage of this idea is, it groups up relevant information into a dot. Using software to visualize the cloud of concepts and the relationship between them. This would enable the user to navigate different ideas quicker.
	- Decoupling context from the concepts
		- Many books, articles relies on lecture notes, providing adhering meanings with the use of context. 
		- However, when the user already know the meaning of that concept, the context become redundant and wordy. 
- Pattern knowledge:
	- Focus on solving the difficulties on capturing pattern knowledge
	- Pain point: while factual knowledge can be easily captured (eg: database), the the number of parameters between the "Weight of Word Embedding" and the "Weight of Attention" in popular models like BERT and GPT is typically around 1:3 to 1:4. (The finding in 27 July 2023). SO the most 
- Computations 
	- Computational efficient
		- Build a better data representation of notes, that allows the vault to add more functions in the future. 
	- Discoverable:
		- Users could record their own knowledge base into a system. Their previous writing will be recalled and suggested to the user when the user is writing another area of notes. 


---
# Success indicator
- Sept 2022 first version
- July 2023 second version
- Setting up the [[objective]] for the evolution of the vault design:
	- 1. Shorter information retrieval time consumption
		- Shorten the time needed for the machine or human agent to gather information that surpass the gate of "familiarity".
		- Concept retrieval time (t) 
			- Case 1: reading a single plain note: $t = {C \over s}$,  $C$ is the total content of one note, $s$ is the speed of the agent.  
	- 2. Algebraic computability
		- Enable the machine or human agent to perform inference with the graph. 
		- Some example is JSON, XML etc. These formats is like key-value pairs, that sticks one label to one value. Query language could search on the data based on those "attributes".
		- With computable notes, we can build up some more advanced applications like, generating notes for a concept + multiple sources of handout copies related to that concepts, that generate a much more sense making notes. 
	- 3. Context = Informative and making sense
		- Content is meaningful for making sense. While we are shortening the information retrieval time, we also recognize the value of content, eg: examples, demonstrations.
	- 4. Reducing entropy in the process of providing structure to the mass of the elements of the note
		- By artfully arrange the structure of "concepts" and "context", we can boost up both (a) concept searching speed and (b) the sensemaking of the concept.
	- 5. Discoverable
		- It is very often in our real life or in the way of making notes, a large portion of the notes becomes very hard to be discovered. If the notes is not reusable, what is the value of writing them? 
	- 6. Avoid double accounting as much as possible.
		- We need to control there is only a single place to add up information for one concept, so the value of prior works would be discovered and interacted.
	- 7. Supports arithmetic comparison in between same class concepts
		- Supports raising questions about "difference between dataframe (X) and NumPy array (Y). " That requires both sides of the notes have some related dimensions 

---
# Conceptual design

- Make a UML class diagram here


- Make a UML sequence diagram here


----

