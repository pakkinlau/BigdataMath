- 26-9-2022: created

---
- Contribute to: [[Foundational model]]

---

- Why call it "foundational model" instead of "pre-trained model" or "self-supervised model": Existing terms partially capture the technical dimension of these models, but fail to capture the significance of the paradigm shift in an accessible manner for those beyond machine learning. 

![[Pasted image 20220926233850.png]]
- Figure: The model can be adapted to a wide range of downstream tasks. 

---
![[Pasted image 20220926234422.png]]
- Figure: Overview of what AI can do in the current stage

- Modeling qualities:
	- Next generation of models (from [[On the Opportunities and Risks of Foundation Models (Bommasani et. al, 2021).pdf]])
		- [[Multimodality]] (to consume, process and potentially produce content from different sources and domains, such as text + image)
		- Memory capacity (to effectively store and retrieve the acquired knowledge)
		- Compositionality (to foster successful generalization to novel settings and environments)

- Training qualities
	- Instead of modality-specific objectives, which often heuristically.
	- training objective for foundational models will have 2 changes: 
		- "principled selection", derived from systematic evidence and evaluation.
		- "domain-generality", to provide rich, scalable and unified training signal across data sources and modalities. 
	- Trade-off between [[Generative learning algorithms]] and [[Discriminative learning algorithms]]

- Language
	- To date in 2021, NLP has been the field most profoundly affected by foundation models. 
	- The first generation of foundational models showcased an impressive variety of linguistic abilities, and a suprising amount of adaptability to large range of linguistic situations. 
	- The introduction of ELMo and BERY in 2018, the field of NLP become largely centered around using and understanding foundational models. 
	- The field using foundational model, moving towards more generalized language learning as a central approach and goal. 
	- Impacts FM --> NLP
		- 1. skilled langauge generators eg GPT-3
		- 2. tasks:
			- classification tasks for a whole sentence or documents
			- sequence labelling
			- span relation classificaiton
			- generation task (producing new text that is conditioned strongly on an input)

- Reasoning and search (section 2.4)
	- 1. In the early days, symbolic methods were the dominant approach for reasoning, (before 1995) but the involved engineering effort and the need to formalize [[Heuristics]] to tackle intractable search spaces quickly proved cumbersome. 
		- ----------------> Why it is cumbersome and require a lot of engineering effort?
	- 2. Recent results:
		- AlphaGO (2016), by exploiting statistical structures and learning useful heuristics. 
		- -----------------> How alphaGo exploit statistical structures and learn useful [[Heuristics]]?
	- 3. foundation models should play a central role towards general reasoning as vehicles for
		-  (Generativity) capturing the statistical regularities of unbounded search spaces 
		- (Universality) allowing positive transfer across tasks and scenarios 
		- (Grounding) exploiting the grounding of knowledge in multi-modal environments
	- 4. Problem of reasoning: unbounded search spaces, where systems must deal with numerous kinds of open-ended alternatives
		- eg: a triangeometry  problem,  the system could add a new auxiliary point with an arbitrary construction, say a perpendicular line, a parallel line, or a tangent circle, and the search space only grows larger as the diagram grows more complicated.
			- how can systems find this without extensive search?
	- 5. Humans (mathematicans) are not confined with searching in diagram constructions, they can apply a vast number of theorems from various branches of mathematics, make high-level conjectures, formalize new mathematical concepts, or find counterexamples. This contrast AlphaGo, the search space is considered much smaller.

- 2.6 Philosophy of understanding
	- 1. How foundation model are trained? -- since the training regime delimits what information the model gets about the world
	- 2. Why it is important to clarify these questions for the further development of such models.
	- 3. What we mean by understanding, by clarify it, to determine whether a model has achieved understanding (epistemology)

- 2.6.1 What is a foundation model? 
	- 1. They are self-supervised. As long as it is just learning co-occurence patterns of the sequencees it is exposed to, then it counts as a foundation model by our definition. 
	- On the case where self-supervision is the model's only formal objective: 
		- In self-supervision, the model’s sole objective is to learn abstract co-occurrence patterns in the sequences of symbols it was trained on. 
		- There is no obvious sense in which this kind of [[Self-supervised learning|self-supervision]] tells the model anything about what the symbols mean. -- knowling that "sandwich" and "peanut" likely to co-occur says nothing about what sandwiches are, what jelly is, how these objects will be combined.

- 2.6.2 What is at stake (what's important)?
	- Trust 
	- Interpertability
	- Accountability

- 2.6.3 What is understanding
	- Internalism: 
		- Language understanding amounts to "retrieval of the right internal representational structures" in response to linguistic input. Thus, language understanding is not even a possibility without a rich internal conceptual repertoire of the right kind.
	- Referentialism: 
		- Roughly, an agent understands language when they are in a position to know what it would take for different sentences in that language to be true (relative to a context). That is, words have referents and (declarative) utterances are truth-evaluable
	- Pragmatism: 
		- Understanding requires nothing in the way of internal representations or computations, and truth and reference are not fundamental. Rather, what matters is that the agent be disposed to use language in the right way. This might include dispositions toward inference or reasoning patterns, appropriate conversational moves, and so on. Crucially, "the relevant verbal abilities constitute understanding".
- Internalism and referentialism can both be cast as defining a mapping problem: to associate a linguistic sign with a “meaning” or a “semantic value”. 
---

![[On the Opportunities and Risks of Foundation Models (Bommasani et. al, 2021).pdf]]