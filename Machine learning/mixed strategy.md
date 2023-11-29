**Concept**: Mixed Strategy in Mathematical Game Theory

**Context**: Mathematical Game Theory

**Notes**:

1. **Introduction to Mixed Strategies**:
   - In mathematical game theory, mixed strategies are a fundamental concept used to analyze strategic interactions in games.
   - Unlike pure strategies, where a player makes a single, deterministic choice, mixed strategies involve a probability distribution over the set of available pure strategies.

- Definition:
	- A mixed strategy is a row vector $x = x_1, x_2, \dots, x_m) \in R^m$ such that:
		- $x_1 \geq 0$ for any $i = 1,2, \dots, m$
		- $\sum_{i=1}^m x_i = 1$
		- When $x$ is used , the player uses his $i$-th strategy with a probability of $x_i$ for $i = 1,2, \dots, m$.  
	- In other words, a vector is a mixed strategy if it is a probability vector. 
	- We will denote the set of probability $m$ vectors by $P^m$. 
	- Mixed strategies are generalization of [[pure strategy]]

2. **Pure vs. Mixed Strategies**:
   - Pure strategies involve making a single, definite choice, like always playing Rock in Rock-Paper-Scissors.
   - Mixed strategies, on the other hand, involve randomizing decisions. For example, a player may choose Rock with a 50% probability and Paper with a 50% probability in the same game.

3. **Representation of Mixed Strategies**:
   - Mixed strategies are represented using probability distributions. In a game with 'n' pure strategies, a mixed strategy is typically represented as a vector of probabilities $(p_1, p_2, \dots, p_n)$ where each pi represents the probability of choosing the corresponding pure strategy.

4. **Expected Payoffs and Utility**:
   - When analyzing games with mixed strategies, players calculate their expected payoffs or utilities based on the probabilities assigned to each pure strategy.
   - Expected payoff is the average payoff a player can expect to receive over many repetitions of the game when following a particular mixed strategy.

5. **Nash Equilibrium with Mixed Strategies**:
   - Nash equilibrium is a central concept in game theory where no player has an incentive to unilaterally change their strategy.
   - Mixed strategy Nash equilibria occur when at least one player employs a mixed strategy, and the probabilities are such that no player can gain by deviating from their strategy.

6. **Applications**:
   - Mixed strategies find applications in various real-world scenarios, such as economics (e.g., oligopoly pricing), biology (e.g., animal foraging behavior), and even in military strategy.

7. **Randomization and Uncertainty**:
   - Mixed strategies are often used when there is inherent uncertainty in the game, or when players want to introduce an element of unpredictability to their actions.

8. **Behavioral Insights**:
   - The study of mixed strategies has provided valuable insights into human behavior and decision-making, especially when individuals face strategic uncertainty or when there is incomplete information.

9. **Computational Complexity**:
   - Solving games with mixed strategies can be computationally challenging, especially for large-scale games. Various algorithms and techniques have been developed to find mixed strategy equilibria.

10. **Conclusion**:
    - Mixed strategies are a crucial concept in mathematical game theory, allowing for a more nuanced analysis of strategic interactions. They capture the idea that in many situations, players may choose to be unpredictable or randomize their actions to maximize their expected outcomes. Understanding mixed strategies is essential for gaining insights into the dynamics of complex strategic situations.