---
alias: [ologs]
---

- 29-9-2022: created

- This concept is created by Spivak himself. So his book [[(Book) Spivak, D. (2015). Category Theory for the Sciences. MIT Press]] should be sufficient. 

- Definition:
	- The theory of ologs is an attempt to provide a rigorous mathemeical framework for knowledge represenation, construction of scientific models and data storage using category theory, linguistic and graphical tool. (Wiki)
	- It is short for "ontology log". (Wiki)
	- Precisely, it encompasses a "database schema", which means a system of interconnected tables that are initially empty but into which data can be entered. (R1)

- Components:
	- 1. Types
		- There is no difference of "link" and "node" in olog. A type could be a pair of thing that is "factorized" from a relation. eg: a person owns a car, but it yields invalid aspect if we just throw it to be A->B. The solution is on point 6. 
		- A type is an abstract concept, a distinction the author has made. We represent as a box containing a "singular indefinite noun phrase". The label on taht box is what one should call "each sample" of that class, thus "a man" box represent a set of men.
	- 2. Types with compound structure: 
		- Compound = composed of smaller units
			- (a) pair of thing: A man and a woman $\xrightarrow{replace}$ A pair (m,w) where m is a man, w is a woman
			- (b) adverb clauses: A food portion f and a child c such that c ate all of f
			- (c) a triple (p,a,j) where p is a paper, a is an author of p, and j is a journal in which p was published. 
	- 3. Aspects (~ Abstraction or ~ characterized aspects)
		- An aspect of a thing $x$ = A way of viewing $x$, a way in which $x$ can be regarded or measured. 
		- An aspect of a thing $x$ = The codomain of the set of possible answers, or results of the measurement. 
		- eg: A woman "can be regarded as" a person. 
		- eg: A molecule "has a molecular mass" positive real number (a screenshot of some characteristics of the object)
	- 4. Invalid aspects
		- eg: a person has a child
			- A person could have no children or have more than 1 children.
		- eg: pencil "uses" a piece of lead
			- invalid behavior of the source object
	- 5. Reading aspects and paths as English phrases
		- Each $X \xrightarrow{f} Y$ can be converted to English sentence.
	- 6. Converting non-functional relationships to aspects
		- Non-functional relationship = Some arguments that are invalid if we just throw it to be A>B. eg: A person owns a car. The predicate is not a right description for the source object. The rephrased sentence could be "A person (could) owns a car".
	- 7. Facts (path equivalence)
		- In a commutative diagram (which means showing there is a set of paths commute each other), use a check mark (V), in the region bounded by the two paths,.

![[Pasted image 20220930175716.png]]
- Figure in (R1, p.9)
	- Type specification , which each arrows are depicting a valid aspect of the source object.
	- The whole thing is an olog. 
	- olog represents a framework in which to record data about objects held above the ground, their mass, their height, and a comparison (the ?-mark in the middle) between the number of seconds till they hit the ground 

![[Pasted image 20220930184906.png]]
- Figure in (R1, p28)
	- Type specification 
	- When converting ologs back to natural language, which means " states path A = path B.". For example, Path 1 P(x) = a phone which has an area code phone number, path 2 Q(x) = a phone that is physical phone located in a region. And then state P(x) = Q(x) by the commutative diagram. 
	- Shortened the label to be a pair of variable, and also classified the type of variable.

![[Pasted image 20220929044251.png]]
- Figure: writing facts as English. 

---
- Expressing products category
	- See [[Product (category)]]


---

- Ologs versus flow chart:

- A list of good practice rules (R1)
	- 1. Begin with the word a or an.
	- 2. refer to a distinction made and recognizable by the olog's author (relate a new concept to a known concept.)
	- 3. refer to a distinction for which instances can be documented. 
	- 4. be the common name that each instance of that distinction can be called
	- 5. declare all variables in a compound structure.
	- First four rules ensure that the class of things represented by each box appears to the author to be a well defined set, and that the class is appropriately named. The fifth rule encourages good readability of arrows
	- 6. Rules for arrow label texts
		- a. Begins with a verb
		- b. Yield an English sentence
		- c. Refer to a functional relationship
		- d. Constitute a useful description of that functional relationship
		- (First three rules ensure the class of thigns represented by each box appears to the author as a well-defined set. The fourth rule encourages good readability.)

- [[category theory|category theory]]




---
## Reference
1. [[(Book) Spivak, D. (2015). Category Theory for the Sciences. MIT Press]]
2. [[(Paper) Spivak, D. I., & Kent, R. E. (2012). Ologs -- A Categorical Framework for Knowledge Representation. PLoS ONE, 7(1), e24274]]