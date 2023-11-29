- Two-person zero sum games
- Linear programming and maximin theorem
- Bimatrix games
- Extensive form
- Cooperative games

---
## Relevance to machine learning
- Two-person zero sum games (R: 90/100)
	- Two-person zero-sum games are used in machine learning for modelling scenarios where two agents have opposing objectives, such as in adversarial machine learning and reinforcement learning. 
	- It's also relevant in reinforcement learning when modeling competitive scenarios. In big data analytics, these games can be used for decision-making in competitive markets and pricing strategies.
	- Another Examples include minimax strategies in deep learning for generating adversarial examples and the exploration-exploitation trade-off in reinforcement learning.
- Linear programming and maximin theorem (R: 75/100)
	- Linear programming is used in machine learning for optimization problems like support vector machines.
	- The maximin theorem can be applied in decision-making contexts. In big data analytics, linear programming is relevant for resource allocation and optimization in large-scale systems.
- Bimatrix games (R: 85/100)
	- Bimatrix games are used in machine learning for modeling situations with multiple agents, such as in multi-agent reinforcement learning. 
	- hey can also be applied to model strategic interactions in data-driven decision-making in big data analytics.
- Extensive form (R: 70/100)
	- Less relevant.  Extensive form games are less commonly used in machine learning and big data analytics compared to other game theory concepts. However, they can be relevant when modeling sequential decision-making in AI systems and analyzing strategic decision trees.
- Cooperative games (R: 80/100)
	- Cooperative games are relevant in machine learning for scenarios where agents collaborate to achieve a common goal, such as in ensemble learning. 
	- In big data analytics, they can be used to model collaborative data sharing and resource allocation among multiple parties.


---

### Two-person zero sum games

- Terminology: 
	- Game
		- a mathematical model describing the concerned scenario
	- Players
		- 
	- Strategies
		- We call the participants of a game players and their available actions strategies. 
		- Chance move 
			- The payoff of the action is based on probability. 
	- Payoffs
		- To apply a mathematical, objective, rational analysis on such games, we assign numbers to different players on various different outcomes based on their strategies. We call these numbers payoffs.
- Suppose the player of the game is $A_1, A_2, \dots A_N$.
- For each player $i$, the set of strategies available to that player is $S_i$. 
- Payoff function: Outcome of the game:
	- $\pi_i: S_1 \times S_2 \times \dots S_N \rightarrow \mathbb{R}$
		- Breakdown of the expression:
			- $S_1 , S_2 , \dots S_N$: it is the strategy sets for each players in the game.
			- $\times$: The [[cross product]] of the individual strategies of each players. 
			- $\rightarrow$: Indicating the mapping or function. It signifies the payoff function takes a strategy profile, and maps it to a real number.  
			- $\mathbb{R}$: Payoffs are typically expressed as real numbers. 

- constant sum game
	- If there exist $c \in \mathbb{R}$ such that ... ,that is constant sum game. 
	- $\forall s_1 \in S1, \forall s_2 \in S_2, \dots, \forall s_n \in S_n, \sum_i, \pi_i(s_1, s_2, \dots, s_N) = c$
		- The first part:
			- It is considering all possible combinations of choices or strategies from these sets.
		- The second part:
			- It means the summary of the payoff of all players are constant, after summation. 
- simultaneous game 
	- It is a kind of game which players decide their strategies without the strategies taken by other players. 

- representation of 2-person game
	- normal form 
		- The normal form is typically presented in a tabular format, with rows representing the strategies of one player and columns representing the strategies of the other player(s). 
		- conventionally, $A_1$ is the row player (rows as his strategies), $A_2$ is the column player (columns as his strategies).
	- [[payoff matrix]]
- movement diagram
	- If a rock-paper-scissors game, a player can know the action of his opponent, he would change his action accordingly. 
	- If two players has the same oversight. The train of movement would not stop. 
	- How to draw movement diagram?
		- 1
		- 2
		- 3

- Saddle point
	- Definition:
		- $\forall_i, \forall_{s_i} \in S_i,\ \  \pi_i(\vec s^*) \geq \pi_i(s_i^*, \dots, s_{i-1}^*, s_i^*, s_{i+1}^*,\dots, s_n^*)$, which $\vec s^* = (s_1*, s_2*, \dots, s_n*)$ 
		- We compare entire strategy in the left to the set of individual strategies in the right. 
		- Individual rationality versus collective rationality:
			- In game theory, we often analyze situations where multiple players make decisions simultaneously. The left-hand side of the formula, $π_i(𝐬*)$, represents the payoff or utility that player $i$ receives when they, along with all other players, follow a specific strategy profile 𝐬*. This reflects the collective rationality of all players making choices that are mutually consistent with the strategy profile 𝐬*.
		- Comparing to Individual Deviations:
			- The right-hand side of the formula, $π_i(s_i*, …, s_{i-1}, s_i, s_{i+1}, …, s_n)$, represents the payoff that player i would receive if they deviate from the strategy profile 𝐬* and play an individual strategy $s_i*$, while all other players continue following their strategies from 𝐬*. This comparison allows us to assess whether it is in player i's best interest to stick with the collective strategy profile 𝐬* or to deviate from it.
		- Breakdown:
			- $*$: The star means the utility or payoff that player $i$ reaches saddle point, denoted as $s_i^*$.
			- The first half sentence:
				- $\forall_i, \forall_{s_i} \in S_i$:
					- The definition of saddle point considers all the players in the game and all the possible strategies each player can choose.
			- Left hand side
				- $π_i(\vec 𝐬*)$: 
					- $\vec s*$: 
						- The lowercase $s$ means a specific strategy in the collection of possible strategies of $i$ ($S_i$). 
						- $*$ means such strategies could provide saddle point payoff. 
						- $\vec s$: Which means the entire strategy profile. 
							- The vector sign means "a vector of strategies". $\vec s = (s_1, s_2, \dots, s_n)$ represents a strategy profile where $s_i$ is the strategy chosen by player $i$. 
						- In summary, this notation is used to denote the payoff for player i under a specific set of strategies.
			- Right hand side:
				- $\pi_i(s_i^*, \dots, s_{i-1}^*, s_i^*, s_{i+1}^*,\dots, s_n^*)$
					- $s_i^*, \dots, s_{i-1}^*, s_i^*, s_{i+1}^*,\dots, s_n^*$:
						- Each $s$ represents an individual strategy choice for a specific player. For example, $s_i$ represents the strategy choice of player $i$, and $s_{i-1}$, $s_{i+1}$, etc., represent the strategy choices of other players in the game.
		- i.e. no one can benefit by changing alone

- [[mixed strategy]]

- N-person games probability matrix:
	- Formulation: $\mathcal{P}^n = \{ \vec p =(p_1, p_2. \dots, p_n) \in \mathbb{R}^n | \sum_{i} p_i = 1 \land \forall_i, p_i \geq 0 \}$
		- $\mathcal{P}^n$: 
			- It is our probability matrix. In this context, a probability matrix is a mathematical representation used to describe the probability distribution of strategies chosen by the players in an N-person game. It's denoted as $\mathcal{P}^n$ to emphasize that it's specific to N-person games.
		- $\vec p= (p_1, p_2. \dots, p_n) \in \mathcal{P}^n$
			- It is our probability vector
			- It represents a vector $\vec p$ consisting of $N$ components, where each component $p_i$ represents the probability that player $i$ chooses a particular strategy.
		- $\vec p \in \mathbb{R}^n$:
			- Of course, the vector belongs to the set of real numbers of dimension $N$.
		- $|$:
			- It means "such that" or "subject to".
		- $\sum_{i} p_i = 1$:
			- It ensures that the probabilities assigned to each outcome must be non-negative.
		- $\forall_i, p_i \geq 0$:
			- It means all specific strategies are non-negative events. 

- [[mixed strategy]]
	- A probability vector $\vec p = (p_1, p_2, \dots, p_{|S_i|}) \in \mathcal{P}^{|S_i|}$ is called a mixed strategy of $A_i$ 
		- We also call it pure strategy if $\exists j, p_j = 1$.
- $A_i$'s payoff
	- $\sum_{s_1 \in S_1, s_2 \in S_2, \dots, s_n \in S_n}Pr(\cdot)\ \pi_i (s_i, \dots, s_n)$
		- $Pr( \cdot )$ denotes "$P(A_1$ adopt $s_1$, $\dots$, $A_n$ adopt $s_n)$" = $P(A_1$ adopt $s_1$)$\dots$$P(A_n$ adopt $s_n$) 
			- The equal sign holds true because we assume these events are independent events. 
	- $= \sum_{j_1, j_2, \dots, j_N} (\vec p_1)_{j_1}(\vec p_2)_{j_2}\dots(\vec p_N)_{j_N} \pi_i (s_i, \dots, s_n)$
		- $(\vec p_1)_{j_1}(\vec p_2)_{j_2}\dots(\vec p_N)_{j_N}$
			- These terms represent the probabilities of each player $A_1$ through $A_N$ adopting their respective strategies $s_1, s_2, \dots, s_N$ in the game.
			- The notation $(\vec p_i)_{j_i}$ indicates the probability of player $A_i$ adopting strategy $s_i$ (i.e., the probability of event $P(A_i \text{ adopts } s_i)$).
			- The product of these probabilities represents the joint probability of all players adopting their respective strategies as specified by the indices $j_1, j_2, \dots, j_N$.

- 2 person gaming, $\vec p$, $\vec q$ are the mixed strategies adopted by Row and column player respectively.
- $\pi_k(\vec p, \vec q) = \sum_{i,j}(\vec p)_i (\vec q)_j\ \pi_k(s_i,s_j)= \vec p^T B_k \vec q$, 
	- $\vec p$, $\vec q$
		- where $\vec p$, $\vec q$ represent the mixed strategies adopted by the Row player and the Column player, respectively.
		- Mixed strategies mean players don't always choose a single pure strategy but rather select different strategies with certain probabilities.
		- $\vec p = \begin{bmatrix} (\vec p)_1 \ (\vec p)_2 \ \vdots \ (\vec p)_n \end{bmatrix}$
		- $\vec q = \begin{bmatrix} (\vec q)_1 \ (\vec q)_2 \ \vdots \ (\vec q)_m \end{bmatrix}$
	- $\pi_k(\vec p, \vec q)$
		- This function calculates the expected payoff for player k (either Row or Column player) when they play the mixed strategies $\vec p$ and $\vec q$. This is calculated as a sum of the payoffs for all possible combinations of pure strategies chosen by the players.
	- $B_k$, payoff matrix
		- where $B_k$ is the matrix with $(i,j)$-th entry, given by $\pi_k(s_i, s_j)$.
		- The note introduces the concept of a payoff matrix denoted as $B_k$. This matrix is used to compute the expected payoff for player k. Each entry in the matrix $B_k$ represents the payoff that player k receives when a specific combination of pure strategies is played. In other words, $B_k$ is a matrix that describes the outcomes of the game for each possible combination of strategies chosen by the players.
	- Inner product at "$\vec p^T B_k \vec q$"
		- Inner Product: The notation $\vec p^T B_k \vec q$ represents the inner product (also known as the dot product) between the mixed strategy vectors $\vec p$ and $\vec q$, weighted by the matrix $B_k$. This operation calculates the expected payoff for player k based on their mixed strategy choices and the payoff matrix $B_k$.
		- $\vec p^T B_k = \begin{bmatrix} (\vec p)_1 & (\vec p)_2 & \cdots & (\vec p)_n \end{bmatrix} \begin{bmatrix} \pi_k(s_1, s_1) & \pi_k(s_1, s_2) & \cdots & \pi_k(s_1, s_m) \ \pi_k(s_2, s_1) & \pi_k(s_2, s_2) & \cdots & \pi_k(s_2, s_m) \ \vdots & \vdots & \ddots & \vdots \ \pi_k(s_n, s_1) & \pi_k(s_n, s_2) & \cdots & \pi_k(s_n, s_m) \end{bmatrix}$
		- Finally, multiplying $\vec p^T B_k$ by $\vec q$ results in $\vec p^T B_k \vec q$, which represents the expected payoff for Player k when they use their respective mixed strategies.

- Nash equilibrium
	- In 2 person games, 
		- Row's payoff = $\vec p^T B \vec q$
		- Col's payoff = $- \vec p^T B \vec q$
	- A pair $(\vec p^*, \vec q^*) \in \mathcal{P}^{S_1} \times \mathcal{P}^{S_2}$ will be a Nash equilibrium if and only if $\forall \vec p \in \mathcal{P}^{|S_1|}$, $\vec p^{*T} B \vec q^* \geq \vec p^T B \vec q^*$ , and $\forall \vec q \in \mathcal{P}^{|S_2|}$, $\vec p^{*T} B \vec q^* \leq \vec p^{*T} B \vec q$


- [[perfect information ]]
- Tree diagram
	- Directed graph
		- Vertices
		- Edges

- [[zero sum games]]
	- Σ(payoffs) = 0
	- maximize their own payoffs while anticipating and countering their opponent's moves
- [[perfect information]]
	- [[payoff matrix]]
- [[strategic form]]
- optimal strategy
	- [[saddle point]]
		- How to determine?
			- [[maximin]]
			- [[minimax]]
	- stable / unstable of [[saddle point]]
- [[pure strategy]]
- [[mixed strategy]]
- [[probability vector]]
- [[expected payoff]]
- [[security level]]
- [[maximin theorem]]
- [[minimax theorem]]
- [[maximin strategy]]
- [[minimax strategy]]
- Theorem 1.22
	- Let $A = \begin{pmatrix} a & b \\ c& d\end{pmatrix}$ be a $2 \times 2$ game matrix. Suppose $A$ has no saddle point. Then:
		- The [[security level]] of the game is $v = \frac{ad - bc}{a - b - c + d}$
		- The [[maximin strategy]] for the row player is $p = (\frac{d - c}{a - b - c + d}, \frac{a - b}{a - b - c + d})$
		- The [[minimax strategy]] for the column player is $q = (\frac{d - b}{a - b - c + d}, \frac{a - c}{a - b - c + d})$

- [[dominate row or column]]
- [[2 x n and m x 2 games]]
- [[lower envelope]]
- [[principle of indifference]]
- [[zero sum game duality]]


---
### Linear programming and maximin theorem


- [[solved games]]
	- [[minimax theorem]]


---
- [[nash equilibirum]]
- [[extensive form games]]