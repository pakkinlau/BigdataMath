---
category: []
alias: [entropy, binary entropy]
tags: []
---

- 25-9-2022: created

- Used in: the loss function in [[Unsupervised learning]] 
- Used in: [[Compress|compression]]
- Superset:
	- [[information theory]]
	- [[computational neuroscience]]

- Relationship between $m$: (equiprobable destinations/values), and $n$ (bit/forks/entropy)
	- $m = 2^n$
		- $m$: (equiprobable destinations/values/ equiprobable output state)
		- $n$ (bit/forks/entropy)
	- Taking $log_2$ for both sides, we have $H = log_2 (m)$
	- Entropy $H$
		- $H$ is the number of bits of information required to specifiy one of $m$ equiprobable destinations or values is equal to the logarithms, base 2, of $m$. 

- [[Shannon information]]
![[Shannon information#^ef7e49]]
- What is cross entropy / entropy?:
	- Definition: 
		- Average of surprise / Shannon information, weighted by their probability, i.e. $H(x) =\sum_i prob._i \times v_{sur_i} = -\sum_i p(x_i) log p(x_i)$ 
			- eg: $m = 2^{0.469}$ or 1.38 equiprobable values / bits 
		- It is a measurement of disorder or impurities in the information processed in machine learning. It could be illustrated as if balls in two colors are uniformly mixed together within a box.  (R1)
	- Intuitions
		- We don't talk about the entropy of a single state. But the average of them (R3)
		- The entropy of the stimulus can be intuitively understood as "how long a message (in bits) do I need to convey the value of the stimulus?"(R2)
		- Entropy quantifies the amount of uncertainty involved in the value of a random variable or the outcome of a random process. (R2)
		- The entropy counts the number of yes/no (binary) question, as we say that we specifies a variable. (R3)
			- (In the case of squash ball game, each question cuts prob of the venue in half.) (R3)
			- eg: binary (such as left or right): 1bit to convey which target appeared. 
		- The entropy can be thought of as a measure of uncertainty.
			- If there is higher entropy, there are more possible states the system could be.
	- In [[computational neuroscience]], 
		- a spike train is a time sequence in which we are marking spikes, 1 = having spike, 0 = silence. (R3)
			- If all states are equally probable, then the entropy is just the log of the number of states.
				- say A box with five head/tail coins can take $2^5$ = 32 states, the entropy is just the log of the number of states: $log_2(2^5) = 5$.
			- We use logarithm so that entropy only grows linearly as the number of coins increases. 
			- say P(1) = p, P(0) = 1-p. The surprise of seeing a spike is defined by $-log_2(p)$. Of silence: $-log_2(1-p)$.
			- The log base 2 used in the equation is assuming the signal is binary (eg: electrical signals). Information in Electrical engineering is bit.
	- computation (R3)
		- entropies are always computed in log-base-2, and their units are in bits. 

---
- Distribution of signals / information
	- Entropy can be treated as a machine learning metric that measures the unpredictability or impurity in the system.
		- (source: https://www.javatpoint.com/entropy-in-machine-learning#:~:text=Introduction%20to%20Entropy%20in%20Machine,or%20impurity%20in%20the%20system.)
		- Formula:
			- $E = - \sum_{i=1}^{N} P_i log_2 P_i$
			- where $P_i$ is the probability of randomly selecting an example in class $i$. 
		- Applications 
			- eg: 3 red balls and 7 green balls. 2 Classes in total, so $H(q)=log(2)$
			- $E = -\frac{3}{10}log_2 {\frac{3}{10}} - \frac{7}{10}log_2{\frac{7}{10}} = 0.88$
			- $E$ reaches its maximum if the number of red and green balls are the same.

![[Pasted image 20220917035641.png]]
![[Pasted image 20220917034406.png]]
- Figure: The entropy of data goes to the maximum when the chance of drawing a ball is half-half.



---

![[Pasted image 20221028190208.png]]
- eg: squash 
	- each information cuts the possibility down by an additional factor of 2. what we are doing is multiplying the probability of being in this half, is $p = 0.5$. P(front corner) = ${1 \over 2} \times {1 \over 2}$. 
	- Taking the negative log (base 2), turns these ${1 \over 2}$ into 1+1 = 2 bits. 
	- In generally P(x) is not uniform but it would be best for you, if it were. In such case, your opponents has his hard time to predict your next move.
	- The capacity (best performance) of a player could yield highest entropy by manipulating the probability distribution of the input data $x$, 
		- $C = \underset{p(x)}{max} H(x)$ 
	- The capacity of a noisy channel:
		- $C = \underset{p(x)}{max} I(x,y)$
		- $C = \underset{p(x)}{max} [H(y) - H(\eta)]$
		- $C = \underset{p(x)}{max} [H(y) - H(y|x)]$

---
- Application of cross entropy 


- Binary search
	- Locating a bar by dividing the search space. 
	- The algorithm terminates when the search space is reduced to a single location where the car is located
	- Entropy quantify the amount of information gained at each step of the search algorithm.

![[Pasted image 20221028190953.png]]
- eg: A guard that only answer me yes-no question to locate my car
	- $p_i$ the probability of the thing located to location $i$. For [[identical and independently distributed|i.i.d.]], it is simply $1 \over 8$.
	- $-log_2({1 \over 8}) = -3$, $8 \times {1 \over 8} \times 3 = 3$
	- If Six of these place are considered as one, what would be the entropy?
		- $\log_2({3 \over 4}) =  0.415$, Entropy = $0.415 \times {3 \over 4} + 2 \times {1 \over 8} \times 3 = 1.06$, which intuitively means we need on average 1.06 of yes-no questions to get the location of the car.


- Example 3: A set of 6 equiprobable points. 
![[Pasted image 20221030221238.png]]


![[Screenshot 2022-10-30 221020.png]]
- Fig: Chart for log base 2. The surprise / Shannon information grows exponentially when that event is very rare.

---

![[Pasted image 20221028225322.png]]
![[Pasted image 20221028225405.png]]
![[Pasted image 20221028225527.png]]

- Fig: we cut some samples from stimulus from every trial. Sort and group the observations into distribution. 
	- The most common: silence (all zeros)
	- And only other few possible combinations.
- Noise: 
	- The noise distribution $P(w|s)$ is narrower then the total entropy distribution.
	- It is exactly this reduction in the entropy from knowing nothing about the stimulus, to know something about the stimulus that information will be capturing.


- Intrinsic capability of encoding (R3)
	- Encoding relies on the ability to generate stimulus driven variations in the output.
	- If an output has no variation, such as in this case. We're not very optimistic about its ability to encode inputs.
	- The more intrinsic variability $r$ there is, the more capacity that code has for representation. 
		- say there are 100 time-bins and each bit can equally probably contain a spike, the total entropy of a message is $log_2{2^{100}} =100$.
	- If we have a binary [[representation]] that two symbols are used equally often, then this representation has the most variability to generate stimulus.

- Total entropy
	- The total number of states regardless of what stimulus there is. 
	- For binary communication, it is $2^n$?
- Noise entropy
	- The total number of states the message $r$ can take on, when the stimulus occurs.
	- eg: The stimulus always cause first 95 bins to spike, and having 5 final bins to have 0.5 probability to spike. Thus, there are only $2^5$ states available to the neuron after/when the stimulus is presented. 

- Economy
	- When a neuron encode a stimulus, the stimulus causes the neuron to choose a certain firing pattern or set of firing patterns and to have only a small variability around that choice. 

- Information gain
	- The information gained from a message/firing pattern about a stimulus is the total entropy minus the noise entropy. 
		- eg: the way to walk through a maze, if we can get the exact way to complete the task, then that contains the most amount of information.

- [[Mutual information]]
- Mutual information (between noise and container?)
	- 
	- $I(S;R) = H[R] - \sum_S P(s)H[R|s)]$
		- s: stimulus, repeat many times to obtain $P(R|s)$.
		- $H[R|s)]$: Variability due to noise
		- $\sum_SP(s)H[R|s)]$: Repeat for all s and take an average.
		- $H[R]$: Total entropy
	- Intuition
		- Intuitively, mutual information measures the information that $X$ and $Y$ share: It measures how much knowing one of these variables reduces uncertainty about the other. 
		- If $X$ and $Y$ are independent to each other, then their mutual information is zero. If $X$ is deterministic of $Y$ and $Y$ is deterministic of $X$, then all information conveyed by $X$ is shared with $Y$. Moreover, this mutual information is the same as the uncertainty contained in $Y$ or $X$, namely the entropy of $Y$ or $X$.
	- Mutual information is a measure of the inherent dependence expressed in the joint distribution of $X$ and $Y$ relative to the marginal distribution of $X$ and $Y$ under the assumption of independence.
	- Since each stimulus yield different information gain, we look at the average information gain and call it mutual information.
		- $I(X;Y)=0$ if and only if $X$ and $Y$ are independent
	- This is characteristic of the message-transmitting system as a whole, rather than of a specific stimulus
	- Intuition:
		- It make senses that if there is a high mutual information between two random variables, then two random variables are not independent.
		- eg:
			- daily temperature and cloud cover in the city. You can narrow your guess about one thing if you have already know another.
			- Thus, the cloud cover contains some information about the temperature.


![[Pasted image 20221028230921.png]]
![[Pasted image 20221028231800.png]]
- LGN
	- Run a fixed stimulus, call it frozen white noise, which has some structure.
	- In response to that "stimulus", spikes  appeared in a time log sequence.
	- PSTH: which is a Post Stimulus Time Histogram, where these events show these large modulations in the time varying fire rate, produced in response to that stimulus. 
	- fig C:
		- At very fine time scales, there is quite a bit of jitter in those responses. 
- paper: 
	- at what time scales, do these responses continuous to convey information about the stimulus? 
	- spike train: $\delta t$ and length $L$
- fig 2:
	- As the word gets longer, for a finite amount of data, you are going to have very few sample of a word of that length.
	- When one tries to estimate the entropy of the distribution of words of this length, it's very unlikely you will have seen them all.
	- In fig2a, 
		- the entropy drop off rapidly, indicating the information is not completely sampled. --> So what we can do is, compute the entropy for different lengths of words. 
	- In fig2b.
		- one can look over different $\delta t$ and different word length to see how information depended on these parameters. 
		- There is some limits of $\delta t$ , beyond it the information doesn't grow anymore. 


---

- Loss function of binary classification: $CE(y,f(x))=-\sum_{i=1}^C(y_ilog_2f(x)_i)$

- eg: (R1)
	- [[gray level]] (i.e. $p_i = {1 \over 256}$)the number of bits needed to code each gray level is 8 bits. 


----
![[Pasted image 20220925201040.png]]
- Figure: This excel sheet shows summation over $y_ilog_2y$
![[Pasted image 20220925201050.png]]

---
![[Pasted image 20221029002634.png]]
- Fig: change illumination to see both the inside and outside of the photo.
	- Depth and perspective
	- 1. Huge dynamic range of light level and contrast that range over orders of magnitude.
	- 2. Comparing boxes, we can see similar structure, well defined shapes and objects at different length scales. 
		- This is reflected in the power spectrum of natural image. 
	- 3. $\omega$ : spatial frequency of components. 
	- 4. The graph of $log P(\omega)$ versus $\omega$ reflects the characteristic scale, in a power law form.
		- This reflects the lack of any characteristic scale.
	- 5. We would like to be able to distinguish detail at every point in it, unlike this camera.

![[Pasted image 20221029004100.png]]
- Fig:
	- Fast variations

- Coding principle
	- Efficient coding is when we map a stimulus onto a "symbol", that symbol may be many things. 
		- instance of a single spike
		- a spike train
		- instantaneous firing rate of a neuron at a moment in time.
	- 1-to-1 input-output mapping --> perfect code.
	- If each stimulus maps somewhat noisily/probabilistically to an output, we want our function to be constructed as little overlay as possible between the response distributions the different stimuli map to.
	- Best input-output function
		- It is the one that maximizes the mutual information between the distributions of response and stimulus.

![[Pasted image 20221030233112.png]]
- Fig: R3
	- A job as an encoder is to map the stimulus onto the symbols that we have at our disposal.
	- Say we have max. firing rate, so we have some limited range of possible symbols at out disposal, say 0 to 20 Hz.
	- By using all of our symbols about equally often, then we get the most information by maximizing our output entropy.
	- histogram equalization
	- A good coding system, its input output function, should be determined by the distribution of natural inputs. 

![[Pasted image 20221030233937.png]]
- Fig: R3
	- A researcher measured the typical contrasts, that is deviations in the light levels, divided by the mean light level. 
	- If response does indeed follow the distribution of natural inputs, then the response curve should look like the cumulative probability determined by integrating $p(c)$.

![[Pasted image 20221030235817.png]]
- Fig: The neuron response of a fly (R3)
	- white noise input (change every 90s) + some slow time varying envelope (repeat in every 90s)
	- Response rate (y-axis) versus stimulus (x-axis) 
	- If we normalize those curves, they fall into the same curve. What it meant is the code has the freedom to stretch its input access such that it is accommodating these variations in the overall scale of the stimulus.

![[Pasted image 20221031000256.png]]
- Adaptive representation of information
	- As one changes the characteristic of the stimulus, eg changing its overall amplitude, changes can occur in the input output function. 
	- Changes can happen in the feature, as the statistics of the inputs are changed. 

![[Pasted image 20221031000758.png]]
- Fig: Feature adaptation
	- The feature that's selected by a neural system can also adapt to changes in the stimulus statistics
	- Consider imposing a linear transformation function, or a filter, what's the shape of that filter that maximize information transmission 
		- solution depends on two things:
			- 1. The power spectrum of natural images
			- 2. The signal to noise ratio
		- At high light levels,  the filter is like a differentiator, looking for edges of the stimulus
		- At low light levels, the predicted optimal filter is integrating, avreages its inputs to reduce noise.

![[Pasted image 20221031001046.png]]
- Fig: (R3)
	- One can extract form the stimulus, some component that maximize the Colbeck-Libler Divergence between the spike conditional and the prior distributions.

- How to have efficient code?
	- Entropy reaches its max when symbols are appearing equally frequent.


---
## Reference

1. https://users.cs.cf.ac.uk/dave/Multimedia/node208.html#SECTION04241000000000000000
2. https://wachemo-elearning.net/courses/multimedia-systems-course-module-itec3121/lessons/chapter-seven-lossless-compression-algorithms-2/topic/7-2-basics-of-information-theory/
3. [[computational neuroscience]]: coursera https://www.coursera.org/learn/computational-neuroscience/lecture/K5L8z/4-1-information-and-entropy
4. [[(Paper) Information Theory-- A Tutorial Introduction]]