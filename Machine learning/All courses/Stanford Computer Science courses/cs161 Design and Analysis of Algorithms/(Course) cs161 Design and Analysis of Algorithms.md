- Overview of the content of this course
	- 1. Algorithm analysis


---
- Outline of the subject:
![[Pasted image 20230610213105.png]]

---
# Course topic
- vocabulary for design and analysis of algorithms
	- eg: big oh notation
	- sweet spot for high level reasoning about algorithms, which is to ignore constant factors and lower-order terms. and to concentrate on how well algorithm performance scales with large input size.
	- big oh notation is the way to mathematize the sweet spot. 
- divide and conquer algorithm design paradigm
	- there is no silver bullet in algorithm design. 
	- d and c algorithm is to break down problems into smaller one and then quickly combine the solutions to the sub problems into one for the original problem that you care about. 
	- applications:
		  sorting 
		  matrix multiplication
- randomization in algorithm design
	- properties
		- flip coins during execution
		- different executions on fixed input
		- randomization often leads to simple elegant practical solutions
	- application
		- quicksort
		- primality testing
		- graph partitioning 
		- hashing
			- hash function
			- hash map
- computational primitives, (for reasoning about graphs )
	- fast primitives are essentially free, in terms of running time. 
		- in computer science, fast primitives refers to "computational operations that can be executed very quickly", often in time that is proportional to the size of the input. 
		- these primitives are designed to be highly efficient and optimized, with the goal of minimizing the time required to perform a given task.
	- apply them whenever possible, even in preprocessing step
	- examples:
		- sorting - one canonical example of a very fast, almost for-free primitive of this form. 
		- connectivity information
		- shortest paths (graph traversal algorithms)
		- data structures, such as hash tables, and balanced binary search trees. 
	- because these primitives can be executed quickly, they are often used as building blocks in the design of more complex algorithms and data processing pipelines. 
- use and implementation of data structures
	- organize data for fast queries
	- different structures support different queries
	- familiarity with basic structures (arrays, lists, stacks, queues, trees, heaps)
	- maintains ordering on set of elements, supports queries in logarithmic time, supports fast insert and lookup queries
- Skills you will learn
	- Better programmer
		- Assume you know lists, stacks, queues. You have seen heaps and trees. 
		- Two data structures - 
			- binary search trees
				- dynamically maintain an ordering on a set of elements, while supporting a large number of queries that run in time logarithmic in the size of the set. 
			- hash tables
				- It keep track of a dynamic set, while supporting extremely fast insert and lookup queries. 

- Part 2:
	- Items to be discussed:
		- Greedy algorithms with applications to minimum spanning trees, scheduling, and information theoretic coding.
		- Dynamic programming algorithms with example applications in genome sequence alignment and the shortest path protocols in communication networks.
		- NP complete problems and how to approach them.
	- NP complete problems
		- NP complete problems are problems that, assuming a famous mathematical conjecture you might have heard of, which is called the "P not equal to NP" conjecture, are problems that cannot be solved under this conjecture by any computationally efficient algorithm. 
		-  We'll discuss the theory of NP completeness, and, with a focus on what it means for you as an algorithm designer. We'll also talk about several ways to approach NP complete problems, including: fast algorithms that correctly solve special cases; fast heuristics with provable performance guarantees; and exponential time algorithms that are qualitatively faster than brute force search. 
	- Fast heuristics with provable guarantees
		- They are algorithms that use heuristics or rules of thumb to find solutions to problems quickly, while still having provable guarantees about the quality of the solutions they produce. 
		-  These algorithms are designed to trade off speed for accuracy, as they sacrifice the certainty of producing an optimal solution for the ability to produce a good solution quickly.
		- The heuristics used in these algorithms are typically based on some sort of prior knowledge about the problem being solved, and are often optimized through empirical testing. 
		- The provable guarantees that these algorithms provide typically come in the form of worst-case analysis, which shows that the algorithm will produce a solution of a certain quality within a certain amount of time.
		- Fast heuristics with provable guarantees are commonly used to solve NP-complete problems, which are difficult problems that cannot be solved in polynomial time using current algorithms. By using heuristics to find approximate solutions quickly, these algorithms can provide practical solutions to these problems in many real-world applications.
		- Examples:
			- Approximations
			- Metaheuristics: simulated annealing, tabu search, genetic algorithm
			- Local search: starts with an initial solution and iteratively improve it by making small changes to the solution.
			- Branch and bound: divide the search space into smaller subspaces and systematically explore them to find the optimal solution
			- Randomized: use randomization to speed up the search for a solution.
	- Fast exact algorithms for special cases
	- Exact algorithms that beat brute-force search
		- Faster than brute force search by exploiting some characteristics of the problem, such as symmetries and substructures. 

- Skills:
	- Better programmer
		- high level problem solving strategies
		- learn several fast subroutines for processing data and several useful data structures for organizing data that can be deployed  directly in your own programs
	- fair amount of mathematical analysis
		- to explain why things are the way they are. 
		- good algorithmic ideas usually require nontrivial mathematical analysis
	- start "thinking algorithmically"
		- can be applied to many fields in the real world
	- literacy with computer science's greatest hit

- doesn't matter which language you know
	- many professional computer scientists don't feel they really understand an algorithm until they have coded it up.
- should have some mathematical experience
	- basic discrete math, proofs by induction etc. 

---

## Lecture 1 Introduction

- Why we learn algorithm?
	- Algorithms are fundamental to all areas of CS
	- Algorithms are useful
	- Algorithms are fun

### Karatsuba Integer Multiplication
- This algorithms shows how algorithms can be way more efficient and outperform naive approaches. 
- This algorithms show the power of recursive thinking and understand how to break down complex problems into smaller, more manageable subproblems. 
- Input:
	- 2 $n$-digit numbers $x$ and $y$
- Output:
	- the product $x \cdot y$ 
- The way we will access the performance of the algorithm is, through the number of basic operations that it performs. 
- Basic/primitive operations
	- adding or multiplying two single digits numbers together?
- Grade school algorithm
	- that is called "correct" algorithms
	- the algorithm will eventually terminates will be answer we want
	- the amount of time needed to carries the computations
	- upshot:
		- the number of operations overall $\leq$ constant $\times n^2$.
- The algorithm designer's Mantra
	- perhaps the most important principle is to refuse to be content
	- can we do better?
- Karatsuba multiplication
	- this algorithm in this subject shows the algorithm design space is rich.
		- there are arrays of options to solve the problem
	- say $x = 5678$, $y = 1234$
	- we treat $56 = a$, $78 = b$. $12 = c$, $34 = d$. 
	- step 1: compute $a \cdot c$, $b \cdot d$
	- step 2: compute $(a+c)(b+d)$
	- step 3: compute step 2 - step 1
	- step 4: get the result
- grade school algorithm is not the only way in the town. 

- A recursive algorithm (a simpler approach to integer multiplication)
	- that is algorithms which invoke themselves as a subroutine with a smaller input.
	- to make recursion works, we form the input in smaller size.
	- write $x = 10^{\frac{n}{2}}a + b$,  $y = 10^{\frac{n}{2}} + d$ m where $a,b,c,d$ are $\frac{n}{2}$ digit numbers
		- example: $a = 56 , b = 78, c = 12, d = 34$
	- $x \cdot y$ = $10^{n} ac + 10^{\frac{n}{2}}(ad + bc) +bd$
	- idea:
		- it suggest a recursive approach to multiplying two numbers 
		- recursively compute $ac, ad, bc, bd$, which are smaller numbers. compute in the straight forward way. 
	- Q: can we just do 3 recursive call instead of 4 in each recursion?
	- A: yes.
		- compute $ac, bd$, and $(a+b)(c+d) = ac + ad + bc +bd$
		- then compute 3 -1-2 = $ad + bc$
		- so we only need 3 recursion? (and some addition)
- recursive algorithm need a base case so it won't call itself infinitely. 

- Time complexity on naive approach versus Karatsuba algorithm approach
	- analysis:
		- Naive method:
			- Time complexity: $O(n^2)$
			- Breakdown:
				- say we have $m$-digits times $n$-digits numbers. 
				- in the first layer, we do a multiplication, and we might do an addition. So the number of operations is $\leq 2n$ per row.
				- and we have $m$ rows
				- so we need $\leq 2n \cdot m$ to complete the whole computation.
			- Memory required:
				- Grows linearly ($O(n)$) with the number of digits in the input numbers.
				- eg: $1234 \times 5678$, store 4 intermediate results: `4 * 5678, 3 * 5678, 2 * 5678, 1 * 5678`
		- Karatsuba:
			- Time complexity: $O(n^{log2(3)}) = O(n^{1.585})$
			- Breakdown:
				- The improvement in time complexity of the Karatsuba algorithm stems from the observation that we can compute the product of n-digit numbers using only three recursive multiplications on $\frac{n}{2}$ digit numbers. 
			- Memory required:
				- Memory required for each level: $3 \times \frac{n}{2}$, 
					- Multiplication of the high-order parts: $\frac{n}{2}$
					- Multiplication of the low-order parts: $\frac{n}{2}$
					- Multiplication of the cross terms: $\frac{n}{2}$
				- Sum of all levels: $O(log\ n)$
					- Consider the total number of levels in the recursion $k$, is the number of halving the $n$ until the $n$ decreases to be $1$. 
					- So we have $\frac{n}{2^k} \leq 1 \implies n \leq 2^k \implies k \geq log_2(n)$
				- eg: $1234 \times 5678$,  store 2 intermediate results in each level, and the length of the variable reduces in each level. 
---

### Divide and conquer

### Recurrence relation
- Definition
	- Recurrence means using one or more previous terms to express the current term.
	- Usefulness:
		- Recursively define the elements of a sequence based on their relationship with earlier elements. 
	- General form:
		- $a_n = f(a_{n-1}, a_{n-2}, \dots, a_{n-k})$
		- where $a_n$ represents the $n^{th}$ term of the sequence, $f$ determines the relationship between the terms. $a_{n-1}, a_{n-2}, \dots, a_{n-k}$ are the previous terms in the sequences. 
		- $f$ might involves arithmetic operations, logical operations, or any other mathematical operations that necessary to determine the next item based on the previous term. 
- Types of recurrence relations
	- Linear recurrence relation
	- Homogeneous recurrence relation
		- Fibonacci sequence 
	- Non-homogeneous recurrence relation
- Base cases
	- recursive function includes a base case, which specifies the condition under which the function stops calling itself and returns a value, effectively terminating the recursion. 
- Function call stacks
	- Recursion relies on the function call stack to manage the recursive calls. Each function call is pushed onto the stack, and return values are computed as the calls are popped off the stack.
- Indirect problem solving
	- Recursion allow tackling complex problem by recursively solving smaller instances of the same problem, gradually building up the solution.
- Mathematical manipulation:
	- Be comfortable with manipulating and simplifying recurrence relations using algebraic techniques such as factoring, substitution and rearrangement. 
- Potential efficiency concerns
	- Recursive solutions may suffer from performance issues like excessive memory usage and redundant computations if not implemented carefully or optimized using techniques like memorization. 
- Inductive reasoning
	- Proving the correctness of recursive algorithms often requiring inductive reasoning and establishing the base case and inductive step.
- Solving techniques
	- substitution method
	- recursion tree method
	- iterative method:
		- it refers to the process of repeating a set of instructions or block of code multiple times, until a certain condition is met, or a specific number of iterations are completed. 
		- control flow - iteration follow a straightforward control flow, where the loop condition is evaluated at each iteration to determine whether to continue or terminate the loop
		- stack efficiency - iterative solutions generally require less memory compared to recursive solutions since they do not involve function call stack operations. 
		- tailoring efficiency - in some cases iteration is more efficient because the function have direct access to elements or indices. 
		- code clarity - iterative code can sometimes be more readable and easier to understood. 
	- master method
- Run-time / Time complexity analysis
	- For example, we can analyze the run-time of Karatsuba algorithm. 
		- Let $T(n)$ be the runtime of the algorithm
			- In Karatsuba algorithm, we break multiplications into 4 subproblems in each level. 
			- So $T(n) = 4T(n/2) + O(n)$
				- where $T(n)$ is still a unknown function in the moment
				- $O(n)$ is linear cost which depends on the length of $n$ 
		- By repeatedly breaking up the problems into subproblems, we find that: 
			- $T(n) = 4T(n/2) = 16T(n/4) \dots = 2^{2t}T(\frac{n}{2^t}) = n^2T(1)$
- Iterations versus recursion
	- sds
- Examples using recursion
	- Fibonacci sequence
	- Merge sort
	- Binary search
	- Dynamic programming
- Induction proofs
	- how mathematical induction is used to prove the correctness of solutions to recurrence computations
- Boundary conditions:
	- Pay attention to the initial conditions or base cases needed to solve recurrence relations. These conditions provides a starting point for the recursive computation.
- Practical consideration
	- Optimizing algorithm performance
	- Designing efficient algorithms
	- Understanding the limitations of recursive approaches

---
- Why Romans are so bad at multiplications?
	- What is LXXXIX times CM
	- Roman numerals is a pretty lousy data structure if you want to do arithmetic.
---
## Lecture 2 Merge Sort, Recurrences 101, Asymptotic analysis

### Writing pseudo code
- Pursuing qualities of pseudo code
	- Clarity and readability
		- Pseudocode should be clear, concise, and easily understandable. It should communicate the algorithm's logic effectively to both the reader and the programmer who will eventually translate it into code.
	- Modularity
		- Encourage modularity by breaking down complex algorithms into smaller, manageable tasks. Use subroutines or functions to encapsulate these tasks, promoting code reuse and readability.
	- Simplicity and efficiency
		- Aim for simplicity and efficiency in your pseudocode. Simplify complex operations, eliminate redundancies, and consider algorithmic optimizations if applicable.
- Structures in pseudo code
	- Pseudocode should follow a structured approach similar to the flow of control structures in programming languages. It should include constructs such as sequence, selection (if-else), iteration (loops), and subroutines (functions).
	- Flesh out these:
		- Sequence
		- Selection
		- Iteration
		- Subroutines
		- Error handling
			- Consider how you will handle errors or exceptional cases in your algorithm. Include appropriate error-checking mechanisms or exception handling if required.
		- Comments
			- Add comments within the pseudocode to explain the purpose, logic, or any other relevant details. Comments help others understand your algorithm better.
		- Testing and verification
- Items in pseudo code
	- Variables and data structures
		- Use appropriate variable names that are meaningful and representative of their purpose. Declare variables when necessary and define the data structures you plan to use in your algorithm.
	- Inputs and outputs
		- Clearly specify the input requirements and expected output of the algorithm. This can include defining input parameters, reading from user input or files, and displaying output.
		- That is similar to giving annotation to the inputs and outputs in programming 
	- Expressing operations in pseudo code 
		- Use standard mathematical notations and logical operators to express operations. This includes arithmetic operations (`+, -, *, /`), logical operations (AND, OR, NOT), and relational operators `(>, <, ==, etc.)`


### Stating the problem formally

### Loop invariant
- Meaning of this entity
	- In mathematics, invariant means  "a object that remains unchanged after operations or transformations of a certain type are applied to the objects".
	- In computer science, loop invariant means a property of a program loop that is true before (and after) each iteration. 
	- When the first two properties (initialization and maintenance) hold, the loop invariant is true prior to every iteration of the loop. Which is similar to mathematical induction.
	- The third property is properly the most important one when we are showing correctness. 
		- The termination differs from how we usually use mathematical induction, in which we use inductive step infinitely. 
		- Here, we stop the induction when the loop terminates. 
- Usefulness
	- We use loop invariants to help us understand why an algorithm is correct. We must show three things about a loop invariant. We often have to use "loop invariant" to prove your algorithm is correct. 
	- the invariant should be helpful in reasoning about the algorithm's correctness and properties. It should provide insights into how the loop variables change and what guarantees can be made about them 
- Components: 
	- Initialization
		- it is true prior to the first iteration of the loop
	- maintenance
		- if it is true before an iteration of the loop, it remains true before the next iteration
		- a more formal treatment would require us to state and show a loop invariant for the while loop. 
	- termination
		- when the loop terminates, the invariant gives a useful property that helps show that the algorithm is correct. 


- Example of running these 3 property for insertion sort:
	- Initialization
		- when $j = 2$, the subarray $A[1, \cdots, j-1]$ consists of just one element $A[1]$. 
		- Moreover, it is sorted, which shows that the loop invariant holds, prior to the first iteration of the loop. 
	- Maintenance
		- informally, the body of the for loop works by moving $A[j-1]$, $A[j-2]$ and so on until if finds the proper position. 
	- Termination
		- examine what happens when the loop terminates. 
		- in insertion sort, each loop iteration increases $j$ by 1, we must have $j = n+1$ at the time of termination. 
		- Substituting $n+1$ for $j$ we have subarray $A[1, \cdots, n]$ consists of the elements originally $A[1, \cdots, n]$ is sorted order. 
		- Observing the array $A[1, \cdots, n]$  is the entire array, we conclude that the entire array is sorted. 

- examples of loop invariant, applications:
	- binary search:
		- In a binary search algorithm, a common loop invariant is that the target element, if present in the sorted portion of the array being searched, must lie between the low and high indices of the current subarray.
	- selection sort
		- In selection sort, after each iteration of the outer loop, the smallest remaining element is placed at its correct position in the sorted portion of the array.
	- bubble sort
		- In bubble sort, after each iteration of the inner loop, the largest remaining element "bubbles up" to the correct position at the end of the unsorted portion of the array.
	- quick sort
		- In the partition step of quicksort, the elements to the left of the pivot are smaller than or equal to the pivot, and the elements to the right of the pivot are larger than the pivot.
	- insertion sort
		- In insertion sort, after each iteration of the inner loop, the current element being considered is inserted into its correct position within the sorted portion of the array.

### Correctness of an algorithm
- "Correctness of an algorithm" refers to the property of an algorithm that ensures it produces the correct and desired output for all possible inputs within its defined scope. In other words, an algorithm is considered correct if it solves the problem it was designed to solve and provides the expected results consistently.
- Criteria need to be satisfied:
	- 1. Input-Output Relationship: 
		- The algorithm should produce the correct output for every valid input. It should adhere to the problem's specifications and constraints, providing the desired results within the expected range or format.
	- 2. Termination: 
		- The algorithm should terminate after a finite number of steps for any input. It should not enter an infinite loop or run indefinitely without producing a result.
	- 3. Partial Correctness: 
		- The algorithm should maintain "partial correctness" throughout its execution. This means that if the algorithm terminates, the output it produces should be correct, satisfying the problem's requirements.
		- However, partial correctness does not provide any guarantees about the termination of the algorithm itself. There may be cases where the algorithm does not terminate but still maintains correctness based on the problem's specifications.
	- 4. Preservation of Invariant: 
		- If an algorithm uses an invariant (a condition that holds true at a specific point during execution), it should preserve that invariant as it progresses. This ensures that the algorithm's assumptions and conditions remain valid and do not lead to incorrect results.

- Methods of determine algorithm correctness:
	- 1. Loop invariant 
		- Loop invariants are conditions that hold true before and after each iteration of a loop. They help ensure that the algorithm is correctly executed within a loop. The course may teach how to identify and use loop invariants as a technique for proving algorithm correctness.
	- 2. Mathematical induction
		- Mathematical induction is a powerful proof technique used to establish correctness for algorithms that involve repetitive or recursive steps. The course may introduce mathematical induction and demonstrate its application in proving the correctness of algorithms.
	- 3. Formal proofs
		- The course may cover various proof techniques, such as direct proofs, proof by contradiction, and proof by contrapositive, which are commonly used to demonstrate the correctness of algorithms.


### Insertion sort
- Basic concept and purpose of insertion sort
	- Insertion sort is a simple comparison-based sorting algorithm that builds the final sorted array one element at a time. 
		- It is an in-place algorithm, meaning it doesn't require additional memory beyond the input array.
	- The algorithm divides the array into two portions: a sorted portion and an unsorted portion. 
		- Initially, the sorted portion contains only the first element of the array, and the rest of the elements are in the unsorted portion. 
		- The algorithm iterates over the unsorted portion, taking one element at a time and inserting it into its correct position within the sorted portion.
		- The algorithm divides the array into two portions: a sorted portion and an unsorted portion. Initially, the sorted portion contains only the first element of the array, and the rest of the elements are in the unsorted portion. The algorithm iterates over the unsorted portion, taking one element at a time and inserting it into its correct position within the sorted portion.
		- This process is repeated until all elements from the unsorted portion have been inserted into the sorted portion, resulting in a fully sorted array.
- Properties
	- Time complexity of insertion sort is also $O(n^2)$, which means that it's not an optimal sorting algorithm for large input sizes.

- Algorithmic steps
```sql
procedure insertionSort(array):
    for i from 1 to length(array) - 1 do
        key := array[i]
        j := i - 1 // One to j means sorted part of the array
        while j >= 0 and array[j] > key do 
        //if there are any elements in the sorted part bigger than key, switch place, repeat.
            array[j + 1] := array[j]
            j := j - 1
        end while
        array[j + 1] := key 
        //terminate the forward lookup when no disorder found near the boundary
    end for
end procedure
```

- Time complexity
	- Assumptions:
		- The time cost for comparing and inserting elements is considered uniform in this analysis. 
	- Best case: 
		- When the input array is already sorted, insertion sort has a time complexity of $O(n)$. This is because in the best case scenario, each element in the array only needs to be compared to its previous element, and no actual swapping or shifting of elements is required.
	- worst case: 
		- apart from comparing elements, the algorithm also perform insertion. Both comparing and insertion cost uniform time-cost. from element $1$ to element $n$, the sum of the time-cost would be a geometric sequence $1+2+\dots+ (n-1) + n \implies O(n^2)$ 

- Space / memory complexity 
	- Since insertion sort performs all its operations directly on the input array without creating any auxiliary data structures, the space complexity of insertion sort is considered to be $O(1)$, or constant space. 
	- Regardless of the size of the input array, the amount of extra space used by the algorithm remains constant. 
	- This makes insertion sort efficient in terms of space utilization, particularly when working with large arrays where memory constraints are a concern.

- Applications:
	- Small input size
	- Partially sorted list
	- Online sorting (where data arrives incrementally)
	- Teaching and learning (It is easy for beginner to understand)

- comparison with other sorting algorithms
	- Nonetheless, it can be useful for small arrays or nearly sorted arrays, where its time complexity can approach $O(n)$ in the best case.
- optimization techniques
- analysis and proof

- Practice 2.1.1
	- Illustrate the operation of insertion sort on the array $A = 31,41,59,26,41,58$
	- step 1: j=2
		- sorted subarray - 31, holding element - 41, unsorted subarray - $59,26,41,58$
		- 31 is smaller than 41, so nothing happens to the sorted subarray. 41 is inserted to j=2
	- step 2: j =3
		- sorted subarray - 31,41, holding element - 59, unsorted subarray - $26,41,58$
		- 41 is smaller than 59, so nothing happens to the sorted subarray. 59 is inserted to j=3
	- step 3: j=4
		- sorted subarray - 31,41,59, holding element - 26, unsorted subarray - $41,58$
		- now we compare holding element with sorted subarray. the rightmost element of the sorted subarray 59 is bigger than 26, so 59 is inserted into j=4, and  holding element 26 replacing its place and continue the while loop
		- the next rightmost element of the sorted subarray 41 is bigger than 26, so 41 is inserted into j=3, and  holding element 26 replacing its place and continue the while loop
		- the next rightmost element of the sorted subarray 31 is bigger than 26, so 31 is inserted into j=2, and  holding element 26 replacing its place and continue the while loop
		- since j = 1, the holding element has nothing to compare with, so it is being inserted into j = 1
	- step 4: j=5
		- sorted subarray - 26,31,41,59, holding element - 41, unsorted subarray - 58
		- now we compare holding element with sorted subarray. the rightmost element of the sorted subarray 59 is bigger than 41, so 59 is inserted into j=5, and  holding element 41 replacing its place and continue the while loop
		- 41 is the same as 41, so nothing happens to the sorted subarray. 41 is inserted to j=4
	- step 5: j=6
		- sorted subarray - 26,31,41,41,59, holding element - 58
		- now we compare holding element with sorted subarray. the rightmost element of the sorted subarray 59 is bigger than 58, so 59 is inserted into j=6, and  holding element 58 replacing its place and continue the while loop
		- 58 is smaller than 41, so nothing happens to the sorted subarray. 58 is inserted to j=5
	- No more elements is in the unsorted array and holding element array, so the insertion sort terminates. 


### Pseudo code conventions
- Indentation
	- Indentation indicates block structure
- Looping constructs
	- eg `while`, `for` and `repeat-until`, and `if else`
	- keywords:
		- `for` 
			- loop header - in line 1. So when this loop terminates.
		- `to`
			- We use `to` when a `for` loop increments its loop counter in each iteration. 
		- `downto`
			- when a for loop decrements its loop counter
		- `by`
			- when the loop counter changes by an amount greater than 1
- comments
	- `//`
- multiple assignment
	- `i = j = e` indicates both $i$ and $j$ assigned the value of $e$. 
- variables
	- such as $i$, $j$ and keys
	- local to the given procedure
	- access array element
		- $A[i]$
- object attributes
	- followed by a dot, followed by an attribute name, 
		- eg: `A.length`
	- We treat a variable representing an array of object as a pointer to the data, representing the array or object. 
		- eg: for all attribute $f$ of an object $x$, setting $y=x$ cause $y.f = x.f$. 
	- attribute notation can cascade, means that $f$ is itself a pointer to some type of object that has an attribute $g$. Then the notation becomes $x.f.g$ implicitly parenthesized as $(x.f).g$
	- Sometimes, the pointer will refer to no object at all. 
- We pass parameters to a procedure `by value`
	- the called procedure receives its own copy of the parameters, and if it assigns a value to a parameter, the change is not seen by the calling procedure. In other words, any modifications made to the parameter inside the called procedure do not affect the original value of the parameter in the calling procedure. 
	- When objects are passed, the pointer to the data representing the object is copied, but the object's attributes are not. In other words, any changes made to the parameters or object attributes within the called procedure do not affect the original values in the calling procedure.
- `return` 
	- it immediately transfers control back to the point of call in the calling procedure. 
- `error`
	- indicates that an error occurred because conditions were wrong for the procedure to have been called. The calling procedure is responsible for handling the error. 

### Pseudo code of insertion sort
- Input: a sequence of $n$ numbers $\langle a_1, a_2, \dots, a_n \rangle$
- Output: a permutation (reordering) $\langle a_1', a_2', \dots, a_n' \rangle$ of the input sequence such that $a_1' \leq a_2' \leq \cdots \leq a_n'$
```pesudo
INSERTION-SORT(A)
	if TYPE_OF(A)!= ARRAY or A.length <2
		//handle the exceptional case
		print "invalid input"
		RETURN
	
	for j = 2 to A.length
		key = A[j]
		// Insert A[j] into the sorted sequence A[1, ... , j-1]
		i = j-1
		while i>0 and A[i] > key
			A[i+1] = A[i]
			i = i-1
		A[i+1] = key
```

Practice: write a pseudo code for searching problem (Q 2.1.3):
Input: a sequence of numbers $A = \langle a_1, a_2, \cdots, a_n \rangle$
Output: an index $i$ such that $v = A[i]$ or the special value NIL if $v$ does not appear in $A$.
```pesudo
LINEAR-SEARCH(A, v)
	for i = 1 to A.length
		if A[i] == v
			return i
		else pass
	return NIL
```
- ChatGPT's comment
	- 1. Structure - it is clear and easy to understand
	- 2. Variable naming - the choice of variable names is appropriate and intuitive
	- 3. Loop iteration - The loop is the correct range for accessing each element of the sequence. 
	- 4. Early return - When a matching element is found, your code correctly return the index. That is efficient because it terminates the loop and avoid unnecessary iterations. 

- Practice: Showing the correctness of linear search algorithm, using a loop invariant
	- Initialization
		- we show when the first iteration of the loop, i.e. $i = 1$, the loop is working properly.
		- this iteration the loop compare the first item in the list with the specified value `v`. If it is matched, it return the index `i`. Otherwise, it goes to the next iteration. So the first iteration is true.
	- Maintenance
		- we show if it is true before any iteration of the loop, it remain true before next iteration.
		- informally, the body of the for loop works by moving `A[2], A[3], \cdots, A[j]` until it finds a match with the specified value `v`
		- the loop will either return the index if it is matched, or pass to the next iteration if it is not matched. 
		- Thus the loop invariant holds in the loop process.
	- Termination
		- in each iteration, it is possible to trigger early termination when the match is found.
		- in the last possible iteration, if it still cannot find a match. The control flow would goes to the next line after the for loop, which is return `NIL`, which also fits the requirement of the algorithm.
	
	- chatGPT's comment: 
		- your explanation demonstrates a clear understanding of the linear search algorithm and how the loop invariant applies to it. Well done!

---

### Merge sort
- why learning merge sort?
	- 1. good introduction to divide and conquer - it is most transparent application of divide and conquer paradigm
		- improves over "selection sort", "insertion sort", "bubble sort"
	- calibrate your preparation
		- which means you are expected to be able to turn a pseudo-code into a real program
	- motivate guiding principles for algorithm analysis (worst case and asymptotic analysis)
		- expose a couple of assumptions in our analysis
		- worst case behavior
		- asymptotic analysis - more concerned with the rate of growth on an algorithm's performance than on low-order terms or small changes in the constant factors. 
	- recursion tree method
		- typing up the total number of operations that are executed by an algorithm
		- analysis generalize to "master method"
			this recursion tree method generalizes greatly.


- Objectives of algorithm analysis:
	- Does it work?
		- Correctness analysis
	- Does it have good performance?
		- Running time analysis


- the sorting problem
	- input
		- array of $n$ array, unsorted
	- output
		- same array, sorted in increasing order

- pseudo code
	- `merge_sort` 
		- It takes `arr` as input and recursively divide it into smaller halves, until the base case is reached.
	- `merge`
		- It takes two sorted array. 
		- When merging, it compares the elements from left and right iteratively.
```python
merge_sort(arr)
    if length(arr) <= 1
        return arr

    mid = length(arr) / 2
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:end])

    return merge(left, right)

merge(left, right)
    merged = []
    i = 0
    j = 0

    while i < length(left) and j < length(right)
        if left[i] <= right[j]
            merged.append(left[i])
            i += 1
        else
            merged.append(right[j])
            j += 1

    append remaining elements from left (if any) to merged
    append remaining elements from right (if any) to merged

    return merged
```

- Analysis
	- Time complexity
		- It would be $O(n\ log\ n + n) = O(n\ log\ n)$
			- To begin, it just split the array in halves recursively until the length of each subarray = 1 or 0. Let $k$ be how many iteration of split requires, then $\frac{n}{2^k} \leq 1 \implies k \geq \log_2 n$. 
				- For $k$ levels, each levels require $\frac{n}{2}$ splits. The number of splits increases as $k$ goes up.
				- So the total amount of operation is $n \sum_1^k \frac{1}{2^k}$, which is a geometric sequence. Its sum could be obtained by $S = \frac{a \times(1 - r^k)}{1-r} = \frac{0.5 \times (1 - 0.5^k)}{0.5} = 1 - 0.5^k$. Thus, the sum converges to $1$, so the number of splits is proportional to $n(1) = n$. 
			- Next, the algorithm start merging the subarrays. When merging, comparing the value is required. In the worst case scenario, the algorithm have to check the value of all elements in the array. 
				- In the lowest level, where the max length of subarray is $1$, the number of subarray is $n$, it checks at most $1$ element per subarray, so the number of operation is $n$. 
				- In the second level, the number of subarray is $n/2$, it checks at most  $2$ element per subarray, so the number of operation is $n$. 
				- So the total number of operation in the whole merging process is $n \times k \implies n\ log_2\ n$
			- So time complexity of merge sort is $O(n\ log\ n + n) = O(n\ log\ n)$, lower order terms are omitted in the practice of time complexity analysis. 
	- Space complexity:
		- It would be $O(n\ log\ n)$
			- For $k$ levels of the splitting process
				- level 2 we have 2 subarrays, each subarray has a length $\leq \frac{n}{2}$, so level 1 requires creating $n$ memory unit to hold those values temporarily. 
				- level k we have $2^k$ subarrays, each subarray has a length $\leq \frac{n}{2^k}$, so level $k$ requires $n$ memory unit. 
				- So it requires $O(nk) = O(n\ log\ n)$ memory unit.
			- In the merging process, 
				- The program update the values of the prior layer subarrays. No new subarrays needed to be created in the process. After successful merging, the memory unit consumed by the lower level subarrays could be released because the computation is completed. The action of freeing memory will be keep going in the process of merging. We can see that there is no extra memory needed in the whole process. 
		- So space complexity of merge sort is $O(n\ log\ n)$

- Correctness of merge sort algorithm:
	- By induction
		- Base case (suppose $i = 1$)
		- Inductive step 
		- Conclusion

---
### $O(n\ log\ n)$ behavior in algorithm
- In computer science,
	- It is generally considered as good performance for an algorithm. In the world of algorithm analysis, there is a classification of algorithms based on their time complexity and how they scale with increasing input sizes.
		- Versus $O(n)$ behavior
			- When the input size doubles, the algorithm with $O(n)$ will take approximately twice as long to run, while the algorithm with $O(n\ log\ n)$ will take more than twice as long, but not significantly more.
	- They are classified as efficient and are often preferred over algorithms with higher time complexities.
- Mathematics
	- In respect to $log$ functions are decaying as $n$ increase. $n\ log\ n$ is much closer to growing linearly than it is to grow quadratically. 
- Examples:
	- Merge sort
	- Quick sort
	- Binary search
	- Heap sort

---



---
# Chapter 2.2

### RAM model
- In the RAM model, instructions are executed one after another, with no concurrent operations. 
- This model helps in analyzing the efficiency and complexity of algorithms.

### Size of data type
- When we work with inputs of size $n$, we typically assume that integers are represented by $c\ log(n)$ bits for some constant $c \geq 1$. 
	- Why $c\ log(n)$:
		- 1. Let denote the size of the input word as $n$. 
		- 2. The choice of $c\ log(n)$ is based on a trade off. The size of integers should grow logarithmically with the input size $n$. 
		- WHY IT is $c\ log(n)$?
	- We requires $c \geq 1$ so each word can hold the value of $n$, enabling us to index the individual input elements.
	- We restrict $c$ to be a constant so that word size does not grow arbitrarily. Otherwise we could store huge amount of data in one word, and operate on it all in constant time.

### The nature of various running time of a function
- $exp()$ in general case is not running in constant time because it takes several instructions to compute. In restricted situations however, $exp()$ is a constant-time operation. 
- $2^k$ is a constant time operation
	- Shift one position means times 2. 
	- Shift $k$ positions mean times $2^k$. 

### The nature of various expression in run time analysis
- Even though we typically select only one machine model to analyze a given algorithm, we still face many choices in deciding how to express our analysis.
- So we look for a way that is simple to write and manipulate, shows the important characteristics of an algorithm's resource requirements, and suppresses tedious details. 

### Do not model memory hierarchy that is common in contemporary computers
- Models that include the memory hierarchy are quite a bit complex than the RAM model.
	- Excluding the modeling of memory hierarchy, which is commonly found in contemporary computers, simplifies the analysis and understanding of algorithms in the 'Introduction to Algorithm' course. By focusing on the Random Access Machine (RAM) model, which abstracts away the complexities of memory hierarchy, students can grasp fundamental concepts more easily.
	- Including the memory hierarchy in algorithm analysis introduces additional complexity, as it requires accounting for different levels of memory, such as caches, main memory, and disk storage. Analyzing algorithms under these circumstances becomes more intricate and less straightforward.
- RAM model analyses are usually excellent predictors of performance on actual machines.

### Skills required in RAM model analysis
- Combinatorics
- Probability theory
- Algebraic dexterity
- Ability to identify the most significant terms in a formula

### Representation of execution time in RAM model 
- Input size
	- Number of items in the input, which refers to the number of items in the input, such as the number of elements in an array or the length of a string. 
	- Total number of bits needed to represent the input in ordinary binary notation.
- Line execution
	- Cost of each line
		- Assume a constant amount of time $c_1, c_2, c_3, \cdots$ is required to execute each line $l_1, l_2, l_3, \cdots$, for simplicity.
	- Time of each line
		- For loop
			- If there is a for-loop code block that loops for $n-1$ times, then the body of the block would runs $n-1$ times, and the head of the code block run loop for $n$ times, the additional $1$ time accounts for the final checking of whether the code block is completed running. 
		- If-loop, while-loop
			- If there is a while-loop or if-loop, then the body of the block would runs $\sum_{i=1}^n t_i$ times and the total size of this would depends on how many times the loop is hitting the condition causes the compilers runs the line inside the code block.
		- if-loop (which could not flip the control flow to the previous line)
			- The lower bound of  $\sum_{i=1}^n t_i$ is $0$, such as, there are a if-loop or while-loop loop over $n$ items, but no items matched with the condition.
			- The upper bound is $t_1$. If the loop is the outer-most loop, then $t_1 = 1$. If the loop is not the outer-most loop, then $t_i$ have to consider how many times the outer loop have to run.
		- while-loop (which could flip the control flow back to previous line)
			- The lower bound of  $\sum_{i=1}^n t_i$ is $0$, such as, there are a if-loop or while-loop loop over $n$ items, but no items matched with the condition.
			- The upper bound is $t_1$. If the loop is the outer-most loop, then $t_1 = n$. If the loop is not the outer-most loop, then $t_i$ have to consider how many times the outer loop have to run.
		- Nested loop
			- If there is a nested loop, we will account for the nested effect into $t_i$ of the term $\sum_{i=1}^n t_i$. For example there is a line in a while-loop nested inside another for-loop. The time required for this line expressed as $\sum_{i=1}^n (t_i-1) = \frac{n-1(n)}{2}$ for the body of the inner loop and $\sum_{i=1}^n t_i = \frac{n(n+1)}{2}$ for the head of the inner loop. 
	- Cost of each line x time of each line = Actual running time of each line 
		- which reflect how the pseudocode would be implemented on most actual computers. 
- Assuming inputs of a equal size is equally likely
	- This assumption may be violated, and use randomized algorithm which makes random choices, to allow probabilistic analysis and yield an expected running time. 
	- In practice. In cases where the inputs can vary significantly in size, it may be necessary to use a more sophisticated analysis, such as considering the worst-case or average-case time complexity.
- Randomized algorithm
	- Such algorithms are often used for their ability to provide probabilistic analysis and yield an expected running time. 
	- By introducing randomness, these algorithms can provide efficient solutions for certain problems and handle input scenarios that deterministic algorithms may struggle with.


- Figure: example of representing the running time in RAM model
- ![[Pasted image 20230512174300.png]]


- Example: Q2.2-3 in linear search algorithm, what is the best case and the worst case?
-       | cost | time
- LN1  c_1    n
- LN2  c_2    n
- LN3  c_3    $\sum_{i=1}^n (t_i-1)$
- LN4  c_4    $\sum_{i=1}^n (t_i-1)$
- LN5  c_5    1
- $T(n) = c_1 n + c_2 n + c_3 \sum_{i=1}^n (t_i-1) + c_4 \sum_{i=1}^n (t_i-1) + c_5$
- Best case:
	- The best case is when summation terms becomes linear terms. $\sum_{i=1}^n (t_i-1)$ becomes $0$ because the compiler don't need to run it anymore. 
- Worst case:
	- The worst case is when summation terms becomes quadratic terms. $\sum_{i=1}^n (t_i-1)$ becomes $n$ because there is $n$ outer loops and $n-1$ inner loops.
```pesudo
LINEAR-SEARCH(A, v)
	for i = 1 to A.length
		if A[i] == v
			return i
		else pass
	return NIL
```


### Drawback of these representation
- 1. We ignored the actual cost of each statement / line, using the constant $c_i$.
- 2. Even these constants give us more detail than we need, we expressed the worst-case running time $an^2 + bn +c$ for some constants $a,b,c$ that depend on $c_i$




### Worst case analysis
- We have 3 reasons why we usually focus on worst cases
	- 1. It gives us an upper bound on the running time for any inputs. Which provides a guarantee that the algorithm will never take any longer. 
	- 2. Worst cases occurs fairly often. eg: when searching, it will often occur when the information is not present in the database.
	- 3. The average case is often roughly as bad as the worst case. 
- If we are interested in average case, we shall see the technique of probabilistic analysis applied to various algorithms throughout the book.
- Q:
	- How can we modify almost any algorithm to have a good best-case running time?
- A:
	- Feeding the kind of data that gives us the smallest value in all summation signs in the $T(n)$ computation. 

### Order of growth (of the running time that interests us)
- To mitigate those drawbacks, we make one more simplifying abstraction - rate of growth or order of growth
- Rule:
	- 1. Consider only the leading term of a formula, since the lower order terms are relatively insignificant for large values of $n$.
	- 2. Ignore the leading term's constant coefficient, since constant factors are less significant than the rate of growth in determining the computational efficiency for large inputs. 
- When rule 1 and 2 is applied, only $n^2$ left in the computation time expression for $n^2$. 
- We write it as $\Theta(n^2)$ (pronounced "theta - n - squared")
- Example Q2.2-1
	- Q: Express $n^3/1000 - 100n^2 - 100n+3$ in $\Theta$ notation
	- A: $\Theta(n^3)$

### Designing algorithms

### Analyzing recursive algorithm
![[Pasted image 20230512182813.png]]


### Merge sort
- Strategy:
	- Break the problem into sub-problems
	- Solve the sub-problems (often recursively)
	- Combine the results of the sub-problems to solve big problems

- it is a recursive algorithm, so it call itself in the midway 
- $54187263 \rightarrow$  $5418$, $7263$, $\rightarrow 1458, 2367$
	- split
	- merge


- Pseudo code
	- there is gonna be 2 recursive calls, and a merging step.

	- 1. Base cases
		- In any recursive algorithm, you gotta have some bases cases
		- that means if the input is sufficiently small, you don't do any recursion
- pseudo code
```
C = output array [length = n]
A = 1st sorted array [length = n/2]
B = 2nd sorted array [length = n/2]
```



### Recursion tree
- The concept of a recursion tree is useful when learning about algorithms like merge sort because it provides a visual representation of how recursive calls are made and how the problem is divided into subproblems.
- Reasons why this tree is helpful:
	- 1. Visualizing the recursive calls: 
		- The recursion tree allows you to see the sequence of recursive calls made during the sorting process. Each node in the tree represents a recursive call, and the edges represent the flow of execution. This visualization helps you trace the path of execution and understand how the algorithm progresses.
	- 2. Understanding the division of the problem: 
		- The recursion tree illustrates how the original problem of sorting a large array is divided into smaller subproblems. At each level of the tree, the array is split in half until individual elements are reached. This division is fundamental to the divide-and-conquer approach of merge sort.
	- 3. Analyzing the time complexity: 
		- The recursion tree provides insights into the time complexity of merge sort. By analyzing the tree's structure, you can determine the number of levels and the number of operations performed at each level. This analysis helps you understand why merge sort has a time complexity of O(n log n) and how the work is distributed across different levels.
	- 4. Identifying overlapping subproblems: 
		- When studying the recursion tree, you may notice that certain subproblems appear multiple times. This observation leads to an important property of merge sort known as "overlapping subproblems." Understanding this property is crucial because it explains why merge sort achieves efficiency through reusing solutions to subproblems rather than recomputing them.

- Figure:
![[Pasted image 20230512182932.png]]



---

### Asymptotic analysis
- Asymptotic analysis focuses on understanding the behavior of an algorithm as the input size increases towards infinity.
- It allows us to reason about the scalability and efficiency of algorithms without getting bogged down by the specific details of constant factors or lower-order terms.

### Asymptotic notation
- The notation are defined in terms of function whose domains are the set of natural numbers $\mathbb{N}$. Such notations are convenient for describing the worst-case running-time function $T(n)$, which usually is defined only on integer input sizes. 
- We should make sure to understand the precise meaning of the notation so that when we abuse, we do not misuse it. 
- eg:
	- The running time for the worst cases of insertion sort is $\Theta(n^2)$.
- Time-space ambiguity
	- In the book, the function we apply asymptotic notation will usually refer to running time, but it can apply to functions that characterize some other aspect of algorithms (the amount of space they use, for example.)
- Worst-best ambiguity
	- We might mean best or worst time by using the same notation too.




- Big-Oh notation
	- When we have only an asymptotic upper bound
- Big-Omega notation
	- When we have only an asymptotic lower bound
	- Benefits:
		- Simplified Analysis: 
			- Big O and Big Omega notations provide simplified analysis by focusing on the worst-case (Big O) or best-case (Big Omega) scenarios. This simplification allows us to understand the upper and lower bounds of an algorithm's complexity quickly and easily.
		- Emphasis on Efficiency: 
			- Big O notation, in particular, is commonly used to assess algorithm efficiency. It helps identify algorithms that scale well with input size and have a manageable impact on resources.
		- Algorithm Selection: 
			- Big O and Big Omega notations assist in algorithm selection. By comparing the complexities of different algorithms, we can choose the one that suits our requirements best. Big O and Big Omega notations provide a quick way to gauge the relative efficiency of algorithms.
		- Algorithm Design: 
			- These notations influence algorithm design by encouraging developers to consider the worst-case (Big O) and best-case (Big Omega) scenarios. By understanding these bounds, developers can optimize their algorithms to achieve better performance in real-world scenarios.
		- Asymptotic Analysis: 
			- Big O and Big Omega notations provide a high-level view of an algorithm's complexity, emphasizing its growth rate as the input size increases. This asymptotic analysis helps us focus on the most significant factors affecting an algorithm's efficiency.
		- Standardized Language: 
			- Big O and Big Omega notations have become a standardized language in computer science and algorithm analysis. They provide a common vocabulary to discuss and compare algorithmic complexities among researchers, educators, and practitioners.
- Big-Theta ($\Theta$) notation
	- $f(n) \in \Theta(g(n)) = \{  \exists c_1>0, \exists c_2>0,\exists  n_0, 0 \leq c_1 g(n) \leq f(n) \leq c_2 g(n), \forall n \geq n_0 \}$
	- $n_0$ shows the minimum possible input length.
	- $f(n) \in \Theta(g(n))$ if there exists $c_1, c_2$ positive constants such that it can be sandwiched between $c_1 g(n)$ and $c_2 g(n)$ for sufficiently large $n$.
	- Benefits:
		- Tight Bound: 
			- Big Theta notation provides a tight bound by specifying both the upper and lower limits of an algorithm's complexity. It tells you that the algorithm's running time or space complexity grows at the same rate as the input size
		- Average-Case Analysis: 
			- Big Theta notation is particularly useful for average-case analysis. In some cases, an algorithm may have a different best-case and worst-case behavior, but its average behavior is consistent. Big Theta allows you to express this average-case complexity.
		- Clearer Comparisons: 
			- Big Theta notation allows for clearer comparisons between algorithms. If two algorithms have the same Big Theta complexity, it means they have the same growth rate and can be considered equally efficient.
- Choose between these three:
	- While it is true that both Big O and Big Omega notations can express upper and lower bounds separately, they do not provide a complete picture of the algorithm's behavior. By using Big Theta notation, you can convey that the algorithm's growth rate is both bounded from above and below by specific functions.


- Figure: Graphic examples of "Theta", "Oh" and "Omega" notations
![[Pasted image 20230512192953.png]]



### Asymptotically tight bound
- Growth Rates: 
	- Asymptotically tight bounds classify algorithms based on their growth rates. 
	- Common growth rates include constant time (O(1)), logarithmic time (O(log n)), linear time (O(n)), quadratic time (O(n^2)), and exponential time (O(2^n)).
	- Understanding these growth rates helps in comparing and selecting algorithms based on their efficiency.
- Order of Growth: 
	- The order of growth refers to the dominant term or the term with the highest degree in the polynomial representation of an algorithm's time complexity. It provides insights into how an algorithm's performance scales with increasing input size.
- Analyzing Loops and Recurrences: 
	- Asymptotic analysis also involves analyzing loops and recursive functions to determine their time complexity. Techniques like summations, substitution method, recursion trees, and master theorem are used to derive the asymptotic bounds of algorithms with loops or recursive structures.

### Asymptotically non-negative


---


### Standard notations and common functions

### Monotonicity
- A function is monotonically increasing if $m \leq n \implies f(m) \leq f(n)$. 

### Floors and ceilings
- $\forall x \in \mathbb{R}$, we denote the greatest integer less than or equal to $x$ by $\lfloor x \rfloor$ (reads "the floor of 'x'")
- $\forall x \in \mathbb{R}$, we denote the least integer greater than or equal to $x$ by $\lceil x \rceil$ (reads "the ceiling of x")
- $\forall x \in \mathbb{R}$, $x - 1 < \lfloor x \rfloor \leq x \leq \lceil x \rceil < x+1$


### Modular arithmetic
- The value of $a\ mod \ n$ is the remainder of the quotient $a / n$:
	- $a\ mod\ n = a - n \lfloor a/n \rfloor$


### Polynomials

### Exponentials

### Logarithms

### Factorials

### Functional iterations

### The iterated logarithm function

### Fibonacci numbers





---
## Lecture 3 - Solving recurrences and the selection problems

### Recurrences
- Examples
	- Integer multiplication
	- Merge sort

### The master method
- a general method for solving recurrences where all the subproblems are of the same size. 
- Recurrence relations are typically in the form of:
	- $T(n) = a \cdot T(\frac{n}{b}) + O(n^d)$
		- $T(n)$: 
			- Time complexity of the problem
		- $n$: 
			- The length of the input array
		- $a$: 
			- the number of subproblems that we create from one problem, and must be an integer greater than or equal to $1$. 
		- $T(n)$ the time complexity of the problem of size $n$. 
		- $b$:
			- the factor by which the input size shrinks (it must hold that $b > 1$.)
		- $d$:
			- the exponent of $n$ in the time in summing time of "combining steps"
		- $O(n^d)$: 
			- the time complexity of the operation that is outside of the recursive  structure. These operations are not part of the recursive calls, or the subproblem solving process. These operation are not part of the recurrence structure but still contribute by the term $O(n^d)$. 
				- Such as
					- Initialization
					- Combining the results of subproblems 
					- Post-processing steps
			- Example:
				- If the whole set of operations outside the recursive structure is having  $O(n^2)$ time complexity, then $d =2$ for this case. 
		- $n/b$: the size of each subproblems
		- Important note:
			- $a,b,d$ are independent to $n$. 
		- $f(n)$ The work outside of the recurrence calls. 
- Why the boundary that separates 3 cases is $c = \log_{b}(a)$?
	- We see how many layers in the recursion process
		- Each splits we creates subarray $a \cdot T(\frac{n}{b})$, the process is terminating when the element size of $T(\frac{n}{b}) \leq 1$
		- Thus, if $k$ is the number of layers, then $\frac{n}{b^k} \geq 1 \implies log_b(n) \leq k$. 
- Scenarios:
	- $\begin{align*}T(n) &= O(n^d\ log\ n) & &\text{if } a = b^d \\ T(n) &= O(n^d)  & &\text{if } a < b^d \\ T(n) &= O(n^{log_b(a)}) & &\text{if } a > b^d \end{align*}$
- Proof:
	- Decomposition of the structure of the recursion tree
		- Suppose we have $T(n) = a \cdot T(\frac{n}{b}) + O(n^d)$
			- the first part is a partial variance of the recurrence relation, represents the recurrence structure time cost, and the second part represents the time cost outside of the recursive structure. 
		- Each level: 
			- Each subproblems:
				- Each sized $\frac{n}{b^j}$. We had a general representation of $O(n^d)$ to describe any random problems that we don't know its complexity. For a sized $\frac{n}{d}$ input array subproblem, each of them takes at most $c(\frac{n}{b^j})^d$ to solve. 
				- In total there are $a^j$ pieces of subproblems in that level. :
			- The whole level: 
				- If not considering the time-cost of subproblems
					- the total work done at level $j$ is $a^j \cdot c(\frac{n}{b^j})^d = cn^d (\frac{a}{b^d})^j$. We group up the terms involving $j$ (level number), to facilitate later computations. 
		- All levels in total: 
			- Totally we have $log_b\ n$ levels.
			- The total cost would be $cn^d \sum_{j=0}^{log_b\ n} (\frac{a}{b^d})^j$.
- Focus 1: Why we choose $a = b^d$ will be our boundary of cases:
	- We can show if $a = b^d$, the amount of work done at each level is the same -- $cn^d$:
		- Level 1 (j = 1): 
			- $cn^d (\frac{a}{b^d})^j = cn^d (\frac{b^d}{b^d})^1= cn^d$  
		- Level 2 (j = 2):
			-  $cn^d (\frac{a}{b^d})^j = cn^d (\frac{b^d}{b^d})^2 = cn^d$  
	- By choosing $a = b^d$ as the boundary of cases, we are actually determines $\frac{a}{b^d} > 1$ or $\frac{a}{b^d}<1$ or $\frac{a}{b^d}=1$. If $\frac{a}{b^d} > 1$, the time complexity increases in the process of getting into a deeper recursive level. 
- In above expression, we can already see how the time-cost evolves in each level as $j$ increase. To make it to be a single statement, we can discuss the summation of the time-cost in all levels of the recursive structure.  Now we discuss each case separately: 
- Focus 2: The total time-cost of the whole recursive structure in 3 cases 
	- Case 1, $a = b^d$ , then $T(n) = O(n^d\ log\ n)$ 
		- (See page 21 of the notes)
		- Since there are $log_b{n+1}$ levels, the total running time is $O(n^d\ log\ n)$. 
	- Case 2, $a < b^d$, which means $\frac{a}{b^d} < 1$, then $T(n) = O(n^d)$
		- $a < b^d \implies \frac{a}{b^d} < 1$
		- $\sum_{j=0}^{log_b\ n} (\frac{a}{b^d})^j \leq \sum_{j=0}^\infty (\frac{a}{b^d})^j = \frac{1}{1 - \frac{a}{b^d}} = \frac{b^d}{b^d - a}$
			- Involved the "infinite sum of converging series"  
		- So the total worst case running time is $cn^d  \frac{b^d}{b^d - a} \implies O(n^d)$
			- (Because only $n^d$ is not constant in the expression). 
		- Therefore $O(n^d)$
			- In this case, the work is dominated by just what is done outside the recursion in the outermost call. 
			- So the work done in the highest level "dominates" the other factors in the running time. 
	- Case 3, $a > b^d$, then $O(n^{log_b a})$
		- $\sum_{j=0}^{log_b\ n} (\frac{a}{b^d})^j = \frac{(\frac{a}{b^d})^{log_b{n+1}}-1}{\frac{a}{b^d})^{log_b{n+1}}}$
			- Involved the summation of the geometric series.  
		- Then $cn^d \sum_{j=0}^{log_b\ n} (\frac{a}{b^d})^j$ $\implies$ $O(n^d (\frac{a}{b^d})^{log_b{n+1}}) \implies O(n^{log_b a})$
			- (Because only $(\frac{a}{b^d})^{log_b{n+1}}$ is not constant)
		- Therefore, $O(n^{log_b a})$.
			- In this case, the branching factor is more significant, so the total work done at each level increases, and the leaves of the tree "dominates".



### The substitution method
- Usefulness
	- Recurrence trees can get messy when attempting to solve complex recurrences. The substitution method is a condensed way of proving an asymptotic bound on a recurrence by induction.
	- Instead of trying to find an exact closed-form solution, we only try to find a closed-form bound on the recurrence. 
		- With the substitution method, reduces the complexity of the analysis by introducing inequalities for us to guess what the runtime is of the recurrence trees, plug it something simpler into the complicate parts of the recurrence and see if it works out.
- Definition:
	- $T(n) \leq \begin{cases} d \cdot g(n_0) & \text{if } n = n_0 \\ d \cdot g(n) & \text{if } n > n_0 \end{cases}$
		- , for some constants $d > 0$ and $n_0 \geq 1$ and a function $g(n)$. We are essentially guessing $T(n_0) \leq d \cdot g(n_0)$
- Applications
	- Solving the "Recurrence of Select" using the substitution method


---



### Selection
- The selection problem is to find the $k^{\text{th}}$ smallest number in an array $A$. 

### Linear-time selection


- 3 ideas that is related to linear-time selection
	- choose a random pivot
	- choose a pivot that creates the most balanced split
	- find a pivot that close enough to the median

### Solve the recurrence of select using the substitution method

### Issues when using the substitution method

---
## Lecture 4 - Median and selection

### Selection
- The selection...
- again?
- Minimum element

### Linear time selection
- again?
---
## Lecture 5 - randomized algorithm and quick sort

### Quick sort overview

### Speculation on the runtime
- random pivot selection

- worst-case analysis
- alternative proof

---
### Lecture 6 - Sorting lower bounds, counting sort and radix sort

### Lower bounds for comparison-based sorting algorithms

### Counting sort

### Radix sort

---
## Lecture 7 - Heaps and binary search trees

### Data structures

### Heaps
- Basic operations on heaps

### Binary search trees
- Basic operations on BSTs
	- search
	- insert
	- delete
	- runtimes

### Red-black trees
- Rotations
- Insertion in a red-black tree

---
### Lecture 8 - Hashing

### Hash tables
- implementation
- examples
- time complexity
- choice of size of hash table
- potential problem with this implementation
- possible solutions

### Hashing with a completely random hash function
- expected cost of hash table operations with random hash function

### Universal hash functions 

### A universal family of hash functions

### Balls and bins
- No collisions

---
## Lecture 9 - Graph, DFS and BFS
### Graphs
- a graph is a set of vertices and edges connecting those vertices
- Formally, we define a graph $G$ as $G = (V,E)$ when $E \subseteq V \times V$.
- For ease of analysis, the variables $n$ and $m$ typically stand for the number of vertices and edges. 

### Representation
- Common issue is how to represent a graph's edges in memory. Two standard methods for this task
	- adjacency matrix
	- adjacency list
	- degree
	- sparse
	- dense

### Depth first search
- Runtime

### Breadth first search
- runtime
- correctness 

### DFS versus BFS

---
## Lecture 10 - strongly connected components

### Connected components in undirected graphs

### Algorithms to find connected components in a undirected graph

### Connectivity in directed graphs

### Algorithm to find strongly connected components of a directed graph

### The acyclic meta-graph of SCCs

### Proof of correctness
- The key lemma
- the final argument

---
## Lecture 11 - Dijkstra and Bellman-Ford

### Dijkstra's algorithm
- claim 1
- claim 2

### Implementation of Dijkstra's algorithm

### Negative edge weights

### Bellman-Ford algorithm
- claim 3
- claim 4

### Amortized time

---
## Lecture 12 - Dynamic programming: Bellman-Ford and Floyd-Warshall

### More on the Bellman-Ford Algorithm
- optimal substructure
- overlapping subproblems
- Runtime and storage
- What is really going on here?

### Dynamic programming

### Dynamic programming algorithm recipe
- optimal substructure
- overlapping subproblems
- implementations

### Floyd-Warshall algorithm
- correctness when there are no negative cycles
- negative cycles
- runtime
- space usage

### Why is it called dynamic programming?

---
## Lecture 13 - More dynamic programming

### Steps to coming up with a dynamic programming algorithm
- 1. identify optimal substructure
- 2. recursively define the value of an optimal solution / write a recursive formulation
- 3. find the optimal value / define an algorithm using our recursive relationship
- 4. find the optimal solution / recovering the actual sequence
- 5. tweak the implementation

### Longest common subsequence
- step 1 and 2
- step 3
- step 4

### The Knapsack problem 

### The unbounded Knapsack problem

### The 0-1 Knapsack problem

### The independent set problem

---
## Lecture 14 - Greedy algorithms

### Greedy algorithm

### Activity selection problem
- Optimal substructure
	- proposition 1

### Scheduling 
- intuition
- optimal substructure

### Optimal codes
- Tree representation
- How good is a code?
- Huffman code
- Proof of correctness
	- proposition 2
	- proposition 3

---
## Lecture 15 - minimum spanning trees
### Minimum spanning trees

### A template for minimum spanning tree algorithms


### Cut and light edges
- (Theorem 1) There exists and MST that contains $A \bigcup \{ (u,v)\}$

### Prim's algorithm
- correctness
-  running time 

### Kruskal's algorithm
- correctness
- running time

### The latest and greatest algorithms

---
## Lecture 16 - Max flow, min cut and Ford-Fulkerson

### History of flows and cuts

### Formulation of the maximum flow problem


### Example

### Formulation of the minimum cut problem

### The max-flow min-cut theorem
- Lemma 2
- Corollary 3
- Theorem 4 (Max-flow min-cut theorem)

### The Ford-Fulkerson Max-Flow algorithm
- Lemma 5
- Lemma 6
- The fattest path method
- The shortest path method

### Running time of various implementations of Ford-Fulkerson

### The fattest path version of Ford-Fulkerson
- proposition 8

### The shortest path version of Ford-Fulkerson

### Applications
- Bipartite perfect matching

---
## Lecture 17 - Stable matching and Gale-Shapley

### Stable matching

### Deferred acceptance algorithm
- Proof of correctness

### Doctor-optimality

### Incentive compatibility









