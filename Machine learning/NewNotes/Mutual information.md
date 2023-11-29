---
category: []
alias: []
tags: []
---

- 30-10-2022 22:21: created

- What is Mutual information?
	- In probability theory and information theory, the mutual information (MI) of two random variables is a measure of the mutual dependence between the two variables.  (wiki), expressed in the joint distribution of $X$ and $Y$ relative to the marginal distribution of $X$ and $Y$ under the assumption of independence.
	- $I(X;Y)=0$ if and only if $X$ and $Y$ are independent
	- The mutual information $I(x,y)$ between two variables, such as a channel input $x$, and output $y$, is the average amount of information that each value of $x$ provide about $y$. (R2)
		- Recall: the total number $m_y$ of equiprobable output states is $m_y = m_x \times m_\eta$ 
		- $H(y) = log_2(m_y)$
		- $H(y) = log_2(m_x) + log_2(m_\eta) = H(x) + H(\eta)$
		- $I(x,y) = H(x) = H(y) - H(\eta)$ bits
	- In [[computational neuroscience]],
		- $MI(S,R) = H_{\text{total}} - H_{\text{noise}} = H[R] - \sum_S P(s)H[R|s)]$,  
			- $S$ stands for stimulus (input) that repeated many times
			- $R$ stands for response (output) to the stimulus
	- Intuition
		- Intuitively, mutual information measures the information that $X$ and $Y$ share: It measures how much knowing one of these variables reduces uncertainty about the other. 
		- If $X$ and $Y$ are independent to each other, then their mutual information is zero. If $X$ is deterministic of $Y$ and $Y$ is deterministic of $X$, then all information conveyed by $X$ is shared with $Y$. Moreover, this mutual information is the same as the uncertainty contained in $Y$ or $X$, namely the entropy of $Y$ or $X$.
		- It make senses that if there is a high mutual information between two random variables, then two random variables are not independent.
			- daily temperature and cloud cover in the city. You can narrow your guess about one thing if you have already know another.
			- Thus, the cloud cover contains some information about the temperature.

![[Pasted image 20221030225556.png]]
- Fig: R1

![[Pasted image 20221030230432.png]]
- Fig: R2
	- If there is no noise, the entropy is just the entropy of the response.
	- As error grows, mutual information drops. Spiking is less and less likely represent the stimulus $s$.
---
## Reference

1. [[(Paper) Information Theory-- A Tutorial Introduction]]
2. [[computational neuroscience]]: coursera https://www.coursera.org/learn/computational-neuroscience/lecture/K5L8z/4-1-information-and-entropy