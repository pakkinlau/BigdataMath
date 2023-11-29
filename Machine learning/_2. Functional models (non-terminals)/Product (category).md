- 30-9-2022:

- Why learn this?
	- It tells us our construction of the set of object does pick out a specific object. 
		- eg: the empty set is uniquely characterized by its universal property.

- What to learn?
	- defining a product be referring not to what is in the product, but instead to how the product interacts with other objects. 

- Product of two sets: $X \times Y = \{(x,y)| x \in X, y \in Y \}$
	- eg: X is the possible number value of a poker card. Y is the possible "flower" of a poker card. 
	- Projection functions of product: ($\pi$): $\pi_1 : X \times X \rightarrow X$  and $\pi_2: Y \times Y \rightarrow Y$. The intuition of this, is like extracting from every grid element $z \in X \times Y$ its column / row elements. 

![[Pasted image 20220930192059.png]]

---
## Universal property of products (category)

- What is universal property: 
	- Categories and functors allow us to study universal properties.  (R4)
	- Universal properties occur almost everywhere in mathematics, and the use of the concept allows the use of general properties of universal properties for easily proving some properties that would need boring verifications otherwise. (wiki)

- How to learn universal property
	- The best way to learn universal properties is to look at many and many examples, and see what they have in common. (R4)


- Usefulness 
	- 1. Knowing characteristics of an object implicity
		- A univerasl property characterizes an object in a category, in an essentially unique way, in terms of its relation to other objects through arrows.  (R4)
			- This stands in contrast to characterization that might refer to "intrinsic details of an object", which might irrelevant from a cetegory theoretic perspective. (R4)
			- By doing this, it abstracts away potentially complicated or messy details of a particular construction, leading to more elegant results. 
	- 2. Interfacing some difficult proofs
		-  This universal property is defined once, without referring to a specific construction. This defintion can be then applied to multiple categories (R2)
		- It also allow us avoid repeating the same proofs over and over again in different categories.
			- Once we know an object is universal, anything that follows from the universal property is known to be true of that object. 
		- As a result, it abstracts away potentially complicated or messy details of a particular construction, leading to more elegant results, by allowing us to avoid repeating the same proof over and over in different categories. 
	- 3. "Best" property of a category
		- Universal property is one of the most important concepts in category theory. An object in a category which "satisfies a universal property" is in a sense the 'best' (often meaning smallest or largest) object satisfying a certain property. This can be often be used to describe a "universal way constructions" like "products" which are defined for multiple distinct structures. (R2)
		- Once we know that an object in a category is universal, anything that follows from the universal property is known to be true of that object. 
			- eg: Universal properties are anaalogous to interfaces in computer programming. 
			- eg: Fuctor class in Haskell, specifies an interface, namely `fmap` that functorial types must expose, but it doesn't specify any implementation details. Using univerasl property in a proof is therefore like programming to the interface. But universals are stronger than most interfaces in programming because they determine objects (essentially) uniquely (R3)

---
## Universal property and interfaces in programming

- Universal properties are analogous to interfaces in programming 
	- eg: Functor type class in Haskell in part 2 of 3, specifies an interface (fmap) that functorial types must expose, but it doesn't specifies any implementation details. 
	- Using interfaces, is like "programming to the interface". You are only using things that are exposed by the interface, not any intrinsic details of the universal objects. 
	- However, they are stronger than most interfaces because they determine objects (essentially) uniquely
	- Univeral property = defining a very strict interface. 

- In [[lambda calculus]], function of multiple variables can be implemented using functions of single variables, which return functions. This technique is called "Currying".

- eg: $(x,y) \mapsto x+y$ can be implemented as $(\lambda x.(\lambda y. x + y))$. This can be described by universal property. 
	- 1. Outer function  takes x as input and output an inner function; 
	- 2. Inner function takes y an input and output x +y. 
	- 3. Notice that the inner function depends on x, but it doesn't take x as input. 
	- Q: so it is like $g \circ f$? should not be the same?


---
## Examples of products

- eg: products in logic
	- Q and R product under logical implication
	- By definition, it is a proposiiton P implying both Q and R, such that any proposition S implying both Q and R also implies P.
	- Therefor P is the conjunction $Q \land R$ .
	- If T is a tautology, then $P \land T$ is also a product of Q and R. 


- Like categories and functors, universal properties are everywhere (R3)
	- eg: $A \times B = \{ (a,b) | a \in A \land b \in B \}$, which consists of all ordered pairs of elements of A and B. 
	- Many things you could say about this product. 
		- eg: how the ordered pair is actually defined or implemented using sets. 
		- However, in Category theory perspective, there is only one thing that is importnat. Product. 
		- LOOK: Product allows us to freely translate between a pair of functions into $X \rightarrow A$ and $X \rightarrow B$, and a single function into the product $X \rightarrow A \times B$. 
			- From that, you can derive anything you need of the product, without relying on intrinsic imlementation details. 

![[Pasted image 20220930222642.png]]
- Figure:
	- 1. Natural projections exists
	- 2. This diagram commute. 
![[Pasted image 20220930222825.png]]
- Figure: Conversely, 
	- 1. Say we have the structure above
	- 2. Then we have the structure below. 

---
- 1. "Universal property" for products
	- What is it?
		- - Layman's perspective: 
			- "As an observer $a \in A$, to look into a table $X \times Y$, there is a way $f$ and $g$ that I can extract the row or column element $x \in X$ or $y \in Y$ from the table $X \times Y$." , given that projection $\pi$ exists. 
			- "In the field of number theory, I can tell the quotient-remainder theorem ( $A \rightarrow X \times Y$, by given the fact that we already have the knowledge of $X$ and $Y$, (i.e. $A \rightarrow X$ and $A \rightarrow Y$). "
			- "Every $X \times Y$ naturally has $\pi()$ projection to its component elements" 
		- What is universal property?
			- If we are not allowed to define the empty set as "the set with no elements", we can still define it, by means of a "universal property" talking, instead about the function from the emty set, rather than about the elemnet of the empty set. (R2)
			- For any kinds of commutative diagram, universal property is a property that characterizes up to an isomorphism the result of some construction. If there is some paths (having the same source and target), then we say that set of paths commute each others.   (R1)
			- [[category theory|category theory]]
			- In category theory, we avoid thinking about what an object is, and look only at how it interacts with other objects. 
		- $\langle f,g \rangle (a):=( f(a),g(a))$   .... = $g \circ f(a)$  ? 
	- Proof:
		- Let $X$ and $Y$ be sets. 
		- For any set $A$ and also $f: A \rightarrow X$ and $g: A \rightarrow Y$, there exists $A \rightarrow X \times Y$ such that a diamond shape diagram commutation diagram. 
		- there exist a unique function $A \rightarrow X \times Y$ such that the flow points back to the starting point and the diagram commute. A diamond shape pattern appears.  
		- If there is a set $A$ that could performs $f: A \rightarrow X$ and $g: A \rightarrow Y$, then there also exist a function $\langle f,g \rangle$ that produce $X \times Y$ product. 

2. Ologging products
	- 


- The product of two (or more) objects in a category is a notion designed to capture the essence behind constructions in other areas of mathematics, such as:
	- Cartesian products of sets
	- Direct product of groups or rings
	- Product of topological spaces
	- Essentially, the product of a family of objects (i.e. the category) is the "most general" object which admits a morphism to each of the given objects.

---
## Reference
1. [[(Book) Spivak, D. (2015). Category Theory for the Sciences. MIT Press]]
2. Some random blog, Arbital: https://arbital.com/p/universal_property/
3. Category Theory Part 3 of 3: Universal Properties https://www.youtube.com/watch?v=bPvWEN8UGuo
4. [[(Video) Blargoner 2020, Category theory, 3 parts series]]