---
alias: [categories]
---

- 29-9-2022: created



- What is a category
	- Category = A colleciton of objects that can relate to each other via morphisms in senible wys, like composition and associativity. (R8)
	- Category = a collection of things and binary relationships (transitions) between them, such that these relationships can be combined and include the "[[identity]] relationship". (R10)
	- Category = A [[quiver]] with a rule saying how to compose two edges that fit together to get a new edge. (R10)
	- Category is a template for all mathematics, depending on what you feed into the template, you will recover one of the mathematical realm. (R9)
	- Mathematical objects are determined by--and understood by--the network of relationships they enjoy with all the other objects of their species. (R9)
	- Category = set of objects, and collection of arrows $F$. Each arrow  $f: A \rightarrow B, f \in F$ points from domain $A$ to codomain $B$.
		- In this defintion, we don't say that what the objects and arrows are, we only specifies the properties they must satisfy to constitue a category. 
		- This is what makes the definition abstract.
	- network of relationship of  $ob(C) \xrightarrow{make \ senses\ of} C$ 
	- Notion:
		- Category $C$, the category (R1) 
		- the set of objects $ob(C)$, whose elements $x \in ob(C)$ , are called objects (R1) 
		- $Hom(C)$, the set of all morphisms between the collection of all $ob(C)$ in a graph.  (R1) 
		- $Hom(A,B)$, all morphisms from element A to B.  (R1) 
		- Morphisms $f: A \rightarrow B, f \in hom(C)$

---
## Attempts to define category: (R10)

- Trial 1: with one collection of morphisms (R10)
	- $C_0$: A collection of objects
	- $C_1$: A collection of morphisms (or arrows)
	- For every $f$, it has a source/domain $s(f)$, and a target / codomain $t(f)$.
	- For every pair of morphisms $f$ and $g$ where $t(f)$ = $s(g)$, a morphism $g \circ f$ called their composite. Sometime written $f;g$ and $gf$.
	- For every object $x$, a morphism $id_z$ (or $1_z$) called [[identity]] morphism on x.
	- such that the following properties are satisfied:
		- 1. source and target are respected by composition
		- 2. source and target are respected by identities
		- 3. composition is associative
		- 4. composition satisfies the left and right unit laws
	- Every composition of function is always associative ane unital, so the above 4 rules can be re-written as: (R12)
		- To makes all arrows to be composible, 
	- People often write $x \in C$ instead of $x \in C_0$, and $Ob(C)$ and $Mor(C)$ instead of $C_0$ and $C_1$.
	- One usually writes $f: x \rightarrow y , if\ f \in C_1$ to state that $s(f) = x$ and $t(f) = y$.
	- People often write $hom(x,y)$, $hom_C(x,y)$ or $C(x,y)$ for the collection of morphisms $f: x \rightarrow y$.
	- If the identity -assigning map is omitted, then it is "semicategory".

- Curly form of categories
	- Written the category (eg: variable C) in curly $\mathscr{C}(C, A \times B)$ means "the set of all possible arrows from "C" to "$A \times B$". 
	- We will see it a lot when discussing 


- Types of category
	- [[Product (category)]]
	- Sum
	- Coproduct
	- Limit and colimits
	- Diagonal functor
	- Adjoint functor
	- Monad

---
- Example of category:
	- Category of 'all the graphs in git commit' (R6), which each object contains the whole git commit graph. 
		- Category: category of all git commit graphs (instead of a graph for one git commit graph)
		- Objects: Graphs themselves, itstead of a single node.
		- Morphisms: Structure-presefving graph homomorphism
![[Pasted image 20220929225053.png]]

- eg: Set as a category 
	- objects: sets, 
	- arrows: functions
		- eg: set N = {0,1,2,...} is an object, function f(x) = x^2 + 2x + 1 is an arrow $\mathbb{R} \rightarrow \mathbb{R}$. 

- eg: Vector as category
	- object: vector space (over R, say)
	- arrow: linear mappings
	- sub category $Vect_{fin}$: space are finite-dimensional, vectors and mappings are represented by matrices. 

- eg: "logic" as category
	- object: proposition P,Q,...
	- arrows: implicationss. eg: P implies Q denote as P $\rightarrow$ Q 
	- eg:
		- I am a teapot --> I am a teapot
	- We could take the arrows to be formal proof in some deduction system. In this case, there may be more than one arrow between two propositions. 

- eg: "[[lambda calculus]]" as category
	- object: datatypes, eg: str, int, char.
	- arrows: lambda expression functions 
		- eg: $(\lambda x.x  **2 + 2*x+1) : int \rightarrow int$

- eg: "[[Kernel space]]" as category
	- ?? 
	- Wiki-tab: Kernel (category theory) ?? 

- Other examples of categories: 
category's name| its object | its morphisms
---|---|---
set|sets|functions
group|groups|group homomorphisms
top|topological spaces|continuous functions
$vect_k$|vector spaces over a field, k|linear transformation
meas|measurable spaces|measurable functions
Poset|partially ordered sets|order-preserving functions
Man|Smooth manifolds|smooth maps

- What is [[quiver]] (mentioned in the definition of category)
	- In mathematics, a quiver is a [[directed]] where loops and multiple arrows between two vertices are allowed
	- i.e. a multidigraph. 
	- They are commonly used in [[Representation theory]]: a representation V of a quiver assigns a vector space V(x) to each vertex x of the quiver and a linear map V(a) to each arrow a.

- Vocabularies:
	- Concrete category: 
		- a category that looks like a category of "sets with extra structure", that is a category of structured sets. 
	- [[Internel category]]
	- Enriched category:
