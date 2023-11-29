- Textbook:
	- "Computer systems - a programmer's perspective" Bryant and O'Hallaron

---
# Lecture 1


- cs107 follows [[cs106x programming abstractions in c++]] to build up and expand the breadth and depth of programming experience and techniques to show how machine really works.
- goal:
	- how is data in our program really represented?
	- how does heap memory work?
	- how does a computer know how to run the code we write?
	- how does a program map onto the components of computer systems?
	- why is my program doing X when I expected it to do Y?

- objectives:
	- how a computer can represent and manipulate these data? 
		- bits and bytes
		- char and c-strings
	- how computer programs can effectively manage these data structures?
		- pointers, stack and heap
	- "Generics"
		- How can we use our knowledge of memory and data representation to write code that works with any data types?
	- Assembly
		- How does a computer interpret and execute C programs?
	- The ability to translate C to/from assembly
	- Identify bottlenecks and improving runtime performance
	- Work effectively in a Unix development environment

### Unix
- It is a set of standards and tools commonly used in software development
	- macOS and Linux are operating systems built on top of Unix
- You can navigate a Unix system using the command line 


### Command line
- It is a text-based interface to navigate a computer, instead of a GUI.
- unix commands to try
	- `cd`
	- `ls`
	- `mkdir`
	- `emacs`
	- `rm`
	- `man`


### Whe learn unix / command line?
- You can navigate almost any device using the same toiols and commands.
	- Servers
	- Laptops and desktops
	- Embedded devices
	- Mobile devices
- Use cases
	- Web development
	- Machine learning
	- Systems
	- Mobile development

---
# Lecture 2

- nothing to learn

---
# Lecture 3

### Binary
- Why we learn this
	- Computers use this, but it is not human-readable
- Base 10 to base 2
	- Algorithm:
		- $6$ in base10 turns to base2, how to do that?
		- Ans: 
			- Iterating $2^n \leq N$ to divide $N$ and its remainder, where $N$ is the number of base10 that going to be converted.
			- For integer $6$, the first quotient is $2^2$, the remainder is $2$. 
			- The second quotient is $2^1$, the remainder is $0$.
			- So $6_{10} \rightarrow 110_2$ 

### Hexadecimal
- Why we learn this
	- Easy to convert to base-2
	- More portable as a human-readable format
- 4 bits compose 1 hexadecimal number
- hexadecimal is base-16, so we need digits for 1-15. 
- recognize Base 16 and base 2 numbers 
	- $0xf5_{16} \rightarrow 0b11110101_2$
	- $0x$ is the prefix that indicates the following is hexadecimal number
	- $0b$ indicates the following will be binary number
- Converting base 16 numbers to base 2
	- $0b011010100011$
	- Packing every 4 digits as a group to get the hexadecimal digit
		- $0110 \rightarrow 2^2 + 2^1 \rightarrow 6$
		- $1010 \rightarrow 2^3 + 2^1 \rightarrow 10 \rightarrow A$
		- $0011 \rightarrow 2^1 + 2^0 \rightarrow 3$
		- As a result, $0b011010100011 \rightarrow 0x6A3$

### Base-10
- Human-readable, but cannot easily interpreted by machine 

### Unsigned integers
- In computing, an "unsigned integer" refers to a data type that represents only positive whole numbers (including zero) and does not allow negative values. It is typically used to store numerical values that do not require a sign. 
- It is $0$ or a positive integers
- The range of an unsigned number is $0 \rightarrow 2^w - 1$, where $w$ is the number of bits. 

### Signed integers
- Negative integer, $0$, or a positive integer
- Idea, reserve the most significant bit to store the sign
	- Use 4 bits to represent $(-7, 7)$, the leftmost bit represents the positive and negative sign.
		- $(-7,7)$: total 15 numbers are represented

### Overflow
- In computing, overflow refers to a condition that occurs when the result of an arithmetic operation exceeds the maximum value that can be stored in the allotted memory or data type. It typically occurs in situations where the result of an operation is too large to be represented accurately within the given range.
- If that is the case, you wrap around or overflow back to the smallest bit representation.
	- Say, $0b1111 + 0b1 = 0b0000$
	- The computer don't inherently remember that an overflow occurred. It is typically indicated by the status flag in the computer's processor or arithmetic unit. 

---
# Lecture 4

- Shows us how to more efficiently perform arithmetic

### Truncating bit representation
- If we want to reduce the bit size of a number, C truncates the representation and discards the more significant bits. 
- example
	- ...

### Expanding bit representations
- For unsigned values, C adds leading zeros to the representation
- For signed values, C repeats the sign of the value for new digits
- Example
	- ...

### Casting
- In computing, casting refers to the process of converting a variable from one data type to another. It is also known as type casting or type conversion. 

- Example
```cpp
int num1 = 10;
double num2 = (double)num1;  // Explicitly casting int to double

printf("%f\n", num2);  // Output: 10.000000
```


### Bitwise operator
- Types
	- And
	- Or
	- Not 
	- Exclusive or

### Bit operator
- .... 

### Bitmasks
- ...

### GDB debugger
- ...

---
# Lecture 5

### bit shift operator
- Type
	- Left shift
	- Right shift
- Application
	- Color wheel
	- ...

---
# Lecture 6 C strings

- goal - string diamond

### Char
- It is a variable type that represents a single character
- Under the hood, C represents each `char` as an integer (its "ASCII" value)
- string length
	- Strings are not objects. They do not embed addition information, such as string length.
	- You can use the provided `strlen` function to calculate string length. It is $O(n)$ because it must scan the entire string. You should save the value if we plan to refer to the length later. 
- string as parameters
	- when passing string as parameter, C passes the location of the first character rather than a copy of the whole array.
		- why it is importatn?
- common string operations
	- comparing
		- `strcmp(str1, str2)`
		- return `0` if identical
	- copying
		- We cannot copy strings using `=`. This only copies addresses. 
		- `strcpy(dst, src)`
		- When insufficient space is happening -- buffer overflows
			- It means it overwrites other memory.
	- concatenating
	- substrings

- Example
	- `\0` is the null-terminating character, you always need to allocate one extra space in an array for it. 
![[Pasted image 20230620191359.png|400]]

### Substrings
- `char *s` (pointers to characters) are strings. We can use them to create substrings of larger strings. 

- Example
![[Pasted image 20230620192911.png|400]]







