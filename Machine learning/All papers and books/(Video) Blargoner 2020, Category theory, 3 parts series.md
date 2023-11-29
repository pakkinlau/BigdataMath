- 1-10-2022: created

---
## Part 1 of 3

- What is [[category theory]]
	- It is a sort of universal mathematical langauge which reveals connection between different subjects, like logic and geometry. 
- Highly abstract, abstract nonsense. But it yields deep, elegant and powerful results. 
- A category is a collection of objects, and arrows between those objects, with a law of composition for arrows that is associative and unital (identity)
- $f: A \rightarrow B$ to indicate that F is an arrow with domain A and codomain B.
	- In this defintion, we don't say that what the objects and arrows are, we  only specifies the properties they must satisfy to constitue a category. 
	- This is what makes the definition abstract. 
- What is commute
- Law of compositiion satisti
	- Associativity
	- Unity / (Identity)

- Category are everyehre
	- category set --- 
		- objects: sets, arrows: functions
		- eg: set N = {0,1,2,...} is an object, function f(x) = x^2 + 2x + 1 is an arrow R -> R. 
	- category "vector"
		- object: vector space (over R, say)
		- arrow: linear mappings
		- sub category $Vect_{fin}$: space are finite-dimensional, vectors and mappings are represented by matrices. 
	- category "logic"
		- object: proposition P,Q,...
		- arrows: implicationss P -> Q, .... 
		- eg:
			- I am a teapot --> I am a teapot
		- We could take the arrows to be formal proof in some deduction system. In this case, there may be more than one arrow between two propositions. 
	- category "[[lambda calculus]]"
		- Introduced by Church in 1930s, in his study of the foundations of mathematics and computation. 
		- It provides a formalization of the notion of a "computable by computer" function. Inspired by functional programming languages. Or other programming language's anonymouns lambda functinon 
			- Other ways of defining computable functions
				- Partial recursive functions (Godel, Kleene), 
				- Turing machines (Turing)
				- Symbol manipulation (Post, Markov)
				- Register machines ( Shepherdson, Sturgis)
			- All of these different approaches yield the same class of computable functions 
			- --> Church's thesis -- Any function that we intuitvely think is computable is actually definable in the [[lambda calculus]]. 
			- Function $f(x) = x^2 + 2x +1$ --> lamhda expression:  $(\lambda x.x  **2 + 2*x+1)$ 
			- Lambda expression would replace the variable assoicate with the lambda sign,  like x of $\lambda x$ 
			- Church's insight: no matter how complex the computation is, ultimately can be represented as a sequence of syntactic substitutions. 
			- In lamdba-calculus, values have types. 
				- eg: 3 has type int, written as 3: Int
				- eg: a function returning the length of a string has type $Str \rightarrow Int$. Where Str is `[Char]`, which `[]` is a type constructor, which a list of char type element, it returns a str element.
		  - subtype relation
			  - A -> B means A is a subtype of B, written $A \leq B$ or ( $B \geq A$).
			  - There is an arrow in between A and B if and only if there is a subtype relation between them. 
			  - eg: Int is a subtype of num, so $Int \leq Num$.
		  - $f: A \rightarrow B$ and $g: B \rightarrow C$, then 
			  - $g \circ f = (\lambda x. g(fx)), x:A$. (latter phrase means it only takes type A as x)
			  - $1_A = (\lambda x.x),  x: A$
		- object: 
			- 

- There are many other similar categories of structured sets, where the arrows are functions where "preserve" the structure. 
	- Objects in categories need not have elements
	- Arrows need not be functions

- Duality
	- Important concept in category theory and beyond
	- eg: 1660 mind-body dualism
		- Descartes argued for mind-body dualism (mind is distinct from our body, including our brain, but the two go together and complement each other)
		- This idea of two go together and complementing each other occurs frequently in mathematics, and can be described using category theory.
	- For a category $C$, the dual $C^{op}$ is obtained by formally reversing the arrows in $C$.
	- $: A \rightarrow B$ in $C$ becomes the arrow $f*: A* \leftarrow B*$ in $C^{op}$.
		- star notation reminds us we are in the ual category, but these are the same objects and arrows. The arrows have just been formally turned around. Not inverse arrow. 
	- Composition and itentitied are defined by:
		- $f* \circ g* = (g \circ f)*$
		- $1_A* = (1_A)*$ 
	- It seems trival but it is actually powerful: for any category-theoretic concept in $C$, we get a "dual" concept in $C_{op}$, for which we get theorems for free. And the dual concepts turn out to be just as important as the original concepts. Such that expand the scope of our theory.
 

![[Pasted image 20221001104336.png]]
- Fig: duality 


---
## Part 2 of 3

- Functors
	- Notations of the following: 
		- We have category $C$, $A$ is domain of category $C$, $B$ is codomain of category $C$, and $D$ is the target category of the functor $F$ (self-made, by summarization)
	- For category $C$ and $D$, a functor $F: C \rightarrow D$ maps objects in $C$ to objects in $D$, and maps arrows $f: A \rightarrow B$ in $C$ to arrows $F(f): F(A) \rightarrow F(B)$ in $D$. (R12)
	- $F$ preserves composites and identities in $C$: (R12)
		- $F(g \circ f) = F(g) \circ F(f)$
		- $F(1_A) = 1_{F(A)}$

![[Pasted image 20221001115049.png]]
- Figure: Functor re-create the exacts commutative diagram (R12)


- For category $C$ and $D$, a functor $F: C \rightarrow D$ maps objects in $C$ to objects in $D$, and maps arrows $f: A \rightarrow B$ in $C$ to arrows $F(f): F(A) \rightarrow F(B)$ in $D$.


- examples of functor
- eg: powerset functor $P:sets \rightarrow sets$
	- It maps $A$ to powerset P(A), which $P(A) = \{ X|X \subseteq A\}$ (which means "the set of all subset of A")
	- It maps $f: A \rightarrow B$ to the function $P(f): P(A) \rightarrow P(B)$ defined by $P(f)(X) = \{ f(a) | a \in X\}$ (This function maps a subset X of a, to its image under F, as we can see in the diagram)
	- FIgure: Category C has --  A, B, and $f: A \rightarrow B$ . The functor P maps subsets of a to subsets of B, by applying $F$ to the elements in those subsets of  domains / codomain f of C. 
	- Another description: P lifts the action of f on "elements of a" to "subsets of a". 
	- It's easy to verify p is a functor.

![[Pasted image 20221001120248.png]]
- FIgure: Category C has --  A, B, and $f: A \rightarrow B$ . The functor P maps subsets of a to subsets of B, by applying $F$ to the elements in those subsets of  domains / codomain f of C. 


---
- Revisit lambda calculus 

- [[Lemma]]: 
	- Function subset: In lambda calculus, functions are "covariant" in their output types . Which means  $B \leq C$ implies $(f: A \rightarrow B)$ $\leq$ $(g:A \rightarrow C)$. 
	- words: 
		- subset, superset: they are describing objects
		- subtype, supertype: they are describing the sets of programming data types. 
		- $B$, $C$: Types
		- $f$,$g$: Types constructors (which is explained in point 3)
- Example
	- We have Int is subtype of num
	- Then we have a function has  (Str $\rightarrow$ Int) also has  (Str $\rightarrow$ Num)
- Proof: 
	- 1. [[Covariant, contravariant]] functor
		- In the language of category theory, it is equivalent to saying that the type constructor $A \rightarrow (-)$ is a "covariant" functor in the category of types under subtyping. 
	- 2. Arrows act as an type constructor here. 
		- Given two types, A and B, the arrow returns a new type, namely the type of functions, from A to B. 
		- Type constructor
			- If we fix the type of domain, and let the type of codomain varies, that is a new type constructor, which we denote by $A \rightarrow (-)$. Insert anything to the blank location would create a new type constructor.
	- 3. Covariance of output types
		- Covariance of output types means this constructor is a covariant functor. 
	- 4. Constructors $f$,$g$ preserve subtype relations
		- The covariance condition for output types just says this constructor preserves subtype relations, which are the arrows in the category of types under subtyping. 
		- Category theory elegantly describes this property of functions in programming. 

- Dually functions 
	- [[Lemma]]: Dually of function subset: 
		- Functors are "contravariant" in their input types: $B \leq C$ implies $(f: B \rightarrow A) \geq (g: C \rightarrow A)$, which means "A function that would take the subset of the original source datatype as input"
			- Where $A$, $B$: are types,  $f$,$g$:  are type constructors
			- Contravarience means this constructor reverses sub type relations. That is, it converts subtype relations to supertype relations. 
	- Example: 
		- We have Int is a subtype of num. ( Int $\leq$ Num )
		- Therefore, a function having type (Num $\rightarrow$ Num) , also has type (Int $\rightarrow$ Num).
	- 1. Here we are fixing the output type A and letting the input type varies, to get a new type constructor $(-) \rightarrow A$.

---

- Lemma:
	- The "list type constructor $[-]$ (with map)" is a [[Covariant, contravariant]] functor in the category of both types and functions. denote it as:   $$' map\ f': [A] \rightarrow [B]$$, which means: (map f is a function which takes a list of As, and generates a list of Bs), so map "lifts" the action of $f$ on As, to lists of As. It applies $f$ to each element in a list of As, to obtain a list of Bs. . 
- eg: In many programming language, given a list of As and a function $f: A \rightarrow B$, you can map the function over the list to obtain a list of Bs. 
	- eg: Haskell: `map length["i","heart","functors"] == [1,5,8]`
	- Recall what is map function: 
		- Map functions create a new array (from calling a function) for every array element.
	- 2 ways of looking at it:
		- 1. passing both "the length function" and "the list of string" to the map function, which in turn applies length function to each string in the list. (i.e. map() creates: $[f(ele1), f(ele2),...]$)
		- 2. look at "map-length" is the function by itself. This function takes in a list of strings and returns a list of string lengths. (i.e. $f: A \rightarrow B$ , f is map-length, creates a new datatype all by $f$ itself. 

---
- Q: Can we generalize this beyond list objects? eg: map over a tree or graph?
	- A: Yes, if we specify how to lift a function up a tree. 
		- eg: In haskell, we define 'tree' is a type constructor and 'a' is a type variable for the constructor. The variable will allow us to create different types of trees, like trees of strings, tress of integers. 'leaf' constructor (ceate a leaf of a tree containing a single value of type a), 'node' constructor containing a sub-tree. 
		- `instance Functor Tree`: this is where the magic happens. we make the tree the variable of the functor by providng fmap function  on trees. 
		- `fmap` works like `map f` we see earlier, except it works with any type, not just lists. 
		- Then apply the functor to the 'tree' and 'node' of a tree. 
	- Why we define the functor
		- Avoid writing the same type of code over and over, rather than one function for the list, one function for the tree, etc. 
		- 

![[Pasted image 20221001150245.png]]


---
## 3 of 3 -- Universal properties

- Categories and functors allow us to study universal properties. 
- The best way to learn universal properties is to look at many and many examples, and see what they have in common. 
- A univerasl property characterizes an object in a category, in an essentially unique way, in terms of its relation to other objects through arrows. 
	- This stands in contrast to characterization that might refer to "intrinsic details of an object", which might irrelevant from a cetegory theoretic perspective. 
- Usefulness 
	- By doing this, it abstracts away potentially complicated or messy details of a particular construction, leading to more elegant results. 
	- It also allow us avoid repeating the same proofs over and over again in different categories.
	- Once we know an object is universal, anything that follows from the universal property is known to be true of that object. 
---

- Universal properties are analogous to interfaces in programming 
	- eg: Functor type class in Haskell in part 2 of 3, specifies an interface (fmap) that functorial types must expose, but it doesn't specifies any implementation details. 
	- Using interfaces, is like "programming to the interface". You are only using things that are exposed by the interface, not any intrinsic details of the universal objects. 
	- However, they are stronger than most interfaces because they determine objects (essentially) uniquely
	- Univeral property = defining a very strict interface. 

---
- Univeral properties, just like categories and functors, they are everywhere. 
- $A \times B = \{(a,b) | a \in A \land b \in B\}$, which consists of all ordered pairs of elements of A and B
- Recall what is product: it is like jointing the possible variation of A and B together, and forms a table like format sized set. 
- From category theoretic perspective, only 1 thing is important. 
	- It allows us to "freely translate" between a pair of functions $X \rightarrow A$ and $X \rightarrow B$ and a single function $X \rightarrow A \times B$.
- This property completely characterizes the product. 

---
- How it works
	- 1. There are two projection functions
	- 2. For any function P into the product A x B, "this diagram" commutes. 
	- 3. Compose $p$ and $p_1$ 
	- 4. Finally, we obtain a pair of function $p_1 \circ p : X \rightarrow A$ to make the diagram commutes. 
	- Note:
		- by doing this, "we move from the inside of the triangle to the outside". Which means $p: X \rightarrow A \times B$ is known, and $p_1 \circ p : X \rightarrow A$ is what we just obtained from the diagram.  
		- Why commutes is important? That means two paths P(x) and Q(x) are equivalent. 

![[Pasted image 20221001153218.png]]

---

- Conversely, for any pairs of functions $f:X \rightarrow A$ and $g: X \rightarrow B$, 
	- 1. Instead of having We have a function $p_1 \circ p : X \rightarrow A$ and $p_2 \circ p : X \rightarrow A$ is unknown, now we say they are given, and mark them as $f$ and $g$ respectively.
	- 2. And also we have a pair of projection from A x B to its singular element A and B
	- 3. To make it commute, we obtain a function $p: X \rightarrow A \times B$. 
	- Remarks:
		- The function p must be defined by $p(x) = (f(x),g(x))
		- Here we move from the outside of the triangle to the inside. Which means $f$ and $g$ are known and $p$ is the thing we just obtained. 
- Q: Why we always draw this diagram / arguments in a pair of A and B , and also A x B?
	- With X going to two elements A and B, now X could goes to a different category type of thing. (my guess)

![[Pasted image 20221001153728.png]]
--- 
- Conclusion
	- The "product consisting of the set A and  B ($A \times B$) , and a pair of projection function p1 and p2 ($p_1 : A \times B \rightarrow A$) , is universal, in the sense that "any pair of function from a set into A and B" can be obtained through" this one", in a "unique way". 
	- Application:
		- Define a product in an arbitrary category 


![[Pasted image 20221001154544.png]]

---
- Why saying this commutative diagram is commute is important?

----

- In a category C, a product of objects A and B is an object P and pair of arrows p1 and p2 from P into A and B.  Such that for any pair of arrows f and g from an object X into A and B, there is an unique arrow p, making this diagram commute. 

![[Pasted image 20221001155232.png]]

---
- eg: products in logic
	- Q and R product under logical implication
	- By definition, it is a proposiiton P implying both Q and R, such that any proposition S implying both Q and R also implies P.
	- Therefor P is the conjunction $Q \land R$ .
	- If T is a tautology, then $P \land T$ is also a product of Q and R. 

- From a category theroetic perspective, the Cartesian product of two sets and the logical conjunction of two propoitions are the same sort of thing. They both satisfy all the same category theoretic properties. 


---
- Duality of $C^{op}$:
![[Pasted image 20221001155818.png]]


---
- In lambda calculus, function of multiple variables can be implemented using functions of single variables, which return functions. This technique is called "Currying".

- eg: $(x,y) \mapsto x+y$ can be implemented as $(\lambda x.(\lambda y. x + y))$. This can be described by universal property. 
	- 1. Outer function  takes x as input and output an inner function; 
	- 2. Inner function takes y an input and output x +y. 
	- 3. Notice that the inner function depends on x, but it doesn't take x as input. 
	- Q: so it is like $g \circ f$? should not be the same?

---
- Let $B^A = A \rightarrow B$. 
	- This notation is motivated by the fact that set theory that the number of functions from a set X to set Y, is equal to the number of elements in Y raised to the power of number of elements in X. 
	- Define evaluation function $$\epsilon: B^A \times A \rightarrow B$$ by $\epsilon = (\lambda z . fst(z) snd(z)), z: B^A \times A$.
	- For any function $f: X \times A \rightarrow B$, define the curried version $\tilde f: X \rightarrow B^A$ by $$\tilde f = (\lambda x . ( \lambda y . f(x,y))),  \ x:X, y:A$$. Then $\epsilon \circ (\tilde f \times 1_A) = f$, where $(\tilde f \times 1_A)(x,a) = (\tilde f (x),a)$

![[Pasted image 20221001161827.png]]



---
## 4 of 3 -- Natural transformation 

- 1. In categories, sometimes arrows do not depend in an essential way on the particular objects thet relate. Such arrows are called "natural".
- eg:
![[Pasted image 20221001171205.png]]


- swap function does not depend in an essential way on the particular objects it swaps, since it is defined in the same way for any pair of objects. 
- We can make it clear by commutative diagram:
![[Pasted image 20221001171454.png]]
Figure: this diagram shows the swap function works the same in any situation???

---
 - Swappijng is best viewed as an arrow between functors. 
---

![[Pasted image 20221001171613.png]]


---
Definition of natural transforamtion
- Say we have C, and two imaged category F(C) and G(C).
- Functor reserve the structure of the category C. 
- "Natural transformation" tries to there is a family of arrows that could accepts any nodes of the orignal category C into any images of category F(C) and G(C) etc, such that any element of F(C) or G(C) has a set of natural transformation arrows between them. 
- Natural transformation are composed component-wise. 
![[Pasted image 20221001171751.png]]


---
![[Pasted image 20221001171836.png]]




---
- 5:00 ~9:44 did n't  read
- 

---
![[Pasted image 20221001172330.png]]

----
-