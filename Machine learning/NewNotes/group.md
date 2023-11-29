---
category: []
alias: []
tags: []
---

- 03-02-2023 08:12: created

- What is group?
	- "Group"  = A set and an "associative operation" that combines any two elements of the set to produce a third element of the set. 
	- "Group" is a algebraic structure. 
	- Applications
		- Group theory is generally concerned with the study of symmetry. 
		- Groups and fields are useful in coding theory. Groups and rings are used in cryptography as well as in number theory. Ring theory has applications in digital image segmentation.
	- Properties
		- 1. Associativity
			- for all $a,b,c$ in G $(a \cdot b) \cdot c = a \cdot (b \cdot c)$
		- 2. Identity element
			- $e \cdot a = a$ , $a \cdot e = a$
		- 3. Inverse element
			- If there is $a \cdot b = e$ and $b \cdot a = e$ . $b$ is the inverse of $a$, and it is commonly denoted as $a^{-1}$.

- Examples of application of "group" concept:
	- Number theory
		- $\mathbb{R}$ is a set 
		- $(\mathbb{R}, +)$ is a group, which has a single binary operation. Group models symmetries.
			- $(\mathbb{R}, +)$ is an additive group
			- $(\mathbb{R}, \cdot)$ is an multiplication group
		- $(\mathbb{R}, +, \cdot)$ is a field, which has two binary operations. Fields are modeled after number systems. Every field is a group.
		- Each field is a ring, and each ring is also a group. 
	- Geometry
		- Geometry groups arise naturally in the study of symmetries and geometric transformations
	- Solving polynomial equations 
		- Galois theory
- But it is common to write $\mathbb{R}$ to denote any of these three objects. 

- Geometry example
- Point group
	- ![[Pasted image 20230203084229.png]]
	- C5: Hong Kong flag
- Orthogonal group in dimension n (denote: $O(n)$)
	- Distance-preserving transformation of a Euclidean space of dimension $n$ that preserve a fixed point, where the group operation is given by composing transformation. 

---
## Reference

1. https://www.wikiwand.com/en/Group_(mathematics)