---
category: []
alias: []
tags: []
---

- 30-10-2022 17:18: created

- Abstract:
	- Shannon’s mathematical theory of communication defines fundamental limits on how much information can be transmitted between the different components of any man-made or biological system.
- 1. Introduction
	- A basic idea in information theory is that information can be treated very much like a physical quantity, such as mass or energy. (Caude Shannon, 1985)
	- Basic laws of information:
		- 1. there is a definite upper limit, the channel capacity, to the amount of information that can be communicated through that channel
		- 2. this limit shrinks as the amount of noise in the channel increases
		- 3. this limit can very nearly be reached by judicious packaging, or encoding, of data.

$$m = 2^n$$
$$n = log_2m$$
	- m: destinations, or equiprobable values
	- n: forks, or bits, or entropy H

![[Pasted image 20221030172535.png]]
![[Pasted image 20221030172529.png]]

- Section 3: Bits are not binary digits
	- bit: amount of information = a pint of milk
	- 1 bit = One "answer" in a system of equiprobable binary communication
	- binary digits = pint-sized bottle, just a bottle that contains between zero and one point.
	- 1 binary digits = A unit that might be either 0 or 1, but no "answer" inside, so it is not information.
	- To mistake a binary digit for a bit is a category error.

- Information and entropy
	- Shannon information
		- Shannon information = $log{1 \over p(x_h)}$ bits measures surprisal of each outcome of the set of possible outcomes. 
		- eg: flip coin, 90% heads up, 
	- It often expressed as information = $-log\ p(x_h)$ bits
	- Entropy:
		- Average of surprise, weighted by their probability.
		- $H(x) =\sum_i prob._i \times v_{sur_i} = -\sum_i p(x_i) log p(x_i)$ 
		- Intuition:
			- $m = 2^{0.469}$ or 1.38 equiprobable values / bits 
- For a binary 1-digit event, the maximum entropy is "fair coin", i.e. $-log(0.5) \times 2$ 
- Insight:
	- The more the agents tells you some unlikely occurring data, the more informative it is.
![[Pasted image 20221030180725.png]]
- 

- Section 7: channel capacity
	- Channel is the additive channel.
	- As encoded values pass through an additive channel, $\eta$ , so that the channel output is a noisy version $y$ of the channel input $x$. 
	- channel capacity $C$ is the max info that a channel can provide at its output about the input.
	- Information rate:
		- 1. $H(x)$ : the entropy of the input
		- 2. $H(y)$: The entropy of the output
		- 3. $H(\eta)$: The entropy of the noise in the channel.
![[Pasted image 20221030182951.png]]

- A noiseless channel with communicates $R$ binary digits per second can communicate information at the rate of up to $R$ bits/s.
- the capacity $C$ is the max rate at with it can communicate info from input to output, if follows that the capacity of a noise less channel is equal to the number of $R$ of binary digits communicated per second.

- Shannon's fundamental theorem for a discrete noiseless channel / first fundamental coding theorem
	- Say source: entropy H, channel: capacity C, then it is possible to encode the output of the source to transmit at the average rate C/H (symbols / s)
	- 1. Max output rate = $C/H$. 
	- 2. Channel capacity $R<C$ is the max rate communicate info from input to output.
	- 3. Channel capacity $C = \underset{p(x)}{max} H(x)$ bits per second.
		- The shape of distribution puts an upper limits on the entropy of $H(x)$ and 

- Section 9: Noise reduces channel capacity
	- Some of the entropy of output due to noise , so not all of the output entropy comprises information about the input.