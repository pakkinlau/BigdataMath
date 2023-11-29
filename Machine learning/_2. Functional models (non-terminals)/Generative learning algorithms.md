- 26-9-2022: created

- Related: [[Generative adversarial network]]

- superset:
	- [[Generalization]]

- Instead of looking at all classes at one time, and find the decision boundary line, this algorithm tries to only look at the classes one at a time. 
	- eg: 1. look at all of the malignment tumors, in the cancer example, and try to build a model for what malignment tumors look like. 
- Instead of learning $p(y|x)$, learning 
	- $p(x|y)$: The probability of what feature would be like, given a class. 
	- $p(y)$: Called "class prior". Before you see the patient, what's the chance the object is actually in that class. 
- Methods
	- [[Gaussian discriminant analysis]]

- There are two classes of learning algorithm:
	- [[Generative learning algorithms]]
	- [[Discriminative learning algorithms]]

- Steps (general)
	- 1. We have a collection of labels $y$ indicates whether an example is dog(0) or an elephant(1). 
	- 2. $p(x|y=0)$ models the distribution of dogs' features, and $p(x|y=1)$ models the distribution of elepants' features.  
		- Result: Learnt $p(y)$ and $p(x|y)$ that could be used to calculate values in step 3. 
	- 3. Use Bauers rule to derive the posterios distribution on $y$ given $x$: $$p(y|x) = {p(x|y)p(y) \over p(x)}$$, given:
		-  $p(x) = p(x|y=1)p(y=1) + p(x|y=0)p(y=0)$
	- 4. If we were calculating $p(y|x)$ to make prediction, we don't need to calculate the denominator, since
		- $\underset{y}{argmax}\ p(y|x) = \underset{y}{argmax}\ {p(x|y)p(y) \over p(x)} =  \underset{y}{argmax}\ {p(x|y)p(y)}$
			- Related: [[argmax (arguments of the maxima)]]

- A discriminateive classifier tries to model by just: depending on the observed data.


---
## Reference:
- [[(Course) CS229 Machine learning]]
- Webpage: 
	- https://mohitjain.me/2018/03/12/generative-learning-algorithms/#:~:text=Generative%20approaches%20try%20to%20build,one%20model%20becomes%20more%20likely.
- 