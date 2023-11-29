- 2-10-2022: created

- What is a functor?
	- Functor is a mapping between categories. (R6)
	- A functor is a homomorphism of categories (R10)
	- It means "function (words)" in linguistics.
	- Functors were first considered in algebraic topologic. Now functors are important in all areas within mathematics to which category theory is applied. 

- Notation:
	- We have category $C$, $A$ is domain of category $C$, $B$ is codomain of category $C$, and $D$ is the target category of the functor $F$ (self-made, by summarization)
	-  For category $C$ and $D$, a functor $F: C \rightarrow D$ maps objects in $C$ to objects in $D$, and maps arrows $f: A \rightarrow B$ in $C$ to arrows $F(f): F(A) \rightarrow F(B)$ in $D$. (R12)

![[Pasted image 20221002064154.png|300x300]]  ![[Pasted image 20221002064027.png|300x300]]
- Figure: Functor in different kind of expressions. The right hand side is commutative diagram expression. 

---
## examples of functors 
- eg: a programming function which converts string to integer
	- Some programming in-built has such "functor" operation, which allows for a in-built datatype to apply a function inside, without changing the structure of the generic type.  
	- Strings and integers are two different categories. Each of them has a list of specific morphisms.

- eg: Functor in haskell
	- It simply maps the domain and codomain of the category with f, a mapping function.
	```haskell
	class Functor f where
	  fmap :: (a -> b) -> f a -> f b
	
	fmap id = id
	fmap (g . h) = (fmap g) . (fmap h)
	```
	- Scala's example
		- 
	```Scala
	trait Functor[F[_]] {
	  def map[A,B](a: F[A])(f: A => B): F[B]
	}
	```


- eg: powerset functor $P:sets \rightarrow sets$ (R12)
	- Powerset = the set of all subsets of S, including the empty set and S itself (wiki). 
	- In this example, we set up a mathematical operations which domain $A$ and codomain $B$ of the morphism $f$ might be or might not be in the same category. 
	- Object-wise, $P()$ maps $A$ to powerset P(A), which $P(A) = \{ X|X \subseteq A\}$ (which means "the set of all subset of A"), obviously. 
	- Morphism-wise, $P$ maps $f: A \rightarrow B$ to the function $P(f): P(A) \rightarrow P(B)$ defined by $P(f)(X) = \{ f(a) | a \in X\}$. Which means the domain and codomain of $f$ also dynamically following the change of boundary of $A$. 
	- In other words, "P lifts the action of f from "A" to "subsets of A". 
	- It's easy to verify p is a functor.

![[Pasted image 20221001120248.png]]
- FIgure: Category C has objects: {A, B}, and $f: A \rightarrow B$ . The functor $P$ maps everything of category C to be category D. In this example the functor "map-subset" all elements of category C, by applying $P$ to the components of morphisms/ domains / codomain f of C.  $P(A) \mapsto X$ , $P(f) \mapsto g$, $P(B) \mapsto (Y)$.
---
## Examples of functors in [[lambda calculus]]

- Lemmas:
	- 1. Functions are [[Covariant, contravariant|covariant]] in their output types. 
		- [[Covariant, contravariant|covariant]] in their output type, means this constructor is a cov
		- $B \leq C$ implies $(f: A \rightarrow B)$ $\leq$ $(g:A \rightarrow C)$. 
		- Function subset: In lambda calculus, functions are "covariant" in their output types. 
		- Example: We have Int is subtype of num, then we have a function has  (Str $\rightarrow$ Int) also has  (Str $\rightarrow$ Num).
	- 2. 

---

- Difference between morphisms $f$ and functors $F$: (my own writings)
	- 1. They are in different dimension. $f \in C$ , morphism $f$ is a component of $C$, and $F$ are interacting in between different distinct categories. That might be the same thing if you claim $C$ is a category of categories (high-dimensional category). If we are out of this situation, $f$  and $F$ are completely differnt. 
	- 2. Functors $F: C \rightarrow D$, where C and D are distinct category, each of them has structure that is composed by a set of objects and a set of morphisms $f$.  $F$ here is a structure preserving function, that convert the whole structure of $C$, to another category $D$, preserving the structure of $C$.

	- $F$ preserves composites and identities in $C$: (R12)
		- $F(g \circ f) = F(g) \circ F(f)$
		- $F(1_A) = 1_{F(A)}$

---
## Other types of functors

- A contravariant functor $F: C\rightarrow D$ is a functor $F: C^{op} \rightarrow D$. Duality C is obtained by formally reversing the arrows in C. This means if $f:A \rightarrow B$ in $C$, then $F(f): F(A) \leftarrow F(B)$ in $D$, so $F$ reverses the direction of arrows. 
	- i.e. The contravarient functor execute two changes of the source category.

- Forgetful / stripping functor: 
	- Functor by default are structure preserving
	- A forget functor is a functor which is defined by 'forgetting' some structure. eg: the forgetful functor from Group to Set forgets the group structure of a group, remembering only the underlying set. (R10)
	- They forgets or drops some or all of the input's structure or peroperties before mapping to the output. (Wiki)
	- This may be expressed by curtailing the signature: the new signature is an edited form of the old one. 
	- Because many structures in mathematics consist of a set with an additional added structure, a forgetful functor that maps to the underlying set is the most common case.
- Option functor

- Hom functor
	- Hom(X,Y) is the set of morphisms from object X to object Y. X and Y is gonna be the same category. We can turn this into a functor.  (R6)
	- `Hom(_, Y)` is a functor. Recall, functor is a mapping between categories. And `Hom(_,Y)` converts every possible category to be a set of morphisms. So it is a functor.

---
## Connections

- Functors form a base for more complex abstractions like: Applicative, Monad, Comonad.




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
13. Wiki: tab: Functor (functional programming)ctor