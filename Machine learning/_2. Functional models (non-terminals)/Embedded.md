- 5-10-2022: created

- Related: [[Feature selection]]

- Embedded methods perform variable selection in the process of training and are usually specific to given learning machines (R1)
- Embedded methods are not new: 1984 decision trees such as CART, for instance, have a built-in mechanism to perform variable selection (R1)

- But embedded methods that incorporate variable [[Feature selection]] as part of the training process may be more efficient in several respects R1)
	- 1. they make better use of the available [[Data|data]] by not needing to split the training data into a training and validation set (R1)
	- 2. they reach a solution faster by avoiding retraining a predictor from scratch for every variable subset investigated. R1)

- Two families of embedded methods
	- [[Nested subset method]]
	- Direct objective optimization

---
## Reference
1. [[(Paper) 2003  18500 citation, Guyon and Elisseeff, An introduction to Variable and feature selection]]