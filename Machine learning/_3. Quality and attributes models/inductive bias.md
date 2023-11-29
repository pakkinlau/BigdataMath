- 7-10-2022: created

- The inductive bias (also known as learning bias) of a learning algorithm is the set of assumptions that the learner uses to predict outputs of given inputs that it has not encountered. (wiki)

- To achieve this, the learning algorithm is presented some training examples that demonstrate the intended relation of input and output values. Then the learner is supposed to approximate the correct output, even for examples that have not been shown during training.  (wiki)

- A classical example of an inductive bias is Occam's razor, assuming that the simplest consistent hypothesis about the target function is actually the best. Here consistent means that the hypothesis of the learner yields correct outputs for all of the examples that have been given to the algorithm.  (wiki)

- Types
	- Maximum conditional independence
	- Minimum [[cross-validation]] error: choose the lowest cross-validation error among hypothesis. The [[no free lunch]] theorems show that [[cross-validation]] must be biased. 
	- Maximum margin
	- Minimum description length
	- Minimum features
	- Nearest neighbors