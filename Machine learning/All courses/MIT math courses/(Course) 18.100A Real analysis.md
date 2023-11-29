- source: https://www.youtube.com/watch?v=LY7YmuDbuW0&list=PLUl4u3cNGP61O7HkcF7UImpM0cR_L2gSw


---
- 2 books that are writing to new real analysis learner:
	- Proofs: a long-form mathematics textbook https://www.doc88.com/p-21973918406856.html
	- 
---
### Learning objectives
- 1. By proving the theorems, we practice how to deploy the related definitions and axioms 
- 2. Understand the properties and behaviors of foundational concepts and techniques for mathematical analysis.
	- continuity
	- convergence
	- completeness
	- and more 
- 3. develop logical reasoning skills
	- deductive reasoning
	- learn how to construct rigorous mathematical arguments.
- 4. developing critical thinking skills?

---
### My views on how to learn mathematical analysis well (chatGPT agrees)
- My overall perspective on how to learn this subject well can be summarized as "solution space" orientated. By solution space, in this subject, is the way that people could produce their definitions, proofs, theories. By building up the content prioritize on "solution space" building, which means that we need to generalize patterns from each examples encountered. With more patterns that hints us how to generate definitions, theories and proofs. We can accumulate those common pattern as a list of tools that alleviate the cognitive load each time we understand new rigorous mathematical texts. 
- Here are some rules for "solution space" orientated learning:
	- 1. Breaking down the topics into manageable entity based notes that only focus on one concept on each block.
		- Tackle each concept separately could reduce the memory needed. 
		- This could allow you to focus on one concept at a time, which can reduce cognitive load and facilitate better comprehension.
	- 2. Don't focus on "what are the concepts involved and try to memorize it", focus on "how to generate the set of solution space". 
		- for example, we encounter a concept. we could just read it and make sense of it and pass. This kind of study could not equip myself an ability to generate the solution space that generate proofs to a set of other problems. 
		- We should focusing on understanding how to generate the solution space. This approach encourages active learning and critical thinking.
	- 3. Create a set of prompts / problems that pull on the top of the content of each concept.
		- Example prompts / problem to ask:
			- If there is a "definition" --> Ask why it is defined as such
			- If there is a "proof" --> Ask what kind of proving structure is used. Extract the proofing structure and identify each used properties. And looks for any chances that the proof can be written more comprehensive. (I don't pursue terse and concise proofs)
	- 4. After asking the questions in (2), write down those additional aspect 

---


- Say there are $n$ concepts in each chapter in real analysis textbook. And there are $m$ examples associating with each concept. 
- The solution space of proving each example is much bigger than those numbers of example.
- So, I think a better way of learning mathematical analysis is, to extract the repeating characteristics existing in the proving steps, instead of just learn those concepts, and tries to create a proof from scratch. 

- ChatGPT's response:
	- By identifying the common patterns and techniques used in proving examples, you can develop a more intuitive understanding of the subject matter. 
	- This approach allows you to recognize recurring ideas, key strategies, and fundamental principles that underpin multiple concepts. It also helps you build a solid foundation of problem-solving skills that can be applied to various situations.
	- Benefits:
		- By extracting the repeating characteristics, you develop a broader perspective on how different concepts are interconnected. This can lead to a more holistic understanding of the subject, as you start to see the underlying structure and connections between different ideas.
		- It also helps in developing a more flexible mindset, allowing you to adapt and apply your knowledge to new and unfamiliar problems.
		- this approach encourages active learning and engagement with the material. Instead of passively absorbing information, you are actively analyzing and synthesizing the patterns and techniques used in proofs. 
	- However, it's important to note that while identifying common characteristics and patterns is valuable, it should not overshadow the need to understand the underlying concepts themselves.

---
### Book author's commenting on how to think of analysis 
- 1. Auto mechanic versus Engineer
	- To use, or teach mathematics effectively, you cannot simply know what is true, you must know why it is true. Analysis shows why something in mathematics is true, in its finest grain.
- 2. Prove things in different style
	- If we want to prove $a = b$ in algebra, we prove two inequality $a \geq b$ and $a \leq b$. 
	- In many cases we also define some concepts in such way because it is too hard to define with set build notation.
- 3. Modern analysis uses the language of sets.
- 4. Learning math rigorously and everything is unambiguously defined

### Another book (proof a long form textbook)
- Chapter 1 pro-tips
	- In order to not just learn the material but deeply understand it, you need to test it
	- Think about math as a giant, no teacher can download this castle into your brain. We use definitions and theorems and proofs and examples and non-examples and conjectures to introduce you a new room or alcove of the castle.
	- Mathematics research has been won without personal struggle in which mistakes were made and small steps were taken. To be the first to discover a new feature of the castle is reward reserved only for tenacious learners. 
	- You must practice fighting through difficulties in order to become good at fighting through difficulties. 
	- While math is intrinsic, proofs are human. Math is a search for objective truth, while proofs are the search for subjective agreement. The goal of a proof is to communicate your ideas and convince ithers that you are correct, and so it is important to discuss your ideas and share your thoughts with others. 
	- When writing out their homework solutions, students are far more likely to write too little than they are to write too much

- Chapter 2 (Direct proofs)
	- Definitions are important in math, which gives us precision. They are also subjective, human choices. While math is deep and intrinsic, definitions are our inventions to make it easier to discuss the math.
	- Definitions are precise. If you change something small about a sandwich, you might still count it as sandwich. The same is not true in math.


- Figure:
	- We use the definition of even integers to translate the problem to one that is just about integers. 
	- Then we solve the integer problem
	- Then we translate what we found back to a conclusion about even integers. 
	- Terms:
		- Def 2.2: An integer $n$ is even if $n = 2k$ for some integer $k$; an integer $n$ is odd if $n=2k+1$ for some integer $k$. 
		- TBD: To be determined
![[Pasted image 20230513082756.png|400]]
![[Pasted image 20230513082904.png|400]]

- If, else statement
	- If "statement 1" is true, then "statement 2" is true
	- "statement 1" implies "statement 2".
	- General form: $P \implies Q$, where $P$ and $Q$ are each statement.
- Symbols like this are commonly used in scratch work.
- Proofs are usually obtained only after a lot of scratch work, and writing stuff down is a good way to generate ideas. 
- However, when writing formally, like when writing up the final draft of your homework, these symbols are rarely used.

- Take a look at the proofs of propositions 2.4, 2.5 and 2.6 and see if you can identify this general structure in each one.

- Figure: Structure of direct proof
![[Pasted image 20230513091830.png|500]]

- Proof by cases
	- This is a "divide and conquer" strategy where one breaks up their work into two or more cases. 
	- eg: If $n$ is an integer, proof $n^2 + n + 6$ is even 
		- transformation: even is defined as... 
	- eg2: proposition - let $a,b,c$ be integers. If $a|b$ and $b|c$, then $a|c$
		- transformation: divide is defined as - $a$ is said to decide $b$ if $b = ak$ for some integer. 
		- So $a = bk_1$, and $b = ck_2$, where $k_1, k_2$ are integers. 
		- Then $a = k_1 k_2 c$ if we substitute $b = ck_2$ into $a = bk_1$.
		- So $a = kc$, where $k_1k_2$ is an integer. so $a|c$ is true. 

- Chapter 2 pro-tips
	- When reading a definition, get in the habit of asking "why is it called that". Often the word that mathematicians chose provides some intuition for what is being defined. For more abstract area of math, the connections can be harder to spot.
	- Definitions are not only offer us precision in our language, but they present to us objects worthy to study. Which allows mathematicians to focus their attention and sharpen their dialogue.
	- Basically all of pure mathematics, $log$ refers to the natural log, the log with a base $e$. 
	- The best way to find the holes in your understanding is to try to explain it to someone else, and responding to their questions. 
	- Most math courses will feature new notation, most research articles you pick up will invent some new notation to further their discussion.
	- Mathematical notations can be ambiguous. "~" means so many different things in math, it is just ridiculous. Math is a big field and we ran out of symbols quickly. You must use context clues to know what the symbols mean.

- Chapter 3 - sets
	- subsets
	- set builder notation
	- direct proofs, prove by cases, with these new notations 
	- Union, intersection, complement, subtraction
	- Power sets and cardinality
	- prove set A = set B 
		- $A \subseteq B$ and $B \subseteq A$

- Chapter 3 pro-tip
	- If we learn to drive perfectly, then once you relax and you will still end up in a great place.

- Figure: the meaning transformation from set builder notation to plain words
![[Pasted image 20230513094205.png|500]]

- Chapter 4 - induction
	- useless
- Chapter 5 - Logic
	- Statement - a statement is a sentence or mathematical expression that is either true or false.
	- Implies, if and only if
	- Converse - the converse of $P \implies Q$ is $Q \implies P$
	- Truth table
		- De Morgan law: $\neg(P \land Q) \iff \neg P \lor \neg Q$
	- Truth table with implications 
		- (which means involving ($\implies$) in the truth table)
		- We define implications with truth table, which makes it executable with the language of truth table. 
	- Quantifiers and negations
		- Order of quantifiers are important - 
			- $\forall x \in \mathbb{R}, \exists y \in \mathbb{R}$ such that $x^2 = y$
			- $\exists x \in \mathbb{R}$ such that $\forall y \in \mathbb{R}, x^2 = y$
			- Two statements are mentioning different thing and the second statement is wrong because of squared roots over negative numbers produce imaginary numbers.
	- Negation
		- $\neg \land = \lor$
		- $\neg \lor = \land$
		- $\neg \forall = \exists$
		- $\neg \exists = \forall$
	- Contrapositive
		- To see more, go to the below entity
- Proving quantified statements
	- Existential proofs
		- To prove an existence statement, it suffices to exhibit an example satisfying the criteria. 
		- To find one that satisfy the condition - that is called a constructive proof - you literally construct an example. 
		- Non-constructive proofs make use of some other theorem
			- eg: Prove there exists $c \in \mathbb{R}$ for which $c^y = c^2 +1$
			- Let $f(x) = x^7 - x^2 -1$. The statement become prove $f(x) = 0$ for some $x$
			- That makes intermediate value theorem becomes useful.
	- Universal proof
		- To prove a universal statement, it suffices to choose an arbitrary case and prove it works there. 
		- eg: Prove "for every odd number $n$, if follows that $n+1$ is even"
		- The point is by letting $n = 2a + 1$, you were essentially selecting an arbitrary odd number, and operating on that. Every odd number can be written in that form, and every odd number can have 1 added to it and then factored like we particular odd number. 
- Paradoxes

- Ch6 Contrapositive
- Ch7 Contradiction
- Ch 10 Introduction to group theory

---
### Youtubers' comment about learning analysis

- Focus
	- It's not about solving real world problems, but understanding quantitative spaces and structures.
	- Learning how to prove your solution. 
- 6 things I wish I knew taking real analysis
	- 1. It is not plug and chug class, it is about proving statement rigorously. Logic based.
	- 2. You need to have all general proving techniques
	- 3. Understand how important definitions are. 
		- eg: "a sequence converges", what does that mean?
		- when professor writing down definition, its something you should know by heart
	- 4. Know how to use definitions in proofs.
		- linking up "what you know" and "what you want"
	- 5. Realize how important the logical quantifiers
		- eg: $a \in A$
		- Notation things can be very important
		- Taking introductory proof class before taking real analysis?
	- 6. Persistence is key?
		- If you want to do well, keep showing up.

----
### Interesting connection of analysis to programming

- 1. Reduce(function, iterable) in python 
	- versus "sequence and series" in math, geometric series, harmonic series, recursive functions, Taylor series, Fourier series, series-sum, series-product, average, median, mode, variance in math
- 2. "List comprehension in python" versus "set builder notation in math"
	- Both list comprehension and set builder notation are ways of defining a set of list of objects based on a rule or condition. 
	- While python is more concrete and specific to programming, set builder notation is more abstract and general, and it can be used to define sets based on any logical condition or formula.
	- eg: `x = [1, 'A', 2, 'B', 3, 'C']`, `strings = [y for y in x if type(y) ==str]`
	- eg: $K = \{ 1, 'A', 2, 'B', 3, 'C' \}$,  $String = \{ x\mid x\in K \land S \}$, which $S$ is a set of string. 

---
## Difficulty score for each topic, given by chatgpt

- Limits and continuity - 2/5
	- While the basic concepts of limits and continuity may be relatively easy to grasp, more advanced topics such as differentiability and the epsilon-delta definition of limits can be challenging.
- Sequence and series - 3/5
	- While the basic theory of convergence and divergence of sequences and series is relatively straightforward, more advanced topics such as convergence tests, absolute convergence, and the convergence of power series can be more challenging. 
- Differentiation - 4/5
	- While the basic theory of differentiation is relatively easy to understand, mastering the various differentiation techniques and their applications can be challenging.
- Integration - 5/5
	- It includes topics such as the Riemann integral, improper integrals, and the fundamental theorem of calculus. Integration is often considered more challenging than differentiation because of the wide range of integration techniques and the subtleties of convergence.
- Metric space - 5/5
	- This topic involves the study of general spaces where distances between points can be defined. It includes topics such as the definition and properties of metric spaces, completeness, and compactness. Metric spaces can be more abstract and difficult than the previous topics, and mastering the various concepts and techniques can require a high level of mathematical maturity.
- Topology - 5/5
	- This topic involves the study of general properties of spaces, such as continuity, connectedness, and compactness, that are independent of the specific metric used to define distances. Topology is considered one of the most abstract and challenging topics in real analysis, and it requires a high level of mathematical maturity and abstraction.


---
# Lecture 1 - sets, set operations and mathematical induction

- Purpose:
	- knows how to read and write proofs
	- prove statements about real numbers, functions and limits (analysis part)

- this course is probably the first really rigorous course in math.
	- everything will be rigorously and unambiguously defined.

- definitions are meant to be a rigorous way of defining an object we are interested in studying.

---

### Formal language
- It is a language that is defined by a set of rules and symbols that have precise meanings and are used to represent mathematical or logical concepts.
- Examples:
	- Symbolic representation
	- Set builder notation
	- Predicate logic
	- Function notation
	- Calculus notation
	- Topology notation
	- Measure theory notation


### Symbolic representation
- A way of writing definitions and statements  using logical symbols and mathematical notations. 
- In might be advantages in certain context, such as in mathematical proofs or in computer programming, where space and readability are important. 

### Set building notation
- Other kind of formal language, apart from symbolic representation which is commonly used in mathematical analysis
- Notation
	- Manner 1: $\{ x \in A | P(x)\}$ or $\{ x  | P(x)\}$
	- Manner 2: $\{ x:x \in A \lor x \in B\}$
- Comments
	- The notation $\{ x : P(x) \}$ is read "The set of all $x$ such that $P(x)$ is true.". $x$ is just an example, we can use any other variable we want to describe the elements of the set.
	- Inside the curly bracket, we have 2 parts of information. 
		- LHS: the variable that will be used to describe the elements of the set. 
		- Blocker: Most commonly use "|" or ":" sign as a blocker between LHS and RHS
		- The right hand side we put the condition $P(x)$ on the set that $x$ belongs to.
		- RHS: The condition $P(x)$ that is on the variable $x$ itself. (Not on the set that $x$ belongs to)
		- Separator for $P(x)$: we most commonly use either "," or "such that" to separate conditions sequentially. 
		- Ordering of a list of $P(x)$: Same as the ordering of quantifiers can significantly changes the statement, the ordering of how each condition $P(x)_i$ would also significant change the statement.

 - This notation refers to a subset of the set $A$ containing all elements of $A$ that satisfy the property $P(x)$. 
	- We can denote membership ($\in$) in different location. In manner 1, we are embedding condition $P(x)$ on a set; while in manner 2, we are embedding the membership description on an element. 
	- The order of conditions only matters when it had to dealing with nested quantifiers, which arise where we have more than 1 variable in a logical statement. 
- Logic
	- 

### Assignment symbol $:=$
- $:=$ means" is defined to be", "is assigned to", while $=$ equal sign means equality between two objects.
- Comparison
	- versus $=$: 
		- Use $=$ instead of $:=$ can causes confusion that it is an assertion of equality between two sides of the equations. Similarly, using $:=$ instead of $=$ can also suggesting the equation is being defined or assigned values.



### Discussions on varies expressions
 - 1. Using or not using set builder notation
	 - (a) Let $E \subset S$, where $S$ is an ordered set. If $\exists b \in S$, $\forall x \in E(x \leq b)$, then $b$ is an upper bound of $E$.
	 - (b) Let $E \subset S$, where $S$ is an ordered set. f $\exists b \in S$, $b \in \{ b' \in S | \forall x \in E, x \leq b' \}$, then $b$ is an upper bound of $E$. 
	 - (c) Let $E \subset S$, where $S$ is an ordered set.  An element $b \in S$ is an upper bound of $E$ if for every $x \in E$, we have $x \leq b$.
 	 - Statement (b) does not make a redundant definition. It is a restatement of the definition of an upper bound of a set. The set $\{ b' \in S | \forall x \in E, x \leq b' \}$ represents the set of all upper bounds of $E$. And if there exists an element $b$ belongs to this set, then $b$ is an upper bound of $E$. 
 	 - Statement (a) and (c) are equivalent. However,

- 2. Defining an element using quantifiers versus using verbal sentence.
	 - (a) Let $E \subset S$, where $S$ is an ordered set. If $\exists b \in S$, $\forall x \in E(x \leq b)$, then $b$ is an upper bound of $E$.
	 - (b) Let $E \subset S$, where $S$ is an ordered set.  An element $b \in S$ is an upper bound of $E$ if for every $x \in E$, we have $x \leq b$.
	 - Statement a and b are equivalent. However, statement 3 is more clear because it puts the subject "an element $b$" as the subject of the sentence. 

- 2. Causing problem by eating the potential set builder notation from the statement
	- 1. $\exists b \in S$, $\forall x \in E(x \leq b)$
	- 2. $\exists b \in S(\forall x \in E(x \leq b))$
	- In the first statement, we are looking for a specific element $b \in S$ that satisfies a certain condition, while in the second statement, we are simply asserting the existence of an element $b$ that satisfies a condition for all $x \in E$. 
	- Q: 
		- So the first statement is close to  set builder notation, while the second statement is close to a conditional statement, which is the second component of the set builder notation?
		- A: Yes, that's a good way to think about it. 

- 4. Wrong set notation usage (don't use set builder notation to define an element)
	- (a) Let $E \subset S$, where $S$ is an ordered set.  $b = \{b \in S | \forall x \in E \land x \leq b \}$
	- (b) Let $E \subset S$, where $S$ is an ordered set.  $\exists b \in S, b \in \{b' \in S | \forall x \in E \land x \leq b' \}$
	- The statement (a)imposes an error, which RHS is expressing a set, which b is a element in S. LHS suppose should be a set as well, because RHS is defining a set. However b has been used as element in RHS definition. So we can see there are inconsistent meaning for b. Thus statement (a) is wrong.   

- 5. Definition imports / Definitional extension / definition by reference
	- In real analysis, we have a notion of "definition import" that simplifies the definition statement for one entity. Demonstrate it with example.
	- "If there exists an upper bound $b_0$ of $E$ such that whenever $b$ is any upper bound for $E$, we have $b_0 \leq b$, then $b_0$ is called the least upper bound or the supremum of $E$. We write $supE = b_0$"
		- Instead of defining the whole statement from raw sets. We can imports the established meaning with verbal reference.
		- We define supremum by mentioning $b$ is any upper bound for $E$ before definition.
	
---
# Feature engineering on learning analysis
- When learning something and we feels the solution space is big, we can try to find some commonalities in the example data set and tries to give them labels. Those labels could shrink the searching space for the agent to determine the solution.
- The following parts are features:
	- 1. Abstractions in mathematical proofs:
		- a list of abstractions that illustrate the relationship between smaller objects/statements and larger objects/statements. 
		- along with the corresponding proving techniques commonly employed
	- 2. Common techniques in mathematical proofs
		- 


---
### Abstractions in mathematical proofs
- Here are a list of abstract reasoning relationships:
	- 1. Composition
		- When we have smaller components or parts and want to reason about the larger whole.
		- Smaller and larger are relative terms that refer to the relationships between objects or statements, rather than their size or magnitude. 
		- Techniques:
			- direct proof, proof by induction, or proof by construction to establish properties of the composite object.
		- Example: 
			-  Suppose we have two continuous functions \($f: [a, b] \to [c, d]$) and ($g: [c, d] \to [e, f]$). To prove that the composition ($g \circ f$) is continuous, we can use a direct proof by showing that the composition preserves the sequential criterion for continuity.
			- In this example, $g \circ f$ is composed by $f$ and $g$ thus we can say that $g \circ f$ is larger. 
	- 2. Implication
		- When we have a conditional statement where the truth of one statement implies the truth of another. 
		- Techniques:
			-  direct proof or proof by contrapositive to establish the implication.
	- 3. Existence
		- When we want to prove the existence of an object satisfying certain conditions
		- Techniques:
			-  proof by construction, proof by contradiction, or proof by exhaustion to demonstrate the existence of such an object.
	- 4. Equivalence
		- When we have two statements that are equivalent or logically equivalent
		- Techniques:
			- proof by equivalence or proof by biconditional implication to establish the equivalence.
	- 5. Reduction
		- When we have a complex or difficult problem and want to simplify it into a more manageable form
		- Techniques:
			- proof by contradiction, proof by cases, or proof by contradiction to reduce the problem to simpler subproblems.
	- 6. Enumeration
		- When we want to prove a statement for all elements of a finite set or all natural numbers
		- Techniques:
			- proof by induction or proof by exhaustion to establish the property for each element.
	- 7. Duality
		- When we have a statement or object and want to reason about its dual or converse statement or object
		- Techniques:
			- proof by contradiction or proof by contrapositive to establish the desired result.

---
## Common techniques in mathematical definition and proofs

### Existential instantiation (Prove $\exists x \mid f(x)$ by showing $\exists !x \mid f(x)$)
- Definition:
	- Existential instantiation is a logical inference rule that allows us to prove the existence of an object by demonstrating that there is at least one object that satisfies a particular property. 
- Example:
	- $\forall x \exists y \ (x + y = 10)$
		- The statement asserts that for all $x$ there exists a corresponding value of $y$ such that there sum is equal to $10$. 
		- To prove the statement using existential instantiation, we start by instantiating the existential quantifier with a specific value for $x$. Let's choose $x = 5$. 
		- Now, we need to show that there exists a value of $y$ that satisfies the equation $x + y = 10$.
		- By simple arithmetic, we can determine that $y = 5$ satisfies the equation, since $5 + 5 = 10$. Therefore, we have found a specific value of $y$ that makes the equation true.

### Direct proof
- Starts with the assumption, use logical deductions to arrive at the conclusion.
- Structure:
	- Construct a logical structure for your proof. Identify the main steps you need to take to establish the truth of the statement. This may involve breaking down the problem into smaller sub-problems or applying known results.
- Rigorous reasoning
	- Emphasize precise and rigorous reasoning throughout your proof. Each step should be logically justified, with clear connections between statements. Avoid making unwarranted assumptions or leaps in logic.
- Completeness and generality: 
	- Strive for completeness and generality in your proof. Aim to cover all cases and ensure that your proof holds for any relevant situation. Consider potential counterexamples or exceptions.
- Clear and concise writing: 
	- Communicate your proof effectively through clear and concise writing. Use mathematical notation appropriately and explain your thought process thoroughly. Write in a logical order, guiding the reader through your argument.
- Symbolically,
	- Definitions - Let $D_1, D_2, \cdots, D_n$ be the relevant definitions involved in $P$. 
	- Prepositions and theorems - Let $T_1, T_2, \cdots, T_k$ be the relevant propositions and theorems that provide the foundation for the proof.
	- Assumptions and axioms - Let $A_1, A_2, \cdots, A_m$ be the assumptions or axioms that can be relied upon in the proof.
	- $Q$: The conclusion or statement that directly proves $P$. 
	- The direct proof of $P$ can be symbolically represented as follow:
		- P = ((A1 ∧ A2 ∧ ... ∧ Am) ∧ (D1 ∧ D2 ∧ ... ∧ Dn)) → (S1 → S2 → ... → Sk → P)
		- $P = ((A_1 \land A_2 \land \cdots A_m) \land (D_1 \land D_2 \land \cdots D_n)) \land (T_1 \land T_2 \land \cdots T_k)) \rightarrow Q$

### Induction
- Principle of Mathematical Induction: 
	- Understand the principle itself, which is a powerful proof technique used to establish statements that hold for all natural numbers. It consists of two steps: the base case and the inductive step.
	- Base Case: Learn how to verify the statement for the initial value, usually n = 1 or n = 0, depending on the context. This serves as the starting point for the induction.
	- Inductive Step: Master the process of constructing the inductive step. Assume that the statement holds for some arbitrary value k, and then prove that it holds for k + 1. This step establishes the domino effect, where the truth of the statement for one value guarantees its truth for the next.
- Well-Ordering Principle: 
	- Realize that the principle of mathematical induction relies on the well-ordering property of the natural numbers, which states that every non-empty set of natural numbers has a least element.
- Hypothesis: 
	- Understand the role of the induction hypothesis, which assumes that the statement holds for a particular value and is used to prove its validity for the next value in the inductive step.
- Strong Induction: 
	- Explore the concept of strong induction, which is an extension of mathematical induction. It allows you to assume that the statement holds for all values up to k (instead of just k) in the inductive step. Strong induction can be useful in certain scenarios.
- Recursive Definitions: 
	- Understand how induction can be applied to define and prove properties of recursive sequences or functions.
- Symbolically,
	- 1. Base step
	- 2. Inductive step
	- 3. Strong induction
	- 4. Recursive definition 

### Contradiction
- It is a technique used to establish the truth of a statement by assuming its negation and then deriving a contradiction. If assuming the opposite of the statement leads to an absurdity or contradiction, then the original statement must be true.
- Logical reasoning:
	- Develop your skills in logical reasoning, as proof by contradiction relies heavily on logical principles. Learn about logical operators (such as negation, conjunction, disjunction, implication) and their corresponding truth tables. This knowledge will help you build logical arguments and understand how to derive contradictions.
- Structure:
	- 1. Assume the negation: Start by assuming the opposite of the statement you want to prove.
	- 2. Derive a contradiction: Use logical reasoning, definitions, and previously established theorems to deduce a contradiction or an inconsistency.
	- 3. Conclude the original statement: Since the assumption of the negation led to a contradiction, the original statement must be true.
- Counter examples and counterintuitive example:
	- Explore counterexamples and counterintuitive examples to deepen your understanding of how proof by contradiction works. Counterexamples demonstrate that a statement is false, while counterintuitive examples challenge our intuition. Understanding these cases will help you appreciate the power of proof by contradiction.
- Symbolically
	- 1. Assume $\neg P$
		- read as "not $P$"
	- 2. Derive a contradiction $\bot$
		- $\bot$ is called the bottom or falsum symbol. It is used to represent a contradiction or a statement is always false. 
	- 3. Conclude $P$ is true. 

### Counterexample
- Shows a statement is true is false by providing a specific case in which the statement does not hold. 
- This technique is often used to disprove conjectures or to show a statement is not true for all cases. 
- General structure of the proof:
	- 1. Assume $P(x)$ is true for all $x$ in the given domain
	- 2. Construct a specific instance or value, denoted as $c$, within the domain, such as $P(c)$ is false. 
	- 3. Show that $P(c)$ is false by providing a logical argument or calculation that demonstrate the contradiction. 
- Symbolically,
	- $P(c) \rightarrow \neg (\forall x \mid P(x))$
		- read as "If $P(c)$ is true, then it is not the case that for all $x$, $P(x)$ is true."

### Contrapositive
- Contrapositive Definition: 
	- The contrapositive of a logical implication is a statement formed by negating both the antecedent (the "if" part)(Denote as $P$ ) and the consequent (the "then" part) (denote as $Q$) of the original implication, and then switching their order.
	- Symbolic notation:
		- $(P \implies Q) \equiv (\neg Q \implies \neg P)$. 
			- Which the former and latter statements are contrapositive of each others. 


### Proof by contrapositive
- It is a technique in which we prove the statement "if A then B" by showing "if not B then not A" is true. 
- This is often used when a direct proof is difficult to construct.
- Contrapositive Definition: 
	- The contrapositive of an implication "If P, then Q ($P \implies Q$)" is the statement "If not Q, then not P. ($\neg Q \implies \neg P$)" It essentially flips the hypothesis (P) and conclusion (Q) of the original implication and negates them.
	- We call "($\neg Q \implies \neg P$)" the "contrapositive" of the original statement "($P \implies Q$)"
- Transformation of "Logical Implication": 
	- The contrapositive is a logical transformation of an implication statement (if-then statement). In real analysis, you often encounter statements of the form "If P, then Q," where P and Q represent mathematical propositions.
- "Implication statement" and "Contrapositive of implication statement" are equivalent: 
	- The original implication and its contrapositive are logically equivalent. If the original statement is true, its contrapositive is also true, and vice versa. This means that you can prove a statement by proving its contrapositive.
- Examples and Counterexamples: 
	- It's crucial to practice identifying and constructing contrapositives for various mathematical statements. Working with examples and counterexamples helps solidify your understanding of the concept and how it relates to real analysis.
- Implications in Real Analysis: 
	- In real analysis, the contrapositive is often employed to prove statements about limits, continuity, convergence, and other foundational concepts. Understanding how to apply the contrapositive correctly can simplify and clarify your reasoning in these areas.
- Proof techniques:
	- The contrapositive is often used as a proof technique known as proof by contrapositive or indirect proof. Instead of proving the statement directly, you can prove its contrapositive, which might be easier and straightforward. 





### Proof by exhaustion
- Show a statement is true by examining all possible cases. 
- It is used for problems that involves a small number of cases.

### Proof by induction on more general structure
- Induction on more general structures, such as graphs or trees, rather than just for individual numbers.

### Proof by construction
- It involves explicitly constructing an object that satisfies the conditions of the statement we want to prove. It shows the existence of an object with certain properties.

### Reduction 
- Involves reducing a problem to a simpler or better understood problem. 
- For example, a complex problem in algebra may be reduced to a simpler problem in arithmetic.

---
### Set theoretic operation
- Set as variable and nested operation
	- In the following expressions, sets could be treated as variables. Say we have a variable $A$, we can plug in another set to perform nested set theoretic operations.
- Union
	- $A \lor B := \{ x: x\in A \lor x \in B\}$
- Intersection
	- $A \land B := \{ x: x \in A \land x \in B \}$
- Set difference
	- $A \setminus B = \{ x: x \in A \land x \notin B \}$
- complement
	- $A^c = \{ x: x \in A \land x \}$
- Disjoint 
	- 2 sets has no common elements
	- $A \land B = \emptyset$
- Symmetric difference
	- Symmetric sum of sets $A$ and $B$ is the set of elements are in either $A$ or $B$, but not in both $A$ and $B$. 
	- $A \bigtriangleup B$ 
- Cartesian product
	- $A \times B$
- Power set
	- $P(A)$
- Disjoint union
	- $A \uplus B$ 
- Direct product
	- $\prod_{i \in I} A_i$, which $A_i$ is a series of sets.
- Direct sum
	- The direct sum of a family of sets 
	- Study it only when encounter it
	- Manner 1: $E_1 \bigoplus E_2 \bigoplus \dots \bigoplus E_n$
	- Manner 2: $\bigoplus_{i \in I} A_i$


### De Morgan's Law (complement law)
- $(B \lor C)^c = B^c \land C^c$
- $(B \land C)^c = B^c \lor C^c$
- $A \setminus (B \lor C) = (A \setminus B) \land (A \setminus C)$
- $A \setminus (B \land C) = (A \setminus B) \lor (A \setminus C)$



### The rule of negation
- Negation of implications
	- $\neg{(P \implies Q)} \implies (P \wedge \neg{Q})$
	- The later statement $(\neg Q \implies \neg P)$ itself can be independently evaluated and proven true or false without assuming the original statement is true.
- Negation of quantifiers
	- $\neg(\forall x \in X) \implies \exists x \in X$
- Negation of logical operators:
	- $\neg (A \land B) \implies (\neg A \lor \neg B)$
	- $\neg (A \lor B) \implies (\neg A \land \neg  B)$
- Negation of statements
	- Negating a statement might encounter all kinds of objects mentioned earlier (implications, quantifiers, sets  etc.). The trick is to distribute the negation symbol to all objects in the outermost layer. 
	- Example:
		- $\neg(\forall P, P \implies (A \land B))$
		- Before simplify this statement, we can parenthesize the statements standing after the quantifier to make it easier to work with. The quantifier is applying to the whole following statement so the original statement is equivalent to  $\neg(\forall P(P \implies (A \land B)))$
		- Now we distribute the negation to the outermost layer, which is the quantifier. So we have 
		- $\exists P[ \neg (P \implies (A \land B))]$
		- Now the negation symbol is distributing to the implication statement. So we have 
		- $\exists P(P  \land \neg (A \land B)))$
		-  Now the negation symbol is distributing to $\neg (A \land B)$. So we have  
		- $\exists P, P  \land \neg A \lor \neg B$


---

### Union of several sets
- $\{ A_1, A_2, A_3, \dots \}$
- Manners:
	- Manner 1: $\bigcup_{n=1}^\infty A_n := \{ x: x \in A_n,  for some n \in N \}$
	- Manner 2: $\bigcup_{n=1}^\infty A_n := \{ x: x \in A_n,  \exists n \in N \}$
	- Manner 3: $\bigcup_{n=1}^\infty A_n := \{\exists n \in N,  x: x \in A_n \}$
- Comments:
	- 1. "for some $n \in N$" can be replaced by $\exists n \in N$
	- 2. The order of conditions is not matter if there are no nested quantifiers on it

### Intersection of several sets
- Notation:
	- $\bigcap_{n=1}^\infty A_n := \{ x:x \in A_n, \exists n \in N\}$

---


- Most proofs have the following structure
	- if $P$ then $Q$?

- Prove property 1 of De Morgan's Law 
- $(B \lor C)^c = B^c \land C^c$
	- $(B \lor C)^c \subset B^c \land C^c$ and $B^c \land C^c \subset (B \lor C)^c$
- WTS (want to show):  $(B \lor C)^c \subset B^c \land C^c$
	- Let $x \in (B \lor C)^c$ and $x \notin (B \lor C)$, thus $x \notin B$ and $x \notin C$, thus $x \in B^c$ and $x \in C^c$, thus $x \in B^c \land C^c$
	- Thus  $(B \lor C)^c \subset B^c \land C^c$

---
- The set of natural numbers
	- $\mathbb{N} = \{ 1,2,3,4, \dots \}$
- The set of integers
	- $\mathbb{Z} = \{ -2, -1, 0, 1,2,3,4, \dots \}$
- The set of rational numbers
	- Rational number is any number that can be expressed as the quotient or fraction of two integers.
	- $\mathbb{Q} = \{ \frac{m}{n}, m,n \in \mathbb{Z}, n \neq 0 \dots \}$
- The set of real numbers
	- $\mathbb{R}$: = $\mathbb{Q}$ along with irrationals
- Odd numbers: $\{ 2m -1 | m \in \mathbb{N} \}$
- $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$

- $\mathbb{I}$: Imaginary number
- $\mathbb{C}$: Complex number
- $\mathbb{C} \supset  \mathbb{R}, \mathbb{I}$

#### First goal: describe what is $\mathbb{R}$

---
### Quantifiers
- $\exists$:
	- Existential quantifier
	- Used to make a statement about the existence of at least one element in a particular set that satisfies a given property.
- $\exists !$
	- Unique existential quantifier 
- $\forall$
	- Universal quantifier
	- Used to make a statement about all elements of a particular set. 

### Ordering of quantifiers 
- Same as the ordering of variable is important (Non-commutative means the order of the operands are arranged does not affects the result of the operation), It can have significant impact on the meaning of the statement.

### Quantifier exchange rule
- Say we have two quantifiers $Q_1$ and $Q_2$, where $Q_1, Q_2$ can be either $\forall$ or $\exists$.
- Then our rule would be: $Q_1 x Q_2 y R(x,y) \iff Q_2 y  Q_1 x R(x,y)$ (Not sure)


### Expressing mathematical definitions and theorems with quantifiers
- eg1:
	- Natural text statement: 
		- " for any positive number ε, there exists a positive number δ such that the distance between f(x) and a limit L is less than ε whenever x is sufficiently close to a, but not equal to a."
	-  symbolic statement:
		- "∀ε > 0, ∃δ > 0 such that |f(x) - L| < ε whenever 0 < |x - a| < δ"
		- "∀ε ∈ (0, ∞), ∃δ ∈ (0, ∞) such that ∀x ∈ dom(f), (0 < |x - a| < δ) ⇒ (|f(x) - L| < ε)"****



---
### "A property of subsets of the set"
- In real analysis, a property of subsets is a property that applies to a set of elements, rather than to individual elements themselves. 
- That is, a property of subsets is a property that depends on the elements in a set and how they are related to each other, rather than on the elements themselves.
- Examples:
	- well ordering property
	- completeness property of the real numbers
	- compactness
	- connectedness
	- boundedness
	- countability


### Well ordering property of $\mathbb{N}$
- It is a property of subsets of the set $\mathbb{N}$.
- Property
	- Every non-empty subset of $\mathbb{N}$, has a least (smallest) element. That is, 
	- $\forall S \subseteq \mathbb{N}, \exists x \in S, \forall y \in S, x \leq y.$
	- Verbal version of the symbolic expression:
		- With a set of natural number $\mathbb{N} = \{ 1,2,3, \dots \}$ and we give them natural ordering, that is $1 <2 <3 < 4< \dots$. By $S \subset \mathbb{N}$ having least element, we exists an $x \in S$ such that for every $y \in S$, we have $x \leq y$. 
- Formulation
	- $\mathbb{N} = \{1,2,3, \dots \}$
	- $S \subset \mathbb{N}$
	- $\exists x \in S, \forall y \in S, x \leq y$
- Q: Why we need to show the existence of a subset $S \in \mathbb{N}$ that satisfies the well-ordering property
- A: It is because well-ordering property is not a property of individual elements, but rather a property of subsets. 

### Mathematical induction
- (Basis statement) $P(1)$ is true
- (Induction step) if $P(n)$ is true, then $P(n+1)$ is true.

---
- Theorem
- Proposition
- Lemma
	- A result leading to another result
- Corollary
	- A quick consequence of the preceding result


---


---
# Week 2 Cardinality

- Let $h: A\rightarrow C$ be the function $h(x) = (g \circ f)(x)$ we want to prove $h$ is a bijection
- (1/2) Injective or 1-to-1:
	- if $h(x_1) = h(x_2)$, then $g(f(x_1)) = g(f(x_2))$
	-  $\Rightarrow$ $f(x_1) = f(x_2)$, since $g$ is 1-to-1.
	- $\Rightarrow$ $x_1 = x_2$, since $f$ is 1-to-1.
- (2/2) Surjective:
	- We want to prove $h(A) = C$, $\forall z \in C$, $\exists x \in A$ such that $h(x) = z$
	- Let $z \in C$, since $g$ is surjective, $\exists y \in B$ such that $g(y) = z$.
	- Since $f$ is surjective, $\exists x \in A$ such that $f(x) = y$
	- $h(x) = g(f(x)) = g(y) = z$
	- therefore $h(x) = z$
- Q: When proving  f: A -> B is surjective, why we write  $\exists x \in A$, $\forall y \in B$, such that $f(x) = y$?
	- My concern is why the quantifier for $x$ and $y$ is different?


### Cartesian products
- Notations:
	- ordered pair
		- $(a,b)$
		- The use of ordered pairs in the definition of Cartesian product is important because it allows us to specify the relationship between the elements of two sets in a precise and unambiguous way. 
		- The first element in an ordered pair is called the "first coordinate" or "x-coordinate," and the second element is called the "second coordinate" or "y-coordinate."
	- triple
		- $(a,b,c)$
	- N-tuple
		- $(e_1, e_2, \dots, e_n)$
	- Cartesian product
		- $A \times B$
	- Cartesian plane
		- $\mathbb{R} \times \mathbb{R} = \mathbb{R}^2$
	- Cartesian power
		- $A^n$
- Definition:
	- Let $A$ and $B$ be sets. The Cartesian product is the set of tuples defined as $A \times B := \{ (x,y):x \in A, y \in B\}$
- Examples:
	- If $A = \{ 1,2,3\}$, $B = \{a,b,c \}$, then $A \times B$ is the set of combination of them: $\{(1,a),(1,b),(1,c),(2,a),(2,b),(2,c) \}$

### "Defining one mathematics notion by a subset of other distinct mathematics notion"
- Examples:
	- 1. Function $\subset$ Cartesian product
	- 2. Derivatives of functions $\subset$ Concept of limit
	- 3. Integral $\subset$ Riemann sum
	- 4. Continuity of a function $\subset$ Limits and neighborhoods
	- 5. Group $\subset$ Closure, associativity, identity and inverse element. 
$f$ is a function from $X$ to $Y$ if and only if $f \subseteq X \times Y$ and for each $x \in X$, there exists a unique $y \in Y$ such that $(x,y) \in f$.

### Function
- It is an example of "Defining one mathematics notion by a subset of other distinct mathematics notion"
- Verbally, function is (a kind of / $\subset$) mapping that$\forall x \in A$, $\exists ! (x,y) \in f$.
- Function signature
	- $f: X \rightarrow Y$, where $X = dom(f)$, $Y = range(f)$
- Definition in verbal terms:
	- $f$ taking a set $A$ to a set $B$ is (a kind of / $\subset$) mapping that $\exists x \in A$ assigns a unique $y \in B$. 
- Definition in set-theoretic terms:
	- Manner 1:$f = \{(x,y) \in (X \times Y) : \forall x \in X, \exists ! y \in Y\}$
	- Manner 2: $f \subseteq (A \times B) \land \forall x \in A$, $\exists ! \in B$ such that $(x,y) \in f$ 
- Domain of a function
	- $\{ x | P(x)\}$, $P(x)$ is a predicate that specifies the set of all possible input values for which $f(x)$ is defined. 
- Range of a function
	- $f: X \rightarrow Y$, 
	- Manner 1: $Range(f) := \{ f(x) | x \in X\}$
	- Manner 2: $Range(f) := \{ y \in Y | \exists x \in X, f(x) = y \}$


### Image / direct image
- Image is the range where we put a subset of elements from the domain into the equation
- Image refers to  the set of output values that the function $f$ can produce when its input takes on values from a certain set $C \in A$, rather than a set of elements from the domain $A$. 
- Define image $C$ as:
	- $f: A \rightarrow B$, $C \subset A$, $D \subset B$
	- $D = f(C) := \{ f(x) \in B : x \in C \}$

### Pre-image / inverse image 
- Pre-image of a subset of the range of a function is the set of all points in the domain that map to the given subset.
- Let $f: X \rightarrow Y$ be a function between two sets $X$ and $Y$. Let $B \subseteq Y$ be a subset of the range of $f$. The pre-image defined as:
	- $A = f^{-1}(B) := \{ x \in X : f(x) \in B \}$

---
## Function classes


### Injective (one-to-one) function
- v1 Definition
	- Function is injective if $\forall x_1, x_2, f(x_1) = f(x_2) \implies x_1 = x_2$ 
- v2 definition
	- A function is injective if for any two distinct elements in the domain, the function maps them to distinct elements in the codomain. In other words, if $f(x_1) = f(x_2)$, then it must be the case that $x_1 = x_2$.
- Usage:
	- 1. Showing a function is injective:
		- To prove that a function is injective, we can directly verify that $x_1$ and $x_2$ in the domain, $f(x_1)$ and $f(x_2)$ are equal only when $x_1$ and $x_2$ are equal.
	- 2. Injectivity from sets to sets
		- To show that a function from one set to another set is injective, we need to provide an example function $\exists f$ that satisfies the injectivity property.
			- Therefore, we must propose a specific function that guarantees the statement holds true.
- Non-injective function:
	- Recall injectivity definition, which is: $\forall x_1, x_2, f(x_1) = f(x_2) \implies x_1 = x_2$ 
	- We negates the definition to injectivity to obtain the definition of no-injectivity, which becomes:
		- $\neg(\forall x_1, x_2, f(x_1) = f(x_2) \implies x_1 = x_2)$ 
		- $\exists x_1, x_2, f(x_1) = f(x_2)$ and $x_1 \neq x_2$
	- For more information of negation statement, refers to "negation of statement" part of the note. 

-   To define a non-injective function, we can negate the injectivity definition, resulting in the following statement:
    -   $\neg(\forall x_1, x_2, f(x_1) = f(x_2) \implies x_1 = x_2)$
    -   This can be further simplified to:
    -   $\exists x_1, x_2, f(x_1) = f(x_2)$ and $x_1 \neq x_2$
-   If there exist elements $x_1$ and $x_2$ in the domain such that $f(x_1) = f(x_2)$ but $x_1$ is not equal to $x_2$, then the function is considered non-injective.****



### Surjective (onto) function
- Definition:
	- It is requiring every element in the codomain has a preimage in the domain.
	- "Every element of the function's codomain is the image of at least one element of its domain. It is not required that $x$ be unique"
	- "completely covers the function's codomain.", a function that "covers" its entire range. 
- Definition:
	- For $f: X \rightarrow Y$, $\forall y \in Y, \exists x \in X \text{, such that } f(x) = y$
	- For $f: X \rightarrow Y$, $\exists x \in X \text{, such that } f(x) = Y$ (doubtful)
- Application:
- Q: 
	- Why when showing a function is surjective, we show all of its output elements has corresponding input element, not the opposite, which means all input values has corresponding output value?
- A: 
	- We can't do it that way. We must align with the definition of surjectivity which is "Surjective = "completely covers the function's codomain."

---







---
### Bijective
- $f$ is bijective If it is both injective and surjective.  
- Property
	- if there exists an injection from set $A$ to $B$, we write $|A| = |B|$, if $A$ and $B$ have the same cardinality.


---





---
### Relations
- Given a set $A$, a binary relation on $A$ is a subset $R \subset A \times A$, which are those pairs where the relation is said to hold. Instead of $(a,b) \in R$, we can write $aRb$.  
- Examples of relations:
	- $<$
	- $=$
	- $\subset$


---

## Relation classes

### Reflexive
- $aRa, \forall a \in A$

### Symmetric
- $aRb \implies bRa$

### Transitive
- $aRb \land bRc \implies aRc$

### Equivalence 
- If $R$ is reflexive, symmetric and transitive

---


### Equivalence classes
- Equivalence relations are useful in that they divide a set into sets of equivalent elements. Each equivalence class contains all the elements that are equivalent to a particular element, and no element that is not equivalent to it. In that way, the set is divided into non-overlapping subsets, and every element belongs to exactly one subset. 
- Application
	- Demonstrate some aspects of "cardinality"?
- Let $A$ be a set, $R$ is equivalence relation. We denote equivalence class of "$a \in A$" is $[a]$.
	- Then $[a] = \{ x \in A: aRx \}$.
	- For the set $A$, say $card(A) = n$, then $A$ would have $n$ distinct equivalent classes. 
	- $\forall a \in A$, there is exactly one equivalence class $[a]$. An element cannot belong to two distinct equivalence classes, since equivalence classes are mutually exclusive and exhaustive. 
	- $aRb$ if and only iff $[a] = [b]$. 
		- It is a key property if equivalence relations. That means two elements are related by R if and only if they belong to the same equivalence class. 
- Example:
	- $A = \{ 1,2,3\}$  
	- Then this class would have 3 equivalence classes, $[1], [2]$ and $[3]$.

---

### Cardinality
- Definition of cardinality:
	- Cardinality carries the notion of "size" of sets. 
	- We state that two sets $A$ and $B$ have the same cardinality if there exists a bijection $f: A \rightarrow B$, in which bijection can be think of as a way of comparing the size of sets without explicitly counting their elements. 
- Use cardinality to describe sets:
	-  Comparing the sizes of sets typically uses various operations such as union, intersection and complement.
	- To count the cardinality of a set that contains repeated elements, you should only count the distinct elements in the set. 
- Use cardinality to describe functions:
	- In the context of comparing cardinality between 2 sets, we cannot state $|C| = |D|$ by counting $|C|$ and $|D|$ separately. The notion of bijection captures the idea of a perfect matching between the elements of two sets, which can be though of a way of comparing the size of sets without explicitly counting their elements. 
	- Let $A$ and $B$ be sets. $A$ and $B$ have the same cardinality when there exists a bijection $f: A \rightarrow B$
		- The existence of a bijection really is an equivalence relation. 
			- Recall: $aRb$ if and only if $[a] = [b]$, which $R$ is equivalence relation. 
		- This is because the cardinality of a set is a measure of the size of the set, and we can compare the size of the sets by seeing whether we can match up their elements in one-to-one manner. 
			- (But we can also link up two sets with same number of elements, but one of them has repeated numbers?)
				- See example 2
		- Bijections are precisely the function that preserve the number of element in a set. Therefore they provide a natural way to compare the sizes of two sets.
- Example 1 (Bijection shows two sets have the same cardinality): 
	- If $A = \{ a,a,b \}$, what is $card(A)$?
	- $card(A)$ is three. Note that $a$ appears twice in $A$, it is still counted as only one element when computing cardinality of $A$. 
	- In this case, a possible bijection is $f:A \rightarrow B$ defined by $f(1) = a$, $f(2) = b$, and $f(3) = c$. This function maps each element of $A$ to a unique element of $B$, and vice versa, so it is a bijection.
- Example 2:
	- consider the sets $C = {1, 2, 3}$ and $D = {1, 2, 4}$. We can see that $card(C) = 3$ and $card(D) = 3$, but we cannot conclude that $C$ and $D$ have the same cardinality.
	- In fact, there is no bijection between $C$ and $D$, because there is no way to map the element 3 in $C$ to an element in $D$. Therefore, we cannot conclude that $C$ and $D$ have the same cardinality.
	- we will discuss more of this in theorem 12 (CSB theorem)
- Example 3 (Shows counting cardinality separately is a flawed reasoning):
	- Consider $A = \mathbb{N}$ and $B = \mathbb{Z}$
	- It is easy to see there is injection $f: A \rightarrow B$ given by $f(n) = n, \forall n \in A$
	- It is easy to see there is injection $f: B \rightarrow A$ given by $g(m) = |m|, \forall m \in B$
	- We might conclude $|A| = \infty$ and $|B| = \infty$ and therefore $|A| = |B|$. This reasoning is flawed, since the notion of "infinity" is not a cardinality in the sense of set theory.


### Theorem 12 (Cantor-Schroder-Bernstein)
- If $|A| \leq |B|$ and $|B| \leq |A|$, then $|A| = |B|$.
	- In other words, if there is a one-to-one correspondence from $A$ to $B$ and from $B$ to $A$, then $A$ onto $B$ and $B$ onto $A$. 
- Background
	- It is a fundamental result in set theory and real analysis that establishes a necessary and sufficient condition for two sets to have the same cardinality.
	- Although the statement of the theorem may seem intuitive, the proof is nontrivial and requires some technical ideas from set theory. 
- Difficulty of the proof:
	- The main difficulty arises from the fact that we need to construct a bijection between two sets without assuming any additional structure on the sets or on the functions relating them.
	- say $E = \{ e \mid e = 2n \land n \in \mathbb{N}\}$, show $|E| = |\mathbb{N}|$
	- Recall: definition of surjective function is, For $f: X \rightarrow Y$, $\forall y \in Y, \exists x \in X \text{, such that } f(x) = y$
	- We might think we can establish a bijection function by simply pairing each natural number with its double, i.e. defining $f: \mathbb{N} \to 2\mathbb{N}$ by $f(n) = 2n$. This function is clearly injective, since different natural numbers map to different even numbers. However, the function is not surjective, since there are even numbers that are not of the form $2n$ for any $n$
		- eg: $0$ is an even number in 
----
## Interesting sets that flesh out cardinality

### Countable 
- If $A$ is finite or countably infinite, we say $A$ is countable. Otherwise, we say $A$ is uncountable.

### Finite / Countably infinite 
- If $|A| = |N|$, that means there exists a bijection from $A$ to natural numbers, then $A$ is countably infinite, or finite.
	- We define countably finite as that, because when we count, we count the number in the manner of $1,2,3,4,\dots$

- Discuss whether the following number sets are countably infinite:
	- 1. Even number set $E = \{ 2n \mid n \in \mathbb{N}\}$
	- 2. natural number function $f: \mathbb{N} \times \mathbb{N}$
	- 3. Rational number $\mathbb{Q}$
	- 4. Integers $\mathbb{Z}$
	- 5. Real numbers $\mathbb{R}$

- Example 1:
	- Even number: $|\{ 2n | n \in N\}| = |N|$
	- Odd number: $|\{ 2n-1 | n \in N\}| = |N|$
	- Proof:
		- 0/2 Before you show something is a bijection, first write down what is the function being discussed. 
		- 1/2 Injective
			- i.e. If $f(n_1) = f(n_2)$ then $n_1 = n_2$. 
		- 2/2 Surjective
			- i.e. $\forall m \in \{ 2n : n \in \mathbb{N} \}$
	- Comments:
		- You might think that even numbers and odd numbers are disjoint so the cardinality of even / odd numbers would be the halve of natural numbers? 
		- But that is not how cardinality works. You don't add cardinalities to get cardinalities. 

- Example 2:
	- $\mathbb{N} \times \mathbb{N}$ is countably infinite. 
	- Comments:
		- 1. Write down first all the elements whose two entries sum to $k$, then write all the elements whose entries sum to $k+1$ and so on.
			- We can propose writing elements of this $\mathbb{N} \times \mathbb{N}$ as $(1,1), (1,2), (2,1), (1,3), (2,2), (3,1), \cdots$
			- We can write these elements in a 2D table. 
		- 2. Define a bijection with $\mathbb{N}$ by letting $1$ go to $(1,1)$, $2$ go to $(1,2)$ and so on.
			- Define $f(m,n) = \frac{1}{2}(m+n-2)(m+n-1)+m$
			- This function assigns a unique natural number to each element in $\mathbb{N} \times \mathbb{N}$
			- Show $f$ is injective:
				- Show when $f(m_1, n_1) = f(m_2, n_2)$, $m_1 = m_2$ and $n_1 = n_2$
				- $\begin{align*} f(m_1, n_1) &= f(m_2, n_2) \\ (m_1 + n_1 - 2) (m_1 + n_1 -2)(m_1 + n_1 -1) + 2m_1 &= (m_2 + n_2 - 2) (m_2 + n_2 -2)(m_2 + n_2 -1) + 2m_2 \\ m_1^2 + n_1^2 - m_2^2 - n_2^2 &= m_1 - m_2 + n_1 - n_2 \end{align*}$ 
				- To make this equation holds, the only way is if $m_1 = m_2$, and $n_1 = n_2$. 
			- Show $f$ is surjective:
				- Show for $f: X \rightarrow Y$, $\forall y \in Y, \exists x \in X$ 
		- 3. Conclusion
			-  In the table, every element of $\mathbb{N} \times \mathbb{N}$ appears exactly once in this enumeration. 



- Example 3:
	- $|\mathbb{Z}| = |\mathbb{N}|$
	- Proof:
		- We propose a function $f: \mathbb{N} \rightarrow \mathbb{Z}$ as follow:
		- $f(n) = \begin{cases} \frac{n}{2}, &  \text{if n is even} \\ -\frac{n+1}{2}, &  \text{if n is odd} \end{cases}$
			- This function maps each natural number to a unique integer and each integer to a unique natural number, thereby establishing a one-to-one correspondence between the two sets. 
		- Show $f$ is bijective:
			- 1/2 Injective (i.e. $f(m) = f(n) \implies m = n$ )
				- If $m$ and $n$ are even
					- Say we have $f(m) = f(n)$
					- then $\frac{n}{2} = \frac{m}{2}$
					- so $m = n$
				- If $n$ and $m$ are odd
					- Say we have $f(m) = f(n)$
					- then $-\frac{n+1}{2} = -\frac{m+1}{2}$
					- So $m = n$
				- If one number is even, and other is odd, then $f(m) \neq f(n)$m since $\frac{n}{2} \neq -\frac{n+1}{2}$
				- Therefore, we have shown that $f$ is injective. 
			- 2/2 Surjective (i.e. show for $f: X \rightarrow Y$, $\forall y \in Y, \exists x \in X(f(x) = y)$)
				- In our case, $f: \mathbb{N}  \rightarrow \mathbb{Z}$
				- We need to show that $\forall z \in \mathbb{Z}$ , $\exists n \in \mathbb{N}(f(n) = z)$
				- If $z$ is non-negative, then $f(n) = \frac{n}{2} = z$
				- If $z$ is negative, then $f(n) = -\frac{n+1}{2} = z$

- Example 4:
	- $|\{ q \in \mathbb{Q}, q>0 \}| = |N|$
	- $\mathbb{Q} = \{ \frac{m}{n}, m,n \in \mathbb{Z}, n \neq 0 \dots \}$
	- 0/2 Suppose we have a bijective function that maps $\mathbb{Q}$ to $\mathbb{N}$. i.e. $f : \mathbb{Q} \rightarrow \mathbb{N}$ 
	- Suppose $\forall q \in Q, q > 0$ can be written as $q = \frac{p_1^{r_1} \dots p_N^{r_N} }{q_1^{S_1} \dots q_M^{S_M}}, r_j, s_k \in \mathbb{N}, \forall j,k(q_j \neq p_k)$

---
### Zermelo-Fraenkel set theory
- Axiom of extensionality:
	- two sets are equal iff they have the same elements
- Axiom of empty set:
	- there exists a set with no elements
- Axiom of pairing:
	- given any two sets, there exists a set with no element. 
- Axiom of union:
	- given any set, there exists a set that contains all the elements of the sets in the original set.
- Axiom of power set:
	- given any set, there exists a set that contains all the subsets of the original set.
- Axiom of regularity:
	- every non-empty set has an element that is disjoint from the set itself.
- Axiom of choice:
	- given any collection of non-empty sets, there exists a way to choose one element from each set in the collection
- Axiom of infinity:
	- there exists an infinite set. 


---
### Symmetricity of cardinality
- Theorem: If $|A| = |B|$, then $|B| = |A|$.
- Proof:
	- 1. Axiom of choice in set theory
		- It is typically taken as an axiom in set theory. The axiom of choice guarantees the existence of a function that selects one element from each set in a collection of non-empty sets. 
	- 2. Constructing bijections between $A$ and $B$ by pairing up elements in one-to-one correspondence.
		- Using this function, we can construct a bijection between two sets $A$ and $B$ of the same cardinality by pairing up the elements of $A$ and $B$ in one-to-one correspondence.
	- Since the axiom of choice holds for arbitrary sets, we can apply it to any two sets of the same cardinality, which implies that the cardinalities are equal in both directions.


### Transitivity of cardinality
- If $|A| = |B|$, $|B| = |C|$, then $|A| = |C|$.
- Proof:
	- Suppose $|A| = |B|$ and $|B| = |C|$, then there exists bijections from $f: A \rightarrow B$ and $g: B \rightarrow C$. 
	- Let $h: A \rightarrow C$ be the function $h(x) = (g \circ f)(x)$. We want to prove $h$ is a bijection. 
	- To show $h$ is bijection, we have to show it is:
		- Injective / one-to-one correspondence
		- 

---

### Powersets
- It is the set of all subsets of $A$. 
- Formally, we can define it as $P(A) = \{ B \mid B \subset A\}$

### Theorem 15 (Cantor): If $A$ is a set, then $|A| < |P(A)|$ 
- Extension of the theory: $|A| < |P(A)| < |P(P(A))| < \dots$ 
- The trickiness of this theorem is that the domain and range of $g$ could be overlapped. 
- Example:
	- Let $A = \{ 1,2,3 \}$, then $P(A) = \{ \emptyset, \{ 1 \}, \{ 2\}, \{ 3\}, \{ 1,2\}, \{ 1,3\}, \{2,3 \}, \{ 1,2,3\} \}$
	- Test for the theorem: write down any function $f: A \rightarrow P(A)$ that is either injective and/or surjective 
- Proof:  
	- 1. Show $|A| \leq |P(A)|$
		- For each element of $A$, we need to associate with a unique element of $P(A)$. 
		- Manner 1: $f(x):=\{x\}$ 
			- Which maps $A$ to $P(A)$ for any $x \in A$. 
			- Therefore, $|A| \leq |P(A)|$. 
		- Manner 2: $f(1) = \{ 1,2\}, f(2) = \{ 1,3\}, f(3) = \emptyset$
			- Which maps $A$ to $P(A)$ for any $x \in A$. 
			- Therefore, $|A| \leq |P(A)|$. 
		- Keeps your own injective function $f$ to show it also surjective. 
	- 2. Show $|A| = |P(A)|$ is not true
		- To show $f: A \rightarrow P(A)$ is not bijection, now we must show that no function $g: A \rightarrow P(A)$ is a surjection, because we have already proven that exists some $f$ that maps $A$ to $P(A)$. 
		- Recall what is surjective:
			- Show $g$ is surjective means show (i.e. show for $g: A \rightarrow P(A)$, $\forall b \in P(A), \exists a \in A \text{, such that }  g(a) = b$)
			- $\Leftrightarrow \forall a \in A, f(x) \in P(A)$ 
		- The intuitive answer 
			- It is no, and you might say something like "because $A$ has 3 things and $P(A)$ has 8 things, so there is no way to be surjective."
		- Proof (by contradiction):
			-  1. We suppose $g$ is surjective, which means $g(x) = y$ holds. 
			- For $x \in A$, $g(x) \subset A$. Define the set $B:=  \{  x \in A : x \notin g(x) \} \in P(A)$. 
				- My interpretation:
					- 1. $B$ is the set of elements from the domain of $g$ , where these elements are also not a member of the image of $g(x)$. 
					- 1b. We also call $B$ to be "diagonal"
					- 2. $B$ allow us to identify a subset of elements in the domain of $g$ that is not in the range of $g$. To prove $g$ is surjective, we need to show for every element $b$ in the range of $g$, there exists an element $a$ in the domain of $g$ such that $g(a) = b$. 
			- For our function $f$, is there any $y \in A$ such that $f(y) = D$? 
			- Manner 1: $f(x):= \{ x \}$
				-  $B = \emptyset$
			- Manner 2: $f(1) = \{ 1,2\}, f(2) = \{ 1,3\}, f(3) = \emptyset$
				- $B = \{2,3 \}$
				- For this function, $\forall y \in A$, such that$f(y) = B$?
					- No. $f(1) \neq B$, $f(2) \neq B$, $f(3) \neq B$. 
			- In other words, $B$ is the set of all elements of $A$ that are not mapped to themselves by $f$. 
		- Case 1, $x \in g(x)$
			- If $x \in g(x) \implies x \in P(A)  \implies x \notin A$ . So it leads to a contradiction. 
		- Case 2, $x \notin g(x)$
			- $x \in g(x) = B$

	- Q: 
		- Why when showing a function is surjective, we show all of its output elements has corresponding input element, not the opposite, which means all input values has corresponding output value?
	- A: 
		- We need to align our steps with the definition of surjectivity, and its definition is simply whether the function could "completely covers the range of function". 

- Figure:
	- Diagonal arguments
	- If diagonally there is a thing, $B$ would not include it. If there is not a thing, we include that element.
	- $D \notin range(f)$ since it differs from set $f(a)$ at element $a$. 
	- So no $f$ points into $D$, $f$ is not a surjection. 
![[Pasted image 20230504153430.png|400]]
![[Pasted image 20230504153450.png|400]]

- Application:
	- $|\mathbb{N}| < |pow(\mathbb{N})|$, thus $pow(\mathbb{N})$ is uncountable.

### Cantor-Bernstein-Schroder theorem
- $A$ and $B$ have the same cardinality iff $|A| \leq |B|$ and $|B| \leq |A|$. 

---


### Ordered sets
- An ordered set is a set $S$, together with a relation $<$ such that it satisfies two conditions: 
	- condition 1 (comparability):
		- $\forall x,y \in S$ either $x<y, y<x$, or $x = y$. 
	- condition 2 (not necessary) (transitivity): 
		-  $\forall x,y,z \in S$, $(x <y) \land (y<z) \implies x<z$
	- These two conditions capture the essence of order, and allows for comparisons between elements.
- Alternative definitions of "ordered set" and discuss is it good or bad
	- Q: Defining an ordered set as a set where the relation of "<" and "=" is valid between all elements is certainly a valid approach. 
	- A: But if we separate the conditions of comparability and transitivity, that could provide a more structured and precise understanding of "order".
		- Condition 1 ensures every pair of the elements in the set can be compared using the "<" relation.
		- Condition 2 ensures that the order relation is consistent and behaves in a predictable way.
	- Q: I think condition 1 could covers the meaning of condition 2
	- A: You are correct that condition 1 already implies the transitivity.
- Examples of ordered set
	- $\mathbb{Z}$: $m < n \iff n - m \in \mathbb{N}$
	- $\mathbb{Q}$: $q<p\iff \exists m,n \in \mathbb{N}$ such that $p - q = \frac{m}{n}$
		- $q<r \iff   q-r \in \mathbb{Q}$
	- In these examples, we use a symbol such as "$<$" to indicate the order relation between elements of the set. 
- Example of ordered set
	- Dictionary ordering of $\mathbb{Q} \times \mathbb{Q}$: $\{ A \times B | a \in A, b \in B\}$
	- We say $(a,b) < (q,r)$ if either $a<q$ or $a=q \land b<r$.
- Non-example of ordered set
	- Say $S = P(N)$, we define a relation $K$ such that $AKB$ if $A \subset B$.
	- The $K$ satisfies condition 2, which $A \subset B$ and $B \subset C$, then $A \subset C$. 
	- But $K$ does not satisfies condition 1, because $\{ 0 \} \neq \{ 1\}$, they are neither subset nor superset of each others. 



### Ordered field
- An ordered field is a field $\mathbb{F}$ equipped with a total ordering $\leq$ that is compatible with the field operations.
- Specifically, for any $a,b,c\in\mathbb{F}$, the following properties hold:
	- 1.  Trichotomy: Exactly one of the following holds: $a<b$, $a=b$, or $a>b$.
	- 2. Additive Compatibility: If $a<b$ and $c\in\mathbb{F}$, then $a+c<b+c$.
	- 3. Multiplicative Compatibility: If $a<b$ and $c>0$, then $ac<bc$.
- An ordered field must also satisfy the usual algebraic properties of a field, such as commutativity, associativity, distributivity, and the existence of additive and multiplicative inverses

---

### Upper bound
- 1) Using quantifier
	- Let $E \subset S$, where $S$ is an ordered set. If $\exists b \in S$, $\forall x \in E(x \leq b)$, then $b$ is an upper bound of $E$.
- 2) Using set builder notation.
	- Let $E \subset S$, where $S$ is an ordered set.  $b = \{b \in S | \forall x \in E \land x \leq b \}$
	- Let $E \subset S$, where $S$ is an ordered set.  $\exists b \in S, b \in \{b' \in S | \forall x \in E \land x \leq b' \}$
- 3) Using verbal language
	- Let $E \subset S$, where $S$ is an ordered set. An element $b \in S$ is an upper bound of $E$ if for every $x \in E$, we have $x \leq b$.
- Statement 3 seems to be the easiest to be understand. 

### Lower bound
- Let $E \subset S$, where $S$ is an ordered set. An element $b \in S$ is an lower bound of $E$ if for every $x \in E$, we have $x \geq b$.

### Supremum / Least upper bound property
- We can imports the definition of "upper bound" to help simplify the definition of "least upper bound property"
- Definition of supremum:
	- If there exists an upper bound $b_0$ of $E$ such that whenever $b$ is any upper bound for $E$, we have $b_0 \leq b$, then $b_0$ is called the least upper bound or the supremum of $E$. We write $supE = b_0$

### Infimum / Greatest lower bound
- Definition of infimum:
	- If there exists an lower bound $b_1$ of $E$ such that whenever $b$ is any lower bound for $E$, we have $b_1 \geq b$, then $b_0$ is called the greatest lower bound or the infimum of $E$. We write $infE = b_1$****

### Bounded
- If a set $E$ is both bounded above (with $b_0$) and bounded below (with $b_1$), we say simply that $E$ is bounded. 

- examples (where $supE$ and $infE$ are in the set $E$):
	- $S = \mathbb{Z}$, $E = \{ -1,0,2\}$
	- UBs = 2,3,4,5,...
	- $sup E := 2$, $supE \in S$
	- LBs = -1,-2,-3,-4,....
	- $inf E := -1$, $infE \in S$
- example (where $sup$ and $inf$ are not in the set $E$)
	- $S = \mathbb{Q}$. $E = \{  q \in Q | 0<q<1\}$, then $supE=1\not in E$, $inf=0 \notin E$. 
		- To show $1$ is an upper bound of $E$, we need to show that $q \leq 1$ for all $q \in E$. 
		- Since $E=\{ q \in \mathbb{Q} \mid 0<q<1\}$, it follows that $0<q<1$. 
		- Since $1$ is greater than or equal to every number in the interval $(0,1)$, we have $q \leq 1$ for all $q \in E$. Therefore, $1$ is an upper bound of $E$. 
	- Recall: the set of rational numbers
		- $\mathbb{Q} = \{ \frac{m}{n}, m,n \in \mathbb{Z}, n \neq 0 \dots \}$

---
### Least upper bound property / completeness property
- An ordered set $S$ has the least upper bound property if every non-empty subset $E \subset S$ that is bounded above, has a least upper bound, that is $supE$ exists in $S$. 
- If there are subset of $S$ that does not have upper bound, we describe it as "set $S$ does not have least upper bound property."
- Q:
	- Can I state that, if any sets $K = \{k \in K \mid k > \theta \land k< \phi \}$ has "least upper bound property", it means the $supK$ right above the boundary of set $K$, for this $K$, $supK = \phi$ and $infK = \theta$? 
- A:
	- No. This statement is incorrect. It state that every non-empty subset of a partially ordered set that is bounded above, has a least upper bound. It does not guarantee that the least upper bound of a subset equals the supremum of that subset. 
	- To illustrate this, consider the set $K={q\in\mathbb{Q}:q<0}$, which is a subset of $\mathbb{Q}$ that is bounded above by $0$. It is easy to see that $K$ has the least upper bound property in $\mathbb{Q}$, since the supremum of any non-empty subset of $K$ is also an upper bound of $K$ and therefore has a least upper bound. However, the supremum of $K$ is $0$, while $\phi=\inf K=-\infty$, so $supK$ is not equal to $\phi$.

---

The value of $\phi = \inf K = -\infty$ is relevant because it is the greatest lower bound of $K$ in the extended real number system. By definition, the infimum of a set $K$ is the greatest lower bound of $K$ if and only if the following two conditions hold:

1.  $\inf K$ is a lower bound of $K$, i.e., $\inf K \leq k$ for all $k\in K$.
2.  For any lower bound $b$ of $K$, i.e., $b\leq k$ for all $k\in K$, we have $b\leq \inf K$.

In this case, we have $K = {q\in\mathbb{Q}:q<0}$, which is a subset of $\mathbb{Q}$ that is not bounded below in $\mathbb{Q}$. However, in the extended real number system, $K$ is bounded below by $-\infty$, which is the infimum of $K$.

The relevance of this is that, even though $K$ has the least upper bound property in $\mathbb{Q}$, it does not have a greatest element or a minimum element in $\mathbb{Q}$. In other words, $K$ does not have a well-defined "boundary" in $\mathbb{Q}$. The value of $\inf K = -\infty$ in the extended real number system captures this fact and shows that $K$ extends indefinitely to the left in the real line.

Therefore, the fact that $\phi = \inf K = -\infty$ is relevant because it helps to understand the behavior of $K$ in the real line and shows that $K$ does not have a least upper bound in $\mathbb{Q}$ that corresponds to its "boundary" in $\mathbb{Q}$.


---

- eg 1 (countable set):
	- $S = \{0,1\}$
	- $E \subset S$ and $E = \{0\}$
		- $supE$ = $0 \in S$
	- $E \subset S$ and $E = \{1\}$
		- $supE$ = $1 \in S$
	- $E \subset S$ and $E = \{0,1\}$
		- $supE$ = $1 \in S$
	- Therefore, $S$ has least upper bound property.

- eg 2 (countably infinite set):
	- Show $S = \{ -1, -2, -3, \dots \}$ has least upper bound property. 
		- To show that $S$ has the least upper bound property, we need to show that any non-empty subset $E$ of $S$ has a supremum (i.e., a least upper bound) in $S$.
	- $E \subset S$,  $E$ non-empty.
		- This simply sets up the subset $E$ of $S$ that we will work with.
	- Thus $-E = \{ -x \mid x \in E \} \subset \mathbb{N}$
		- Here, we define the set $-E$ as the set of negations of all the elements of $E$. Since $E \subset S$, all the elements of $E$ are negative, and thus all the elements of $-E$ are positive (i.e., in $\mathbb{N}$).
	- By the well ordering property of $\mathbb{N}$, $\exists m \in -E$ such that $m \leq -x$ for all $x \in E$. 
		- This follows from the well ordering property of $\mathbb{N}$, which states that any non-empty subset of $\mathbb{N}$ has a least element. Since $-E \subset \mathbb{N}$, it has a least element, which we call $m$. By definition of $-E$, we have $m \leq -x$ for all $x \in E$.
	- $-m \in E \land \forall x \in E, x \leq -m \implies$ -m is the supremum of $E$.  
		- Since $m \in -E$, we have shown that $-E$ has an lower bound (namely, $m$). 
		- Since $-m \in E$, we have shown that $E$ has an upper bound (namely, $-m$). 
		- To show that $-m$ is the least upper bound (i.e., supremum) of $E$, we need to show that it is not exceeded by any other upper bound. That is, we need to show that for any $x \in E$, we have $x \leq -m$. This follows from the definition of $m$ in step 4, since $m \leq -x$ for all $x \in E$, which is equivalent to $x \leq -m$. Therefore, $-m$ is the supremum of $E$.




---
### Theorem: $\mathbb{Q}$ is not continuous
- To prove this, we can use the fact that there exist irrational numbers between any two distinct rational numbers. 
- Suppose $a,b$ are two distinct rational numbers, with $a < b$. We need to show there exist an irrational number $x$ such that $a < x < b$. 
- There exists some irrational numbers in between two rational numbers, such as $a,b = 1,2$. and $x = \sqrt{2}$. This contradicts 
- thus $\mathbb{Q}$ is not continuous.

---
### Theorem: prove that $\mathbb{Q}$ does not have the least upper bound property
- To prove that $\mathbb{Q}$ does not have the least upper bound property, we need to find a subset of $\mathbb{Q}$ that has an upper bound but no least upper bound in $\mathbb{Q}$.

- Consider the subset $E={q\in\mathbb{Q} : q^2 < 2}$. Clearly, $S$ is bounded above by the real number $\sqrt{2}$, since for any $q\in S$, we have $q<\sqrt{2}$.

- what is rational number $\mathbb{Q}$?
	- $\mathbb{Q} = \{ \frac{m}{n}, m,n \in \mathbb{Z}, n \neq 0 \dots \}$

- What is upper bound?
	- Let $E \subset S$, where $S$ is an ordered set. If $\exists b \in S$, $\forall x \in E(x \leq b)$, then $b$ is an upper bound of $E$.

- What is least upper bound?
	- If there exists an upper bound $b_0$ of $E$ such that whenever $b$ is any upper bound for $E$, we have $b_0 \leq b$, then $b_0$ is called the least upper bound or the supremum of $E$. We write $supE = b_0$

- bounded above:
	- it is a kind of description that describing a set $S$ that we can always find an upper bound $a$ such that $\forall x \in S, x < a$.
	- Discuss $\mathbb{Z}, \mathbb{R}, \mathbb{N}, \mathbb{Q}$ are whether bounded above:
		- $\mathbb{N}$: It is not bounded above or below
			- For any natural number $n$, you can always find a larger natural number $n+1$
		- $\mathbb{Z}$: It is unbounded above or below
			- For any integer $n$, you can always find a larger integer $n+1$
		- $\mathbb{Q}$: It is not bounded above or below
			- Say $c = \frac{a}{b}$, where $c$ represents rational number, $a, b$ are integer. 
			- To find a larger integer, we need to increase $a$ while keeping $b$ fixed. 
			- Since $a \in \mathbb{Z}$, we can always find a larger integer that is bigger than $a$. 
		- $\mathbb{R}$: It is unbounded above or below

- Q: if we have open bounded, well-ordered, and has the property of being bounded above with an existing upper bound, can we flipping the set(multiplying all elements by -1), result in a set that is bounded below with existing lower bound?
- A: Yes. 
	- Before flipping, say we have a upper bound $b$ such that $\forall x \in S, x \leq b$. 
	- After multiplying all elements with $-1$, we obtain a new set with all the elements negated. We call this set $S'$. 
	- Since $\forall x \in S, x \leq b$, it follows that $\forall x \in S', x \geq -b$. Therefore, $-b$ serves as an lower bound for the set $S'$. 
	- Well-ordering property states that every non-empty subset of the set has a least element. This property holds for the original set and the negated set. 
	- 

- Make an assumption and least upper bound $s \geq \sqrt{2}$
	- Suppose $\mathbb{Q}$ has the least upper bound property, then $S$ has a least upper bound $s\in\mathbb{Q}$. Since $S$ is bounded above by $\sqrt{2}$, we have $s\geq \sqrt{2}$.

- To prove $s \geq \sqrt{2}$, we tries to prove the opposite is wrong ($s < \sqrt{2}$)
	- If $s<\sqrt{2}$, then we can find a rational number $r$ such that $s<r<\sqrt{2}$. 
		- To see this, note that since $s<\sqrt{2}$, we can find a positive rational number $p$ such that $s+p^2<\sqrt{2}$ (for example, take $p=\frac{\sqrt{2}-s}{2}$). 
		- Then, we can choose a rational number $r$ such that $s<p<r$ (for example, choose $r=\frac{2ps+p^2}{2ps}$). It follows that $r\in S$ and $r>s$, contradicting the assumption that $s$ is an upper bound of $S$. Therefore, we must have $s=\sqrt{2}$.
		- So we prove $s \geq \sqrt{2}$

- To prove $s = \sqrt{2}$ is not upper bound of $E$. 
	- $\sqrt{2} \notin \mathbb{Q}$, which means $s = \sqrt{2}$ could not be a upper bound of $S$ because $\sqrt{2} \notin S$. 
	- Therefore, $supE > b_0 = \sqrt{2}$. 
	- And any value exceeding $\sqrt{2}$ is not a member of $E$. Therefore, $\mathbb{Q}$ does not have least upper boundary property.


---
### Theorem 27: If $x \in \mathbb{Q}$ and $x = sup\{q \in \mathbb{Q} \mid q > 0, q^2 < 2\}$, then $x>0 \land x^2 =2$. 


- Theorem: if $x \in \mathbb{Q}$ and $x = supE = sup\{ q \in \mathbb{Q} | q > 0 \land q^2 < 2\}$, then $x \geq 1$ and $x^2  = 2$ 
	- If $x \in E$, then $x$ is not an upper bound of $E$ because there exists a larger rational number also belongs to $E$. 
	- If $x \notin E$, then there exists a smaller rational number that belongs to $E$ and its also an upper bound of $E$. 
	- Therefore, $x$ cannot be a supremum of $E \in \mathbb{Q}$. 
	- Proof by contradiction:
		- Let $E = \{ q \in \mathbb{Q} | q > 0 \land q^2 < 2\}$
		- Suppose $x \in \mathbb{Q}$ and $x = supE = sup\{ q \in \mathbb{Q} \mid q > 0 \land q^2 < 2\}$, then $x \geq 1$ and $x^2  = 2$ 
		- Show $x \geq 1$: 
			- since the fact that 
				- $1 \in E$ (which we knows that by searching the area near $(0,2) \in \mathbb{Q})$, 
				- $x = supE$ (The theorem mentioned that in its definition.)
			- meaning it is an upper bound for $E$, it must be bigger or equal to everything on $E$.  That implies $1 \leq x \implies x > 0$ 
		- Show $x^2 = 2$:
			- Trick: show equality by showing 2 inequalities are true.
			- Prove $x^2 \geq 2$:
				- Define $h = min\{\frac{1}{2}, \frac{2 -  x^2}{2(2x+1)}\} < 1$, if $x^2 < 2$
				- We prove $x^2 \geq 2$ by contradiction. 
					- So we assume $x < 2$ and $x = supE$. 
				- We compute:
					- $\begin{align*}(x+h)^2 &= x^2 + 2xh + h^2 \\ &< x^2 + 2xh + h &\text{, (because h<1)} \\ &= x^2 + (2x+1)h \\ &< x^2 + (2x+1) \frac{2-x^2}{2(2x+1)} < x^2 + 2 - x^2 &\text{, (because we assumed x < 2)} \\ &< 2\end{align*}$ 
				- $\implies x+h < \sqrt{2} \implies (x+h) \in E \implies x \neq supE$ 
					- ( it is because $b_0$ is not an upper bound if $\exists x \in E$ such that $x > b_0$ )
					- And $x + h \in E$, which means $x$ is not $supE$, which is a contradiction to our assumptions. 
			- Prove $x^2 \leq 2$:
				- assume $x > 2$ and $x = supE$. 
				- ...
				- $(x - h)^2 >2$ 
				- Then $q^2 < 2 < (x-h)^2 \implies (x-h)^2 - q^2 > 0$
				- $[(x-h)+q][(x-h)-q] > 0 \implies (x-h)-q >0$
				- Thus $\forall q \in E$, we have $(x-h)$ to be upper bound for $E$. While $x \in E \land h>0 \implies (x - h) \in E$ 
				- And $(x - h) < x$ while $(x-h)$ is an upper bound for $E$. That implies $x \neq supE$.
				- Thus the assumption of $x > 2$ is false. 
				- Thus $x^2 \leq 2$.
			- We have $x^2 \geq 2$ and $x^2 \leq 2$, thus $x = 2$. 

---

### Theorem 28: The set $E = \{ q \in \mathbb{Q} \mid q > 0, q^2 < 2\}$ does not have a supremum in $\mathbb{Q}$. 

- In theorem 27, it only states that supremum of $E$ exists and equals to $\sqrt{2}$, but it does not prove that there is no supremum of $E$ in rational numbers. 
- To prove theorem 28, one needs to use the fact that the rational numbers are not complete and and construct a sequence of rational numbers that approaches the supremum of $E$ but does not converge to a rational number, which requires a different argument than the one used to prove theorem 27.

- Say $\exists m,n \in \mathbb{N}$ such that $m > n$ and $x = \frac{m}{n}$. 
	- Don't mess up $x$, here,  $x \notin \mathbb{Q}$ and $x \notin \mathbb{N}$
		- Recall $\mathbb{Q} = \frac{m}{n}$, and $m, n \in \mathbb{Z}$ 
		- And $x = \frac{m}{n}$ and $m,n \in \mathbb{N}$
- Let $S = \{ k \in \mathbb{N} \mid kx \in \mathbb{N} \}$
	- $S \neq \emptyset$ since $n \in S$. (We can see $n \in S$ by showing $n$ fulfills $S$'s description because we substitute $k$ into $S$'s notation, $nx = m$, which shows $n$ fulfills $S$'s description.)
- By well-ordering property of $\mathbb{N}$, $S$ has a least element $k_0 \in S$.
- Our strategy of proving the theorem is, showing $k_0$ is not the least element in $S$. 
- Let $k_1 = k_0 x - k_0 \in \mathbb{Z}$, then $k_1 = k_0(x - 1) > 0$ since $k_0 \in \mathbb{N}$ and $x > 1$. 
	- why $k_1 \in \mathbb{Z}$?
		- It is because $k_0 x, k_0 \in \mathbb{N}$ 
- Now $x^2 = 2 \implies x < 2$
- So $k_1 = k_0(x - 1) < k_0(2-1)$, which means $k_1 < k_0$. 
	- by the fact that $x < 2, so $k_1$ is bounded by $k_0(2-1)$.
- So $0 < k_1 < k_0$,
- So $k_0 < k_1$ and $k_1 \in \mathbb{N} \implies k_1 \notin \mathbb{S}$,  as $k_0$ is the least element of $S$. 

- But, $x k_1 = k_0 x^2 - x k_0 = 2 k_0 - x k_0 = k_0 - k_1 \in \mathbb{N}$. 
- $x k_1 \in \mathbb{N}$ $\implies k_1 \in S$ and $k_1 < k_0$

- Thus, $k_0$ is not the least element of $S$. 
- Thus $\nexists x \in \mathbb{Q}$  such that $x = sup E$. 


---
### Prime factorization

- Say $\exists m,n \in \mathbb{N}$, $gcd(m,n)$ not always equal to $1$. So how we can write it in more general form?
- Use the prime factorization of $a$ and $b$. Specifically,
- $a = p_1^{a_1} p_2^{a_2} \dots p_k^{a_k}$ and $b = p_1^{b_1} p_2^{b_2} \dots p_k^{b_k}$, where $p_1, p_2, \dots, p_k$ are distinct primes (but the value of $p_k$ is the same across $a,b$) and $a_i, b_i \geq 0$ for $i = 1,2, \dots k$.
- Then $gcd(a,b) = p_1^{min(a_1, b_1)}  p_2^{min(a_2, b_2)}, \dots  p_k^{min(a_k, b_k)}$
	- We can see that $a_k$ and $b_k$ are acting as "the appearance of some distinct primes". If there is a prime $p_a$ that $a$ has, and $b$ don't, then $p_a$ would appear in $b$ in the form of $p_a^0$, which basically equals to $1$. 
- eg: $12 = 2 \cdot 2 \cdot 3$ and $18 = 2 \cdot 3 \cdot 3$. 
- Then $gcd(a,b) = 2^{min(2,1)} \cdot 3^{min(1,2)} = 2 \cdot 3 = 6$



---
## Lecture 4 - The characterization of the real numbers


### Field
- A set $F$ is a field if it has two operations: addition and multiplication with the following properties:
	- Properties:
		- Addition
			- (Closure)
				- if $x,y \in F$, then $x + y \in F$
			- (Commutativity) 
				- $\forall x,y \in F, x+y = y+x$.
			- (Associativity) 
				- $\forall x,y,z \in F, (x+y)+z = x +(y+z)$
			- (Identity)
				- $\exists$ an element $0 \in F$ such that $0+x = x = x+0$
			- (Additive inverse)
				- $\forall x \in F, \exists y \in F$ such that $x+y = 0$. We denote $y = -x$. 
		- Multiplication
			- (Closure)
				- If $x,y \in F$, then $x \cdot y \in F$.
			- (Commutativity) 
				- $\forall x,y \in F$, $x \cdot y = y \cdot x$.
			- (Associativity) 
				- $\forall x,y,z \in F, (x,y) \cdot z = x \cdot (y \cdot z)$
			- (Identity)
				- $\exists 1 \in F$ such that $1 \cdot x = x = x \cdot 1$ for all $x \in F$.
			- (Multiplicative inverse)
				- $\forall x \in F \setminus \{0\}, \exists x^{-1}$ such that $x \cdot x^{-1} = 1$. 
		- (Distributivity) $\forall x,y,z \in F, (x+y)z = xz + yz$. 
	- Examples
		- $\mathbb{Q}$ is an example of field
	- Non-example
		- $\mathbb{Z}_2 = \{ 0,1\}$, where $1+1=0$.  
		- $\mathbb{Z}_3 = \{ 0,1,2\}$, where $c: a + b (mod 3)$.
		- These finite fields could produce an output that is outside of the boundary of the field. So we need to define for the behaviors if those cases is happening.

- Q:
	- while these finite fields don't satisfies all properties of "fields", why we still call them with the word "fields"? so confusing
- A: 
	- It is true that finite fields do not satisfy all of the properties that we usually associate with fields, such as the property of being infinite. However, the term "field" is used to refer to these structures because they share many of the important properties of fields, such as the existence of addition, multiplication, additive and multiplicative inverses, and the distributive law. 

---

### Theorem 32: If $x \in F$ where $F$ is a field, $0x = 0$.
- Learning objective:
	- To deploy the axioms of a field to prove such claims. 
- Proof:
	- $\begin{align*}0 &= 0 \cdot x  + (- 0 \cdot x) &\text{(every element has an additive inverse)} \\ &= (0+0) \cdot x  + (- 0 \cdot x) \\ &= 0x+0x   + (- 0 \cdot x) &\text{(distributive law)} \\ &= 0x \end{align*}$

---
### Ordered field
- A field $F$ is an ordered field if $F$ is also an ordered set with ordering $<$ and
	- (i) $\forall x,y,z \in F, x < y \implies x + z < y + z$.
	- (ii) If $x > 0$ and $y > 0$ then $xy > 0$.
- If $x > 0$ ($x \geq 0$) we say $x$ is positive (non-negative). 
- Example:
	- $\mathbb{Q}$ is an ordered field
- Non-example:
	- $\mathbb{Z}_2$: $\{ 0,1\}$:
		- consider $0 < 1$, then $1+0 < 1+1 = 0 \implies 1 < 0$ which leads to contradiction.
	- In general, there are no "finite ordered field". 

### Theorem 35: If $x > 0$, then $- x < 0$
- Learning objective:
	- Apply the definition of "ordered field" to prove such claims
- proof:
	- If $x \in F$, and $x > 0$, then $x -x > 0-x \implies 0 > -x$

### Proposition 1.1.8 Standard inequality manipulation
![[Pasted image 20230508053341.png|400]]


### Theorem: Let $F$ be an ordered field with the least upper bound property. Then if $A \subset F$, $A \neq \emptyset$ and bounded below, then $inf A$ exists in $F$. 

- Properties of field:
	- Supports field axioms, those are additions and multiplications with closure, commutativity, associativity, identity and inverse property.
- Properties of ordered field:
	- A field $F$ is an ordered field if $F$ is also an ordered set with ordering $<$ and
		- (i) $\forall x,y,z \in F, x < y \implies x + z < y + z$.
		- (ii) If $x > 0$ and $y > 0$ then $xy > 0$.
- Intuition:
	- Draw like $F$ is a number line.
	- Set $A$ is a part of $F$. 
	- Set $-A$ is the set of elements that are the additive inverses of $A$. 
	- Set $-A$ has least upper bound, as $-A \subset F$. 
	- Flip $-A$ back. $A$ has greatest lower bound property.
- Proof of the theorem:
	- We have $F$ is an ordered field with least upper bound property. $A \subset F$ and $A \neq \emptyset$. 
	- Suppose $A$ bounded below. 
	- Let $-A = \{ x \in A\}$
	- Show existence of supremum in $-A$
		- Let $b$ is an arbitrary lower bound of $A$, then $-b$ is an upper bound for $-A$
		- $-b \in F$ since $F$ is a field. 
			- By explicitly states this, we emphasize $-b$ is a valid element in the field $F$ and operation s of $F$ can be applied to $-b$ as well.
			- We need to show $i \leq j$ later using the operation of $F$ (namely, the addition and multiplication.) 
		- $\exists b \in F$ such that $\forall a \in A$ $b \leq a$ 
		- Then $\forall a \in A, b \leq a \implies \forall a \in A, -a \leq -b \implies$ $-b$ is an upper bound for $-A$. 
	- Show $-c$ is a lower bound of $A$
		- Let $c = sup(-A)$, show $-c$ is a lower bound for $A$
		- $c \in F$ since $F$ is a field (why we need to state that?)
		- Since $F$ has the least upper bound property, $\exists c \in F$ such that $c = sup(-A)$. 
		- Show $-c$ is the infimum of the set $A$: 
		- Then $\forall a \in A, -a \leq c \implies \forall a \in A, -c \leq a$ which means $-c$ is a lower bound for $A$. 
	- Show $inf(A)$ exists and $inf(A) = sup(-A)$
		- Let $y$ is a lower bound for $A$, show $c = inf(A)$. 
		- Show that if $y$ is a lower bound for $A$, then $y \leq -c$. Where $-c$ is the greatest lower bound for $A$. 
		- Let $y$ be a lower bound for $A$, then $-y$ is an upper bound for $-A$, implies $c \leq -y$ since $c = sup(-A) \implies y \leq -c$.
		- Hence, $inf(A)$ exists in $F$ and $inf(A) = sup(-A)$

### Theorem 39: There exists a "unique" ordered field, labeled $\mathbb{K}$, such that $\mathbb{Q} \subset \mathbb{K}$ and $\mathbb{K}$ has the least upper bound property
- "Unique" up to isomorphism. Isomorphism is a fancy way of saying what you call apples I call manzanas. 
- Background:
	- Start off in ancient times with the natural numbers $\mathbb{N}$. 
	- Then move to the integers $\mathbb{Z}$ so that we can take additive inverses, although they didn't call them that. and we wanted $0$.
	- Then we moved to rational numbers $\mathbb{Q}$ because we didn't have ways to solve equations $2x + 1 = 0$. 
	- Then we moved on from $\mathbb{Q}$ to $\mathbb{R}$ essentially because we can't solve $x^2 -2 = 0$. The inability of solving $x^2 - 2 = 0$ means that $\mathbb{Q}$ is incomplete as an ordered set. $\mathbb{Q}$ does not have the least upper bound property.
	- What characterizes $\mathbb{R}$ is that it is an ordered field containing $\mathbb{Q}$, and it is a unique one that has the least upper bound property.
- Proof:
	- One can construct $\mathbb{K}$ using Dedekind cuts or as equivalence classes of Cauchy sequences. (We will define Cauchy sequences later in the course.)


### Theorem 40: $\exists ! r \in \mathbb{R}$ such that $r > 0$ and $r^2 = 2$. In other words, $\sqrt{2} \in \mathbb{R}$ but $\sqrt{2} \notin \mathbb{Q}$
- If $r$ is not unique, then there would be two distinct positive real number $r_1$ and $r_2$ with $r_1^2=2$ and $r_2^2 =2$. 
- The proof established the existence and uniqueness of a positive real number $r$ such that $r^2 = 2$. 
	- This means $\sqrt{2}$ exists in real numbers, but this number cannot be expressed as a ratio of two integers, otherwise it would contradicts the assumption that $r$ is the supremum of the set $E$ defined in the proof.
- Show existence
	- By constructing the set $E$ as the set of all positive real numbers whose squares are less than $2$, the proof shows that $r$ is the least upper bound of $E$, hence it satisfies $r^2 = 2$. 
		- Q: Do we need $r \in E$ to state $r = supE$?   
		- A: No. It is not necessary. Upper bound means $\forall x \in E, x \leq r$. Least upper bound means for any other upper bound $b$, least upper bound $b_0$ holds $b_0 \leq b$  for all $b$. 
	- The completeness property of $\mathbb{R}$ guarantees that every non-empty set that is bounded above has a least upper bound.
- Show uniqueness:
	- It is established by assuming the existence of another positive real number $\bar r$ that also satisfies $r^2=2$. And then shows $\bar r = r$. 
- Proof:
	- Let $E = \{ x \in \mathbb{R} \mid x > 0 \land x^2 < 2\}$, since $E$ is bounded above, we have $r:= supE$ exists in $\mathbb{R}$. Then one can show $r >0$ and $r^2 = 2$. 
	- Proof $r$ is unique (since we have mentioned $\exists !$):
		- Suppose there is $\bar r > 0$ with $\bar r^2 = 2$. Then $(r + \bar r)>0$
		- 0 = $\bar r^2 - r^2$ (since both $r^2 = 2$ and $\bar r^2 = 2$)
		- $(r + \bar r)(r - \bar r) = 0$
		- implies $r = \bar r$





---

## Lecture 5 - Archimedean property, density of the rationals, absolute value

## Real numbers

- What is $\mathbb{R}$?
	- There exists a unique ordered field, containing $\mathbb{Q}$ with the least upper bound property, which we denote by $\mathbb{R}$.
	- Simple fact:
		- If $x,y \in \mathbb{R}$, and $x < y$, then $\exists r \in \mathbb{N}$ such that $x < r < y$. For example, $r = \frac{x+y}{2}$
	- Q1:
		- It will be proved that $\mathbb{Q}$ does not have the least upper bound property. So what is the meaning of $\mathbb{R}$ is an ordered field containing $\mathbb{Q}$ with the least upper bound property? 
	- A1:
		- We knows it after understanding "what is ordered field" and "what is least upper bound property".
	- Q2:
		- why we would associate "least upper bound property" with the definition of $\mathbb{R}$? I can suggest it is unnecessary, or if it is necessary, I can add a lot of other property to the definition to make it very long.
	- A2:
		- The least upper bound property is a fundamental and distinguishing property of the real numbers that sets them apart from other number systems like the rational numbers. It captures a key feature of the real numbers that makes them useful for mathematical analysis and modeling of the physical world.
		- While it is true that there are other properties of the real numbers are important, such as completeness, order, and algebraic properties. The least upper bound property is a key defining characteristic that distinguishes the real numbers from other number systems. 

### Archimedean property
- Motivation:
	- Archimedean property provides a fundamental; connection between the natural numbers and the real numbers. 
	- While it is true that we can directly prove that both the set of natural numbers ($\mathbb{N}$) and the set of real numbers ($\mathbb{R}$) are not bounded above, the Archimedean property offers a more general and powerful statement.
	- It shows that the natural number can "catch up" to any real number when multiplied by a sufficiently large factor. By understanding the Archimedean property, we gain insight into the behavior and structure of the real numbers. 
	- It allows us to prove important results such as the unboundedness of sequences, the density of rational numbers in the real numbers, and the existence of limits in calculus.
	- It establishes a bridge between the discrete nature of the natural numbers and the continuous nature of the real numbers. 
	- Archimedean property captures the idea of there are no infinitely large positive real number. 
- Definition:
	- If $x,y \in R$ and $x > 0$, then $\exists n \in \mathbb{N}$ such that $nx > y$, or in other words, $n > \frac{y}{x}$
	- Note: 
		- When applying Archimedean property, we just need to make sure the natural number $n \in \mathbb{N}$ is sticking with a positive real number $x$. $x$ and $y$ could exists in any forms, such as $y-x$, $\frac{a}{b}$, or any constants, $10$ etc. It does not matter. 
		- We can also state $\exists n \in \mathbb{N}, \forall x \in \mathbb{R}, n > x$ but we should appreciate $nx > y$ is a more general statement of Archimedean property, which already included the case of $n > x$. 
- In other words:
	- The verbal explanation for "If $x,y \in R$ and $x > 0$, then $\exists n \in \mathbb{N}$ such that $nx > y$" is, 
		- Say we are comparing two real numbers $x$ and $y$. And if we are picking a positive real number at hand, there exists a natural number multiplier to make one real number greater than another real number. 
	-  The verbal explanation for "$\forall \frac{y}{x} \in \mathbb{R}, t:= \frac{y}{x}$, we can find $n \in \mathbb{N}$ such that $n > t$. " is,
		- Expressing the same concept above. 
- More applications:
	- Archimedean structure
		- An algebraic structure in which any two non-zero elements are comparable, in a sense that neither of them is infinitesimal with respect to the other, is said to be Archimedean.
		- eg: Archimedean group = a linear ordered group that is Archimedean. 
	- Non Archimedean structure
		- A structure which has a pair of non-zero elements, one of which is infinitesimal with respect to the other, is said to be non-Archimedean. 
- Trick of proof:
	- Note that the quantifier of the statement would change during negation of the statement:
		- original statement: $\forall x,y \in \mathbb{R}, \exists n \in \mathbb{N},n > \frac{y}{x}$
		- negate it, it becomes $\exists x,y \in \mathbb{R}, \forall n \in \mathbb{N}, n \leq \frac{y}{x}$
	- Thus change in quantifiers is a result of De Morgan's laws and the negation of quantified statements. 
- Proof:
	- Suppose, for the sake of contradiction, the above statement is false, which means "natural number $\mathbb{N} \subset \mathbb{R}$ is bounded above", then $\forall n \in \mathbb{N}, n \leq \frac{y}{x}, \frac{y}{x} \in \mathbb{R}$. Let $\mathbb{N}$ has supremum $\exists a = sup \mathbb{N} \in \mathbb{R}$.
	- Since $a$ is the least upper bound for $\mathbb{N}$, $a - 1$ cannot be an upper bound for $\mathbb{N}$, then we have $\exists m \in \mathbb{N}$ such that $a - 1 < m$
	- $a - 1 < m \implies a < m+1 \in \mathbb{N}$
		-  $m+1 \in \mathbb{N}$ and it is greater than the least upper bound $a$. This is a contradiction.
	- Thus, we falsified this assumption and proved Archimedean property: $\exists n \in \mathbb{N}$ such that $n \geq \frac{y}{x}$
- Try to do it in opposite way:
	- $\forall n \in \mathbb{N}, n \leq \frac{y}{x}$. In other words, $\mathbb{N}$ is bounded under $\frac{y}{x}$
	- $\exists b = inf\mathbb{N} \in \mathbb{R}$
	- Since $b$ is the greatest lower bound for $\mathbb{N}$, $b+1$ cannot be lower bound for $\mathbb{N}$
	- Hence, $\exists k \in \mathbb{N}$ such that $b+1 > k \implies b > k -1 \in \mathbb{N}$



###  $\mathbb{Q}$ density property in $\mathbb{R}$
- If $x,y \in \mathbb{R}$ and $x < y$, then $\exists r \in \mathbb{Q}$ such that $x < r < y$. 
- Proof:
	- With $x,y \in \mathbb{R}$ and $x < y$, we have 3 cases:
		- $0 \leq x < y$
		- $x < 0 < y$
		- $x < y \leq 0$
	- For the second case, we take $r = 0 \in \mathbb{Q}$. 
	- Recall Archimedean property (AP) we have: If $x,y \in \mathbb{R}$ and $x > 0$, then $\exists n \in \mathbb{N}$ such that $nx >y$. 
	- Applying AP with replacing $x$ and $y$:
		- Replacing $x$ with $y-x$ (both are real numbers), $y$ with $1$ (both are real numbers), we have:  $\exists n \in \mathbb{N}, n(y-x) > 1$. 
	- Applying AP with replacing $n$ with $l$ (both are natural numbers), $x$ with $1$ (both are real numbers), $y$ with $nx$ (both are real numbers), we have: $\exists l \in \mathbb{N}, l > nx$. 
	- Consider the set $S = \{ k \in \mathbb{N} \mid k > nx\}$
	- By well ordering property of $\mathbb{N}$, $S$ has a least element $m$ and $m >nx \implies x < \frac{m}{n} \in \mathbb{Q}$
	- Since $m - 1 \notin S$, $m - 1 \leq nx$, 


### Theorem 45: Suppose $S \subset \mathbb{R}$ is non empty and bounded above. Then $x = sup S$ $\iff$ 1,2 (1: $x$ is an upper bound for $S$, 2: $\forall \epsilon > 0, \exists y \in S$ such that $x - \epsilon < y \leq x$. 

### Theorem 44: $1 = sup\{ 1 - \frac{1}{n} \mid n \in \mathbb{N}\}$
- Let $A :=\{ 1 - \frac{1}{n} \mid n \in \mathbb{N}\}$.  
- $1 = sup\{ 1 - \frac{1}{n} \mid n \in \mathbb{N}\}$ implies 1 is an upper bound of this set so infimum $b:=supA$ exists. 
- Suppose $x$ is an upper bound for this set and  $x \geq 1$.
- For the sake of contradiction, assume $x < 1$
- Recall Archimedean property (AP) we have: If $x,y \in \mathbb{R}$ and $x > 0$, then $\exists n \in \mathbb{N}$ such that $nx >y$. 
- By Archimedean property,  $\exists n \in \mathbb{N}, 1 < n(1-x)$, which replacing $x$ with $(1-x)$, $y$ with $1$ in the original statement. 

### Corollary 1.2.5 $inf\{ \frac{1}{n} \mid n \in \mathbb{N} \} = 0$
- Let $A :=  \{ \frac{1}{n} \mid n \in \mathbb{N} \}$.
- Furthermore, $\frac{1}{n} > 0$ so $0$ is a lower bound and $b := infA$ exists. 
- Also we have $b \geq 0$
- Taking an arbitrary $a > 0$, with Archimedean property of $\mathbb{R}$, $\forall a, \exists n \in \mathbb{N},na > 1$, or in other words $a > \frac{1}{n} \in A$.
- So $a$ cannot be a lower bound for $A$. 
- Hence $b = 0$, 

### Absolute value
- Definition
	- If $x \in \mathbb{R}$ we define
		- $|x| := \begin{cases}x, & x \geq 0  \\ -x & x \leq 0 \end{cases}$
- Theorems:
	- 1. $|x| \leq 0$ and $|x| = 0 \iff x = 0$
	- 2. $\forall x \in \mathbb{R}$, $|-x| = |x|$
	- 3. $\forall x,y \in \mathbb{R}$, $|xy| = |x| |y|$
	- 4. $|x^2| = x^2 = |x|^2$
	- 5. If $x,y \in \mathbb{R}$, then $|x| \leq y \iff -y \leq x \leq y$
	- 6. $\forall x \in \mathbb{R}$, $x \leq |x|$


- Proofs of theorems:
	- Most theorems below are proven by cases. 
	- $|x| \leq 0$ and $|x| = 0 \iff x = 0$
		- Part 1
			- If $x \geq 0$, then $|x| = x \geq 0$ ($|x| = x$ is based on the definition of absolute value)
			- If $x \leq 0$, then $|x| = -x \geq 0$ (the first part is based on the definition of $|x|$, the second part is based on $x \leq 0$)
			- Thus, $|x| \geq 0$
		- Part 2
			- Suppose $x = 0$, then $|x| = x = 0$
			- Suppose $|x| = 0$, 
				- if $x \geq 0 \implies x = |x| = 0$
				- if $x \leq 0 \implies -x = |x| = 0$
			- Therefore $x = 0 \iff |x| = 0$
	- $\forall x \in \mathbb{R}$, $|-x| = |x|$
		- If $x \geq 0$, then $-x \leq 0$. Thus $|x| = x = -(-x) = |-x|$
			- The first equal sign is based on definition
			- The second equal sign is extracting a $-x$ from the expression
			- The third equal sign is applying the extension property of $x \geq 0$, which is $-x \leq 0$, and then using the definition of $|x|$ we have $-(-x) = |-x|$
		- If $x \leq 0$, then $(-x) \geq 0$. Thus $|-x| = -x = |x|$
			- The first equal sign treat "-x" as a new variable. $(-x) \geq 0$ thus when removing the absolute sign, $|-x| = -x$ holds. 
			- The second equal sign treats $x$ as the variable and use the absolute value definition to box it into the sign again. 
		- What is the difficulty of doing this proof?
			- We might stuck on "absolute of a negative value should return a positive number", such as $|-5| = 5$, then we cannot understand $|-x| = -x$
	- $\forall x,y \in \mathbb{R}$, $|xy| = |x| |y|$
		- If ($x \geq 0$ and $y \geq 0$),  or ($x \leq 0$ and $y \leq 0$), then $xy \geq 0$ and $|xy| = xy = |x||y|$.
		- If ($x \leq 0$ and $y \geq 0$) or ($x \geq 0$ and $y \leq 0$), then $xy \leq 0$ and $|xy| = -xy = |x||y|$ 
			- The first equal sign $|xy| = -xy$ is refer to the definition of the absolute value when the variable is negative. 
			- The second equal sign $-xy = |x||y|$ is refer to either $x$ or $y$ is negative. In that case, it would produce a negative sign outside. 
	- $|x^2| = x^2 = |x|^2$
		- Take $x = y$ in theorem 3. Then $|x^2| = |x|^2$. Since $x^2 \geq 0$, it follows $|x^2| = x^2$, which is based on the definition of absolute value. 
	- If $x,y \in \mathbb{R}$, then $|x| \leq y \iff -y \leq x \leq y$
		- Suppose $|x| \leq y$. 
			- If $x \geq 0$, we have $|x| \equiv x$. Our previous conditions becomes $x \leq y \implies x \geq -y$. Combining $x \leq y$ and $x \geq -y$, we have $-y \leq x \leq y$. 
			- If $x \leq 0$ (also implies $-x \geq 0$), we have $|x| \equiv -x$. Our previous condition $|x| \leq y \implies -x \leq y \implies x \geq -y$. So we have $-y \leq x \leq -x \leq y \implies -y \leq x \leq y$. 
		- Suppose $-y \leq x \leq y$
			- We have $x \geq -y$ and $x \leq y$
				- If $x \geq 0$
					- $x \leq y \implies |x| \leq y$
				- If $x \leq 0$
					- $x \geq -y \implies -x \leq y \implies |x| \leq y$
	- $\forall x \in \mathbb{R}$, $x \leq |x|$
		- Take $y = |x|$ in theorem 5.


---

---
# Lecture 6   Uncountability of the real numbers

### Triangle inequality ($\Delta\text{-inequality}$)
- $\forall x,y \in \mathbb{R}, |x+y| \leq |x| + |y|$
	- Proof:
		- We have $x + y \leq |x| + |y|$, by theorem 6 above ($x \leq |x|$)
		- We have $(-x) + (-y) \leq |-x| + |-y|$, by theorem 6 above again ($x \leq |x|$)
		- $(-x) + (-y) \leq |-x| + |-y| \implies (-x) + (-y)$, by theorem 2 of above ($|-x| = |x|$)
		- $(-x) + (-y) \leq |x| + |y| \implies -(|x| +|y|) \leq x+y$
		- Thus we have $-(|x| +|y|) \leq x+y \leq |x| + |y|$
		- And  $-(|x| +|y|) \leq x+y \leq |x| + |y| \implies |x + y| \leq |x| + |y|$ (By theorem 5 -- If $x,y \in \mathbb{R}$, then $|x| \leq y \iff -y \leq x \leq y$)

### Decimal expansion
- We can think of $\mathbb{Q}$ as decimal expansions. In other words, $x \in \mathbb{Q}$ as being in the form $x = 10^k d_k + \dots + 10d_1 + d_0 + 10^{-1}d_{-1} + \dots + 10^{-M} d_{-M}$
- eg:
	- The decimal expansion of $0.5$ is $0.4999 \dots$ 
	- Proof: 
		- $10x = 4.999 \dots$
		- $x = 0.4999 \dots$
		- $9x = 4.5$
		- $x = \frac{9}{18} = 0.5$


### Cantor uncountable theorem: $(0,1]$ is uncountable
- We prove this through contradiction.
	- $(0,1]$ is countable so there exists a bijection $x: \mathbb{N} \rightarrow (0,1]$
	- Also we can list all the elements of $(0,1]$ in a sequence, denoted by $x_1, x_2, x_3, \dots$. 
		- $x(n) = 0 \cdot d_{-1}^{(n)} d_{-2}^{(n)}\dots$
	- We construct $y \in (0,1]$ such that $y$ is not in the range of $x$. 
		- We define $y$ as, $i^{\text{th}}$ decimal place of $y$ is different from the $i^{\text{th}}$ decimal place of $x_i$. In other words, the $i^{\text{th}}$ of $y$ is not equal to $9$ if $i^{\text{th}}$ decimal place of $x_i$ is $9$.
		- By constructing $y$ in this way, we ensure that $y$ differs from every number in the sequence $x_1, x_2, x_3, \dots$. 
		- Therefore $y$ cannot be in the list. 

### Sequences
- Definition
	- 1. Natural numbers indexed
		- A sequence of real number is a function $x: \mathbb{N} \rightarrow \mathbb{R}$. 
		- A sequence is defined as a function that maps the natural numbers $\mathbb{N}$ (or a subset of the natural number $\mathbb{N}$) to a set of elements. Therefore, in order for a collection of values to be considered a sequence, it must be indexed by the natural numbers. 
		- If you have a collection of values that is indexed by a set, other than the natural numbers, it would not be considered a sequence in the context of real analysis. 
	- 2. pointing to real number elements
		- While the index of a sequence is natural number, the value of each element of the sequence can be any real numbers. 
- Notations
	- We denote the $n^{\text{th}}$ element of the sequence as $x(n) = x_n$ 
	- we denote the sequence by $\{ x_n \}_{n=1}^\infty$, $\{ x_n \}$, or$x_1, x_2, \dots$
- A sequence is different from a set:
	- While $-1, 1, -1, 1, \dots = \{ (-1)^n \}_{n=1}^\infty$ is a sequence,
	- $\{(-1)^n| n \in \mathbb{N} \} = \{ -1, 1\}$  is a set. 


### Bounded sequence
- A sequence $\{ x_n \}$ is bounded if $\exists B \geq 0$ such that $\forall n$, $|x_n| \leq B$.  
- eg:
	- $x_n = \frac{1}{n}$ is bounded, since $|\frac{1}{n}| \leq 1$ for all $n \in \mathbb{N}$
	- However, $x_n = n$ is not bounded.

### Limit
- Properties
	- 1. Only exists with convergent sequence
		- Limits exists only when we are talking about convergent sequence. If that sequence is approaching the number $x$, then it is said to be the limit of $\{x_n\}$
	- 2. A fact about limit
		- $\underset{n \rightarrow \infty}{lim} x_n = x \iff \underset{n \rightarrow \infty}{lim} |x_n - x| = 0$
		- Proof:
			- We can make use of the definition of the limit, to see two sides of limit (LHS = RHS) actually meaning the same thing.
			- Recall limits exists only when we are talking about convergent sequence. And the definition of convergent sequence is to a number $x \in \mathbb{R}$, if $\forall \epsilon > 0$, $\exists M \in \mathbb{N}$ such that $\forall n \geq M$, $|x_n - x| < \epsilon$, which $x$ is the limit when $n$ is sufficiently large. 
			- LHS: 
				- With the definition of convergent sequence, we have distance between sequence and limit is $D_1 = |x_n - x|$
			- RHS: 
				- Similarly, with the definition of convergent sequence, we have distance between sequence and limit is $D_2 = |(x_n - x) - 0|$
			- We see LHS = RHS. 
			- QED. 
- Notation of limits
	- 1. $\underset{n \rightarrow \infty}{lim} x_n := x$
	- 2. $x = \text{lim}_{n \rightarrow \infty} x_n$
	- 3. $x_n \rightarrow x$

### Convergent sequence 
- When discussing "convergent sequence", we have made use of the definition of bounded sequence. 
- Definition
	- Convergent sequence 
		- A sequence $\{ x_n \}$ is convergent to a number $x \in \mathbb{R}$, if $\forall \epsilon > 0$, $\exists M \in \mathbb{N}$ such that $\forall n \geq M$,  $|x_n - x| < \epsilon$
			- Bounded sequence
				- First thing is, $|x_n - x| < \epsilon$ is making use of the concept of "bounded sequence" (which is a sequence $\{x_n\}$ is bounded if there exists a $B \in \mathbb{R}$ such that $|x_n| \leq B$ for all $n \in \mathbb{N}$.
				- With this, we know this definition is actually saying that, giving any $\epsilon$, which acting as the range which the sequence is converging, we can always find some threshold $M$ such that all elements beyond that threshold are valued within that $\epsilon$. 
				- It is like a U-shaped box which is formed by a threshold $M$, a pair of value $x + \epsilon$ and $x - \epsilon$,  that locks the range of the sequence. 
			- $\epsilon$ getting smaller and smaller as $M$ increases
				- Approach 1 - showing a decreasing sequence of epsilon satisfies the definition of convergent sequence
					- Given $\{ \epsilon_n \}$ is decreasing, we can establish that $| \epsilon_n - L| < \epsilon$ for any positive $\epsilon > 0$ when $n > N$, where $N$ is some positive integer.
					- Since the sequence $\{ \epsilon_n \}$ is decreasing, for any value of $n \geq N$, $\epsilon_n \geq \epsilon_N$, where $\epsilon_N$ is the initial value at index $N$. 
					- Let's assume $L$ is the infimum of the sequence $\{ \epsilon_n \}$. Since $\{ \epsilon_n \}$ is decreasing, $L$ is lower bound for the sequence. 
					- By the completeness property of the real numbers, the sequence $\{ \epsilon_n \}$ must converge to limit $L$. 
					- To prove that the limit of the sequence $\{ \epsilon_n \}$ is $L$, we need to show that for any positive $\epsilon > 0$, there exists a positive integer $N$ such that for all $n \geq N$, $|\epsilon_n  - L | < \epsilon$. 
					- Given any positive $\epsilon > 0$, we can choose $N$ such that $\epsilon_N < L + \epsilon$. Since the sequence is decreasing, for all $n \geq N$, we have $\epsilon_n \leq \epsilon_N$.
					- Therefore, for $n \geq N$, we have $| \epsilon_n - L| \leq |\epsilon_N - L| < \epsilon$.
					- This shows that the sequence $\{ \epsilon_n \}$ converges to the limit $L$ as $n$ approaches infinity.
				- Approach 2 - assert $x$ is a limit 
					- As $n$ increases, the bound $\epsilon$ that describes $|x_n - x|$ should be decreasing. 
					- The number $x$ is said to be the limit of $\{x_n\}$. We write $\underset{n \rightarrow \infty}{lim} x_n := x$
	- Non convergent sequence
		- The sequence $\{ x_n \}$ is not convergent, or divergent if $\exists \epsilon_0 > 0$, such that $\forall M \in \mathbb{N}$, $\exists n \geq M$ so that $|x_n - x| \geq \epsilon_0$
			- Non bounded sequence
				- Say we inspect a subdomain of a function and knows that the range of the sequence is about a certain range. We impose a bound $B$. 
				- As we keep increase $n$, we might find that 
- Examples:
	- Show $\{ \frac{1}{n} \}$ is convergent and $\underset{n \rightarrow \infty}{lim}\frac{1}{n} = 0$:
		- Approach 1: Archimedean property
			- For any $\epsilon > 0$, we find an $M \in \mathbb{N}$ such that $0 < \frac{1}{M} < \epsilon$, 
				- $\frac{1}{M} < \epsilon$ is coming from Archimedean property at work.
					- Recall the definition of Archimedean property is, If $x,y \in R$ and $x > 0$, then $\exists n \in \mathbb{N}$ such that $nx > y$, or in other words, $n > \frac{y}{x}$
					- In the question we have $\epsilon, 1 \in \mathbb{R}$, and M \in $\mathbb{N}$, so we have $\exists M \in \mathbb{N}$ such that $\epsilon M > 1$.
				- $0 < \frac{1}{M}$ always true because $\forall x \in \mathbb{N}$, $x > 0$. 
			- Then for all $n \geq M$, we have $|x_n - 0| = | \frac{1}{n}| = \frac{1}{n} \leq \frac{1}{M} < \epsilon$
				- The first equal sign holds true by substituting $x_n = \frac{1}{n}$
				- The second equal sign holds true by refer to the definition of absolute value.
				- The third inequality sign, $\frac{1}{n} \leq \frac{1}{M}$, because $n \geq M \implies  \frac{1}{n} \leq \frac{1}{M}$
			- Combine all of these, we have $|x_n - x| < \epsilon$. 
			- Therefore, $\{ \frac{1}{n} \}$ is convergent. 
		- Approach 2: Just picking numbers
			- Let $\epsilon > 0$. Choose $M \in \mathbb{N}$ such that $M^{-1} > \epsilon^{-1}$. Hence, for all $n \geq M$, $|\frac{1}{n} - 0| = \frac{1}{n} \leq \frac{1}{M} \leq \epsilon$.
	- Show $lim_{n \rightarrow \infty} \frac{1}{n^2 + 2n + 100} = 0$
		- Let $\epsilon > 0$ and choose $M \in \mathbb{N}$ such that $M > \frac{\epsilon^{-1}}{2}$. 
		- Then $\forall n \geq M$, $| \frac{1}{n^2 + 2n + 100} - 0| \leq \frac{1}{n^2 + 2n + 100} \leq \frac{1}{2n} \leq \frac{1}{2M} < \epsilon$
			- The first inequal sign is referring to the definition of absolute value
			- The second inequal sign is referring to the fact that "removing positive terms from the denominator of a fraction can only increase its value". 
			- The third inequal sign is referring to $\forall n \geq M \implies \frac{1}{2M} \geq \frac{1}{2n}$. Again it is also the property of fraction, where larger denominator means smaller value of the whole fraction.
			- The fourth inequal sign is referring to the $\epsilon$ sign we have chosen. $M > \frac{\epsilon^{-1}}{2} \implies \epsilon > \frac{1}{2M}$
	- Show the sequence $x_n = (-1)^n$ is divergent
		- Let $x \in \mathbb{R}$
		- We claim $lim_{n \rightarrow \infty} \neq x$. To show this, we simply need find an epsilon that stops the sequence from converging.
		- Consider $\epsilon_0 = \frac{1}{2}$, then 
		- for $M \in \mathbb{N}$, $2 = |(-1)^M - (-1)^{M+1}| \leq |(-1)^M| + |-(-1)^{M+1}| = |(-1)^M -x| + |(-1)^{M+1} - x|$
			- The first equal sign comes from the fact the inner part would be $-2$ when $M$ is odd, and it would be $2$ when $M$ is even. In both cases, the whole term returns $2$. 
			- The following inequality sign holds can be referred to triangular inequality. 
			- The following equal sign holds because of 1, the property of absolute value, which is $|-x| = |x|$ for all $x \in \mathbb{R}$. 2, it is simply shift the sequence vertically by $x$. 
		- So we have $|(-1)^M -x| + |(-1)^{M+1} - x| \geq 2$. 
		- So we have either $|(-1)^M -x| \geq 1$ or  $|(-1)^{M+1} - x| \geq 1$. In either case, this shows that the limit cannot converge to $x$. 


### Theorem: Let $x,y \in \mathbb{R}$. If $\forall \epsilon > 0$, $|x - y| < \epsilon$, then $x = y$
- Suppose $x \neq y$, then $|x - y| > 0$.
- Choosing $\epsilon = \frac{|x - y|}{2}$, we have $|x - y| \leq \frac{|x - y|}{2} \implies \frac{|x - y|}{2} < 0$, which contradicts $|x-y| > 0$ we mentioned before. 

### Theorem: If $\{ x_n \}$ converges for $x$ and $y$, then $x = y$. In other words, limits of convergent sequences of real numbers are unique
- Suppose $x_n$ converges to $x$ and $y$.
- We try to show for all $\epsilon > 0$, $|x - y| < \epsilon$. 
	- Given $x_n \rightarrow x$, for $\epsilon > 0$, there exists an $N_1 \in \mathbb{N}$ such that $\forall n \geq N_1$, $|x_n - x| < \frac{\epsilon}{2}$
		- By convergence we know that the sequence ${x_n}$ converges to $x$ if, for any given positive value of $\epsilon$, there exists a natural number $N_0$ such that for all $n \geq N_0$, $|x_n - x| < \epsilon$.
		- And then, for a given positive value of $\epsilon/2$, there exists $N_1$ such that for all $n \geq N_1 \geq N_0$, $|x_n - x| < \frac{\epsilon}{2}$.
		- By choosing $\frac{\epsilon}{2}$ in both cases, we are essentially splitting the total allowed error $\epsilon$ into two parts, one for the difference between $x_n$ and $x$ and the other for the difference between $x_n$ and $y$. This division of error bounds enables us to combine and manipulate the inequalities to ultimately show that $x = y$.
	- Given $x_n \rightarrow y$, for $\epsilon > 0$, there exists an $N_3 \in \mathbb{N}$ such that $\forall n \geq N_3$, $|x_n - y| < \frac{\epsilon}{2}$
		- By convergence we know that the sequence ${x_n}$ converges to $y$ if, for any given positive value of $\epsilon$, there exists a natural number $N_0$ such that for all $n \geq N_2$, $|x_n - y| < \epsilon$.
		- And then, for a given positive value of $\epsilon/2$, there exists $N_3$ such that for all $n \geq N_3 \geq N_2$, $|x_n - y| < \frac{\epsilon}{2}$.
	- Let $N = max\{ N_1, N_3 \}$, for all $\epsilon > 0$, there exists an $N = max\{ N_1, N_3 \}$ such that for all $n \geq N$, 
		- $|x - y| \leq |x - x_n| + |x_n - y| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$
			- The first inequal sign holds, known by referring to triangular inequality.
			- The second inequal sign holds, by the works we did above. 
	- Hence, for all $\epsilon > 0$, $|x - y| < \epsilon$. Therefore, $x = y$.

### Theorem: If $\{ x_n \}$ is convergent, then $\{ x_n \}$ is bounded.
- Recall bounded sequence:
	- A sequence $\{ x_n \}$ is bounded if $\exists B \geq 0$ such that $\forall n$, $|x_n| \leq B$.  
- Recall convergent sequence:
	- A sequence $\{ x_n \}$ is convergent to a number $x \in \mathbb{R}$, if $\forall \epsilon > 0$, $\exists M \in \mathbb{N}$ such that $\forall n \geq M$,  $|x_n - x| < \epsilon$
- Proof:
	- Let $\epsilon = k$ such that $|x_n - x| < k$ for all $n \leq M$ for some $M \in \mathbb{N}$
		- While convergent sequence holds for $\forall \epsilon >0$, which means the range of all epsilon except the limit $x$ itself.
		- If we let $\epsilon = 1$, the proof is not entirely correct. In the proof, you need to show that the sequence is bounded for any epsilon > 0, not just for epsilon = 1.
	- There are finitely many elements not in the interval $(x-k, x+k)$. We use this to our advantage.
		- "The interval" refers to the fact that the elements in the zone of convergent ($\forall n \geq M$) are valued within $(x-k, x+k)$. Outside the zone, the elements are having the value outside of $(x-k, x+k)$.
	- Convergent property of the sequence
		- Suppose $\text{lim}_{n \rightarrow \infty} x_n = x$, thus there exists an $M \in \mathbb{N}$ such that $|x_n - x| < k$ for all $n \geq M$. 
	- Let $B = max\{ |x_1| , |x_2|, \dots, |x_{M-1}|, |x| +k\}$
	- Proof by cases: 
		- If $n < M$, then $|x_n| \leq B$ by construction of $B$ we just established.
		- If $n \geq M$, then $|x_n| \leq |x_n -x| + |x| < k + |x| \leq B$
			- The first inequal sign refers to triangular inequality
			- The second inequal sign refers to $|x_n - x| < k$ we previously stated
			- The third inequal sign refers to the construction of $B$
	- In both cases, ${x_n} \leq B$. Thus we have proven the theorem. 


---


### Monotone sequences
- A sequence $\{ x_n \}$ is monotone increasing if $x_n \leq x_{n+1}$ for all $n \in \mathbb{N}$.
- A sequence $\{ x_n \}$ is monotone decreasing if $x_n \geq x_{n+1}$ for all $n \in \mathbb{N}$.

### Bounded monotone sequence
- A sequence $\{ x_n \}$ is "bounded and monotone" if and only if it is convergent.

### Bounded monotone increasing sequence
- Apart from it is bounded, it is monotone increasing, there is a new property for such sequence, which is
- Property:
	- $\underset{n \rightarrow \infty}{lim} x_n = sup\{ x_n : n \in \mathbb{N}\}$
- Recall the definition of sequence:
	- In order for a collection of values to be considered a sequence, it must be indexed by the natural numbers. 
- Recall definition of supremum:
	- If there exists an upper bound $b_0$ of $E$ such that whenever $b$ is any upper bound for $E$, we have $b_0 \leq b$, then $b_0$ is called the least upper bound or the supremum of $E$. We write $supE = b_0$
- Recall definition of bounded sequence:
	- A sequence $\{ x_n \}$ is bounded if $\exists B \geq 0$ such that $\forall n$, $|x_n| \leq B$.  
- Proof:
	- Suppose the sequence $\{x_n \}$ is monotone increasing. 
	- Suppose the sequence is bounded, so there exists a $B$ such that $x_n \leq B$ for all $n$, that is $x_n : n \in \mathbb{N}$.
	- Let $x = sup\{ x_n : n \in \mathbb{N}\}$
	- Let $\epsilon > 0$ be arbitrary. 
	- Boundedness
		- Since $\{ x_n \}$ is bounded, there $\exists M \in \mathbb{N}$ such that $x_n \leq M$ for all $n \in \mathbb{N}$.
		- Thus, the set $\{ x_n: n \in \mathbb{N} \}$ is not empty and bounded above. 
	- Supremum
		- $x$ satisfies two properties:
			- 1. For all $n \in \mathbb{N}$, we have $x_n \leq L$, since $L$ is an upper bound of the set.
			- 2. For any $\epsilon > 0$, there exists $N \in \mathbb{N}$ such that $x_N > L - \epsilon$, since $L$ is the least upper bound.
		- As $x$ is the supremum, then there must be at least one $M \in \mathbb{N}$ such that $x_M > x - \epsilon$, because $x$ is the supremum.
	- As $\{ x_n \}$ is monotone increasing, then it is easy to see that $x_n \geq x_M$ for all $n \geq M$.
	- Hence $|x_n - x| = x - x_n \leq x - x_M < \epsilon$
	- Therefore, $|x_n| < |x + \epsilon|$. Therefore, $x_n \rightarrow x$.

### Bounded monotone decreasing sequence
- Also, $\underset{n \rightarrow \infty}{lim} x_n = inf\{ x_n : n \in \mathbb{N}\}$


### Sub-sequence
- Let $\{x_n \}$ be a sequence  and let $\{ n_k\}$ be a strictly increasing sequence of natural numbers. Then $\{x_{n_k} \}_{k=1}^\infty$ is called sub-sequence of $\{ x_n \}$
- Consider $\{ x_n\} = n$.
	- It would be $1,2,3,4, \dots$
- Then $\{x_{n_k}\}$ = $\{ x_{2k}\}$
	- It means that $n_k = 2k$ 
	- It would be $2,4,6,8, \dots$
 
---
# Lecture 8 squeeze theorem and operations involving convergent sequences

### Squeeze theorem (ST)
- Let $\{ a_n \}$, $\{ b_n \}$ and $\{ x_n \}$ be sequences such that $\forall n \in \mathbb{N}$, $a_n \leq x_n \leq b_k$. Suppose that $\{ a_n \}$ and $\{ b_n \}$ converge and $\underset{n \rightarrow \infty}{lim} a_n = x = \underset{n \rightarrow \infty}{lim} b_n$. Therefore, $\{ x \}$ converges and $\underset{n \rightarrow \infty}{lim} x_n = x$
- Proof:
	- Let $\epsilon > 0$. 
	- Since $\underset{n \rightarrow \infty}{lim} a_n =x$, there exists an $M_0 \in \mathbb{N}$ such that $\forall n \geq M_0$, $|a_n - x| < \epsilon \implies (x - \epsilon < a_n < x + \epsilon) \implies x - \epsilon < a_n$
	- Since $\underset{n \rightarrow \infty}{lim} b_n =x$, there exists an $M_0 \in \mathbb{N}$ such that $\forall n \geq M_1$, $|b_n - x| < \epsilon \implies (x - \epsilon < b_n < x + \epsilon) \implies b_n < x + \epsilon$
	- Choose $M = max\{ M_0, M_1\}$, if $n \geq M$, then $x - \epsilon < a_n \leq x_n \leq b_n < x + \epsilon \implies x - \epsilon <  x_n < x + \epsilon \implies |x_n - x| < \epsilon$
	- Therefore, $\{ x_n \}$ is convergent and $lim_{n \rightarrow \infty} x_n = x$. 

### Theorem - Another way to check that a sequence $x_n \rightarrow x$, would be $\underset{n \rightarrow \infty}{lim} x_n = x \iff \underset{n \rightarrow \infty}{lim} |x_n - x| = 0$
- Example:
	- $\underset{n \rightarrow \infty}{lim} \frac{n^2}{n^2 + n + 1} = 1 \iff \underset{n \rightarrow \infty}{lim} |\frac{n^2}{n^2 + n + 1} -1| = 0$

### Theorem: How limits interact with ordering --- if $\{x_n\}$ and $\{y_n\}$ are convergent sequences and $\forall n \in \mathbb{N}$ $x_n \leq y_n$, then $\lim_{n \rightarrow \infty} x_n \leq lim_{n \rightarrow \infty} y_n$
- Let $\{x_n\}$ and $\{y_n\}$ be sequences of real numbers. Then,
	- if $\{x_n\}$ and $\{y_n\}$ are convergent sequences and $\forall n \in \mathbb{N}$ $x_n \leq y_n$, then $\lim_{n \rightarrow \infty} x_n \leq lim_{n \rightarrow \infty} y_n$
		- Proof: 
			- Let $x = \lim_{n \rightarrow \infty} x_n$, 
			- Let $y = lim_{n \rightarrow \infty} y_n$
			- Let $\epsilon > 0$ be given.
			- Find an $M_1$ such that for all $n \geq M_1$ we have $|x_n - x| < \epsilon/2$
				- Recall convergent sequence:
					- A sequence $\{ x_n \}$ is convergent to a number $x \in \mathbb{R}$, if $\forall \epsilon > 0$, $\exists M \in \mathbb{N}$ such that $\forall n \geq M$,  $|x_n - x| < \epsilon$
				- Why we choose $\epsilon < 2$ on $|x_n - x| < \epsilon/2$?
					- Since convergent sequence holds the property $|x_n - x| < \epsilon$ for all $\epsilon$. That means we have a freedom to choose the threshold $M$, and any gap distance, say $D = \epsilon/2$, for the problem.  
			- Find an $M_2$ such that for all $n \geq M_2$ we have $|y_n - y| < \epsilon/2$
			- For all $n \leq max\{ M_1, M_2\}$, we have 
				- $( |x_n - x| < \epsilon/2) \implies x - x_n < \epsilon/2)$ or
				- $(|y_n - y| < \epsilon/2) \implies y_n - y < \epsilon/2$, 
				- where the position of  $\theta_n$ is switched which help the later step.
			- Combining two inequalities we have $( x- x_n) + (y_n - y) = y_n - x_n + x - y < \epsilon \implies y_n - x_n < y - x + \epsilon$. 
				- Since $x_n \leq y_n \implies y_n - x_n \geq 0$, we have $y - x + \epsilon > y_n - x_n \geq 0 \implies y - x + \epsilon > 0$
				- By changing the subject, we have $x - y < \epsilon$
			- Because $\epsilon > 0$ was arbitrary, we obtain $x - y \leq \epsilon < 0\implies x - y < 0$. Therefore, $x \leq y$. 
	- if $\{x_n\}$ is a convergent sequence and $\forall n \in \mathbb{N}$, $a \leq x_n \leq b$, then $a \leq lim_{n \rightarrow \infty} x_n \leq b$. 
		 - Proof:
			 - By considering $y_n = a \leq x_n \leq b = z_n$ for all $n \in \mathbb{N}$. Then the theorem is proven. 


---

### Theorem: How limits interact with algebraic operations --- 4 properties
- Suppose $\lim_{n \rightarrow \infty} x_n = x$ and $\lim_{n \rightarrow \infty} y_n = y$. Then
	- 1.  ($\{ x_y + y_n\}_n$ is convergent and) $lim_{n \rightarrow \infty} (x_n + y_n) = x + y$
		- Proof:
			- Let $\epsilon > 0$ 
			- Since $x_n \rightarrow x$, $\exists M_0$ such that $\forall n \geq M_0$, $|x_n - x| < \frac{\epsilon}{2}$
			- Since $y_n \rightarrow y$, $\exists M_1 \in \mathbb{N}$ such that $\forall n \geq M_1$, $|y_n - y| < \frac{\epsilon}{2}$
			- Hence, letting $M = max\{ M_0, M_1 \}$, we get for all $n \geq M$, $|x_n + y_n - (x+y)|\leq |x_n - x| + |y_n - y |< \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$
	- 2. $\forall c \in \mathbb{R}$, $\{ c x_n\}_n$ is convergent and $lim_{n \rightarrow \infty} cx_n = cx$
		- Proof:
			- Let $\epsilon > 0$
			- Since $x_n \rightarrow x$, $\exists M_0 \in \mathbb{N}$ such that $\forall n \geq M_0, |x_n - x| < \frac{\epsilon}{|c|+1}$
			- Let $M = M_0$, then, $\forall n \geq M$, $|cx_n - cx| = |c| |x_n - x| \leq \frac{|c|}{|c| + 1} \cdot \epsilon < \epsilon$
	- 3. $\{ x_n \cdot y_n \}$ is convergent and $lim_{n \rightarrow \infty} x_n y_n = xy$
	- 4. If $\forall n \in \mathbb{N}$, $y_n \neq 0$, and $y \neq 0$, then $\{ x_n / y_n \}_n$ is convergent and $lim_{n \rightarrow \infty} \frac{x_n}{y_n} = \frac{x}{y}$

---
### Technique of proof: $\forall n ,(\text{statement}) \implies  \exists  n, (\text{statement})$
- It is called "existential instantiation"
- More notations that is describing the same thing:
	- n ∈ ℕ : P(n) → (∃n ∈ ℕ : P(n))
- Advantage:
	- This can make the subsequent steps of the proof more manageable and help derive specific conclusions about the sequences.
- example:
	- if $\forall \epsilon > 0$, $\exists M \in \mathbb{N}$ such that $\forall n \geq M$,  $|x_n - x| < \epsilon$ $\implies$  $\exists A \in \mathbb{R},  0 <A < \epsilon$, $\exists M_0 \in \mathbb{N}$ such that $\forall n \geq M_0$,  $|x_n - x| < A$ 
		- The first statements appears in the definition of "convergent sequence":
			- A sequence $\{ x_n \}$ is convergent to a number $x \in \mathbb{R}$, if $\forall \epsilon > 0$, $\exists M \in \mathbb{N}$ such that $\forall n \geq M$,  $|x_n - x| < \epsilon$
		- The second statement might be found on some proofs about "convergent sequence":
			- $\forall \epsilon \implies \exists \epsilon$
			- The instance of existential quantification are followed by universal quantification and implications, which makes the statements conditionally true. 
			- By choosing a specific value for $A$ that is smaller than $\epsilon$, it allow us to establish a bound on the difference $|x_n - x|$ that is independent of $\epsilon$.

---
- A convergent sequence follow its definition: if $\forall \epsilon > 0$, $\exists M \in \mathbb{N}$ such that $\forall n \geq M$, $|x_n - x| < \epsilon$. - Inspect the definition $|x_n - x| < \epsilon$ holds for all $\epsilon > 0$. - I often see that in the proof related to convergent sequence, we also have we have $|x_n - x| < A$, which $A$ is a value that is smaller than $\epsilon$, such as $\frac{\epsilon}{|c|}$. Is that because in the definition of convergent sequence $|x_n - x| < \epsilon$ holds for all $\epsilon > 0$, so $|x_n - x| < A$ re also true, where $A$ is a constant value and $A \leq \epsilon$ a ?



---

"For any $\epsilon > 0$, there exists $M \in \mathbb{N}$ such that $\forall n \geq M$, (statement)."


---
# Lecture 9 

### Limsup


### Liminf

### Theorem: Let $\{ x_n \}$ be a bounded sequence. Then there exists subsequences $\{ x_{n_k}\}$ and $\{ x_{m_k}\}$ such that $\underset{k \rightarrow \infty}{lim} x_{n_k} = \underset{n \rightarrow \infty}{lim\ sup}\ x_n$

### Bolzano-Weierstrass
- Every bounded sequence has a convergent subsequence

### Theorem: Let $\{ x_n \}$ be a bounded sequence. Then $\{ x_n \}$ converges if and only if $lim\ inf\ x_n = lim\ sup\ x_n$

---
# Lecture 10

### Cauchy sequence
- Definition
	- Cauchy sequence $\{ x_n \}$ is Cauchy if $\forall_\epsilon > 0$, $\exists M \in \mathbb{N}$ such that for all $n,k \geq M$, $|x_n - x_k| < \epsilon$> 
	- On the other hand, a sequence $\{ x_n \}$ is not Cauchy if $\exists \epsilon_0 > 0$ such that for all $M \in \mathbb{N}$, $\exists n,k \geq M$ such that $|x_n - x_k| \geq \epsilon_0$.

### Theorem: If $\{ x_n \}$ is Cauchy, then $\{ x_n \}$ is bounded


### Theorem: If $\{ x_n \}$ is Cauchy and a subsequence $\{ x_{n_k} \}$ converges, then $\{ x_n \}$ converges.


### Theorem: A sequence of real numbers $\{ x_n \}$ is Cauchy if and only if $\{ x_n \}$ is convergent

### Series
- Definition:
	- Given $\{ x_n \}$, the symbol $\sum_{n=1}^{\infty} x_n$ or $\sum x_n$ is the series associated to $\{ x_n \}$. 
	- We say $\sum x_n$ converges if the sequence $\{ s_m = \sum_{n=1}^m x_n  \}_{m=1}^\infty$
- 