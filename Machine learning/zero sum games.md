**Introduction:**
Zero-sum games are a fundamental concept in mathematical game theory, a field that examines strategic interactions among rational decision-makers. These games are characterized by a specific mathematical property wherein one player's gain is exactly balanced by another player's loss, resulting in a constant sum of payoffs equal to zero.

**Formal Definitions:**
1. **Constant Sum Property:** In a zero-sum game, the sum of the [[payoff matrix|payoffs]] to all players remains constant, represented mathematically as:
		∑(Player i's Payoff) = 0 for all players i
	Demonstrated: In a simple example of a two-player zero-sum game, if Player A wins $10, Player B loses $10. The sum of their payoffs is indeed 0: 10 + (-10) = 0.

2. **Competitive Nature:** Zero-sum games are inherently [[competitive]], defined by the antagonistic interests of the players. Each player seeks to maximize their own utility while minimizing the utility of their opponents.
   Demonstrated: In a chess match, Player A capturing Player B's pawn increases Player A's advantage while simultaneously reducing Player B's position, showcasing the competitive nature of zero-sum games.

3. **[[pure strategy|pure strategies]]:** Players typically select strategies from a finite set of pure strategies. A pure strategy for a player $i$ is represented as $S_i$, and the outcomes of these strategies are defined in a payoff matrix, where entries $(S_i, S_j)$ represent the utility associated with the chosen strategies of players $i$ and $j$.

   Demonstrated: In a game theory matrix for a simple two-player game, Player A can choose "Cooperate" or "Defect," and Player B can also choose "Cooperate" or "Defect." The matrix shows the outcomes and utilities for each combination of choices, illustrating pure strategies.

4. **Minimax Theorem:** In zero-sum games, the Minimax Theorem is a fundamental concept. It states that for a two-player zero-sum game, there exists a strategy for each player such that the maximum possible gain for one player is equal to the minimum possible loss for the other player. Mathematically:

   $Max(min(U_i(S_i, S_j))) = Min(max(U_j(S_i, S_j)))$

   Demonstrated: In a game of poker, Player A and Player B both have strategies to maximize their gains while minimizing their losses. The Minimax Theorem ensures that Player A's best strategy aligns with Player B's best strategy, resulting in a balanced outcome.

**Examples:**
1. **Rock-Paper-Scissors:** Even in a simple game like Rock-Paper-Scissors, the constant sum property holds true, with one player's victory directly corresponding to the other's defeat.

   Demonstrated: If Player A plays "Rock" and Player B plays "Scissors," Player A wins while Player B loses, showing the constant sum property.

2. **Chess:** In chess, a player's gain of material or positional advantage is mirrored by their opponent's loss, adhering to the zero-sum characteristic.

   Demonstrated: When Player A captures Player B's knight, Player A gains an advantage while Player B loses a piece, illustrating the zero-sum nature of chess.

3. **Poker:** Various forms of poker, including Texas Hold'em, exemplify zero-sum games where chips won by one player are simultaneously lost by others.

   Demonstrated: In a poker game, when Player A wins a pot of chips, the total winnings and losses at the table remain zero-sum as other players lose chips.

**Applications:**
1. **Economics:** Zero-sum games are widely used to model economic scenarios, including competitive markets, bargaining situations, and trade disputes.

   Demonstrated: In a competitive market, if one company gains market share, others lose it, reflecting the constant sum property.

2. **Conflict Resolution:** Game theory, particularly zero-sum game analysis, is applied to resolve conflicts and formulate negotiation strategies in diplomatic and military contexts.

   Demonstrated: In a diplomatic negotiation, if one party gains a concession, the other party concedes, illustrating the antagonistic nature of negotiations as zero-sum games.

3. **Sports:** Some sports, such as tennis and boxing, can be analyzed as zero-sum games where one athlete's success directly corresponds to the other athlete's failure.

   Demonstrated: In a tennis match, when Player A wins a point, Player B loses it, reflecting the zero-sum nature of competitive sports.

---
- Related concepts:
	- [[nash equilibirum]]
	- [[mixed strategy]]
	- [[payoff matrix]]
	- [[saddle point]]￼￼nash equilibirum￼￼
	- [[pareto efficiency]]
	- [[extensive form games]]
	- [[zero sum game duality]]
	- [[repeated games]]
	- 