- 29-9-2022: created

	1. Category theory is not about categorize / classify things. 
	- 2. If math is a setting, category theory is the setting. (but some story is all about the setting - eg - lord of rings). some are completely not (eg: modern random guys interaction, foucsing on characters or plot). 
	- 3. To tell every story, you need both the high level abstraction and low level details (!!)
	- 4. Not everything is a category: while the idea consider useful for most situations, there are plenty of exception.
	- 5. Category consists of {objects, morphisms, composition and identities} and category subject to 2 laws: {identity law, associativity law}.
		- (a) every category has a collection of objects. Objects can be anything. Here we use mathematical things like numbers or collection of numbers, or collection of numbers with extra structure.
		- (b) we generally specify the objects of a category by writing them in a set. elements written between curly brackets. $\{1,1,1\} = \{1\}$.
	- 6. Categories also have morphisms
		- for any two objects a and b, the category has a set of morphisms from a to b: $C(A,B) = \{f,g,\dots\}$. Morphisms are such a general idea tat can be hard to intuitively explain. It could be $f: A \rightarrow B$.  A is related to B, but B doesn't have to related to A in return. i.e. one-way connection. Or we can have more than one morphism from A to B. They can be a function, but they don't have to be. 
	- 7. Once you have morphism, you can compose them. if $f: A \rightarrow B$, and $g: B \rightarrow C$, then there must be some ways to combine them. so $g \circ f : A \rightarrow C$.
	- 8. A category also requires certain special morphisms to exist, called identities. Identities are morphisms from one object to itself. In a category, we must have one identity for each and every object. Which means morphisms of any objects from any object to itself is not empty: $\mathscr{C}(A,A) = \{1_A, \dots\}$.


.... and more 