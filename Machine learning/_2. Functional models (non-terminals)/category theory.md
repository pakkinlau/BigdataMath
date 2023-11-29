---
alias: [category theory, abstract nonsense]
---

- 28-9-2022: created

- Related: Functional query language, Olog, [[Reductionism]]

- What is category theory?
	- Category theory is a general theory of mathematical structures and tehri relations that was introduced in the middle of the 20th century. (R8)
	- In category theory, we avoid thinking about what an object is, and look only at how it interacts with other objects. It turns out even if we are not allowed to talk about the internal structure of an object, we can still pin down some objects by talking about their interactions. (R11). 
	- You can use category theory to model logic of scientific arguments, or model lambda calculus (which is the basis of computer programming) (R7)
	- Category theory is a sort of universal mathematical [[language]] which reveals connection between different subjects, like logic and geometry. It is abstract, yet it yields deep, elegant and powerful results. (R12).

- Why I found this: when learning [[Kernel space]]

- Why learning category theory? Why category theory is relevent to our problems. 
	1. A mathematical object is determined by its relationships to other objects; an often fruitful way to discover properties of an "object" is NOT to investigate the object itself, but rather to study the collection of maps to or from the object.  (R8)
		- Objects: sets, groups, measurable spaces, vector spaces, topological spaces etc. 
		- Maps: (would be fill in later)
	- 2. Stanford Encyclopedia of Philosophy states: “Roughly, [[category theory|category theory]] is a general mathematical theory of structures and of systems of structures… At a minimum, it is a powerful language, or conceptual framework, allowing us to see the universal components of a family of structures of a given kind, and how the structures of different kinds are interrelated. Category theory is both an interesting object of philosophical study, and a potentially powerful formal tool for philosophical investigations of concepts such as space, system, and even truth.” (R13)
	- 3. By keeping category theory as a reference model, we are more able to see the common components of a family of structures of any given kind that will finally help us understand how constructive and destructive structures and behavior are interrelated and integrated. (R13)


	- Knowing category theory is like, being able to lift yourself above your program. It’s like otherwise you, you know, you’re just like a little ant working in an anthill (R3) 
	- Abstract nonsense: In category theory, people use examples from every branch of mathematics because it’s like a theory that abstracts over all other branches of mathematics. (R3)
	- Informative things is about the structure. Mathematics is all about structure. (R3)
	- We define things and then we describe them by how they interact with other things. Not by inspect the object inside. (R3)
	- Category theory essentially studies all the different ways in which things can be composed and decomposed. (R3)
	- Category is not just about structure study. You can add additional structure to the category or you can discover additional structure in this category. (R3)
	- Language cannot explain argument very well. We humans usually process views in [[Heuristics]]. And arguments are the most important matter for science. (R4)
	- Conceptual chaos is a major resistance for creativity. (Creativity requires charity of thinking, and charity comes from organized understanding of how pieces fit together.) (R4)

- Why we need abstract nonsense:
	- On the other side of the computer and that’s the human programmer. Okay? So programming is not just about the computer, it’s about the interaction between the human and the computer.  (R3)
	- The computer doesn’t really care about, you know, how structured your code is. 
	- A programming language reflects how human mind works, rather than how computer works. 
	- Computer doesn't have such memory-specified structure as a requirement. 
		- In storage of data, Human way: Have a Dewey decimal system where people can locate where books are. Amazon warehouse -- Just put things whereever and just remember where they put them. It's a computer, so they don't need human memory structure. 
	- 

- Category theory and programming
	- mostly category theory is used in functional programming, but object-oriented programming also has very rigid structure (R3).
	- Data hiding: you want to describe your object, not by how it’s implemented, but how it interacts with other objects. Namely its methods. (R3)

- Category theory and the real world 
	- Based on the "Mathematical Universe Hypothesis", the emerging reality is that we live in a "relational reality". (R13)
		- It means that the properties of the biosphere around us stem not from properties of its ultimate building blocks, but from the relations among these building blocks.  (R13)
		- While the position of category theory as a foundational language in applied mathematics and mathematical modeling is still in its infancy and a rather unexplored path, it is crucial to understand how it can help us understand the complex problems facing humanity.
	- This means that the properties of the world around us stem not from properties of its ultimate building blocks or individual units, but from the relations among these building blocks and units. (R13)
		- The systems and structures we look at in the universe are self-organized at several different levels. 
		- We live in a relational reality where self-organization is an obvious principle which is embedded in our description of the universe. 

- Mentality of category theory
	- Composition and decomposition: If we are solving meaningful problems, typically a big problem, we split it to some reusable and maintainable chunks solution, and then combine them back for solving bigger problems. (R3)
		- My thought:
			- Composable comes from the associativity of the morphisms
			- Discomposable comes from the success identification of entities and morphisms out of the mess. 
	- Being able to do these decompose / compose, is essentially the description of "programmer / mathematician /physicist". (R3)

- History of category theory. 
	- Introduced in mid 20 century, in the work of "algebraic topology".
	- Nowadays, category theory is used in almost all areas of mathematics, and in some computer science
	- Many constructions o fnew mathematical objects from previous ones, that appear similarly several contexts are conveniently expressed and unified in terms of categories. 

---

- Tools:
	- [[olog]]

---

- [[Category]]

---
- Morphism
	- Recall a single category has two sets of components: 1. a set of objects, 2. a set of morphisms.
	- My own thought: 
		- all morphisms are the object to object relations, not a category to category relation, because it has a special term called "functor" for the latter one. But I am not sure whether morphisms and functors are in the same family (needs to verify)
	- $f: A \rightarrow B, f \in hom(C)$, One particular morphism or map or arrow. Each morphism $f$ has a source object $a$ and target object $b$.
	- Insight, when defining an arrow, we can also always denote the datatype / source-target object type of the arrow. eg: A function between set objects $A$ and $B$, the function would be $f:    \mathbb{R} \rightarrow    \mathbb{R}$. (R12)
	- Types: Say an arbitrary 'types' (eg: int, or str) are our category, we can form a different "types category" by taking the arrow $A \rightarrow B$ . (R12)
	- $\circ$: compisition of morphisms, such as $g \circ f$.
		- Compositions are governed by two axioms:
		- Associativity law: The bracket won't affect the result -- $h \circ (g \circ f)$ = $(h \circ g) \circ f$. (R1) 
		- Identity law: 
			- "Identity" means after a binary operation, the set of element remain unchanged every element of the set when the operation is applied. (R5)
			- such as: A x W --> W, which A is the identity. 
			- Identity is a shortened version of its full name "identity element"
			- This law tries to explain some self-loops can be collapsed. 
			- Maybe all ologs are DAGs, and all simple paths (with no branches) that ultimately pointing back to itself should be collapsed?
			- For every $ob(C)$, there exists a morphism $1_x: x \rightarrow x$ called identity morphism for x, such that for every morphism $f: a \rightarrow b$ we have $1_b \circ f = f = f \circ 1_a$. (R1) 
			- Another way to describe it:  $\mathscr{C}(A,A) = \{1_A, \dots\}$ (R2)
			- If there is a path that points back to the source of the first arrow, then the path doesn't make any changes after all. Therefore it commutes to an identity arrow.
			- However, tha path cannot be collapsed since there is information in ber

- Types of morphisms (R1)
	- Monomorphism
	- Epimorphism
	- Bimorphism
	- Isomorphism
	- Endomorphism
	- Automorphism
	- Retraction
	- Section

- Example
	- Quotient space
	- Direct products
	- Completion
	- Duality
---
## Duality

- $f: A \rightarrow B$ in $C$ becomes the arrow $f*: A* \leftarrow B*$ in $C^{op}$. (R12)
	- The "op" of $C^{op}$ comes from the word "opposite".
	- star notation reminds us we are in the ual category, but these are the same objects and arrows. The arrows have just been formally turned around. Not inverse arrow.  (R12)
- Composition and itentitied are defined by: (R12)
	- $f* \circ g* = (g \circ f)*$
	- $1_A* = (1_A)*$ 
- It seems trival but it is actually powerful: for any category-theoretic concept in $C$, we get a "dual" concept in $C_{op}$, for which we get theorems for free. And the dual concepts turn out to be just as important as the original concepts. Such that expand the scope of our theory.

- Story of duality (R12)
	- Important concept in category theory and beyond
	- eg: 1660 mind-body dualism
		- Descartes argued for mind-body dualism (mind is distinct from our body, including our brain, but the two go together and complement each other)

![[Pasted image 20221001104336.png]]
- Fig: illustraing the commutative diagram of a duality category C star.


---
 [[Functors]]


---
## Homomorphism

- Hom(X,Y), also called is the set of morphisms from object X to object Y. X and Y is gonna be the same category. We can turn this into a functor. (R6)
	- What is the difference of Hom(X,Y) and a simple functor?
- In a restrictive sense, a homomorphism is a function between two algebras that preserves algebraic structure. (R10)


---
- Commute of diagram
	- Commute: regardless which way you traverse the diagram, from element A to B, it gives the same result, then all possible path that go to B from A are all commutes. 

---
## The above section trying to make sense of what is a single category. Below tries to discuss how a group of category interacts. 

![[Pasted image 20220930124127.png]]
- Figure: illustration from (R8)

- Functor: relationships between (categories)
- Relationship between (functors): natural transformations =$RB^2$(categories)
- We can see a hierarchy of question:  $RB^n$(categories).
	- Application of higher order categories see: https://ncatlab.org/nlab/show/applications+of+%28higher%29+category+theory#related_pages
- 0-category: same as a set. 
- (0,1)-category: A category whose hom-objects are (-1)-groupoids.
- 1-category: 


- parametric polymorphism and natural transformation 
	- Parametric polymorphism
		- "Parametric": a function that can operate on some type that isn't defined when you write the method signature. (R6)
		- "polymorphism" The vectical arrows that changes the category of object.  (R6)
		- In the example below, `optToList` is the parametric poylmorphism? (R6)
	- Natural transformation 
		- For every object X, we have nat trans Option(X) -> List(X), such that for every morphism foo: X->Y, the diagram commutes. (R6) (?)
		- If we can define the same nat trans for every type A, then that nat trans is a polymorphism.  (R6) (?)


![[Pasted image 20220930011131.png]]
- Figure: From R6



- Curry function (R6)

---
## Reference
1. Wiki
2. [[(Video) A sensible introduction to category theory]]
3. [[(Podcast) Category Theory With Bartosz Milewski]]
4. [[(Book) Spivak, D. (2015). Category Theory for the Sciences. MIT Press]]
5. [[(Paper) Wikipedia - Identity element]]
6. [[(Video) Alissa Pajer (2013) Category Theory --  An Abstraction for Anything]]
7. [[(Video) Wadler 2018, Categories for the working hacker]]
8. Blog of Dr somebody: https://www.math3ma.com/blog/the-most-obvious-secret-in-mathematics
9. [[(Paper) Barry Mazur 2007, When is one thing equal to some other thing]]
10. Nlab: research wiki of math: category tab https://ncatlab.org/nlab/show/category
11. Some random blog: https://arbital.com/p/universal_property/
12. [[(Video) Blargoner 2020, Category theory, 3 parts series]]
13. [[(Article) 2019 Pandya, The future will be formulated using category theory]]