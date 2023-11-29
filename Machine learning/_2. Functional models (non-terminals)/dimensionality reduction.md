- 5-10-2022: created

- Superset:
	- [[dimensionality]]

- [[dimensionality reduction]] is a general field of study concerned with reducing the number of input features. (R1)
- Dimensionality reduction methods include feature selection, linear algebra methods, projection methods, and [[autoencoder]] (R1)
- There is no best technique for dimensionality reduction and no mapping of techniques to problems. (R1)

---
- Problems:
	- Large numbers of input features can cause poor [[performance]] for machine learning algorithms. (R1)

---
- Types of dimensionality reduction methods:
	- [[Feature selection]]
	- Matrix factorization
	- [[manifold learning]]
	- [[autoencoder]]

- Typically, linear algebra and [[manifold learning]] methods assume that all input features have the same scale or distribution. This suggests that it is good practice to either normalize or standardize data prior to using these methods if the input variables have differing scales or units.

---
## Reference
1. Brownlee's blog: https://machinelearningmastery.com/dimensionality-reduction-for-machine-learning/