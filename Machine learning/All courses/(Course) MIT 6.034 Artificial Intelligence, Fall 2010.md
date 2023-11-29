## Lesson 1 - Introduction and scope

---
- 1. Getting the representation right --> almost done
	- With the correct representation, we might get the correct answer immediately.

- Representation is important
	- Hitting a rotating wheel 
	- Chicken and goose problem
	- "how many countries in Africa are crossed by the equators"
		- visual system that scan the image-->sends to the language system to tell the answer.

- What is artificial intelligence?
	- "Algorithms enabled by constraints exposed by representation that support models targeted at thinking, perception and action. And with loops that link thinking, perceptions and actions together."

- 2. Simple is not equal to trivial
	- You might be tempted to say to someone, we learned about generate and test today, is simple. 
	- "trivial" is the word to be purged in our vocabulary, is because it is a dangerous label?
	- simple thing could be powerful. Labelling things trivial seems to make something not worthy.

- 3. Rumpelstiltskin principle
- Generate and test
	- G (Generator) --> T --> {a lot of failure + a plenty of successful}
	- Rumpelstiltskin principle:
		- Once you can name something, you get power over it. 
		- "how we call the thing at the end of the shoelace?"
		- aglet = keep the things from unwinding

---
### history of AI
- 1950:
	- the dawn of AI
	- 1. integration
		- use computer to do symbolic integration?
	- 2. Eliza
		- first program that is capable of response to people
	- 3. geometric analogy
		- IQ 
	- 4. vision
		- recognize shapes and 3D from watching strokes
	- 5. learning
		- watching a few pictures of structures involves an arch
		- arch is something on top... 
	- 6. expert system
		- park aircraft effectively

- bulldozer age
	- people realize we can substitute computing for intelligence
	- deep blue - beating world champion
	- right way - imagination
		- the program using a visual system to stimulate the situation such as "a woman run to a man". and then it answer questions according to that imagination

- why human is so different from champanzees?
	- high school - slow and gradual improvement. its not.
	- speaker - if someone came from 20,000 years ago, might be dirty and naked, but that person has not much difference than today human?
	- 50k years ago, some small group of people accidental change the living of the group of species."using 2 concepts, and combine them to make a third concept, without disturbing the original two concepts, without limit" = learn how to describe things.
	- Descriptions allow us to tell stories. imagine things we have never seen.
		- eg: "imagine you take a bottle of water to run, your legs get wet. But you cant find that fact from what you have learnt"

----
## Lesson 2 - Reasoning: Goal Trees and Problem Solving

- appreciation of "what is intelligent"

- building a program that solves symbolic integration
	- prof. Patrick William put it like "how much knowledge pieces I need, to get an A in mathematics major degree?"

- "how much knowledge needed for us to get an A?"

- problem reduction
	- creating another problem to make the original problem easier.
	- in math, some transformation are safe and easy to use.
	- requirements
		- skill
		- understand 
		- witness

- Say we have an integration problem
	- 1. make the problem easier by transforming it
	- 2. heuristic transformation
		- a funny word, meaning that a method that is not guaranteed to work.
		- sometimes it takes you into blind alley, don't always work. But you can't get an A in calculus without knowing some of them.
		- eg: transforming a $f(sinx, cosx, \dots , cotx)$ into $g_1(sinx, cosx)$ or others. 
			- not always work, but sometimes help.
		- eg: we see $1 - x^2$ , we sub $x = sin\ y$ because we see it has the pattern of $sin^2x + cos^2x = 1$.

- problem reduction tree / and-or tree
	- 

- figure: decision tree on freshman's integration problem
	- how to decide the last idea?
	- A: feel? simplicity? tangent feels more familiar?
![[Pasted image 20230426090704.png]]

- how to measure difficulty for integration problem?
	- the length of symbols might not indicates
	- but how many layers it is deeply nested under a lot of function composition is the problem. 

- figure: 
	- the flow of problem solving is:
		- 1. apply all safe transform
		- 2. look up table
		- 3. done?
		- 4. find problem
		- 5. apply heuristic transform
		- 6. back to step 1 if it is needed
	- the flowchart of goal trees problem solving 
	- we would look at the nested functional component of each branches
	- and also looking across the whole tree, the leaves of the tree.
![[Pasted image 20230426092528.png|700]]

- using this structure to build a computer program, and running the program on a 50k memory computer
	- correct answers / accuracy: 54/56
	- depth: in the worst case, it gets down 7 level. average depth is 3?
	- unused branches?

- difficulty of the problem
	- if the depth is 3, everyone can do it, the computer program could also do it
	- if the depth is 5, might be some guys who wants to be math professor?

- catechism
	- what kind
	- how represented
	- how used
	- how much
	- what exactly
- Q when using catechism
	- what kind of knowledge is involved in doing this?
		- transformation?
		- how goal trees work?
		- what things do not needed to be transformed?
- 40:00 of lecture 2
	- review the structure of goal trees
	- what it meant to be intelligent


---
## Lecture 3 - Reasoning: Goal Trees and Rule-Based Expert Systems

- A program that answer the question about its own behavior.

- Put-on methpd
	- 1. find space
	- 2. grasp --L--> clear top --L--> get rid of
	- 3. move
	- 4. ungrasp
- Simon's ant
	- The complexity of the behavior is the $max()$  the $a$: complexity of the program and $b$: the complexity of the environment. 

- Rule-based expert system
	- enthusiasm about the prospects of commercial programs in mid 1980s.
	- writing knowledges in simple rules