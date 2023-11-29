- 7-10-2022: created

- [[no free lunch]]

- Two general purpose "black-box" optimization that exploit little if any knowledge concerning the optimization problem on which they can run.
	- [[evolutionary algorithm]]
	- simulated annealing mimic processes in natural selection and statistical mechanics respectively.

---
## Section 2
- Introducing the necessary notation

- combinatorial optimization in which the search space $\mathcal{X}$, perhaps quite large, is finite. Assume that the space of possible cost values, $\mathcal{Y}$, is also finite.
- these restriction is automatically met for optimization algorithms run on digital computers. eg: $\mathcal{Y}$ is some 32 or 64 bit representation of the real numbers.
- The size of the spaces $\mathcal{X}$ and $\mathcal{Y}$ are indicated by |$\mathcal{X}$| and |$\mathcal{Y}$| respectively. Optimization problem $f$ ([[Loss function|cost function]] / [[objective]] / energy functions) are represented as [[Feature map|map]] $f: X \mapsto Y$. $\mathcal{F} = \mathcal{Y}^\mathcal{X}$ is then the space of all possible problems, which is a very large but finite number. 
- Many searching algorithms are wasteful, i.e. they don't remember where they have already searcheed and therefor often revisit the same points. 
- A time-[[ordered set]] of $m$ distinct visited points a sample of size $m$. samples are denoted by $d_m = \{(d_m^x(1), d_m^y(1)), \dots, (d_m^x(m), d_m^y(m))\}$. 
-  $d_m^x(i)$ indicates the $\mathcal{X}$ value of $i$th successive element in a sample of size $m$ and $d_m^y(i)$ is the associated cost or $\mathcal{Y}$ value. 
- $d_m^y = \{(d_m^y(1), , \dots, d_m^y(m))\}$ will be used to indicate the [[ordered set]] of [[Loss function|cost]] value.
- The space of all sample of size $m$ is $\mathcal{D}_m = (\mathcal{X} \times \mathcal{Y})^m$, so $d_m \in \mathcal{D}_m$.

![[Visualized.png]]
- Figure: My own version of the math part of section 2. 

---
## Section 3
- "Roughly spearking, we show that for both static and time dependent optimization problems, the average performance of any pair of algorithms across all possible problems is exactly identical. 
- "This means in particular that if some algorithm $a$ 's performnace is superior to that of another algorithm $a_2$ over time over some set of optimization problems, then the revenue must be true over the set of all other optimization problems. "
  
---
## Section 4
- Present a geometric interpretation of the NFL theorems.
- we show that an algorithm's average performance is determined by how 'aligned' it is with
the underlying probability distribution over optimization problems on which it is run.
- This section is critical 

---
## Section 5
- Demonstrates NFL theorems allow one to answer a number of what would otherwise seem to be intractable question. Also showing the result of the algo performance and of how best to compare optimization algorithms are explored. 




![[1996 Wolpert, No free lunch theorems for optimization.pdf]]