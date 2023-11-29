---
alias: [poset]
---

- 7-10-2022: created

- Partially ordered set (or, in short, **poset**) or "this precedes that".
	- It consists of a set together with a binary relation indicating that for certain pairs of elements in the set, one of the elements precedes the other in the ordering. The relation itself is called a "partial order"
	-  In order theory, partially ordered set formalizes and generalizes the intuitive concept of an ordering, sequencing or arrangement of the elements of a set.

- Partial order should satisfy the following three characteristics: 
	1. transitive relation: 
		-  In DAG G, $u \rightarrow v, v \rightarrow w, \implies c \rightarrow w$, then  DAG $G^+$ is transitive
		- For any digraph G the walk relations $G^+$ and $G^*$ are transitive.
	2. Asymmetry: Pos length from u to v, implies there is no path from v to u.
		- For a binary relation D on a set A is asymmetry IFF $uRv \implies NOT(vRu)$
- Some characteristics to consider:
	3. Reflexivity: Relation R on set A is reflexive IFF aRa for all $a \in A$, then G is reflexive. i.e. imagine each step in the walk elapsed by time, reflexive order means the agent could hang on some location by arbitrary unit of time.

- Binary relation R is antosymmetric IFF it is asymmetric except for aRa case.

- subset:
	- Strict partial order set
	- Totally ordered set 
	- Path-total order 

- related:
	- [[Hasse diagram]]

---
## Properties of poset (copy and paste from the old note)

- Transitive reduction: 
	- A directed graph that represent another digraph with the same vertices and as few edges as possible. It was introduced in 1972 by Aho, who provided tight bounds on the computational complexity of constructing them.
	- The reduction is a diagraph has the same reachability as D.
	- D and reduce(D) has some transitive closure as each other.
- Covering relation
- Weak partial order (describing the R, relation)
	- Same as a SPO R, except that aRa also always holds. In strong SPO, relations on itself is denied. In weak SPO, element has relation to itself.
	- Example of Strong PO and week PO
		- "Larger or equal to" = weak
- Asymmetry vs antisymmetry
	- A: never alllowed aRa
	- Anti-: sometimes allow
- Representing partial orders by set containment
	- Axioms can be a good way to abstract and reason about important properties of objects, but it helps to have a clear picture of the things that satisfy the axioms. Every partial order can be pictured as a collection of sets related by set containment.
	- By set containment, we can show every partial order has "same shape". "same shape" technically describe is "isomorphic".
	- $A \subset B$: B has everything A has, and $B \not\subset A$
	- example: 
		- ![[Pasted image 20220731234315.png]]
		- Proper subset relations
		- ![[Pasted image 20220731234356.png]]
		- Properly divides
- Isomorphic
	- Isomorphic describes two digraph are having the same shape. It is a structure-preserving mapping between two structures of the same type that can be reversed by an inverse mapping.
	- Two graphs are isomorphic when there is an edge-preserving bijection of their vertices.
	- Two graphs are isomorphic if an isomorphism exists between them.
	- Formal represenation: 
		- $G_1$ isomorphic to $G_2$ IFF $\exists$ bijection f: $V_1 \rightarrow V_2$ with $u \rightarrow v$ in $E_1$ IFF $f(u) \rightarrow f(v)$ in $E_2$
	- Computation:
		- To compute whether two graph is isomorphic, we can compare the adjacency matrix of them.
	- Real world examples:
		- Isomorphism is an absurdly general concept. Any time you treat two things as the same thing, you are implicitly talking about isomorphism. 
		- 1. What's common between two apples, two rocks? Nothing except we treat quantities of any discrete thing.
		- 2. Multiplicative group and additive group of real numbers and logarithms.
		- 3. Fourier transform is also a very important isomorphism
- p.o. represented by $\subset$
	- Every strict partial order is isomorphic to a collection of subsets partially ordered by $\subset$.
	- ![[Pasted image 20220731235207.png]]
	- ![[Pasted image 20220731235223.png]]
- Equivalence relations
	- ![[Pasted image 20220731235303.png]]
	- Two way walks
	- Transitive, symmetric and reflexive
	- ![[Pasted image 20220731235337.png]]
	- ![[Pasted image 20220731235347.png]]
- Graphical properties of relations
	- ![[Pasted image 20220731235413.png]]
- Representing equivalence
	- ![[Pasted image 20220731235436.png]]
	- ![[Pasted image 20220731235444.png]]
	- ![[Pasted image 20220731235452.png]]
	- ![[Pasted image 20220731235502.png]]
	- ![[Pasted image 20220731235513.png]]



---
## Reference
- [[(Course) MIT Mathematics for computer science]]