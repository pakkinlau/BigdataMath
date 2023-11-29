- 29-9-2022: created

(1:13) We use github as an example, to show how [[category theory|category theory]]applies.
- Somebody make commit, have branches
- Mergecommit
- Firstcommit
- indivi-commit
![[Pasted image 20220929221953.png]]

![[Pasted image 20220929222418.png]]

![[Pasted image 20220929222658.png]]

![[Pasted image 20220929224259.png]]

![[Pasted image 20220929224935.png]]
- 1. creating a category (out of the graph)
	-  A collection of objects (nodes in graph of commits )
- 2. Set of "morphisms" or "arrows" vetween 2 objects
	- Morphisms governed by reachability
	- Vague notion, don't have to be function
- 3. Having a way to compose morphisms together 
	- (a) compositional associativity holds (that means it doesn't matter where you put the parentheses)
	- (b) an identity morphism exists for each object (???) 
- 4. Terminal and initial objects
	- Initial object
		- Object F is an initial object, Hom(F,X) has size 1. (What is Hom() ? )
		- i.e. $F\leq X \ , \forall X$, which X is any node in the graph. 
		- i.e. all objects are reachable from F
	- Terminal object
		- FOr every object in the graph X, Hom(X,A) has size 1.
		- (i.e. $X \leq A \ , \forall X$)
		- (i.e. all objects can reach to A)
- 5. Is terminal or initial guarenteed to exist in a DAG, no?
	- There could be some git commit has twin init and twin terminal. 

![[Pasted image 20220929225053.png]]

- 6. Category 
	- (a) Construction of the graph
		- Category: category of all the graphs (eg: graph of git commit). 
		- Objects: graphs themselves (including its nodes, relations between those nodes ), instead of the objects being the individual nodes in a graph. 
		- Morphisms (ways we can transform a grpah): Structure-preserving graph [[homomorphism]]s.
			- Structure perserving is important.
			- That means adjacent nodes are going to map to adjacent nodes. 
			- That's a property that let a graph morphism more meaningful. 
			- If yoy just map everything, you are not preserving anything from the original graph. 
		- (i.e. adjacent nodes map to adjacent nodes)
	- (b) How this category works
		- Red: mapping functions, Black: adjacent objects.
		- If A maps to Q, and B adjacent to A, then B also maps to Q. (based on the video) 
		- D: graph 1, X: graph 2
	- (c) Graph homomorphism
		- Image we need to compose graph 
		- Image a third graph 

![[Pasted image 20220929234334.png]]
- Figure: each node represent one category. One category contains "structure of graph" + "the arrows that represents structure perserving morphism between node (graph)"

- 7. Forgetful functor
	- Functors are morphisms between categories
	- Transform one category into another category
	- Suddenly we have relationships between categories, and not these standalone things
	- Functors are important because they let us relate categories to one another, and talk about what those relations are like. 
	- What is forgetful functor
		- Imagine we have one category for all graphs (eg: capital graph)
		- We can essentially forget the structure of these graphs, and map them to the "category set (a collection of category)" 
		- We are in the category set, the objects, or our sets and the morphisms would be functions from one set to another set. 
	- Mapping targets
		- 1. Map the objects 
		- 2. Mpa the morphisms in a category, because the category isn'tjust objects. It's also morphism. 
	- Graph homomorphism:
		- where to map the objects and where to map the relations between them, suddenly if we are dropping those relations, we don't  need to worry about mapping anymore, because they don't exists. 
		- In order to get a new function and stet, we will just see where that graph homomorphism took the objects and use that as out new function, and we will forget 

![[Pasted image 20220930000113.png]]
- 8. Option functor
	- eg: Option on Scala programmign language: SOME or NONE. 
	- Option tpye is parametrized, and some scala type, eg: option(A) and option(B) , or option(int), option(str). 
	- What it does
		- Option() Wrap up $A$ (one kind of category) to convert $A$ to $Option(A)$.
	- It is not only transforming objects, from the category of scala types to itself, but it's also transforming morphisms. 
	- Option has a way to give us objects in the category of scala types to other objects in that same category 
	- In category theory:
		- 1. We can have a category of scala type, where the objects on this category to be the types, and the morphisms in the category are going to be functions from type to type. Option() as a functor on the category of scala types since it is taking one category to another. 

![[Pasted image 20220930010524.png]]
-

- Example:
	- $option(foo): option(A) \rightarrow option(B)$
	- $list(foo): list(A) \rightarrow list(B)$
		- where foo is a functionm so we have a way to get from list(A) to list(B)

- What about drawing arrow between these two parallel universe?

- Parametric polymorphism
	- "Parametric": a function that can operate on some type that isn't defined when you write the method signature.
	- In her example, function -- "OptToList()"  parametrized in some type A (she use list(A)). 
	- So option(A) --> list(A) has an arrow. 

- More complete diagram
![[Pasted image 20220930011131.png]]


- The diagram "commute" (what is commute?)
	- The whole graph is describing a natural transformation. 
		- natural transformation = transofmr what to what.
			- eg: option functor of A, down to other functor, which is the list(A) we have in the below of it in the graph. 
		1. polymorphism arrows optToList

	- Terms:
		- Commute: regardless which way you traverse the diagram, from element A to B, it gives the same result, then all possible path that go to B from A are all commutes. 
		- Polymorphism: The vectical arrows that changes the category of object. 
		- Natural transformation:
			- For every object X, we have nat trans Option(X) -> List(X), such that for every morphism foo: X->Y, the diagram commutes.
			- If we can define the same nat trans for every type A, then that nat trans is a polymorphism. 

![[Pasted image 20220930012738.png]]

- Curry function
	- Curry is the name of a person, Haskell Curry.  
	- From medium, "Currying is the transformation of a function with multiple arguments into a sequence of single-argument functions". Such as `f(a,b,c,...)` into `f(a)(b)(c)`.
	- Normal function: `isGreaterThan(a,b)`, curried: `isGreatedThan(a)(b)`
	- Provide another example of natural transformation

![[Pasted image 20220930014433.png]]

- Hom functors
	- Hom(X,Y) is the set of morphisms from object X to object Y. X and Y is gonna be the same category.
	- We can turn this into a functor. 
	- `Hom(_, Y)` is a functor. 
		- Recall: functor is a way to get us from a category, to another category. It's a transformation of category. 
	- Apply `Hom(A,B)` = Apply `Hom(_,B)` to an object A. And return a set of morphisms. In programming, the datatype of the output would be "set".
	- `Hom(_,B)` to a morphism $f:P \rightarrow Q$ .
		- `Hom(P,B)`  $\rightarrow$ `Hom(Q,B)`.

![[Pasted image 20220930015207.png]]
(con't)

- Graphically, we have  X --> Y. And Hom(X, ?) means the set of morphisms that from X transform to B.  We simply don't know if we can get a Y to B in many cases. 
- ...
- The correct idea: contravariance