- 7-10-2022: created

- Abstract:
	- [[optimization]], [[Search algorithm|search]], and [[supervised learning]] are the areas that have benefited more
from this important theoretical concept of [[no free lunch]]. 


- intro:
	- [[optimization]] problems occurring in various fields of science, computing, and engineering depend on the number of parameters, the size of the [[solution space]] and,mainly, on the [[objective]] whose definition is critical as it largely determine the level of difficulty of the problem. 
	- Defining and solving an [[optimization]] problem is sometimes an extremely difficult and demanding [[tasks|task]].
	- Researchers tries to build solid mathematical concepts to find "short cuts", bt none of these methods has proven to be successful to all types of the problems it was applied.
	- NFL ([[no free lunch]]) theorem: "averaged over all optimization problems, without re-sampling all optimization algorithms perform equally well."
		- that yields a lot of controversial discussion regarding the possibility to invent and effectively use general purpose algorithms in various fields where only a limited view of the rael-world problem exists. 

- Discussion angle:
	- [[optimization]]
	- [[supervised learning]]
	- [[Search algorithm|search]]
- Worth mention but out of the scope of the paper: 
	- user interface design
	- [[network calculus]]

---
## Early concepts

- Concerns
	- 1. "Can anyone prove [[inductive inference]] from first principle?" that is, given the [[performance]] of a learning [[algorithm]] on the training set, is it possible to obtain information on its ability to provide an exact [[representation|representation]] of the target function for examples outside the [[Data|data]] set?
	- 2. "What are the assumption on the distribution of real-world data (the target function) can help with the generalization for training algorithms, such as back-propagation, which aim to minimize the error on the training data?"
	- 3. "Is there a mathematical basis of estimating when over-training occurs and proceed in modifying the learning algorithm in order to bound the effects of such over-training"
	- 4. Is it possible to express in mathematical terms the ability of a training set to faithfully represent the distribution over the entire data space?
	- 5. What are the hypotheses under which non-parametric statistics techniques, such as cross-validations, which are designed to choose between learning algorithms, succeed to diminish the generalization error?

- In addressing these matters, the formalism proposed seems to extend the classical [[Bayesian inference]] formalism using the [[hypothesis function]], i.e., the distribution of the data set as learned by the generalizer. 

---
## 3. Research efforts


---
## 4. Recent work of Wolpert

---
## 5. Main research carried out by several researchers on NFL for optimization and evolutionary algorithm

---
## 6. NFL theorems for supervised learning


---
## 7. Synopsis and some concluding remarks.




![[2019, Adam et al, No free lunch theorem -- a review.pdf]]
