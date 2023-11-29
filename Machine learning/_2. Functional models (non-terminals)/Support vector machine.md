---
alias: [SVM]
---

- 26-9-2022: created


---
## Section 1: general concepts: 

- SVMs are [[supervised learning]] models with associated learning algorithms that analyze data for [[classification]] and [[regression]] analysis. (wiki)
- Developed at AT&T Bell laboratories by Vladimir Vapnik with colleagues. (wiki)
- SVMs are one of the most robust prediction methods, being based on statistical learning frameworks or VC theory proposed by Vapnik.  (wiki)
- In addition to performing linear [[classification]], SVMs can efficiently perform a non-linear classification using what is called the [[kernel method|kernel trick]], implicitly [[Feature map|map]] their inputs into high-dimensional feature space. 

- Applications of SVMs
	- SVMs mostly out of favor because they need ready real valued vectors as features. It is very cumbersome for many tasks, such as image recognition, to prepare the features in order to feed an SVM. 
	- However, we can use a linear SVM at the end of a deep convolutional deep network  (convNet) and train them jointly using SGD + backprop algorithm. 


- Concepts:
	- "Margin" and the "confidence" of our predictions:
		- The distance separating the closest pair of data points belonging to opposite classes. These points are called the support vectors, because they are the data obsrevations that "support", or determine the decision boundary. 
		- To train a support vector classifier, we find the "maximal margin hyperplane", or "optimal separating hyperplane", which optimally separates two classes in order to generate to new data and make accurate classification predictions. 

---
- Functional margin of $(w,b)$: $\hat \gamma^{(i)} = y^{(i)}(w^Tx^{(i)}+b)$.
.... more (p.63 of cs229 book)

---

- Optimal margin classifier
- Kernal that gives SVMs efficiently in very high dimsnional feature spaces. 

![[Pasted image 20221009125519.png]]
- (R3) We can use SVM to learn very non-linear decision boundaries like that. But that is a linear decision boundary in a very high-dimensional space. 


---
## Reference
- [[(Course) CS229 Machine learning]]
- wikipedia
- CS229 youtube lecture 