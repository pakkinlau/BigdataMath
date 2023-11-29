-27-9-2022: created


- It have been a central them throughout the history of AI.
	- Classic tests of intellect, from strategy games to abstract mathematical discovery, served as inspirational goal posts that pushed the limits of "machine intelligence" through a need to devise ever smarter ways of searching for winning solutions. 

- [[Search algorithm]]

- Good reasoning AI should be: 
	-  (Generativity) capturing the statistical regularities of unbounded [[General space]] 
		- The generative capabilities of foudnation models are esstential for effective reasoning. Due to the unbounded search space, it becomes intractable to enumerate all kinds of possibilities. Instead, with foundation models, one can "model the distribution of the optimal decisions", and generate suitable candidates to process to the next step. 
		- In particular, as foundation models offer a generic way of modeling the output space as a sequence, the next decision generation is entirely unconstrained and hence universal.
		- Such flexibility is essential for many of the reasoning challenges we discussed, to allow creative generation in domains such as mathematical conjecturing and synthesizing novel programs. 
	- (Universality) allowing positive transfer across tasks and scenarios 
		- Many reasoning problems exhibit similar latent structures. The unifying framework imposed by a foundation model can transfer and share significant [[Heuristics]] across tasks, ranging from generalizing low-level techniques that work well for one task to new scenarios all the way to directly finding meta-techniques that work well across numerous kinds of problems.
		- Since a foundation model is trained across many domains, it can positively transfer meta-knowledge encoded in the foundation models’ weights across tasks and domains (Papadimitriou and Jurafsky, 2020; Lu et al. 2021a)
		- The foundation model training and adaptation framework encourage a separation of concerns, where foundation model training learns meta-knowledge such as the shared search tree structure between drug retrosynthesis and propositional logic proofs, and the adaptation phase can focus on learning the task specific vocabulary.
		- Thus, foundation models can reduce the complexity of the learning problem in the adaptation phase, improving sample complexity and generalization.
	- (Grounding) exploiting the grounding of knowledge in multi-modal environments
		- Reasoning problems are often easily expressed in symbolic languages (e.g., mathematics, code, SMILE representation of molecules). However, these symbols have deep underlying semantic meanings — saying “isosceles triangle” paints a vivid image in the human mind. 
		- Foundation models can enable deep groundings and semantic meanings. 
			- 1. First, grounding representations in other modalities, such as visual or physical, are essential to grasp abstract concepts in reasoning tasks and endow them with concrete meaning (Larkin and Simon 1987; Jamnik 2001)
				-  Since the models may be trained on multiple modalities, foundation models can assist in understanding a range of data sources (e.g., images, texts). Hence, in the geometry example case, with its understanding of geometrical shapes learned in natural images, a foundation model could effectively utilize the diagrammatic representation of the problem. 
				- However, aligned multi-modal data in reasoning is scarce, and it remains an open question whether foundation models can discover connections between different modalities in an unsupervised manner (e.g., discovering of commutative diagram with the corresponding algebraic equations).
			- 2. even within the symbolic domain, symbols can have various levels of interpretation. For example, high-level programming languages can be translated to low-level assembly codes. Foundation models can learn a shared representation that encompasses these various views. 
				- Past works have shown that self-supervised tasks (Han et al., 2021; Peng et al, 2021; Li et al, 2021a)  allow the model to understand the inner workings behind the high-level code scripts, and further assist downstream tasks.

- Future challenges in reasoning
	- See p43 of [[On the Opportunities and Risks of Foundation Models (Bommasani et. al, 2021).pdf]]

- Old ways: symbolic methods (but the involved engineering effort and the need to formalize heuristics to tackle intractable search spaces quickly proved cumbersome. )

- Real world problems with unbounded search space
	- 1. Proving theorems
	- 2. Program syntheis (Program Synthesis. Found. Trends Program, Gulwani et. al, 2017)

- Trials:
	- 1. Constrained search space to make the problem tractable. But that suffered from the limited kinds of actions the solver could issue. eg: the solver could only apply theorems from a known database to proce a target theorem, instead of synthesizing novel theorems and lemmas.
	- 2. Apply large language models (which offered a generic way of modeling the output space as a sequence)
		- Predicting protein structures (Senior et al 2020)
		- Proving formal theorems (Polu and Sutskever 2020)
		- Conjecturing theorems (Urban and Jakubuv, 2020, Li et al, 2021b)
		- Synthesizing programs from natural language (Chen et al. 2021f)
		- Repairing, generating and understanding code (Yasunaga and Liang 2021).
	- 3. Scaling model size significantly improves reasoning capabilities (Polu and Sukskever 2020)

---
## Reference

- [[(Paper) On the Opportunities and Risks of Foundation Models (Bommasani et. al, 2021)]]