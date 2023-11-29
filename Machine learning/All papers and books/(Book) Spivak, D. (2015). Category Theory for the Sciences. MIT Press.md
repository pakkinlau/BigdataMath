- 29-9-2022: creaed

---
## Round 1

- Ch1: 
	- A list of views
		- Spivak also observed "language cannot explain arguments very well, like 'I believe in free will'  ". Science is about 1. Agreements that (Observation experiements matches hypothesis = success) 2. Modeling our thoughts on heuristics and graphics is convenient, but it has danger to have mistakes in conceptualizations, and data and hard evidence is grounded and heuristics evaporate.  3. The language and tool set of category theory can be useful throughout science.  4. The paradigm shift brought on by Einstein’s theory of relativity led to a widespread realization that there is no single perspective from which to view the world. 5. Most pure mathematical concepts could be communicated to scientists with no math backgroud beyond linear algebra. 6. Category theory includes a formal treatment of conceptual structures that the scientist sees often. 7. Category theory is incredibly efficient as a language for experimental design patterns, introducing formality while remaining flexible. 8. Conceptual chaos is a major problem. (Creativity --> Charity of thinking --> Organized understanding of how its pieces fit together. )9. Academics are paid to think, understand AND COMMUNICATE their findings. 
	- [[olog|ologs]] (ontology logs): 
		- It give some structure to the kinds of ideas that are often communicated in graphics. 
		- Precisely, it encompasses a "database schema", which means a system of interconnected tables that are initially empty but into which data can be entered. 
		- Completeness of meaning
			- Like figure 1.1. Flowchart (prediction --> experiment) does not specify which experts doing the science at a specific time, so that chart doesn't make sense. 
		- Arrows
			- In an olog, every arrow is intended to represent a mathematical function. 
			- It is diffcult to imagine a function that takes in predictions and outputs experiments, but such a function is necessary in order for the arrow in a olog graph to make sense.
		- Similar thing: 
			- Flow charts 
				- It looks like olog, but it does not conform to the rules laid out for ologs.
	- Meaning of data
		- Datum are only useful when they are organized into structure; teh data must be information in order to be useful.  It is the whole structure that really houses the information.
	- Certain structures and conceptual frameworks show up again and again in our understanding of reality.
		- Vector space
		- Hierarchies
		- Symmetries
		- Actions of agents on objects
		- Data models
		- Global behavior emerging as the aggregate of local behavior
		- Self-similarity
		- The effect of methodological context
	- Undetected sense
		- set-theoretic intersections (eg: a material that is both lightweight and ductile)
		- hierarchies are partial order
		- symmetries are group elements
		- data models are categories
		- agent actions are monoid actions
		- local-to-global principles are sheaves
		- self-similarity is modeled by operads
		- context can be modeled by monads.
	- History of [[category theory|category theory]]:
		- 1957 Grothendieck: Build new mathematical machinery (new cohomology theories) that granted unprecedented insight into the behavior of algebraic equations.
		- 196x: Category theory as "founcdation"
			- set theory is the foundation of math. and Bill Lawvere show category of sets is simply one category with certain nice properties, not necessarily the center of the mathematical universe. He explained how whole algebraic theories can be viewed as examples of a single system. 
		- 1980: Lambek: the types and programs used in computer science form a specific kind of category. This provides a new semantics for taking about programs, allowing people focus on combine and compose to create other program, without caring about the specifics of implementations. 
		- Daniel Kan and Andre Joyal: Repeatedly extracted the essence of a whole mathematical subject to reveal and formalize a stunningly simple yet extremely powerful pattern of thinking. 
		- 200x: Category theory is the language of choice for graduate-evel algebra and topology courses. 
		- 1995: Baez and Dolan have shown its value in making sense of quantum physics. 
			- (Baez, J.C.; Dolan, J. (1995) Higher-dimensional algebra and topological quantum field theory. Journal of Mathematical Physics 36: 6073–6105)
	- This book explain category theory by examples and exercises rather then by theorems and proofs. 
	- Its reference: 
		- "Conceptual mathematics" by Lawvere and Schanuel
		- "Categories for the working mathematician" by Mac Lane
		- "Category theory" Simmons

---
- Ch2:
	- [[set theory]]
		- as a foundation for all of mathematics. The notion of sets and functions serves as a basis on which to build intuition about categories in general.
			- 1. element of set
				- $\{x \in X\}$
				- $\{n \in Z | n > 2\}$: narrow down the range of the elements. 
			- 2. Popular sets 
				- $\emptyset$: empty set
				- $\N$:  set of natural numbers
				- $\Z$: Set of integers
			- 3. Relations between sets
				 $\subseteq$ : subset eq. eg: $Z \subseteq N$.
			 - 4. Functions over sets
				 - If we have two sets X and Y, then a function f from X to Y denoted as $f: X \rightarrow Y$. We call X the domain, and Y the codomain. It is like datatypeannotation in programming, which set type X and Y is annotated for the function. 
				 - Composition of functions. 
					 - Say $f: A \rightarrow B$ and $g: B \rightarrow C$, then $g \circ f : A \rightarrow C$. $f$ executes first and then $g$.
				 - Isomorphism:
					 - A function is an isomorphism, denoted $f: X \rightarrow Y$, if there exists a function $g: Y \rightarrow X$ such that $g \circ f = id_X$ and $f \circ g = id_Y$. We also say f is "invertible" and g is the "Inverse" of f.
				 - One-to-one correspondence:
					 - There is no two arrows will hit the same element of Y.
			 - 5. Mapsto $\mapsto$ notation
				 - If $N \rightarrow N$, and the function sends every natural number to its square, then we express the  changes of the inputs from outputs element: $x \mapsto x^2$.
		- Commutative diagrams
			- That visualize composition of functions in graphs.
	- [[olog|ologs]]
		- 1. Types: 
			- Each type is represented as "a box containing a singular indefinite noun phrase"
			- Possible types could be "a man" (node type), and (link type), like "a pair(a,w), whee w is a woman and a is an automobile"
		- 2. Compund structure type
			- eg: "A man and a woman", "a food portion f and a child c such that c ate all of f", "A triple (p,a,j), where a is an author of p, and j is a journal in wheich p was published. "
			- Decomposition:
				- good parctice to declare the variables in a compound type. eg: "a man m and a woman w", or " a pair (m,w), where m is man and w is a woman".
			- A list of good practice rules
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
		- 3. Aspects
			- An aspect of a thing x is a way of viewing it, a particular way in which x can be regarded or measured. In ologs, the word "aspects" simply means function.
			- Valid aspects: 
				- (a woman) is (a parson), (a molecule) has molecular mass (a positive real number)
			- Invalid aspects
				- (a person) has (a child)
			- Reading aspects and paths as english phrases
		- 4. Facts = Path equvalence: 
			- $A[f,g] \simeq A[h,i]$. (Mathematically, the triangle in olog commutes)
			- Indicate check marks around an arrow to denote that arrow is intended to commute. 
		- 5. English phrase --> ologs
			- A formula for writing facts as English
				- See "EG3"

- Ch3 : [[set theory]]
- Product of two sets: $X \times Y = \{(x,y)| x \in X, y \in Y \}$.
	- Natural projection ($\pi$): $\pi_1 : X \times X \rightarrow X$  and $\pi_2: Y \times Y \rightarrow Y$
	- See figure 4
	- Properties
		- 1. Univeral property for product (diamond pattern)
			- For a natural projection ($\pi$): $\pi_1 : X \times X \rightarrow X$  and $\pi_2: Y \times Y \rightarrow Y$, there exist a unique function $A \rightarrow X \times Y$ such that the flow points back to the starting point and the diagram commute. A diamond shape pattern appears.  
			- If there is a set $A$ that could performs $f: A \rightarrow X$ and $g: A \rightarrow Y$, then there also exist a function $\langle f,g \rangle$ that produce $X \times Y$ product. 
		- 2. Ologging products
			- Given two objects in an olog, there is a canonical label $<< c \times d>>$ for their product $c \times d$, written in $<<c>>$ and $<<d>>$, such that $<<c \times d>>$ := a pair $(x,y)$, where x is $<<c>>$ and y is $<<d>>$.
			- A canonicaled product of two set CANO($C \times D$) --> a pair of canonicaled entity CANO($C$), CANO($D$)
- Coproducts
	- Coproduct of $X:=\{a,b,c,d\}$ and $Y=\{1,2,3\}$ is $X \sqcup Y=\{a,b,c,d,1,2,3\}$. 
	- eg: X: economy-class seat in an airplane. Y: first-class seat in an airplance. $X \sqcup Y$: a set in an airplane. 
	- Properties
		- Universal property for coproduct

- Finite limits in set
	- Pullbacks
		- Fiber product of $f: X \rightarrow Z$ and $g: Y \rightarrow Z$ is $X \times_Z Y := \{(x,z,y) | f(x) = z = g(y)\}$.



- EG1: 
![[Pasted image 20220929042042.png]]
![[Pasted image 20220929042049.png]]
- Figure: Upper one demonstrate an invalid aspect because not every parent has a child. To capture parent-child relationship, have to add a link olog pattern. The way to specify a link type. notice variable "p" and "c" is the arrow type on the olog graph.

- Example 2: 
![[Pasted image 20220929041311.png]]
- Figure: p30 of the book. The way to specify an entity type. This olog gives virtual datatype for machine and human to understand what is "a child". Each path represent some meanings that is different to other paths. 

- EG3
![[Pasted image 20220929044251.png]]
- Figure: writing facts as English

![[Pasted image 20220929044917.png]]
- Figure: From p42. 

![[Pasted image 20220929054831.png]]
- Figure: from p50. Disjoint union of dots. 

---
## Captured images: 


![[Pasted image 20220929013833.png]]
- Figure: 1.1, incomplete olog

![[Pasted image 20220929010508.png]]
- Chapter 1: An example of [[olog]].

---
![[Spivak, D. (2015). Category Theory for the Sciences (Textbook version).pdf]]