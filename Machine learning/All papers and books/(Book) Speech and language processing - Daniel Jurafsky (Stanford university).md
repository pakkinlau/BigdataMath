- 12-10-2022: created
---
- This book is at least used in two courses:
	- [[(Course) cs124 from language to information]]: Ch 2,4,5
	- [[(Course) CS224N Natural Language Processing with Deep Learning]] - Ch8 to Ch 14

---
## Chapter 8

- [[tagging problems over character sequence model]]

- part of speech tagging
	- Thrax of Alexandria wrote a grammatical sketch of Greek that summarized the linguistic knowledge of his day. This work is the source of an astonishing proportion of modern linguistic vocabulary, including syntax, diphthong, clitic and analogy. 
	- Parts of speech (also known as POS) and named entities are useful clues to sentence structure and meaning. Knowing whether a word is a noun or a verb tells us about likely neighboring words and syntactic structure, making art-of-speech tagging a key aspect of parsing. 
- named entity tagging
	- A proper name is often an entire multiword phrase, eg "Marie Curie" or "New York City".
	- [[named entity recognition]]: assigning words or phrases tags like person, location or organization. 
- sequence labeling
	- Hidden Markov model (HMM) (generative)
	- Conditional random field (CRF) (discriminative)
	- Model sequence labelers based on [[Recurrent|RNNs]] and [[Transformer]]

- [[part of speech|POS]] fall into two broad categories: 
	- closed class: 
		- they are those with relatively fixed membership, such as prepositions, new prepositions are rarely coined. 
		- they are generally function words, eg: `of, it, and, you`.
		- 
	- open class: 
		- new nouns like iPhone, fax, are continually being created or borrowed. 
		- four major open classes
			- nouns
				- common nouns
				- classifications
					- count nouns: single/plural, can be counted
					- mass nouns: conceptualized as a homogeneous group: snow, communism, salt
					- proper nouns: Regina, Colorado, IBM
			- verbs
			- adjectives
			- adverbs
				- directional adverbs (home, here, downhill)
				- degree adverbs (extremely, very, somewhat)
				- manner adverbs (slowly, delicately)
				- temporal adverbs (yesterday, Monday, etc)
			- smaller open class of interjections.
				- eg: hello, goodbut, yes, uh-huh.
			- preposition
				- they can indicate spatial / temporal relations, whether it is literal (on it, by the house) or metaphorical (eg: on time, beside herself).
			- particle
				- resembles a preposition or an adverb and is used in combination with a verb.
				- eg: `over` in `she turned the paper over`
			- phrasal verb
			- determiner
			- article
			- conjunction
				- coordinating conjunction: `and`, `or`, `but`
				- subordinating conjunction: `that` in `I thought that you might like some milk`.
			- pronoun
				- shorthand for referring to an entity or event
			- auxiliary
				- makes semantic features of ta main very, such as tense, whether is is completed, whether it is negated, nd whether an action is necessary, possible, suggested, or desired.

- Some linguists argued that some languages like Riau Indonesian and Tongan, don't have such distinction of verb and noun. (Broschart 1997, Evans 2000, Gil 2000)

- [[part of speech tagging]]
	- It is the process of assigning [[part of speech|POS]] to each word in a text. 
	- Tagging is a [[Disambiguation]] tasks, word are ambiguous - have more than one possible [[part of speech|POS]], and the goal is to find the correct tag for the situation. 
	- [[Ambiguity resolution]]
	- The goal of [[part of speech tagging|POS tagging]] is to resolve these ambiguities, choosing the proper tag for the context. 
	- Accuracy (p152)
		- The accuracy of [[part of speech tagging|POS tagging]] is extremely high. 97% across 15 languages from [[Universal dependencies]] [[treebank]].

![[Pasted image 20221017141621.png]]
- Fig: Tag [[ambiguity]] in the Brown and WSJ corpora 

![[Pasted image 20221017141145.png]]
- Fig: the [[tasks|task]] of [[part of speech tagging|POS tagging]]

- Named entity tagging

- Viewed from a semantic perspective, these proper nouns refer to different kinds of entities: Janet is a person, Stanford University is an organization, and Colorado is a location.
- [[named entity recognition|NER]] find spans of text that constitute proper names and tag the type of the entity. 
	- eg: 
		- PER
		- LOC
		- ORG
		- GPE
	- named entity is commonly extended to include things that aren't entities per se, eg dates, times, or other temporal expressions.

![[Pasted image 20221017151300.png]]
- Fig: an example of the output of an [[named entity recognition|NER]] tagger

- [[part of speech tagging|POS tagging]] vs [[named entity recognition]]
	- Unlike [[part of speech tagging|POS tagging]], where there is no segmentation problem since each word gets one tag
	- The task of [[named entity recognition]] is to find and label spans of text, 
		- Difficult, reasons:
			- the ambiguity of segmentation. 
				- We need to decide what's an entity, and where the boundaries are.
				- Indeed, most words in a text will not be named entities.
			- type ambiguity
				- `JFK` can refer to a person, the airport in New York, or any number of schools.


- Standard approach to sequence labeling
	- allow us to treat [[named entity recognition|NER]] like word-by-word sequence labeling task, via tags that capture both the boundary and the named entity type.
	- BIO tagging
		- The BIO format is a common tagging format for tagging tokens in a chunking task in computational linguistics.  (wiki)
		- I-prefix indicate that the tag is inside a chunk, an O tag indicates that a token belongs to no chunks. B-prefix indicate the tag is the beginning of a chunk that immediately follows another chunk without O tags between them.  (wiki)
		- Critism
			- The BIO syntax does not permit any nesting, so cannot also represent even very simple phenomena such as sentence boundaries, the scope of parenthetical expressions in sentences, nested named entities such as University of Wisconsin Dept. of Computer Science"
	- IO tagging 

---

- Ch12: [[Constituency parsing]]
	- The bulk of the chapter is devoted to [[context-free grammar]] grammars, which is the backbone of many formal models of the syntax of natural language. Syntax means "setting out together or arrangement".
	- Related: 
		- combinatory categorial grammars
- 12.1 [[Constituency parsing|Constituency parsing]]
	- In many languages, groups of consecutive words act as a group or a constituent, which can be modeled by [[context-free grammar]] grammars (also known as phrase-structure grammars.)
	- Syntactic [[Constituency parsing]] is the idea that groups of words can be behave as single units, or constituents. Part of developing a grammars involves building an inventory of the constituents in the language. 
		- eg: noun phrase in English
	- Preposed / postposed construction: 
		- "September seventeeneth" can be placed in a number of different locations in a sentence,
	- [[context-free grammar]]  (CFGs):
		- 1. it consists a set of rules / productions, each of which expresses the way that symbols of the languages can be grouped and ordered together, and a **lexicon** of words and symbols. 
		- 2. Lexicon = The vocabulary of a language, or branch of knowledge.
			- Linguistic theories regard human languages consists of 1) Lexicon -- a catalogue of a language's words, and a grammar (a system or rule which allow for the combination of those words into meaningful sentences) (wiki)
			- Wiki -- Lexicalization
				- A central role of the lexicon is the documenting of established lexical norms. Lexicalization is the process by which new words, having hained widespread usage, enter the lexicon.
			- eg: Noun phrase (NP) can be composed of ProperNoun, or determiner + Nominal, Nominals in turn can consist of one or more nouns. 
		- 3. CFGs can be hierarchically embedded. 
		- 4. CFGs are be thought of a generator, and --> arrow as "rewrite the symbol on the left with the string on symbols on the right"
		- 5. Terminal / non-terminals:
			- The symbols that correspond to words in the language are called terminal. The lexicon is the set of rules that introduce these terminal symbols. 
			- The symbols that express abstractions over these terminals are called non-terminals. 
		- 6. Derivation of "context-free language
			- The sequence of rule expansion is called a derivation of the string of words, with using context-free grammars.
	- Generative grammars: 
		- A traditional name in linguistics for a formal language that is used to model the grammar of a natural language.
	- [[parse tree]]
		- It is common to represent a derivation by a [[parse tree]].
	- [[Constituency parsing]]
	- Sentence-level grammatical construction in English
		- 1. Declarative
			- These structure have a S followed by VP. 
			- These sentences have a lot of uses in chatbots and dialogue systems. 
		- 2. Imperative
			- Begin with a PV and have no subjects. 
			- They are almost always used for commands and suggestions. 
		- 3. Yes-no question
			- They begin with auxiliary very, followed by a subject NP, followed by a VP.
		- 4. Wh-question
		- These can be modeled with context-free rules. 
	- NP
		- Must have
			- Head noun
		- Can have
			- Determiners
			- Numbers
			- Quantifiers
			- Adjective phrases
	- Modifiers
		- Postmodifiers
		- Gerundive
		- Infinitive VP
	- V
		- It can be subcategorized by teh types of complements they expect. Simple subcategories are transitive and intransitive.

- Rules for NP (noun phrases)
- Rules for VP (verb phrases)
	- eg of VP: VP --> Verb NP, followed by assorted other thing ("perfer a morning flight")
	- VP --> Verb NP PP ("leave Boston in the moring") (PP = prepositional phrase)


![[Pasted image 20221013230555.png]]
- Figure: [[Parse tree]]

![[Pasted image 20221013233235.png]]
- Figure: let say we have a corpus / document. Then we can distill lexicons and grammar rules from it, like fig 12.2 and 12.3.

- Generative grammar: 
	- Because the language is defined by the set of possible sentences "generated" by the grammer. 

- 12.4 [[Treebank]]
	- Treebank:
		-  A set of annotated corpus is called a "treebank"
		- Sufficiently robust grammers consisting of CFGs can be used to assign a [[parse tree]] to any sentence. This means it is possible to build a corpus where every sentence in the collection is paired with a corresponding [[parse tree]]. 
		- Treebanks play an important role in parsing

![[Pasted image 20221013234853.png]]
- Fig: The tree, corresponding to the Brown corpus sentence. (Penn treebank project)

- Syntactic movement:
	- 

---

- Treebanks as grammar
	- From treebank like the above figure, the sentences in a treebank implicitly constitute a grammar of the language represented by the corpus being annotated. 
	- "The grammar used to parse the Penn treebank is relatively flat, resulting in very many and very long rules"


![[Pasted image 20221013235428.png]]
- Fig: The CFG grammer extracted from treebank. 

---
- Heads and head finding

- Lexical head:
	- N is the head of an NP, V is the head of a VP.

---

- Grammar equivalence and normal form
	- A formal language is defined as a set of strings of words. This suggests that we could ask if two grammars are equivalent by asking if they generate the same set of strings.
	- In fact, it is possible to have two distinct context-free grammars generate the same language.
- Strong (grammer) equivalence:
	- The generate same set of strings AND if they assign the same phrase structure to each sentence (allowing merely for renaming of non-terminal symbols. )
- Weak (grammer) equivalence:
	- The generate same set of strings BUT NOT assign the same phrase structure to each sentence.


---
## Chapter 13 Constituency parsing / syntactical parsing

- Syntactic parsing
	- A task of assigning a syntactic structure to a sentence.
- Ambiguity
	- Part-of-speech ambiguity
	- Structural ambiguity:
		- It occurs when the grammar can assign more than one parse to a sentence.
		- Subset:
			- Attachment ambiguity: 
				- A constituent can be attached to the [[parse tree]] at more than one place.
			- Coordination ambiguity
				- Phrases can be conjoined by a conjunction like "and".
- CKY parsing / dynamic programming approach
	- Dynamic programming use a table of partial parses to efficiently parse ambiguous sentences. 
- Span-based neural constituency parsing
- Partial parsing: Chunking
	- It is the process of identifying and classifying the flat, non-overlapping segments of a sentence that constitute the basic non-recursive phrases corresponding to the major content-word parts-of-speech --- NP, VP, adjective phrases, and prepositional phrases. 
	- Since chunked texts lack a hierarchical structure, a simple bracketing notation is sufficient to denote the location
	- What constitutes a syntactic base phrase depends on the application (and whether the phrases come from a treebank.)
		- eg: `[NP The morning flight] [PP from] [NP Denver] [VP has arrived.]`
		- eg: `[NP The morning flight] from [NP Denver] has arrived`
	- Algorithm
		- It is generallly done via supervised learning, training a BIO sequence labeler of the sort we saw in Chapter 8. 
- CCG parsing
	- 3 parts
		- 1. A set of categories
		- 2. A lexicon that associates words with categories
		- 3. A set of rules that govern how categories combine in context.
	- Categories
		- either atomic elements, such as S and NP, or functions such as (S/NP)/NP which specifies the transitive verb category.
	- Forward composition
	- Backward compositon
	- Type raising
	- Ambiguity in CCG
	- CCG Parsing framework
	- Supertagging 
	- A* algorithm:
		- A heuristic search method that employs an agenda to find an optimal solution
		- Heuristic functions 

---
## Chapter 14 Dependency parsing

- Another family of grammar formalism: dependency grammar [[Dependency parsing]]
	- In dependency-based approaches to syntax, the structure of a sentence is described in terms of a set of binary relations that hold between the words in a sentence. Larger notions of constituency are not directly encoded in dependency analyses.
	- Important in contemporary speech and language processing systems. 
	- Formalisms, phrasal constituents and phrase-structure rules do not play a direct role.
	- Instead, the syntactic structure of a sentence is described solely in terms of the words (or lemmas) in a sentence, and an associated set of directed binary grammatical relations that hold among the words. 
- Typed dependency structure
	- Relations -- directed, labeled arcs from heads to dependents. 
	- The labels are drawn from a fixed inventory of grammatical relations.
	- Root rode
		- Marks the root of the tree, the head of the entire structure. 
- Advantage
	- 1. Their ability to deal with languages that are morphologically rich and have a relatively free word order.
		- eg: word order in Czech can be much more flexible than in English.
	- 2. A phrase -structure grammar would need a separate rule for each possible place in the [[parse tree]] where such an adverbial phrase could occur. A dependency-based approach would just have one link type representing this particular adverbial relations. 

- Dependency relations
	- The relations in a dependency structure capture the head-dependent relationship among the words in a sentence.

- Dependency formalisms
	- projectivity

- Dependency treebanks
	- Dependency-based analysis provides information directly useful in further language processing tasks including information extraction, semantic parsing and question answering.

- Transition-based dependency parsing
	- Transition-based parsing systems employ a greedy stack-based algorithm to create dependency structures.

- Graph-based dpendency parsing 
	- Graph-based methods for creating dependency structures are based on the use of maximum spanning tree methods from graph theory.

- Evaluation
	- Evaluation of dependency parsers is based on labeled and unlabeled accuracy   scores as measured against withheld development and test corpora.
	- Labeled recall = (a / b) , 
		- where a = number of correct constituents in hypothesis parse of s 
		- b = number of correct constituents in reference parse
	- Labeled precision = (a/c)
		- where a = number of correct constituents in hypothesis parse of s 
		- c = number of total constituents in hypothesis parse of s


---
## Ch15 Logical representations of sentence meaning 

- Semantic parsing
	- In this chapter, we assume linguistic expressions have meaning representations that are made up of the same kind of stuff that is used to represent this kind of everyday common-sense knowledge of the world.
	- The process whereby such representations are created and assigned to linguistic inputs is called semantic parsing, or semantic analysis. 
- Computational semantics
	- The entire enterprise of designing meaning representations and assocaited semantic parsers is referred to as computational semantics. 


- Meaning representation
	- eg: tasks that require some form of semantic processing, eg learning to use a new piece of software by reading the manual, reading a restaurant menu, accomplishing these tasks requires represntations that link the linguistic elements to the necessary non-linguistic knowledge of the world. 
	- composed of 
		- a set of symbols / representational vocabulary
		- an arrangement of them -- these symbols structures are taken to correspond to objects, properties of objects, and relations among objects in some state of affairs beign represented or reasoned about. 
	- These meaning represnetation can be viewed from at least 2 distinct perspectives in all of these approaches
		- 1. representations of the meaning of the particular linguistic input "I have a car"
		- 2. representations of "the state of affairs" in some world.

![[Pasted image 20221015103727.png]]
- Fig: four common meaning representation.
	- 1. first order logic
	- 2. abstract meaning representation: directed graph and its corresponding textual form
	- 3. frame-based / slot-filler representation

- State of affairs
	- Instead of matching similar words, the system should be able to answer yes or no by looking up the the knowledge base and return a state of affairs for the question. 

- Computational Desiderata for representations
	- Verifiability: 
		- a system's ability to compare the "state of affairs" described by a representation to the state of affairs in some world as modeled in a knowledge base.
		- eg: `serve(McDonald, Fries)`, which a system can match against its knowledge base of facts about particular restaurant. 
		- say yes / no if knowledge is complete. return unknown if its knowledge is incomplete.
	- Unambiguous represenation
		- words and sentences have different meaning representations in different context
		- eg: " I wanna eat someplace that’s close to ICSI"
			- 1. eat "at" some nearby location; 2. under a Godzilla-as-speaker interpretation.
		- The sentence is ambiguous, but our meaning representation cannot be ambiguous.
		- Vagueness = underspecified meaning
			- A concept closely related to ambiguity is vagueness -- in which a meaning representation leaves some parts of the meaning "underspecified". 
			- Vagueness could be appropriate for some purposes.
	- Canonical form
	- Inference and variables


- Canonical form
	- The distinct inputs that mean the same thing should have the same meaning representation. 
	- This approach greatly simplifies reasoning.
	- We want to map "Does Maharani have vegetarian dishes" + "Do they have vegetarian food at Maharani" to a single canonical meaning representation.
	- The mapping is complicated
		- 1. The system must be able to conclude "vegetarian fare", "vegetarian dishes"... etc refer to the same thing. "having" and "serving" are equivalent just here. 

- Inference
	- "Can vegetarians eat at Maharani"
		- There is a common-sense connection between what vegetarians eat and what vegetarian restaurants serve. 
		- A system must be able to use inference -- to draw valid conclusion based on the meaning representation of inputs and its background knowledge.

- Variables
	- "I would like to find a restaurant where I can get vegetarian food"
	- the user does not make reference to any particular restaurant, the user wants information about an unknown restaurant that serves vegetarian food. No restaurant are named, simple matching is not going to work. Answering this requires the use of variables. 
	- `Serves(x,vegatarianFood)`
	- Matching succeeds only if the variable can be replaced by some object in the knowledge base.

- Expressiveness
	- It must be expressive enough to handle a wide range of subject matter.
	- Probably too much to expect from any single representational system
	- First order logic is expressive enough to handle quite a lot of what needs to be represented.

---
#### 15.2 Model-theoretic semantics


![[model theoretic semantics 1.png]]
- Fig: my drawing of the graphical representation of "model-theoretic semantics". 

![[Pasted image 20221015123737.png]]
- Fig: a model of the restaurant world


- Summarize why it is called "extensional model":
	- Objects denote elements of the domain
	- Properties denote sets of elements of the domain
	- Relations denote sets of tuples of elements of the domain

- My comment:
	- This model is complete, but it is not a good way to produce a control the amount of vocabulary in a reasonable size. 
		- 1. Unique relationships create new objects, the model would creates infinite amount of objects 
		- 2. Relationships cannot be trained by the model, that dramatically increase the cost of training the model. 
		- 3. An abstract object can be a superset of a list of concrete objects. 
		- 4. And more!
	- this model is unable to capture some characteristics of knowledge
		- 1. it is not able to capture 
	- My suggestion is, initiate all "objects", and "relations" to be a wild card objects that could be possibly in 4 roles. 
		- freely allows objects like together, and also let "relations" to be a kind of objects. 

- Model-theoretic semantics
	- bridging the gap from formal representation, to computational representation
		- model -- a formal construct that stands for the particular "state of affairs" in the world.
		- vocabulary of a meaning representation
			- 1. non-logical vocabulary: 
				- open-ended set of names for the objects, properties, and relation that make up the world we are trying to represent 
				- each element of the non-logical vocabulary must have a denotation in the model, meaning that every element corresponds to a fixed, well-defined part of the model.
			- 2. logical vocabulary:  
				- closed set of symbols, operators, quantifiers, links, that provide the formal means for composing expression in a given meaning representation language.
			- 3. domain of a model
				- it is a set of objects that are being represented. 
			- 4. properties of objects in the domain of the model
				- eg: red is the set of things we think are red.
				- Extensional approach
					- We define concepts by their extension, their denotations. 
					- Similarly, a relations among object denote a set of ordered lists, or tuples, of domain elements that take part in the relations: the denotation of the relation Married is set of pairs of domain objects that are married

			- 5. Interpretation 
				- A mapping that gets us from our meaning representation to the corresponding denotations -- a function that maps from non-logical vocaulbary of our meaning representation, to the proper denotations in the model.
![[Pasted image 20221014125102.png]]
- Fig: A model of the restaurant world.
	- represent people as `{a,b,c,d}`: whatever it is we know about these entities from its word, we focus the model have to gather meaning from the formal properties of the model, and not from the names of the symbols. 

#### 15.2 interpretation

- Plausible meaning representations for sentences will not map directly to individual entities, properties or relations. 
	- They involve complications, such as conjunctions, equalities, quantified variables, and negations. 
	- To assess whether these statements are consistent with our model, we will have to tear them apart, assess the parts, and then determine the meaning of the whole, from the meaning of the parts. 
	- eg:
		- 

- What is Interpretation?
	- Interpretation = gets us from our meaning representation to the corresponding denotations -- a function that maps from the non-logical vocabulary of our meaning representation, to the proper denotations in the model. 
	- eg: Noisy -- denote the subset of restaurants from our domain. 
	- eg: Likes -- denote the preference of each person restaurant. 

---
#### First order logic

- Mechanism for referring to objects: 
	- term
	- constant
		- specific object in the world being described
	- function
		- concepts that are often expressed in English as genitives such as X's location
		- After a FOL translation: "Frasca's location" -->"`LocationOf(Frasca)`"
		- Syntactically the same as single argument predicates. 
		- Functions provide a convenient way to refer to specific objects without having to associate a named constant with them. 
	- variable
		- it let us make assertion and draw inferences about object without having to make reference to any particular named object. 
			- this ability enable us --
				- 1. making statements about a particular unknown object
				- 2. making statements about all the objects in some arbitrary world of objects.
- mechanisms that are used to state relations that hold among objects
	- 1. relations
		- they are symbols that refer to, or name, the relations that hold among some fixed number of objects in a given domain.
			- eg: "Maharani serves vegetarian food" --> Serve(Maharani, vegetarianFood)
	- 2. predicates: 
		- fairly typical representation
			- eg: "Maharani is a restaurant" --> Restaurant(Maharani)
			- This is as one-place predicate that is used, not to relate multiple objects, but rather to assert a property of a single object. It encodes the category membership of Maharani.
	- 3. logical connectives
		- larger composite representations can be put together through the use of logical connectives, which let us create larger representations by conjoining logical formulas using one of three operators. 
		- eg:
			- "I only have five dollars and I don’t have a lot of time"
			- Have(Speaker;FiveDollars) $\land$ $\neg$Have(Speaker;LotOfTime)
		- The semantic representation is built up in a straightforward way from the semantics of the individual clauses through the use of $\land$ and $\neg$ operators.

- Variables 
	- usefulness:   
		- 1. refer to particular anonymous objects
		- 2. refer the generically to all objects in a collection. 
		- These two uses are made possible through the user of operator "quantifiers". $\exists$ : existential quantifier, $\forall$ : Universal quantifier
	- eg: " restaurant that serves Mexican food near ICSI"
		- $\exists x$ Restaurant(x) $\land$ Serves(x, MexicanFood) $\land$ Near(LocationOf(x), LocationOf(ICSI))
			- The first part: for this sentence to be true there must be at least one object such that if we were to substitute it for the variable x, the resulting sentence would be true. 
			- Substitute an object to this statement, 

![[Pasted image 20221015191952.png]]
- Fig: All CFG grammar specification of the syntax of FOL representation. 

![[Pasted image 20221015194036.png]]
- Fig: truth table giving the semantics of the various logical connectives. 

- Lambda notation
	- This notation provides a way to abstract from fully specified FOL formulas in a way that will be particular useful for semantic analysis.
		- eg: $\lambda x.P(x)$,
		- eg: $\lambda x. \lambda y. Near(x,y)$
	- The usefulness of these $\lambda$ expression is based on the ability to apply them to logical terms to yield new FOL expressions where the formal parameter variables are bound to the specified terms. 
	- currying 


---

![[Speech and language processing - Daniel Jurafsky (Stanford university).pdf]]

