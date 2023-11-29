- textbook: 
[[programming abstractions in C++ Eric Roberts cs106b.pdf]]

- cs106x lecture:``
	- https://www.youtube.com/watch?v=DFO5nyAIyho&list=PLoCMsyE1cvdVmbGH6Jp-9twXPbi5J_IBT&index=4
- cs106b lecture:
	- https://www.youtube.com/watch?v=9Nkxp47M4FM&list=PLoCMsyE1cvdWiqgyzwAz_uGLSHsuYZlMX&index=3

---
- Lecture 1
	- s

- what is c++?
	- developed in 1983
	- built for high speed and efificiency
- syntax has similiaries with Java and C
	- similiar data types (`int`, `double`...)
	- use braces for scope
	- comes equipped with a large standard library for you to use

- installation of c++ compiler
	- install mingw
	- setup the system environment variable which mentions the location of the mingw c++ compiler.

- breakpoint
	- Breakpoints are one of the most important debugging techniques in your developer's toolbox. You set breakpoints wherever you want to pause debugger execution.
- setup breakpoint
	- select the portion of the content
	- press F9 
- more instructions
	- https://learn.microsoft.com/en-us/visualstudio/debugger/using-breakpoints?view=vs-2022

- C++ programs / files 
	- 1. Unlike a Java `.class`, C++ executables are platform-dependent
		- However, in C++, the executables generated after compilation are specific to the platform or operating system they were compiled for. This means that a C++ executable compiled for one platform may not run on a different platform without recompiling it specifically for that platform.
		- what are the benefits of platform-dependent language?
			- Performance Optimization: 
				- Platform-dependent languages allow developers to take advantage of the specific features, optimizations, and capabilities of a particular platform or operating system. This can result in highly optimized and efficient code, leading to improved performance.
			- Access to System Resources: 
				- Platform-dependent languages often provide direct access to system resources such as memory, hardware peripherals, and low-level operations. This allows developers to have fine-grained control over the system and leverage specific capabilities of the underlying platform.
			- Native Integration: 
				- Platform-dependent languages can easily integrate with existing system libraries, APIs, and frameworks. They can directly call functions and utilize features provided by the operating system or other platform-specific software, enabling seamless integration with the platform ecosystem.
			- Flexibility and Portability: 
				- While platform-dependent languages may be specific to a particular platform, they can still be portable within that platform. Developers can write code that targets a specific operating system or hardware architecture, ensuring maximum compatibility and performance for that platform.
			- Low-Level Programming: 
				- Platform-dependent languages like C++ provide low-level programming capabilities, allowing developers to have precise control over memory management, pointer manipulation, and other low-level operations. This is particularly useful for system-level programming, embedded systems, and performance-critical applications.
	- 2. Source code is compiled into binary object files 
		- In C++, the source code is first written in plain text files with a `.cpp` extension. These files contain the actual program logic and instructions. 
		- To execute the program, the source code needs to be compiled into binary code that the computer can understand. This compilation process transforms the source code into object files (with a `.o` or `.obj` extension) that contain machine code specific to the platform.
	- Additional declarations can be put in header `.h` files

- Figure: how the `.cpp` files is compiled. 
	- object files (`.o` and `.obj` are created)
![[Pasted image 20230520152910.png|400]]

---

- C++ separate two kinds of code file
	- `.h`: A header file containing the interface (declarations)
		- They typically contain class declarations, function prototypes, constant definitions, and other info about the code entities.
		- It provides a blueprint of what is available in a particular code module, without revealing the implementation details. 
	- `.cpp`: A source file containing definitions (method bodies)
		- Contains the actual definitions and implementations of the code entities declared in the header file.
		- It is responsible to provide the executable instructions and behavior associated with the declarations in the header files.
	- `class` Foo: must write both `Foo.h` and `Foo.cpp`
		- When creating a class, it is a common practice to define the class's interface in the header file (`.h`) and provide the implementations in the source file (`.cpp`). This allows other code files to include the header files and access the class's public interface without exposing the implementation details. 

---

### Header file
- Header file in c++ is ... 
- Content of header file:
	- 1. Function declarations: 
		- Header files often contain function prototypes or declarations that provide information about the functions defined in corresponding source files. This allows other parts of the program to use these functions without needing to see the implementation details.
	- 2. Constant definitions: 
		- Header files can define constants using const or `#def.ine` statements. These constants can be used throughout the program and provide meaningful names to values that are used repeatedly.
	- 3. Type definitions: 
		- Header files may contain typedef statements that define aliases for existing types. This can improve code readability and maintainability by providing descriptive names for complex or commonly used types.
	- 4. Enumerations: 
		- Header files can define enumerations using the enum keyword, which allows you to create a set of named constants. Enumerations are useful when you have a fixed set of values that a variable can take.
	- 5. Macro definitions: 
		- Header files can include macro definitions using the `#define`  directive. Macros are used to perform textual substitution before the compilation process and can be used for conditional compilation, creating shortcuts, or defining constants.
	- 6. Inline functions: 
		- Header files may contain inline function definitions. Inline functions are expanded by the compiler at the call site, which can improve performance for small, frequently used functions.
	- 7. Template declarations: 
		- If you're working with templates, header files may contain template declarations for classes or functions. Templates allow you to write generic code that can be used with different types.
	- 8. External variable declarations: 
		- If you have global variables that need to be accessed across multiple source files, their declarations can be placed in a header file. This informs the compiler about the existence and type of the variable.
	- 9. Namespace declarations: 
		- Header files may include namespace declarations to define the scope of the entities defined within the file. This helps prevent naming conflicts between different parts of the code.

- Example: the structure of a header file
	- `#pragma once`:
		- basically says, "if you see this file more than once while compiling, ignore it after the first time" (
```cpp
// classname.h
#pragma once

class ClassName {
    // class definition
};
```

- Example: ^008c2b
	- a header file that including a class declaration
```cpp
#ifndef MYCLASS_H  // Header guard to prevent multiple inclusions
#define MYCLASS_H

class MyClass {
public:
    // Public member functions
    MyClass();  // Constructor
    void publicMethod();

private:
    // Private member variables
    int privateVariable;

    // Private member functions
    void privateMethod();
};

#endif  // End of header guard
```

### Macro
- a macro is a preprocessor directive that defines a symbolic name or constant. It allows you to create shortcuts or replacements for pieces of code, which are expanded by the preprocessor before the actual compilation takes place. 
- Macros are defined using the `#define` directive.
- Syntax:
	- part 1 - the macro name
	- part 2 - the replacement text
- Macro expansion
	- . When the preprocessor encounters the macro name in the code, it replaces it with the corresponding replacement text. This process is known as macro expansion.
- Predefined macros:
	- All predefined macros are having double underscore surrounding it. 
	- examples
		- `__LINE__`: represent the current line number in the source code
		- `__FILE__`: represent the current file name

### Preprocessor directives
- They are instructions to the preprocessor, a tool that processes the source code before it is compiled.
- These directives are used to control the compilation process, define macros, conditionally include or exclude code based on certain conditions, and perform other preprocessing tasks.
- Preprocessor directives in C++ versus decorators in python
	- While both preprocessor directives in C++ and decorators in Python involve modifying code behavior, they operate at different stages and serve different purposes. Preprocessor directives are primarily used for compile-time modifications, affecting the source code before compilation, while decorators in Python are used for runtime modifications, allowing dynamic changes to function or class behavior during program execution.
- Examples:
	- `#include`
	- `#define`
	- `#ifdef
	- `#ifndef`
	- `#endif`

- Example: 
	- A C++ script that contains a rich number of preprocessor directives
	- `#include <iostream>` 
		- It is a directive is used to include the `iostream` standard library header, allowing the use of input and output operations.
	-  `#define MAX_VALUE 100`:
		- It is a directive defines a macro named `MAX_VALUE` with the value `100`.
		- 
```cpp
#include <iostream>

#define MAX_VALUE 100

int main() {
    int value = 50;

#ifdef DEBUG
    std::cout << "Debug mode is enabled." << std::endl;
#endif

#ifndef DEBUG
    std::cout << "Debug mode is disabled." << std::endl;
#endif

#if MAX_VALUE > 50
    std::cout << "The maximum value is greater than 50." << std::endl;
#endif

    return 0;
}
```


---


- Object file
	- The object file (`dummy.o` in this case) generated during the C++ compilation process contains compiled machine code specific to the target platform. While it is possible for an experienced human reader to interpret the object file, it would be extremely challenging and not practical in most cases.
	- Object files are typically in binary format, consisting of low-level machine instructions and data structures. They are not intended to be directly read or understood by humans.

- Standard output stream
	- It is a predefined output stream that is connected to the console or terminal where the program is running. 
	- It is where the program sends its output so that it can be displayed to the user.

- "Standard"
	- it refers to the fact that it is predefined and widely supported that follows a common convention across different systems and programming languages. 
	- which means that these streams are universally available and adhere to a common interface, making it easier for developers to write portable code that can run on different systems without significant modifications. 

- `main()`
	- In C++, the `main()` function serves as the entry point of the program, and its execution is automatically triggered when the program starts. Unlike in Python, you don't need to explicitly call the `main()` function in C++.

- `return 0`
	- in python, any functions you could add `return 0` to indicate successful execution but it is not necessary.
	- Discuss which cases are necessary to put `return 0` at the end of the function in c++
		- 1. `main()`
			- It serves some purposes:
				- 1. interacting with the OS
				- 2. Integration with other codes
				- 3. Testing and debugging
				- 2. function with a return type other than `void`
			- the function will automatically terminate when it reaches the closing curly brace.
		- 3. void functions
			- which means it does not return a value, you can omit return the return statement.
		- 4. early termination:
			- you might want to terminate a function prematurely. With using `return` to exit the function.
	- in c++, we write this for 

- Example code
	- line 1: importing module
	- line 3: 
		- `std::cout` represents the standard output stream.  
		- `<<` is used to insert message into the stream.
		- `std:endl` is used to insert a newline character and flush the output stream. 
	- line 4:
		- `return 0`: returning zero usually signifies successful program execution. 
```c++
#include <iostream>

int main() {
    std::cout << "Hello, world!" << std::endl;
    return 0;
}
```

### function prototype:
- it is a way to declare the signature of a function before its actual definition. It provides the compiler with information about the function's name, return type, and parameters. 
- benefits:
	- more readable?
	- forward declaration is useful when you have multiple files and modules that depend on each other.
	- dependency management:
		- it might? help manage dependency between functions
	- self-documentation
		- Function prototypes 

- A more complex example
```c++
/*
* File: PowersOfTwo.cpp
* ---------------------
* This program generates a list of the powers of
* two up to an exponent limit entered by the user.
*/
#include <iostream>
using namespace std;
/* Function prototypes */
int raiseToPower(int n, int k);
/* Main program */
int main() {
int limit;
	cout << "This program lists powers of two." << endl;
	cout << "Enter exponent limit: ";
	cin >> limit;
	for (int i = 0; i <= limit; i++) {
		cout << "2 to the " << i << " = "
			<< raiseToPower(2, i) << endl;
	}
	return 0;
}
/*
* Function: raiseToPower
* Usage: int p = raiseToPower(n, k);
* ----------------------------------
* Returns the integer n raised to the kth power.
*/
int raiseToPower(int n, int k) {
	int result = 1;
	for (int i = 0; i < k; i++) {
		result *= n;
	}
	return result;
```

---
- function
	- there are two main types of functions in c++.
		- void functions is a function that does not return a value
		- other non-void function types, such as string functions, int functions are expected to produce a value of their specified return type.

- void function
	- a void function is a function that does not return a value. 
	- its return type is specified as void, these functions are typically used to preform certain actions or tasks without producing a result.
		- eg:
			  manipulate data
			  modify variables
			  display output
			  perform other operations




---

- reserved words
	- those are the keyword of c++

- defining local variable
- defining global variable

- enumerated types
	- where `typename` is the name of the new type, `namelist` is a lost of constants in the domain, separated by commas. 
	- syntax
		- `enum typename {namelist}`
	- examples
		- `enum Direction {NORTH, EAST, SOUTH, WEST}`
		- `eum Coin{PENNY = 1, NICKEL = 5, ...}`

- expression
	- composed of terms and operators
		- terms:
			- variables
			- function calls
		- operators:
			- character that indicates a computational operation
			- Binary operator:
				- `+`, `%`
			- Unary operator:
				- `++`, `(type)`, `sizeof`

---
- math: `<cmath>` package

- figure: 
![[Pasted image 20230520210652.png|400]]

---
- Precedence
	- A measure of how tightly an operator binds to its operands in the absence of parentheses.

- Type cast
	- It means that the language we can specifies an explicit conversion from one type to another.

- Logical operators
	- `!`: logical not
	- `&&`: logical and
	- `||`: logical or

- Question mark colon
	- `(condition)? exp1 : exp2`

- statements:
	- simple statements
	- blocks
	- compound statements
	- if statement
		- `if (cond) steatement else statement`

- namespace
	- namespace is a collection of names that contain standard library functions, objects and types.
	- The purpose of `std` namespace is to avoid naming conflicts and organize the various components of the C++ standard library.
	- Exploration and dynamically including headers and namespace
		- In C++, it is not possible to dynamically iterate over namespaces and automatically include then into the global scope using a loop.
		- In C++, there is no built-in mechanism to directly query a header file to explore what are the namespace that a header contains.
		- When working with libraries, users should find comprehensive documentation online. 
	- example of importing namespace content:
		- `using namespace name;`
			- this brings symbols from a library's name space into the global scope of your program so you can refer to them. 
		- `namespace::identifier`
			- without a using declaration, you can access symbols from a namespace by preceding them.


- eg: if-else statement
	- `iostream`: it is not "module". It is called "header" file that provides input output stream functionality.
	- `std`: It is a namespace name
	- `cout` is not a function call, but rather an object. It is an instance of the `std::ostream` class, which represents the standard output stream.
```c++
#include <iostream>

int main() {
    using namespace std;
    
    int n = 2;
    if (n % 2 == 0){
        cout << "That number is even." << endl;
    } else {
        cout << "That number is odd" << endl;
    }
    return 0;
}
```


- example: the switch statement
	- `switch(e)` sets up the switch statement, where `e` is the expression being evaluated
	- `case c1`: if the value of `e` matches `c1`, the statement following this label will be executed. 
	- `break` it used to exit the switch statement
	- `default` represent the default case label
```c++
switch(e){
	case c1:
		statements
		break;
	case c2:
		statements
		break;
	default:
		statements
		break;
}
```

- while statement
	- the general structure of the code is as follow
	- `while(true)` sets up an infinite loop that will continue indefinitely unless a break statement is encountered.
	- "Prompt user and read in a value" means you can display a message or prompt to the user, typically in the form of a text message or input box.
```c++
while (true){
	Prompt user and read in a value
	if (value == sentinel) break;
	Process the data value.
}
```

- example: while statement
```c++
while (cond) {
	statements
}
```

- for statement:
	- general structure
```c++
for (init; test; step){
	statements
}
```

- example: for statement
```c++
for (int i = 0 ; i <= limit; i++){
	cout << "2 to the " << i << " = " << raiseToPower(2,i) << endl;
}
```


---

- The standard C++ libraries
	- eg:
		- `#include <libraryname>`
- Including a local project library
	- which the c++ script would search for local project library within the same directory.
	- eg:
		- `#include "libraryname.h"`
		- `#include "console.h"`: which creates a console window on the screen as soon as your program starts up. 
- Notice the difference
	- `<>` for standard libraries versus `""` for local project libraries
	- `.h` for local project libraries versus no `.h` for standard libraries


---
- inputs:
	- `cin >>` is discouraged
		- problems
			- 1. hard to detect invalid input
				- ask for an integer, user types a string
			- 2. hard to read strings
				- reads a word at a time; hard to get an entire line
	- recommend:
		- `#include "simpio.h"`
		- `getInteger("prompt")`
		- `getReal("prompt")`
		- `getLine("prompt")`
		- `getYesOrNo("prompt")`

- defining a function

- approach 1:
	- classical way
```c++
// defining a function that returns the area of a circle with the given value
int circleArea(double r){
	return 3.1415 * r * r;
}

int main(){
	double a1 = circleArea(1.0);
	cout << a1 << endl;
	return 0
}
```

- approach 2:
	- Putting the function prototype before `main()` function
```c++
#include <iostream>
using namespace std;

// function prototype
int circleArea(double r);

int main(){
    double a1 = circleArea(1.0);
    cout << a1 << endl;
    return 0;
}

// function definition
int circleArea(double r){
    return 3.1415 * r * r;
}
```

---
- value semantics
	- In Java and C++, when variables (int, double) are passed as parameters, their values are copied. 
	- This means that a new copy of the variable is created within the function, and any modifications made to the parameter inside the function do not affect the original variable passed in from outside the function.

- reference:
	- referencing is a mechanism that allows you to create a reference to an existing variable,
	- notation:
		- use reference parameters by declaring a parameter with an ampersand (&) after its type. 
		- if you declare a parameter with an & after its type, it will link the functions to the same place in memory.
	- why it is useful?
		- reference is useful when working with functions.
		- By passing variables by reference, it enable the function to modify the original value, rather than creating a copy. 

- example of `ref` variable referencing `num` variable
```cpp
#include<iostream>

// This main function will return num = 20.
int main() {
    int num = 10;
    int& ref = num; // Creating a reference to 'num'

    ref = 20; // Modifying the value through the reference
    std::cout << num << std::endl; // Output: 20

    return 0;
}
```

---
- procedural decomposition
	- In C++, procedural decomposition refers to the process of breaking down a complex program into smaller, more manageable procedures or functions. It involves dividing the program into smaller units, each responsible for a specific task or functionality. This technique helps in organizing and structuring code, making it easier to understand, test, and maintain.
	- By decomposing a program into smaller procedures, you can encapsulate specific functionality within each procedure, making it easier to understand and reuse in different parts of the program. 
	- It follows the principle of "divide and conquer"
	- Goal:
		- Promote code reusability
		- Modularity: 
			- Procedures can be developed and tested independently, promoting parallel development and facilitating team collaboration. 
		- Maintainability
		- Encapsulation:
			- Procedures encapsulate specific functionality, making it easier to reason about and test. 
	- properties of a good function
		- fully performs a single coherent task
		- do not do too large a share of the work
		- is not unnecessarily connected to other functions
	- the main function should be a "concise" summary of the overall program

---
Characters, string methods

- operators related to characters
	- compare
	- mutable strings

---
# Lecture 4 

- Collections
	- "collections" refer to data structures or containers that are used to store and manage multiple elements or objects. Collections provide a way to organize and manipulate groups of data in a unified and convenient manner.
	- in the context of computer programming, most data structures can be considered as collections. 
	- By using collections, programmers can efficiently manage and manipulate groups of related data, perform operations on them, and implement algorithms and data processing tasks. 

- Lecture 4 covers 6 collection types
	- stack
	- queue
	- set 
	- map
	- grid
	- vector

---


- pass by reference
	- In C++, pass by reference is a mechanism that allows a function to directly access and modify the original variable passed as an argument, rather than creating a copy of the variable. 
- example
	- `modifyValue()` defines the variable `num` with `int&`, which means it will be passing the variable by reference.
	- That means `modifyValue()` would change the value of the original variable instead of copying. 
```c++
void modifyValue(int& num) {
    num = 42; // Modifying the original value
}

int main() {
    int value = 10;
    modifyValue(value); // Passing by reference

    std::cout << value << std::endl; // Output: 42

    return 0;
}
```


- passing grid as parameter
	- it usually means passing a two-dimensional array or a matrix to a function. A grid can be thought of as a collection of elements arranged in rows and columns.
	- when a `Grid` is passed by value, C++ makes a copy of its contents. Copying is slow, you should usually pass by reference (with `&`)
	- variations:
		- `int computeSum(Grid<int>& g){`:
			- this could do the work, but it causes danger that the code could change the original data in an unexpected way.
		- `int computeSum(const Grid<int>& g){`:
			- writing `const` in front of the Grid.
			- It makes the elements of the grid object cannot be changed. 
			- This is good for the function that just need to read values, and don't need to write values. 



---
### Array
- Property:
	- fixed-size 
	- Collection of elements of the same type
	- Stored in contiguous memory locations.
	- Arrays in C++ are zero-indexed, meaning the first element is accessed using index 0.
	- Declaration of array:
		- Syntax: `type name[size];`
		- eg: `int numbers[5];`




---

### Vectors
- Header
	- `#include "vector.h"`
- What is a vector?
	- 1. it is a dynamic array
		- a vector is a dynamic array that can grow or shrink in size as needed. 
	- 2. same type element collection
		- A vector allows you to store and manipulate a collection of elements of the same type. It provides a way to access elements using their indices, similar to arrays, but with additional functionality and flexibility.
	- aka a list, but there are difference as well
	- a collection of elements with 0-based indexes like a dynamically resizing array.
- methods:
	- `v.add`
	- `v.clear()`
	- `v[i]`
	- ...
- Difference between vector and list
	- 1. data structure
		- a list is implemented as a doubly linked list, where each element contains a pointer to the previous and next elements in the list.
		- a vector is implemented as a dynamic array, where elements are stored in contiguous memory locations. 
	- 2. memory allocation
		- List: The memory for each element is allocated individually, which can result in more frequent memory allocations and deallocations when compared to a vector.
		- Vector: The memory for the entire vector is allocated as a single block, providing efficient element access and reducing memory fragmentation.
	- 3. Insertion and deletion
		- List: Insertion and deletion of elements at any position in the list are relatively efficient because it only involves changing the pointers of adjacent elements.
		- Vector: Insertion and deletion of elements at the beginning or middle of a vector require shifting subsequent elements, resulting in a higher time complexity.
	- 4. random access
		- List: Random access to elements in a list is not as efficient since accessing an element requires traversing the list from the beginning or end.
		- Vector: Random access to elements in a vector is efficient because elements are stored contiguously, allowing direct memory access based on the index.
	- 5. memory overhead
	- 6. usage scenarios

- Difference between vector and array 
	- 1. Size flexibility: 
		- Arrays have a fixed size determined at compile time, whereas vectors can dynamically resize themselves at runtime. When using arrays, you need to specify the size when declaring them, and it remains constant throughout the program's execution. Vectors, on the other hand, can be resized using member functions like `push_back()` or `resize()` to add or remove elements as needed.
	- 2. Memory management: 
		- Arrays are typically allocated on the stack or as static variables, and their memory is managed automatically. Vectors, however, are implemented as dynamic arrays, which means they are allocated on the heap using new and deallocated using delete or delete[]. The vector class takes care of the memory management for you, ensuring proper allocation and deallocation.
	- 3. Access and iteration: 
		- Elements in arrays and vectors can be accessed and modified using the indexing operator (`[]`). However, vectors provide additional member functions like `at()`, which performs bounds checking and throws an exception if an out-of-range access is attempted. Arrays, on the other hand, do not perform bounds checking. Iterating over elements in both arrays and vectors can be done using loops, such as the for loop.
	- 4. Dynamic resizing: 
		- Vectors have the advantage of dynamic resizing. When elements are added to a vector and it exceeds its current capacity, the vector automatically allocates more memory and copies the existing elements to the new memory location. This resizing process may involve allocating a new block of memory and copying the elements, which can be computationally expensive. Arrays, being fixed in size, cannot be resized directly. If more elements need to be stored, a new array of the desired size must be created, and the existing elements must be manually copied.
	- 5. Standard library support: 
		- Vectors are part of the C++ Standard Library and provide various member functions and algorithms to manipulate and work with the elements. Arrays, however, are built-in language constructs and offer limited functionality. The vector class provides several helpful features like sorting, searching, inserting, and erasing elements, which are not directly available for arrays.
	- 6. Performance:
		- Arrays have a fixed size determined at compile time, which means the exact amount of memory required for the array is known in advance. 
		- Arrays offer efficient iteration performance because they provide contiguous memory storage. Elements in an array are stored sequentially in memory, which allows for efficient traversal using simple pointer arithmetic or index-based access. This locality of data improves cache utilization and can result in better performance compared to vectors
	- 7. Storage location
		- Arrays 
			- store elements in contiguous memory locations. The elements are stored one after another, occupying a continuous block of memory.
			- The memory for arrays can be allocated either on the stack or as static variables. The memory allocation is fixed and determined at compile time.
			- Arrays have a fixed size, which means the number of elements they can hold is known and does not change during runtime. 
		- Vectors 
			- store elements in dynamically allocated memory blocks. The memory is allocated on the heap using new and is managed by the vector class.
			- The vector class internally handles memory allocation and resizing. It maintains a pointer to the dynamically allocated memory block that holds the elements.
			- The memory allocation for vectors is not necessarily contiguous. Although the vector class tries to allocate a contiguous block of memory, it may need to allocate a new block at a different location if the previous memory block is insufficient or cannot be extended.


- example: declaring a vector
```c++
Vector<int> nums {42,17,6,0,-28};

Vector<string> names;
names.add("Stu"); //{"Stu"}
```

- nested vectors
	- collections can contain other collections
	- eg:
		- `Vector<Vector<int>> vv;`
			- This data structure the data must be rectangular.

- inside an array
	- the vector also stores its size and array capacity
	- if there is no untilled elements, the array is not allowed to grow in size without moving the elements into the new space.
	- special properties
		- unfilled elements:
			- you change your house each time you give birth to a baby, or you don't want to move that often
		- shift:
			- shift elements in order 

- figure:
![[Pasted image 20230520215503.png|400]]
![[Pasted image 20230520215709.png|400]]

### Grid
- Like a 2D array, but more powerful
- must specify element type in `<>` (a template or a type parameter)

- example of grid
```c++
//constructing a grid
Grid<int> matrix(3,4);
matrix[0][0] = 75;

// or specify elements in {}
Grid<int> matrix = {
	{75,61,83,71},
	{94,89,98,100}
};
```

- example:
	- approach 1 creates the grid
```c++
void processGrid(int grid[][3], int rows) {
    // Process the grid here
    // You can access elements as grid[i][j]
}

int main() {
    int myGrid[4][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9},
        {10, 11, 12}
    };

    processGrid(myGrid, 4);

    return 0;
}
```



---

- Abstract data type ADT
	- An Abstract Data Type (ADT) is a theoretical concept in computer science that describes a high-level view of a data structure and the operations that can be performed on it, without specifying the underlying implementation details. 
		- It focuses on what the data structure can do rather than how it is implemented.
	- By abstracting the data structure through the ADT, it becomes possible to reason about and work with data structures in a more general and modular way. It provide a standardized way of understanding and using data structures, allowing programmers to focus on the problem solving aspect of their applications rather than worrying about low-level implementation details. 
	- But ADTs and non-ADTs has no strict boundaries.
	- In practice, data structures are often implemented using classes or structures in programming languages, where the interfaces and behavior of the ADT are defined. 
		- This allows for interchangeable implementations that adhere to the specified interface, promoting code reusability and modularity.
	- we could say both `Vector` and `LinkedList` implement the operations of the abstract data type called "list".
		- other examples of ADTs: stack, queue, set, map, graph
	- the boundary between ADT and what is not can indeed be blurry at times. 

---
- Stacks and queues are not that powerful, so the sales would be tough. But these structures could be powerful for certain tasks
- Stacks and queues can be implemented in various form, such as built by linked list, or built by array. 
- Stacks and queues are abstract data types

---


- Stacks
	- A collection based on the principle of adding elements and retrieving them in the opposite order
	- Last in, first out (LIFO)
	- Client can only add remove examine the last element added
	- How to construct
		- With either linked list or array
		- linked list:
			- it can grow or shrink easily in size as elements are enqueued or dequeued. It does not require resizing or shifting elements, making enqueue and dequeue operations more efficient in terms of time complexity. 
	- Basic operations
		- push
		- pop
		- peek

- figure: stacks cheat sheet
![[Pasted image 20230521121729.png|400]]

- stacks in computer science
	- programming languages and compilers 
		- function calls are placed onto a stack (call = push, return = pop)
			- when a function is called, the program pushes the necessary information onto a stack, commonly known as the call stack. This info includes the return address, local variables and function parameters. 
			- Once the function execution completes, the corresponding information is popped from the stack, allowing the program to return to the calling function. 
		- compilers use stacks to evaluate expressions
			- compilers often use stacks to evaluate expressions
			- by using stacks,, compilers can parse expressions and generate appropriate code to evaluate them correctly.

- figure: illustrate how the notion of stacks exists in the function calls
![[Pasted image 20230521121628.png]]

- matching up related pairs of things
	- stacks are instrumental in determining whether related pairs of elements match or not.
	- eg:
		- palindrome (eg: civic, radar, deified) checking
			- by pushing each char onto the stack and then comparing it to the char popped from the stack, one can check for palindrome property. 
		- braces `{}` matching (within files)
			- Stack-based  algorithms can examine a file or a string to ensure that the opening and closing braces are properly matched.
			- The stack helps keep track of the opening braces encountered and ensures that they are matched with the correct closing braces. 
		- convert `infix` expressions to pre/postfix
			- Converting infix expressions (where operators are placed between operands) to postfix or prefix notation (where operators follow or precede operands) can be accomplished using stacks
			- Stacks facilitate rearranging the expression elements based on their precedence, resulting in postfix or prefix notation.
- sophisticated algorithms
	- searching through a maze with backtracking
	- many programs use undo stack of previous operations 

- Limitations
	- you cannot access a stack's elements by index (i.e. `s[i` is not work)
	- common idiom: pop them off 1 by 1 until the stack empty
		- each operation would eliminate 1 element..

- stack exercise
	- check balance of braces in the string.
		- every left braces must be closed by right braces in the opposite order
		- return the index at which an imbalance occurs
		- if any left braces are never closed, return the string's length

```c++
int checkBalance(string code){
	Stack<char> stack[]
	for (int i = 0; i < code.length(); i++){
		char c = code[i];
		if (c=='('|| c=='{'){
			stack.push(c);}
		else if (c == ')'|| c=='}'
			stack.peek();
			stack.pop();

	 return -1;
 }
```

---

- Queues
- 


---
- efficiency
	- a measure of the use of computing resources by code
	- assumption
		- 1 statement = 1
		- a function call's runtime = sum of runtime of statements in body
		- a loop of N iterations' runtime= (N * (loop body's runtime)
---
# Lecture 6 `Set` and `Map` classes

### Associative
- It means that each element in the container has an associated value or key, which is used to uniquely identify and access that element.
- It refers to 
	- 1. The relationship between elements 
	- 2. The relationship between elements and their associated values. 
- Why associative features within the data structure is useful?
	- The associative nature of sets and maps allows for efficient searching and retrieval operations, as the underlying data structure (usually a balanced binary search tree) is organized in a way that optimizes these operations based on the keys or element values. 
	- 1. Fast retrieval:
		- Hashing algorithms or other indexing techniques to quickly allocate the desired value based on its associative key.
	- 2. Flexible data organization
		- Unlike linear data structure like arrays or lists that use numerical indices, associative structures like use keys that can be various types (eg: string, integers or objects).
		- This flexibility enables efficient storage and retrieval of data, in a way that matches the problem domain and the nature of the data. 
	- 3. Easy data manipulation
		- Associative features simplify data manipulation operations. 
		- They provide convenient methods for adding, removing, and updating data elements based on their associative keys. 
		- These operations typically have constant or near-constant time complexity, making it efficient to modify the data structures.
	- 4. Key-based access
		- When knowing the key and need to retrieve the corresponding value. It eliminates the need for iterating over the entire data structure, leading to improved performance and reduced computational overhead. 
	- 5. Enhanced search capabilities
		- Associative data structure offer powerful search capabilities based on key-value pairs. They allow for efficient searching, filtering and sorting of data elements based on specific criteria.
	- 6. Improved code readability
		- Associative features make code more readable and self-explanatory.
- eg:
	- in set, the elements themselves act as keys and there are no separate values associated with them. Elements are stored and retrieved based on their ordering within the set.
	- in a map, each element has both a key and a value. The key is used to identify and locate the element, and the associated value provides additional information or data associated with that key.
		- each key stores key-value pairs, where each key is unique within the map, allowing efficient lookup and retrieval of values based on their corresponding keys. 
- However, "associative" in math has a different meaning:
	- The associative law states that for certain operation, the grouping of elements does not affect the result. 

### Order or non-order
- The order information has some values:
	- 1. sequential access
		- it is particular useful when the order of data is significant, such as time series data or data that follows a specific pattern
	- 2. index-based access
		- it allows the user to access elements by their indices or positions.
		- this technique is valuable for tasks like sorting, searching and random access to elements. 
	- 3. range operation
		- ordering facilitates performing operations on ranges of elements 
	- 4. searching and sorting
		- ordering is crucial for efficient searching and sorting algorithm.
		- algorithms like binary search which rely on the order of elements, require the dataset to be sorted. 
	- 5. analysis and visualization
		- ordering allows for creating meaningful visual representation

---

### Indexing
- Definition:
	- Indexing - refers to the process of organizing and efficiently accessing data based on specific attributes or keys.
	- It involves creating a data structure called an index that contains references to the actual data, enabling faster searching, retrieval, and sorting operations.
- Where we can see it
	- Database
	- File systems
	- Search engines
- Purpose:
	- Optimize data retrieval by reducing the amount of time and resources required to locate specific information within a large dataset. 
		- When a search or retrieval operation is performed, the index is consulted to determine the location of the desired data.
- Properties related to indexing
	- 1. Specialized storage system 
		- if there is a large number of elements that need to be stored and accessed efficiently, it would be appropriate using a database or specialized data storage system that is designed for efficient querying and retrieval, rather than relying on a single text file. 
			- These systems provide indexing mechanisms and data structures optimized for handling large amount of data with efficient retrieval operations. 
			- By employing indexing techniques, computers can dramatically improve the efficiency of attribute-based tree searches.
		- Examples:
			- Relational databases
			- NoSQL databases
			- Search engines such as Elasticsearch
	- 2. Independent tree structure
		- The process of indexing an attribute-based tree involved building and maintaining these data structures alongside the tree itself. 
			- When new noes are added or existing nodes are modified, the index structures need to be updated accordingly to ensure their accuracy and efficiency.
		- Examples:
			- B-trees
			- Hash tables 
	- 3. Reducing the search space
		- A. general binary tree (what without subsetting characteristics):
			- Ordered indexing:
				- Many indexing structures such as binary trees or skip lists, maintain data in a sorted order based on a specific key or attribute. This sorted arrangement allows for quick and effective searching through techniques like binary search or tree traversal. 
			- Hashing:
				- Hash-based indexing structures uses hash tables or hash map utilize a hash function to map keys to specific positions or buckets in the structure. This hashing process provides a direct and efficient lookup mechanism. 
				- While these structures may not directly support subsetting, they allow for constant-time retrieval of individual items by computing the hash and directly accessing the corresponding bucket, effectively reducing the search space to a single bucket.
			- Indexing statistics
				- Index statistics can include the number of items, ranges, or distribution of values. By utilizing these statistics, search algorithms can make informed decisions about where to start searching or which parts of the index are likely to contain the desired data. This targeted approach further reduces the search space, leading to improved efficiency.
			- Partial matching:
				- Some indexing structures, like inverted indexes commonly used in search engines, are designed to handle partial matching. While not strictly subsetting, these structures allow for efficient retrieval of records that partially match a given query or pattern. 
				- By indexing and organizing data based on tokens, keywords, or features, they can quickly identify and retrieve relevant records, thereby reducing the search space to a subset of the entire dataset.
		- B. trees that their index that is having "Subsetting" characteristics could reduce the search space.
			- Example 1:
				- Such as you search a large dataset that has "Smith" attribute in its last name, then you do not need to sequentially scan the entire dataset toe examine each record to determine if the last name matches. 
			- Example 2: When it is an inclusive tree structure: 
				- Then the parent node would be acting as a description of the child node. When parent nodes are describing the child node, then the parent node can be used as a filter of that search, results in the reduction of the search space, resulting in faster and more efficient search operations. 
			- Example 3: index that is created on attributes commonly used in filtering or searching
				- Primary keys, unique identifiers, frequently used fields
	- 4. Faster data retrieval
		- The main purpose of indexing is to provide a data structure that allows for efficient data retrieval, even if the search space remain the same. 
- Types of indexing
	- Hash indexing:
		- uses a hash function to map keys to specific locations 
	- Search tree indexing
	- Inverted indexing
		- It is commonly used in search engines for keyword-based retrieval.
	- Array
	- Multi-index hashing
		- Multiple indexing trees are created using different hashing functions, and each tree represents a different index structure. Each indexing tree maps the dataset to a set of hash keys, which are used to efficiently retrieve and organize the data. 
		- By employing multiple indexing trees with different hash functions, it becomes possible to address the dataset in various ways simultaneously.
		- Advantages:
			- 1. It allows for multiple query types or access patterns to be supported efficiently.
			- 2. It can improve the overall query performance and scalability of the system by distributing the data across multiple indexing trees and leveraging parallelism. 
			- 3. It provide redundancy and fault tolerance. If one indexing tree becomes unavailable or experiences performance issues, the data can still be accessed through other indexing trees.
- Indexing in database management
	- Primary index 
		- (User- defined. Ordered on a key field). secondary index (candidate key)
	- Dense index 
		- (there is an index record for every search key value in the database)
		- Advantages
			- 1. Support for range queries
			- 2. Efficient data access with indexed key
				- For example, an array which is putting things densely. We have the starting address and the index, and then we would have an exact address of the value. 
				- Dense index enable such direct access to individual records without the need to scan the entire data set sequentially
				- Sparse index, in the other hand, include pointers or references to the actual records..
					- When you perform a record lookup using a sparse index, you need to traverse the index structure to locate the appropriate index entry. 
					- Once you find the relevant index entry, you can use the pointer or reference to access the corresponding record.
	- Sparse index 
		- (index records are not created for every search key)
		- Sparse index is useful when the dataset is large, and storing an entry for every record would be impractical or inefficient. 
		- Advantage
			- 1. reducing storage overhead
				- With dense index, such as an array, the space that are empty are actually filled by zeros. 
			- 2. faster indexing operation
			- 3. efficient for infrequent access patterns 
	- Multilevel index 
		- (As the size of the database grows, there is a need to keep the index records in the main memory, to speed up the search operations. If single-level is used, then a large size index cannot be kept in memory, which leads to multiple disk accesses. )
		- ML index helps in breaking down the index into several smaller indices, in order to make the outermost level so small that it can be saved in a single disk block. 
		- However, the usefulness of the multilevel index, again is not useful unless it follows the hierarchical structure and provides a systematic way to narrow down the search space at each level. 
- Drawbacks of indexing
	- 1. Increased storage space
		- Additional space for the index structure itself. 
	- 2. Increased overhead during data modifications
		- When data is modified (inserting, updating, or deleting), the corresponding indexes need to be updated as well to maintain consistency.
	- 3. Index creation time
		- Indexing or reindexing could be time consuming. 
	- 4. Increased complexity and maintenance
	- 5. Selectivity and query optimization
	- 6. Increased complexity for concurrent operations 
- Decision to use indexing
	- The size of the dataset
	- The frequency and complexity of queries
	- The trade-off between the cost of indexing and the potential performance improvements 

### Inverted indexing
- Traditional indexing:
	- Document:
		- Indexed based on their document ID, or the index maps these IDs to the terms contained in each documents. This allows quick retrieval of documents given their IDs. 
- Inverted indexing:
	- Documents:
		- Inverted indexing creates an index that maps each unique term found in the documents to the documents that contain that term. 
		- The index is essentially a data structure that stores a list of documents associated with each term.
		- Each entry in the index typically includes the term and a list of document identifiers (or pointers) where the term appears. 
	- Search engines:
		- By using inverted indexing, search engines can efficiently find documents containing specific terms or perform complex queries. 
		- When a user submits a query, the search engine looks up the query terms in the inverted index and retrieves the relevant documents associated with those terms. This process is faster compared to scanning all documents because the search engine only needs to examine the entries related to the specific terms.
- Demonstration of inverted indexing:
	- Documents:
		- Document 1: "The quick brown fox jumps over the lazy dog."
		- Document 2: "The lazy dog sleeps all day."
		- Document 3: "The quick brown fox enjoys jumping."
	- Inverted index:
		- We tokenize the documents into individual terms and create an index that maps each term to the documents that contains it. 
			- The: 1, 2, 3
			- quick: 1, 3
			- brown: 1, 3
			- fox: 1, 3
		- So we just need to keep adding new articles to the end of each word-index
	- Data structure for word-index
		- The choice of data structure for storing the word-index entries can vary depending on the specific requirements and constraints of the information retrieval system.
		- Dense array
			- In a search engine scenario, where the number of unique terms can be in the millions or even billions, using a dense array for the inverted index would be impractical. Instead, more efficient data structures, such as trees or hash tables, are commonly used.
			- Because the number of unique terms in a large-scale search engine scenario can be enormous, leading to significant memory waste and inefficient access times.
			- example :
				- 0 | 1, 2, 3
				- 1 | 1, 3
				- 2 | 1, 3
		- Tree: (sparse way to store things)
			- It can be used for storing word-index entries when the number of unique terms is large or when the terms are dynamic and may change frequently. 
			- example:
				- the | 1, 2, 3
				- quick | 1, 3
				- fox | 1, 3
				- brown | 1, 3
	- Adding new items:
		- So we just need to keep adding new articles to the end of each word-index, like article 4 also contains "the quick brown fox", then word-index "the", "quick ", "brown", "fox" would be added index 4.
	- Searching:
		- Say we search "The quick brown fox"
		- And then we search for  "the quick brown fox", we find that 4 word-index "the", "quick ", "brown", "fox"  and intersect them

---

#### Hashing, hash algorithm, hash code, hash indexing 
- Hashing is a technique that converts an element into an almost unique numerical value called a hash code. Converting elements into unique numerical values called hash code. These hash codes serve as the keys for storing and retrieving elements within the set. The `Set` class variable uses these hash codes to organize and store the elements. 
- In short:
	- hash( "key" ) --> (hexagonal) integer
- How a program determine its hash function?
	- the choice depends of various factors:
		- 1. the characteristics of the key
		- 2. the desired performance
		- 3. the potential for collision
- Types:
	- 1. built-in hash functions
		- many programming languages provide built-in hash function for common data types
		- optimized for general purpose use and provide a good balance between performance and distribution of hash codes. 
	- 2. custom hash functions 
		- if the keys have specific characteristics, or requires a specialized hash function, a custom hash function can be implemented. 
		- eg: for string, might takes account each character's ASCII value and combines them in a way that provides a good distribution.
	- 3. library functions and algorithms
		- libraries and frameworks often provides hash functions and hashing algorithms specifically tailored for certain data structures or applications.
	- 4. domain specific knowledge
		- understanding the characteristics and patterns of the key in a specific domain can help guide the choice of a hash function.
- Hash algorithm:
	- The goal of a good hash function is to distribute the hash codes uniformly across the available space, minimizing collisions. 
	- Hashing is a technique used to map data to a fixed-size numerical value, called a hash code or hash value. This hash code is calculated based on the contents of the data, and it serves as an index or address for storing and retrieving the data in a data structure called a hash table.
	- The process aims to make a bijective function between the set of elements and the set of associated hash code. 
	- Hash code:
		- for an entire file that might be megabytes or gigabytes in size, what is gives you is a code, 16 or 32 characters, generally hexadecimal, that "sum up" everything in that file. 
		- If you crush it down, to infinite level, it becomes a hash code.
		- You cannot do it backwards to get the data back out, but it is like a signature, a confirmation that this files is really what it is. 
	- Avalanche effect
		- if you change anything in the file, then the whole hash should be different. 
	- Hash collision:
		- Where you have two documents, which has the same hash. 
		- Pigeonhole principle - if there is $n+1$ data can we only have $n$ slots, then there must be at least one slot has hash collision. 
	- Specific outputs of a hash function (i.e. some hash code) should not be allowed to be manually changed
		- If someone can make a file that sums to a certain hash, then people can fake document then has a signature match. 
	- If a hash is too slow, no one use it. If a hash is too fast, there will be easier to have collision. 
		- MD5 is a fast hash algorithm and was used in the past. Now computer is fast enough that could create hash collision deliberately. 
		- For many years, a word will be stored next to its MD5 for some reasons. If you type an MD5 hash into google frequently the word it was hashing comes out. That means pretty much every word's MD5 hash is known.
- Examples:
	- 1. MD5 (Message digest algorithm)
		- widely used hash function that produces a 128-bit hash value. It takes an input message and generate a fixed size hash code, regardless of the size of input.
	- 2. SHA-256 (Secure hash algorithm 256 bit)
		- widely used cryptographic hash function that produces a 256 bits hash value.
		- It is commonly used in various security applications, including digital signature and blockchain technology.
	-  3. "Check digits" in a bar code on a credit card. 
		- The last digit of that series of digit is determined by the digits in the front. So if you change the previous digit, the last digit would change as well. 
- The sequence of producing a hash code: 
	- 1. Consider having a library with thousands of books, each labeled with a unique book ID. Now we want to find a book without searching through every single book, we create an index card system. 
	- 2. The book ID acts as a hash code in this analogy. 
	- 3. Now if someone want to find a particular book, he don't need to go through the entire library shelf. Instead, he can go to the index card catalog, look for the card with the book ID.
	- 4. Reduce to $O(log\ n)$ operation
		- Assume the index cards are organized using another data structure, such as a binary search tree. In this case, find the index card with the book's ID can be done in $O(log\ n)$ time complexity. Which means a more efficient search operation. 
	- 5. Reduce to $O(1)$ operation
- Reasons hash function could produce an almost unique hash code for a file?
	- 1. Deterministic:
		- a hash function will always produce the same hash code for the same input. The property ensures consistency and reliability.
	- 2. Fixed input size:
		- hash function generate hash codes of fixed length, regardless of the size of the input file. The fixed output size enables efficient storage and comparison of hash codes.
	- 3. Avalanche effect: 
		- a small change in the input will result in a significantly different hash code.
		- even a minor modification in the input cause a drastic change in the resulting hash code. 
	- 4. preimage resistance:
		- it is computationally infeasible to determine the original input file from its hash code. Given a hash code, it is highly unlikely to find a file that produces the same hash code, except through an exhaustive search.
	- 5. Collision resistance:
		- A collision occurs when two different input files produce the same hash code.
- Why it is not truly unique?
	- 1. While there are numerous possible hash code combinations, it is still a limited number of them. And the variety of files could reach infinite, which means the variety range of files is larger than the variety of hash code. In this case, why we still optimistically claim that hash code is almost unique?
		- SHA-256: 
			- The variety range = $2^{256} = 115792089237316195423570985008687907853269984665640564039457584007913129639936$
			- So it takes a lot of computation to find a match. 
			- That also explains why it is good to hash code in membership testing, and use hash code for digital signature. 
	- 2. Hash code collision is happening in the daily life. We can see the non-uniqueness from that. 
		- When mining a bitcoin. It will take very very long time to find one. 
		- Because hash code does not have information about the original document. So brute force is the only way to determine the 
- Applications:
	- 1. `Set` variable:
		- See hash table
	- 2. Digital signature
	- 3. Membership testing  
	- 4. Database indexing 
		- See hash table 
	- when retrieving:
		- the program computes the hash code of the element and use it as a lookup key. 
		- this process has an average time complexity of $O(1)$ for retrieval, meaning it takes a constant amount of time regardless of the size of the set. 
	- compare with array: 
		- On the other hand, arrays require iterating through each element in the array to find the desired element. In the worst case, the time complexity for retrieval in an array is $O(n)$. 
		- Array structures designed for ordered access would have slower performance on membership testing. 


### Hash table / hash map
- Hash table is a data structure that allows for efficient insertion, deletion, and retrieval of key-value pairs. 
- Relationship with hash code.
	- While hash code is just an address, hash table / hash map is a data structure.
	- Hash table uses hash code of an element as key, linking to the actual value of the element. By thinking of hash codes are almost unique, we pass hash codes into modulo operator which the base is the size of the array of buckets which is larger than the total variety of hash code. 
- How it works (ver 1):
	- 1. Hash function
		- See "Hash function"
	- 2a. Bucketing
		- To minimize collisions, hash tables typically use a technique called bucketing or chaining.
		- Each bucket in the array can hold multiple elements. When a collision occurs, the conflicting elements are stored in the same bucket using additional data structures like linked lists, arrays, or trees. This allows for efficient retrieval of elements even when collisions happen.
	- 2b. Array of buckets
		- The hash table consists of an array of buckets or slots. 
		- Each bucket can store a key-value pair or a reference to a linked list of key-value pairs.
		- Factors that affecting the initial size of the array of buckets
			- 1. the load factor
				- it is the ratio of the number of elements stored in hash table, to the total number of buckets in the hash table. 
				- It is typically represented as a decimal value between 0 and 1. 
				- 0.75 means the hash table is 75% of the buckets are occupied
				- eg: expecting store 100 key-value pairs, and choosing a load factor of 0.75, then the initial size would be 133.33.
			- 2. choosing a prime number for the initial size of the hash table helps minimize potential collisions and improves the distribution of hash codes. 
			- 3. dynamic sizing
				- this approach allows the hash table to grow or shrink as needed, optimizing memory storage.
			- 4. load factor and resizing strategy:
				- the specific resizing strategy can vary.
			- 5. Memory constraints
			- 6. The desired trade-off between space and time complexity
		- What are not the factors:
			- Expected number of elements
		- 2c. In true practice, the size of array of buckets is much less than the total variety of the hash-code model such as SHA-256.
			- Q: 
				- Say we are using the most popular hash algorithm SHA-256, the total variety of it is $2^{256}$, which is very large. Is that mean we need to have a very large container for making a hash table that fits it?
			- A:
				- In practice, hash tables are typically implemented with a fixed-size array of buckets that is much smaller than the total variety of hash codes.
				- Hash functions are designed to distribute the hash functions uniformly across the range of possible values. 
				- While it is theoretically possible to have collisions, where two different inputs produce the same hash code, the likelihood of such collisions occurring in practice is extremely low for a well-designed hash function like SHA-256.
	- 3. Hash code to bucket index mapping:
		- How to do that?
			- Modulo operation (%). 
		- Why it is useful?
			- The usefulness of modulo operation only would be manifested If the hash code range is larger than the range of available bucket indices.
			- If the hash code range is smaller than index range, then it is no use to inspect its modulo.
		- The hash code is typically an (hexagonal) integer value (?), which means the hash code is divisible.
		- Bucket:
			- the bucket index refers to the position or slot where an item is stored based on its hash code. 
			- Each bucket can hold multiple items or a reference to a linked list of items with the same hash code.
		- Division:
			- The hash code is divided by the total number of buckets in the data structure, and the remainder (modulo) of that division determines the index.
		- This division ensure the resulting index is within the valid range of bucket indices. 
		- It effectively wraps the index around within the range, allowing for even distribution of items across the buckets. 
	- 4. Insertion:
		- The mapping between the hash code and the index in a hash table typically done using the modulo operator.
			- key --"hash function"--> hash code --"modulo operation"--> index 
		- To insert a key-value pair into the hash table, the hash code is calculated for each key, and the index is determined using the hash code. 
		- If the bucket at that index is empty, the key-value pair is stored directly. 
		- If the bucket is occupied, a collision occurs. 
	- 5. Collision handling
		- Collisions happen when two different keys produce the same hash code or the same index. There are several techniques to handle collision.
		- techniques:
			- 1. separate chaining
				- In this approach, each bucket in the hash table contains a linked list or any other dynamic data structure. When a collision occurs, the collided key-value pair is inserted into the linked list associated with the bucket. This allows multiple key-value pairs to be stored in the same bucket.
				- When retrieving a value, the hash table follows the same hashing function to find the correct bucket and then searches the linked list for the desired key.
			- 2. open addressing
				- With open addressing, collisions are resolved by finding an alternative empty bucket within the hash table itself. When a collision occurs, a probe sequence is generated, which defines the order in which alternative buckets are checked. 
				- Common probe sequences include linear probing (checking adjacent buckets), quadratic probing (checking buckets in a quadratic sequence), and double hashing (using a secondary hash function). 
				- The process continues until an empty bucket is found or the entire table is searched. 
			- 3. Robin Hood Hashing: 
				- Robin Hood hashing is a variation of open addressing that aims to minimize the variance in the probe sequence. 
			- 4. Cuckoo Hashing: 
				- Cuckoo hashing also uses open addressing but with multiple hash functions and multiple tables.
	- 6. Retrieval (value associated with a key)
		- No collision scenario
			- Every time retrieval requires a key.
			- When having keys, we can produce hash code and then pass it into modulo operator to access the index. The index of the value is determined. 
			- If the bucket is empty, the key-value pair associated with that particular key is not found. 
			- If the bucket is occupied, the linked list (in separate chaining) or probing (in open addressing) is used to find the matching key-value pair.
		- Hash tables that using "separate chaining" 
		- Hash tables that using "open addressing"
- Time complexity of hash table manipulations
	- Data insertion
		- When inserting data into a hash table, we mostly do not have the key value pair existing in the hash table. But we can use the document at hand to create the key and then link it with our document. 
		- Action flow
			- having a key (i.e. the document) --"hash function"--> hash code --"modulo operation"--> index (location of the data) determined --> insert the data
		- It is a $O(1)$ operation
	- Data retrieval
		- Querying for specific data based on certain criteria rather than retrieving the exact document itself. 
		- The hash table or database system utilizes its indexing structures and algorithms to locate and retrieve the relevant data based on your query.
		- We might need to learn "B-trees", "Balanced search trees" or "bitmap indexes" to further understand how those data retrieval works. 
		- Action flow
			- 1. You formulate a query specifying the criteria or attributes of the data you are interested in retrieving. This query could include various conditions such as matching certain fields, values, or patterns.
			- 2. The query is executed against the hash table or database system, which internally uses hash-based indexing or other indexing structures.
			- 3. The hash table or database system processes the query using its internal algorithms to locate the relevant data based on the specified criteria.
			- 4. The system uses its own hash functions and indexing mechanisms to efficiently navigate and search through the data.
			- 5. The matching data satisfying the query conditions is retrieved and returned as the result set.
		- The time complexity for retrieval can vary depending on factors such as hash collisions, the quality of the hash function, the size of the hash table, and the implementation details of the database system.
		- Average case: $O(1)$
		- Worst case: $O(n)$
		- Use additional structure to improve the retrieval performance:
			- Worst case becomes $O(log\ n)$
- Applications of hash table:
	- associative arrays
		- hash tables are often used to implement associative arrays or dictionaries, where each key is associated with a value.
	- database
		- many databases use hash tables as an indexing mechanism
	- caches
		- hash tables are commonly used in caching systems to store frequently access data
	- compiler symbol tables
		- compilers use symbol tables to store information about variables, functions and other symbols in a program.
	- cryptography
		- hash functions are an essential component of cryptographic algorithms.
	- spell checkers and dictionaries
		- hash tables are used in spell checkers and dictionaries to efficiently check the correctness of words and provide suggestions for misspelled words
	- router tables
		- hash tables are used in routing tables to determine the next hop for packet forwarding.
	- caching and memorization
		- by using the inputs as key and the corresponding outputs as values, hash tables enable fast lookup and retrieval of cached or memorized results, improving performance in computations and algorithms. 



---

### Set
- Definition
	- A set is a container in C++ that stores a collection of unique elements in a specific order. 
		- `mySet.begin()` and `mySet.end()` is the first and final element of the set that following that order. 
	- It is implemented as an associative container using a balanced binary search tree (usually red-black tree).
- Key points:
	- elements in a set are always sorted in ascending order
	- each element in the set is unique, i.e. no elements can have the same value. 
	- the operation performed on sets, such as insertion, deletion and search, have an average time complexity of $O(log\ n)$, making sets efficient for large datasets. 
	- Sets provide useful member functions like `insert()`, `erase()`, `find()`, `size()` to manipulate and access elements. 
- How to declare set:
	- `std::set<int> mySet;`
	- which `std::set` class is available in the C++ standard library and provides an implementation of sets. 
- How sets look up elements
	- Sets often use data structure like hash tables or hash sets to store the elements and enable fast retrieval.

- Figure: set
![[Pasted image 20230523190616.png|200]]

### Hashset
- implemented using a special array called a hash table
- very fast, elements are stored in unpredictable order
- values must have a `hashCode` function


### Map
- Definition:
	- A map is an associative container in C++ that stores a collection of key-value pairs.
	- It is implemented as a balanced binary search tree (usually a red-black tree) similar to sets. 
	- A map is a collection of pairs `(k, v)`, sometimes called key/value pairs, where v can be found quickly if you know k.
	- Other terms you may hear for a map are dictionary or associative array.
	- A map is a generalization of an `array`, where the "indexes" don't need to be integers:
- Features:
	- Each element in the map consists of a key and its corresponding value, where the key is unique within the map.
	- The elements in a map are sorted based on their keys in ascending order.
	- The time complexity for common operations like insertion, deletion, and search in a map is `O(log n)`.
	- Maps provide member functions such as insert(), erase(), find(), and size() to manage elements efficiently.
	- The std::map class is available in the C++ Standard Library and provides an implementation of maps.
- Examples:
	- Maps are everywhere. The key is the title, the value is the article. 
- Declaration:
	- `Map<string, int> votes;`
- Functions:
	-   `m.clear()` : removes all key/value pairs from the map
	-   `m.containsKey(key)` : returns `true` if the map contains a value for the given key
	-   `m[key]`  
	    `m.get(key)` : returns the value mapped to the given key; **`m[key]` only**: if `key` is not in the map, **adds** it with the default value (e.g., `0` or `""`); **`m.get(key)` only**: if `key` is not in the map, returns the default value for the value type, but does not add it to the map.
	-   `m.isEmpty()` : returns `true` if the map contains no key/value pairs (size 0)
	-   `m.keys()` : returns a `Vector` copy of all keys in the map
	-   `m[key] = value`  
	    `m.put(key, value)` : adds a mapping from the given key to the given value; if the key already exists, **replaces** its value with the given one
	-   `m.remove(key)` : removes any existing mapping for the given key (ignored if the key doesn't exist in the map)
	-   `m.size()` : returns the number of key/value pairs in the map
	-   `m.toString()` : returns a string such as "`{a:90, d:60, c:70}`"
	-   `m.values()` : returns a `Vector` copy of all the values in the map
- Types of maps:
	- Map:
		- Iteration over the elements is in sorted order 
		- Really fast access $O(log\ n)$ per retrieval, 
		- Maps are implemented using a "binary search tree"
	- Hash map
		- Iteration over the elements is not in a useful order (it is jumbled)
		- It is ridiculously fast
		- $O(1)$ per retrieval. 

- Figure: map
![[Pasted image 20230523190631.png|200]]

### Counting unique words using maps


---
# Lecture 7 - Big O and asymptotic analysis

- Big O notation
	- why we love $O(1)$ and $O(log\ n)$ behaviors 
	- $O(1)$: 


- Plotting the time complexity graphs 

- Hidden loop
	- The code might performs loop operations without you writing loop
	- eg: inserts an element at the beginning of a vector. 

- constant time $O(1)$
	- eg:
		- adding or removing from the end of a vector
		- pushing onto a stack or popping off a stack
		- enqueueing or dequeuing from a queue
		- Inserting or searching for a value in a hash table

- linear search
	- which means search for a particular value 1 by 1
	- Best case: $O(1)$
	- Worst case: $O(n)$

- binary search 
	- worst-case complexity: $log_2\ n$

- exponential time 
---

# Lecture 13 C++ classes

### Class 
- Class is a template for a new type of objects
- Objects is entities that combines state and behaviors
- Abstraction:
	- separation between concepts and details
- Elements of a class
	- Member variables
		- State inside each object
		- Also called instance variables or fields
		- Each object has a copy of each member
	- Member functions
		- Behavior inside each object
		- Also called methods
		- Each object has a copy of each method
	- Constructors
		- Initialize new objects as they are created
		- Sets the initial state of each new object
		- Often accepts parameters for the initial state of the field

- Defining a class in the header file:
	- The template could refers to [[cs106x programming abstractions in c++#^008c2b]]

- Declaring a class object
	- `MyClass a;`
- Using public functionalities of the class object 
	- `a.func1(argument)`


### Constructors
- A constructor is a special member function of a class that is used to initialize objects of that class. It is called automatically when an object of the class is created. 
- Constructors are a type of member function, but constructors must follow the following syntax characteristics: 
	- 1. Name: 
		- A constructor has the same name as the class in which it is defined. It does not have a return type, not even void.
	- 2. Initialization: 
		- The primary purpose of a constructor is to initialize the member variables of an object. It ensures that the object starts in a valid and usable state.
	- 3. Automatic invocation: 
		- When an object is created, the constructor is automatically called, and its code is executed before the object is available for use.

### `this` pointer
- In C++ has a `this` _pointer_ to refer to the current object (this is similar to `self` in Python).
- The "this" pointer is a special pointer available within the scope of non-static member functions of a class. It points to the object on which the member function is being called.
- Syntax:
	- `this->member`
- Common usage:
	- In the constructor, so parameter names can match the name of the object's member variable. 
- Example 1
```cpp
BankAccount::BankAccount(string name, double balance) {
    this->name = name;
    this->balance = balance;
}
```
- Example 2a: 
	- A class definition which the constructor is not using parameters that is member variable or function of that class.
	- Thus, we do not need to put `this->` pointer to assert that variable is a member variable. 
```cpp
class Rectangle {
public:
    Rectangle(int width, int height);
    Rectangle(int side);
    Rectangle();
};
```
- Example 2b:
	- The overloading constructor `Rectangle()` is using the member variable `width` and `height`. 
	- In this case, we are using the overloaded constructor `Rectangle` to initialize an object. 
	- The member variables `width` and `height` are indeed set to the specified values
```cpp
class Rectangle {
private:
    int width;
    int height;

public:
    Rectangle(int width, int height) {
        this->width = width;
        this->height = height;
    }

    void printArea() {
        int area = this->width * this->height;
        std::cout << "Area: " << area << std::endl;
    }
};
```


### Overload

### Class overload
- In C++, an overloaded constructor refers to having multiple constructor functions with the same name but different parameter lists within a class. 
- Usefulness:
	- It provides different ways to initialize objects of that class.
	- Overloaded constructors allow you to create objects with different initializations or configurations depending on the arguments passed.
```cpp
// purpose: an overloaded constructor
//          to create a custom fraction
//	        that immediately gets reduced
// arguments: an int numerator
//            and an int denominator
Fraction::Fraction(int num, int denom)
{
      
   this->num = num;
   this->denom = denom;
  
	// reduce in case we were given 
  // an unreduced fraction
	reduce();
      
}
```


### Function overload
- overloading:
	- function overloading is a feature in c++ that allows multiple functions to have the same name but different parameters. This provides flexibility and improves code readability by giving descriptive names to functions performing similar operations.
	- When a function is overloaded, the compiler determines which version of the function to call based on the number, types, and order of arguments provided during the function call. The decision is made at compile time and is known as compile-time polymorphism or static polymorphism.

- Example:
	-  the print function is overloaded with three versions that take different types of parameters. 
```cpp
void print(int value);
void print(float value);
void print(const char* value);
```

### Operator overload

```cpp
ostream& operator<<(ostream& out, Fraction& frac) {
    out << frac.num << "/" << frac.denom;
    return out;
}
```
- Example of using the overloaded `<<` operator
```cpp
Fraction frac(4, 5);
cout << frac << endl; //4 / 5

```


- `friend`:
	- this keyword grants the declared function access to the private and protected members of the class, allowing it to operate on the class's private data. 
	-  In this example, friend function `operator<<` has the effect of allowing the `Fraction` object to be printed directly to an output stream using stream insertion operator,
		- where the replaced printout is 
			- `out` and `frac` variable?
		- where syntax of that line of code is: 
			- `operator<<` is the function that we are going to overload
			- `std::ostream&` is the return type of the function 
			- `(std::ostream& out, Fraction& frac)` is the overloading statement. 
		- the difference of printing a `Fraction` object
			- without that line:
				- the compiler will generate an error. Because `operator<<` is not defined for the `Fraction` class by default. 
			- with that line:
				- `operator<<` is responsible for defining how the `Fraction` object should be formatted and printed to the output stream.


- What is `std::ostream&`?
	- It is not directly related to the class template `std::ostream`, but rather it represents a reference to an object of the `std::stream` class.
	- It is not a standalone type but rather a reference type (`&`) applied to `std::ostream` class
	- `std::ostream&` is the return type of the `operator<<` function.
	- The purpose of the `std::ostream&` return type is to allow chaining of output operations, allowing chaining of output operations on `std::ostream` objects. 
- overloading `std::ostream&`:
	- 1. `&` indicates the variable of this type will refer to an existing `std::ostream` object rather than creating a new object.
	- 


- Without `friend` function:
```cpp
Fraction frac(3, 5);
std::cout << frac;  // Compilation error without friend function
```
- With `friend` function:
```cpp

// friend function in the example of Fraction class declaraion
friend std::ostream& operator<< (std::ostream& out, Fraction& frac);  

// normal overloading, comparing to the above friend function overloading
std::ostream& operator<< (std::ostream& out, Fraction& frac){
    out << frac.num << "/" << frac.denom;
    return out;
}

// The script follows the same logic as function declaraion 
//Oomparing how we define other functions
int add(int a, int b){
	return a + b;
}

// The shorter version of the function declaration for `operator<<`
std::ostream& operator<< (std::ostream& out, Fraction& frac);

// Demonstration of how to use the overloaded operator

Fraction frac(3, 5);
std::cout << frac;  // Output: 3/5
```



- Example: 
```cpp
class MyClass {
private:
    int value;

public:
    // Default constructor
    MyClass() {
        value = 0;
        cout << "Default constructor called." << endl;
    }

    // Parameterized constructor
    MyClass(int val) {
        value = val;
        cout << "Parameterized constructor called." << endl;
    }

    // Copy constructor
    MyClass(const MyClass& other) {
        value = other.value;
        cout << "Copy constructor called." << endl;
    }
};

int main() {
    MyClass obj1;            // Default constructor called.
    MyClass obj2(10);        // Parameterized constructor called.
    MyClass obj3 = obj2;     // Copy constructor called.

    return 0;
}
```

- Example: fraction class outline
```cpp
class Fraction{
public:
	// things we want the class client to see
private:
	// things we want to encapsulate from the clients go here
}
```
- Step 2:
	- Adding public part
		- `add(Fraction)`: 
			- passing fraction objects which forces the methods only Fraction objects can pass
		- `add(Fraction&)`: 
			- It means the function take reference and make changes to the original object. 
		- `add(Fraction& f)`: 
			- It serves as a way to refer to the argument passed to the `add()` function within its body.
		- `friend std::ostream& operator<< (std::ostream& out, Fraction& frac); `:
			- It is similar to `void add(Fraction& f)`;, where
				- `std::ostream&` means the function take reference and make changes to the original object. And `std::ostream` is the data type that `operator<<` manipulating with.
				- `out` is a variable that will be used in the detailed declaration of function, which the data type is `std:ostream&`.
				- `frac` is a variable that is typed of class `Fraction`.
```cpp
class Fraction{
public:
	// things we want the class client to see
	void add(Fraction& f);
	void multiply(Fraction& f);
	double decimal();
	int getNum();
	int getDenom()
	friend std::ostream& operator<< (std::ostream& out, Fraction& frac);    
private:
	// things we want to encapsulate from the clients go here
	int num;   // the numerator
    int denom; // the denominator
}
```

- Step 3: adding Fraction class constructors
	- If you don't add any constructors in the Fraction class, the compiler will automatically generate a default constructor for you.
	- So the compiler would still making `Fraction` objects like we are having `Fraction();` within the class definition.
	- Why we need explicit declaration (writing the default constructor `Fraction();`)
		- 1. Clarity
			- you make it clear to other developers reading your code that the class has a default constructor. It serves as documentation and improves code readability.
		- 2. Intent
			- conveys your intent to provide a constructor with no arguments. It indicates that the class is designed to be instantiated without any specific initialization values.
		- In some cases, you may not need to explicitly declare the default constructor if the default behavior provided by the compiler-generated constructor is sufficient. However, explicitly declaring it can help improve code clarity and maintain consistency in your codebase.
```cpp
class Fraction {
public:
    Fraction(); // the "default" constructor
    Fraction(int num, int denom); // a second constructor

    void add(Fraction& f);
    void multiply(Fraction& f);
    double decimal();
    int getNum();
    int getDenom();
    friend ostream& operator<< (ostream& out, Fraction& frac);    

private:
    int num;   // the numerator
    int denom; // the denominator
};
```


- Step 4: adding private functions and variables
	- `reduce()`: 
		- It is useful to keep reduced versions of the fractions.
		- It needs a `gcd()` to do its magic
```cpp
 class Fraction {
  public:
      Fraction(); // the "default" constructor
      Fraction(int num, int denom); // a second constructor

      void add(Fraction& f);
      void multiply(Fraction& f);
      double decimal();
      int getNum();
      int getDenom();
      friend ostream& operator<< (ostream& out, Fraction& frac);    

  private:
      int num;   // the numerator
      int denom; // the denominator
      void reduce();
      int gcd(int u, int v);
  };
```

- Step 5: adding headers at the top
	- `#include<ostream> // for our operator<< overload`

---
- Example: implementing the `Fraction` class
	- Version 1 uses the default constructor to initialize the `Fraction` object.
	- Version 2 defines a custom constructor that explicitly sets the `num` and `denom` member variables to specific values. 
```cpp
#include "fraction.h"

//version 1
Fraction frac;

//version 2
Fraction::Fraction()
{
    num   = 1;
    denom = 1;
}
```

- Example: `Fraction` object multiplication
	- To make the following operation works....
```cpp
Fraction fracA(1, 2);
Fraction fracB(2, 3);

fracA.multiply(fracB); // fracA now holds 1/3
```
- We need this function
```cpp
void Fraction::multiply(Fraction& other)
{    
    num *= other.num;
    denom *= other.denom; 
    // reduce the fraction
    reduce();
}
```

- Example: fraction reduction
```cpp
// purpose: reduce the fraction to lowest terms
void Fraction::reduce() {
    // find the greatest common divisor
    int frac_gcd = gcd(num,denom);

    // reduce by dividing num and denom by the gcd
    num = num / frac_gcd;
    denom = denom / frac_gcd;
}

int Fraction::gcd(int u, int v)
{
    if (v != 0) {
        return gcd(v, u % v);
    } else {
        return u;
    }
}
```


---

### Stack
- Stack is the name to call the pool of unallocated memory available to a program.
- In most modern architecture, memory is arranged so that the heap and stack grow in opposite direction towards each others. 
	- Stack is used to store local variables and function call information, while the heap is used for dynamically allocated memory.
	- The heap is a region of memory used for dynamic memory allocation. It is where objects and data structures can be allocated at runtime using operators such as new and malloc(). Unlike the stack, which is managed automatically by the compiler, the heap requires manual memory management to allocate and deallocate memory.
	- How they interact?
		- This means that as new stack frames are created, the stack pointer is incremented, and as memory is dynamically allocated on the heap, the heap pointer is incremented. 
		- The stack typically starts at the top of the memory and grows downwards, while the heap starts at the bottom and grows upwards.
		- This arrangement ensures that the stack and heap do not collide with each other in memory. By growing in opposite directions, they can expand towards each other without overlapping or causing conflicts.
		- This separation allows for efficient memory management and prevents interference between the stack and the dynamically allocated memory on the heap.
	- Why both stack and heap grow uni-directionally?
		- Stack:
			- In follows LIFO structure, where variables are pushed and popped in a specific order.
		- Heap:
			- Heap is used for dynamic memory allocation, which involves requesting and deallocating memory at runtime.
			- Randomly placing the heap within a memory region would make it harder to track and manage allocated memory blocks, potentially leading to fragmentation and inefficiency.
- Stack vs heap
	- Stack
		- It is used for storing local variables and function call information. 
		- It is typically organized as a stack data structure, where each function call creates a new stack frame (also known as activation record) that contains information such as return addresses, parameters, and local variables.
	- Heap
		- The heap is another region of memory used for dynamic memory allocation. It is an area where objects or data structures can be allocated and deallocated in a more flexible manner than the stack. 
		- Unlike the stack, the heap does not operate in a strict order like a stack data structure. Instead, it is typically managed by a memory allocator, and memory can be allocated and deallocated in any order. 

- Figure: 
![[Pasted image 20230528215816.png|400]]



---
# Lecture 14 Dynamic memory


---
# Unit of memory


### Basic unit of memory - Bits, bytes and words
- Bit: 
	- Variations: 
		- A bit, short for "binary digit," is the smallest unit of information in computing. It represents a binary value of either `0` or `1`. 
	- Basic unit: 
		- It is the basic building block of all digital data and is used to represent the on/off state of electronic switches within a computer's circuitry. A collection of bits is used to represent more complex information.
- Nibble:
	- A nibble is a group of four bits, equivalent to half a byte.
		- Because it is composed by 4 bits, a nibble can represent $2^4$ or $16$ distinct values. $0$ to $9$, $A$ to $F$, 
		- Length = 2 nibble can represent 255 symbols. 
	- Variations 
		- A nibble can have 16 possible values, ranging from 0000 to 1111 in binary or 0 to 15 in decimal.
	- Usage:
		- See "hexadecimal notation"
- Byte: 
	- Definition: 
		- A byte is a unit of data that consists of 8 bits. 
		- Byte versus nubbles
			- While a nibble is composed by 4 bits, which can represent 16 possible symbols. 1 byte can represent 256 different symbols, can it encode by 2 hexadecimal digits. 
			- Example:
				- `0xAB`
					- `0x` is a prefix that express the following will be a byte. 
					- the first nibble (A) represents the value 10
					- the second nibble (B) represents the value 11.
	- Usage:
		- 1. Representing letters of words (by making use of `256` symbols per a byte character. )
		- 2. It is the most common addressable unit of memory in computer systems. Bytes are the 

### How `byte` unit are representing words? 
- Word: 
	- A word is a unit of data that represents the amount of data processed by the computer's CPU in a single operation. 
	- From bytes to words:
		- Consider the ASCII character encoding scheme, each character is encoded using a single byte (8 bits)
		- `H`:
			- he ASCII value for 'H' is 72. In binary, 72 is represented as 01001000. This is one byte, composed of 8 bits.
		- ASCII is a 8 bit character encoding scheme, running it on a 64 bit system does not affect the nature of it. 
	- The size of a word can vary depending on the computer architecture and the specific processor being used. Common word sizes include 16 bits, 32 bits, and 64 bits. 
		- The size of a word determines the maximum amount of data that can be processed at once and influences the performance and capabilities of a computer system.
		- Advantages:
			- 1. Increased addressable memory
				- The primary advantage of a 64-bit computer is its ability to address a larger memory space. In a 32-bit system, the memory addresses are limited to 32 bits, allowing for a maximum of 4 GB (2^32) of RAM to be directly accessed. In contrast, a 64-bit system can address up to 18.4 million TB (2^64) of RAM, which is an enormous amount of memory. 
				- This larger address space enables the computer to handle more data simultaneously.
			- 2. Increased Integer Range: 
				- In a 32-bit system, the maximum integer value that can be represented directly is 2^31 - 1, or approximately 2.1 billion. However, a 64-bit system can represent integers up to 2^63 - 1, which is significantly larger (approximately 9.2 quintillion). 
				- This expanded integer range allows for more extensive calculations and processing of larger numbers without the risk of overflow or truncation.
			- 2b. Enhanced Floating-Point Precision:
				- Floating-point numbers are used to represent non-integer values in computers. A 64-bit system offers more precision for floating-point calculations compared to a 32-bit system. 
			- 3. Support for Complex Data Structures: 
				- Larger word sizes enable computers to efficiently handle complex data structures and perform operations on them in a single instruction. 
				- For example, a 64-bit word can store a memory address, allowing computers to work with large amounts of data by directly accessing memory locations without the need for additional calculations or multiple instructions.
			- 4. Improved Performance:
				- Some software applications, such as large databases, video editing, 3D modeling, and scientific simulations, benefit greatly from the increased capabilities of a 64-bit system. These applications often involve processing and manipulating large data sets that can exceed the limitations of a 32-bit system. 

### How `byte` became the fundamental unit of data storage?
- fundamental building blocks of data storage and processing in computers. 
	- Example:
		- We use `Giga-bytes` to describe the capacity of a hard disk. 
- Q: Why bytes are used as a basic unit for data transfer and storage measurement.
	- A:
		- 1. Historical development:
			- The concept of byte originated in the early days of computing when storage capacity were limited. 
			- At the time computers were transitioning from punch cards to electronic storage. At that time, a byte was considered a convenient unit because it was aligned well with the 8-bit architecture that was emerging as a standard. 
		- 2. Binary representations
			- $2^8 = 256$, which allows for a wide range of binary values to be represented.
			- Computers work with binary digits, or bits, which are the smallest unit of data storage representing either a `0` or a `1`. 
			- This "256" is well-suited for representing various data types, including numbers, characters, and instructions. 
		- 3. Compatibility
			- It has become a standard unit of storage across computer architectures and platforms. Most computer systems are designed to work with bytes as the fundamental unit of memory, ensuring compatibility and interoperability between different systems and software. 
		- 4. Addressability
			- Memory in computer systems is typically organized into addressable units, with each unit assigned a unique address. Bytes provide a fine-grained level of addressability, allowing individual bytes within memory to be accessed and manipulated independently.
		- 5. Storage efficiency
			- Balance between efficiency and flexibility. It is small enough to minimize wasted space, and memory overhead while being large enough to represent a wide range of data values effectively. 
		- 6. Programming convenience
- Bytes are used to store a single character, such as a letter, number, or symbol. 
	- In most modern computers, the primary unit of storage is the byte. File sizes, RAM capacity, and data transfer rates are typically measured in bytes or their multiples (e.g., kilobytes, megabytes, gigabytes).
- Each byte has a unique address in memory, allowing the computer to locate and manipulate specific data. 


### Binary representations and hexadecimal representations
- Both representations are appearing in memory addressing. 
- Capability of an address:
	- The size of the address determines the total number of unique memory locations that can be accessed. For example, with a 32-bit address, a computer can address $2^{32}$ (4,294,967,296) distinct memory locations.
	- binary and hexadecimal representations do not have any inherent differences in their capability or capacity. 
		- One hexagonal representation character (16 digits) is equivalent to a group of 4 bits (a nibble)
- Binary representation:
	- Binary representation is the most basic form of expressing data in computers, but it can be difficult for humans to read and understand due to its length and complexity.
	- example of binary representation:
		- `42`: `00101010`
- Hexadecimal Representation:
	- Application:
		- 1. More compact data representation than bits 
			- Nibbles are primarily used in hexadecimal notation, which is commonly used in computing and programming. In hexadecimal notation, each digit represents four bits, allowing for a more compact representation of binary data.
			- The effect of compactness can be calculated by $r = \frac{16^n}{10^n}$
				- $r_2 = 2.56$
				- $r_6 = 16.67$
				- $r_{10} = 109.95$
		- 2. Memory addressing:
			- Computer memory is often address and organized using hexadecimal numbers. Memory addresses such as RAM or ROM, are typically represented in hexadecimal. 
			- Demonstration:
				- The number is ranging from $0$ to $9$, $A$ to $F$.
				- It is having a balance between compactness and human-interpretability. If we use "byte" as the address representation, we need 256 characters to represent 1 space, which is not human friendly. 
		- 3. Color representation:
			- Length = 6 nibbles can represent $16,777,216$ distinct colors. 
			- Colors could be represented in hexadecimal notation.  
			- the color code `#FF0000` represents pure red, while `#00FF00` represents pure green.
			- $16^6 = 16777216$ variation of colors.  
		- 4. ASCII and Unicode character encoding
			- Length = 2 nibble can represent 255 symbols. 
			- ASCII and Unicode are character encoding standards that map characters to numerical values. 
			- In these encoding schemes, characters are assigned hexadecimal values, which allows for efficient representation and processing of text data.  
			- eg:
				- English word: `Hello` = `72 101 101 108 111` = `48 65 6C 6C 6F`
				- Chinese word: `中` = `U+4E2D`
					- Unicode can be marked with prefix `"U+"`

- other data types:
	- `char`: 1 byte
	- `bool`: 1 byte
	- `short`: 2 bytes
	- `int`: 4 bytes
	- `float`: 4 bytes
	- `long`: 8 bytes
	- `long double`: 16 bytes

---

# Effective memory allocation 


### Value of effective memory utilization
- Improvement methods:
	- 1. Dynamic memory allocation
		- By minimizes fragmentation and maximizes the use of available memory blocks
	- 2. Data structures and algorithms
		-  Such as using compact data representations, minimizing redundant data storage, and employing efficient algorithms for data access and manipulation.
	- 3. Caching
		-  Reduce the need to access slower memory or storage devices, leading to faster data retrieval.
	- 4. Virtual memory management 
		- a technique that allows the computer to use disk storage as an extension of physical memory. This involves techniques like demand paging, page replacement algorithms, and memory swapping to ensure that the most frequently accessed data is kept in physical memory.
- Benefits:
	- 1. Improved performance: 
		- "Improved memory space utilization" refers to the efficient and effective use of available memory resources in a computer system.
		- Performance improved by the following: 
			- Improved memory space utilization $\rightarrow$ (fragmentation $\downarrow$ and max. memory blocks $\uparrow$) $\rightarrow$ faster data retrieval
				- Because it reduce disk access.
			- Efficient memory space utilization = Using the resources effectively, reducing memory wastage and enabling your program to run faster and more efficiently
	- 2. Reduced memory footprint: 
		- Memory footprint = the amount of memory or storage space that a program or process occupies in a computer's memory. It represents the total amount of memory resources, typically measured in bytes, that are allocated and used by a particular application, software component, or system.
		- This is particularly beneficial in memory-constrained environments or when dealing with large datasets. 
			- By allocating memory dynamically, leading to efficient memory utilization, you can conserve memory resources and ensure that your program operates within the available memory limits, avoiding out-of-memory errors and improving overall system stability.
	- 3. Scalability: 
		- (ability to handle larger datasets and workloads $\uparrow$) $\rightarrow$ 
		- (chance running into memory limitation $\downarrow$) $\rightarrow$ 
		- Allows the code to adapt to growing demands, and handles larger inputs and process more significant amounts of data without sacrificing performance. 
	- 4. Reduced memory fragmentation: 
		- Memory fragmentation occurs when memory is allocated and deallocated over time, resulting in small blocks of free memory scattered throughout the allocated memory space. 
		- (Memory fragmentation $\uparrow$) $\rightarrow$ (inefficient memory usage $\uparrow$) $\rightarrow$ challenging to find contiguous blocks of free memory for new allocations. 
		- By allocating memory dynamically and deallocating it when no longer needed, you can reduce memory fragmentation and ensure that memory is used more cohesively.
	- 5. Optimal resource allocation: 
		- Efficient memory utilization goes hand in hand with optimal resource allocation. When you allocate memory based on runtime conditions, you can allocate resources in a way that aligns with the specific needs of your program at any given time. This helps in achieving an optimal balance between memory usage and other system resources, such as CPU utilization. By efficiently managing memory, you can avoid resource bottlenecks and ensure that your program runs smoothly and efficiently.

### Memory defragmentation
- Methods:
	- 1. Compaction
		- Compaction involves moving all allocated memory blocks together and freeing up the gaps between them.
		- But it can be an expensive operation. 
	- 2. Garbage collection
		- It is a technique used in managed programming language where system automatically reclaims memory occupied by objects that are no longer in use. 
	- 3. Memory pools
		- Memory pools are pre-allocated blocks of memory of fixed sizes. Instead of allocating and deallocating memory individually, objects or data structures are allocated from these fixed-size blocks. 
	- 4. Buddy memory allocation
		- Buddy memory allocation is a technique that divides memory into fixed-size blocks and keeps them in a binary tree structure. When a memory request is made, the system searches for a block that is the closest size match, splitting larger blocks if necessary.

---
### Contiguous memory location

- Contiguous
	- It refers to "touching or connected throughout in an unbroken sequence".
	- It means that the memory addresses assigned to those elements from a continuous block of memory, with each element occupying a fixed amount of memory space. 
	- This allows for efficient traversal and random access to elements using simple arithmetic calculations based on their indices.
- Advantages
	- Efficient access
		- Since elements are stored in consecutive memory addresses, accessing an element by its index becomes straightforward. 
	- Cache efficiency
		- Modern computer architecture uses caching architecture to improve memory access speed.
		- Contiguous memory locations can take advantages of spatial locality, where accessing one element often results in loading nearby element into the cache, reducing the latency for subsequent accesses. 
	- Array operations
		- Contiguous memory layouts are particularly beneficial for array operations, such as iteration, sorting, or searching algorithms. 
		- Sequentially accessing array elements is more cache-friendly and can lead to better performance compared to scattered or fragmented memory layouts.
	- Memory management
		- Allocating and deallocating contiguous blocks of memory is generally more efficient. 
		- It simplifies memory management tasks by allowing memory to be allocated as a single, continuous block, reducing fragmentation and facilitating deallocation of the entire block when it is no longer needed.


### Static memory allocation
- Definition:
	- 1. the reservation of memory for variables during the program's compilation phase
	- 2. the memory remains fixed throughout the program's execution.
- Common examples of static memory allocation in C++:
	- 1. Global variables: 
		- Variables declared outside of any function or class scope are considered global variables. They are allocated statically and have a lifetime that extends throughout the entire program execution.
	- 2. Static variables: 
		- Variables declared with the static keyword inside a function or class have static storage duration. They are allocated statically and retain their values between different function calls. Each instance of a static variable is shared among all instances of the function or class.
	- 3. Static arrays: 
		- Arrays declared with a fixed size at compile-time, either globally or inside a function or class, are statically allocated. The memory for the array is reserved when the program starts, and it remains fixed throughout the program's execution.
- Advantages:
	- 1. Variable memory requirements: 
		- Dynamic memory allocation allows you to allocate memory based on runtime conditions and variables. This means you can adjust the amount of memory allocated according to the specific needs of your program at any given time. For example, if your program processes a varying number of elements or data, dynamic memory allocation enables you to allocate memory accordingly.
	- 2. Efficient memory utilization: 
		- With dynamic memory allocation, you can allocate memory only when it is required and deallocate it when it is no longer needed. This efficient utilization of memory helps optimize your program's performance and reduces memory wastage. It allows you to avoid reserving a fixed amount of memory for the entire program execution, which may not always be necessary.
	- 3. Data structures of variable sizes: 
		- Dynamic memory allocation is particularly useful when dealing with data structures that have variable sizes. For example, if you need to create a dynamic list or tree structure, dynamic memory allocation allows you to allocate memory for new elements as they are added or remove memory when elements are deleted. This flexibility is crucial when working with data structures that grow or shrink dynamically.
	- 4. Runtime input handling: 
		- Dynamic memory allocation enables you to handle input from the user or external sources that may vary in size or content. For example, if you are reading data from a file or receiving input from a network, dynamic memory allocation allows you to allocate memory to store the input data appropriately. This ability to adapt to varying input sizes enhances the versatility and robustness of your program.
	- 5. Resource management: 
		- Dynamic memory allocation gives you more control over managing system resources. It allows you to allocate and deallocate memory as needed, reducing the risk of running out of memory or encountering memory overflow errors. This level of control is particularly critical in resource-constrained environments or when working on memory-intensive tasks.
- Disadvantages:
	- Fixed memory size and the inability to allocate memory dynamically based on runtime conditions. 
- Usage:
	- It is suitable when the memory requirements are known in advance and do not change during program execution.

- Keywords related to dynamic memory allocation:
	- `new`:
		-  used to allocate memory for a single object or an array dynamically.
		- It dynamically allocates memory from the heap and returns the address of the allocated memory. 
	- `delete`:
		- It is used to deallocate memory that was previously allocated using the new operator.

- example of `new` and `delete`
```cpp
//
type* pointer_name = new type;
type* pointer_name = new type[size];

delete pointer_name;
delete[] pointer_name;
```

- Figure: 
	- How it looks like of having a heap locating its elements memory, by pointing to a address. 
	- The left hand side is the address of a storage location in the heap. `new type` does allocate memory on the heap, but it does not correspond to "buckets" capturing elements. The memory allocated is contiguous and can be considered a block of memory rather than individual buckets. 
	- The right hand side is the current stack frame of "stack" / "call stack" / "stack trace". Each stack frame will be assigned a pointer that points to the address of that memory card. 
![[Pasted image 20230528222650.png|400]]

---

### Dynamic memory allocation
- Definition:
	- Dynamic memory allocation in C++ refers to the process of allocating and managing memory during program execution dynamically. 
- The importance comes from the fact that the dynamic allocation makes it possible for data structures to expand as needed while a program is running.
- Unlike static memory allocation, where memory is allocated at compile-time and remains fixed throughout the program's execution, dynamic memory allocation allows for flexible memory management at runtime.
- Property:
	- a way to reserve a section of memory so that it remains available to us throughout our entire program, or until we want to destroy it (give it back to the operating system)
- Advantages:
	- Able to allocate memory dynamically based on runtime conditions. 
- Use cases:
	- Making it useful for scenarios where the memory requirements are not known at compile-time or may change during program execution.
- Extra responsibility for programmer:
	- It also places the responsibility on the programmer to manage memory properly, ensuring that allocated memory is deallocated when no longer needed to avoid memory leaks and excessive memory usage.


### Memory leak
- A memory leak occurs when memory that is dynamically allocated during program execution is not released or freed when it is no longer needed. This can lead to a continuous consumption of memory without the ability to reclaim it, potentially causing your program to consume excessive memory resources over time.
- the memory used by the array will not be released back to the system. This memory leak will persist until the program terminates, leading to inefficient memory usage.
- Memory leaks can have various negative consequences, such as reduced performance, increased memory usage, and, in extreme cases, even causing the program to crash due to running out of memory.

### Natural termination:
- In C++, the memory allocated by a program is automatically deallocated when the program terminates. So, if your script completes running its last line and there is nothing else to be executed, the operating system will reclaim the memory allocated by the program, including any dynamically allocated memory.
- However, it's important to note that relying on the program termination to deallocate memory is not a good practice, especially in larger programs or long-running applications.
- By explicitly freeing memory with delete[] when you're done using a dynamic array, you ensure that memory is released promptly and prevent memory leaks during the program's execution. 




### Freeing memory
- Although they are getting higher all the time, computer memory systems are finite in size.
- The heap will eventually run out of space. At that time, `new` operator will be unable to allocate a block of the requested size. 
- What happens if we don't free memory
	- it can result in a memory leak.


---

### Structure of memory, class of memory containers
- Levels of memory
	- Registers
		- Registers are the fastest and smallest type of memory located within the CPU itself. They store the most frequently used data and instructions directly accessible by the CPU. 
		- Speed:
			- nanoseconds
		- What to memorize?
			- The most frequently accessed instructions, l
	- Cache memory
		- Cache memory is a small, high-speed memory located closer to the CPU than the main memory. It acts as a buffer between the CPU and main memory, storing frequently accessed data and instructions. 
		- The cache is divided into multiple levels, such as L1, L2, and sometimes L3, with each level being larger but slower than the previous one.
	- Main memory Random-access memory (RAM)
		- Random access memory allows the program to use the contents of any memory cell at any time. 
		- Computer memory is used to store data and instructions that are currently being processed by the computer's central processing unit (CPU). 
		- It is the primary storage area for data and instructions during active computer operations. 
		- Main memory is volatile, meaning its contents are lost when the computer is powered off.
		- Speed:
			- nanoseconds or microseconds
	- Secondary storage
		- Secondary storage is non-volatile memory used for long-term storage of data even when the computer is powered off. 
		- It includes devices like hard disk drives (HDDs), solid-state drives (SSDs), and optical drives. 
	- Tertiary storage
		- Tertiary storage refers to removable storage media like tapes and offline storage systems. It provides long-term archival storage and is typically accessed less frequently than secondary storage. 


### Difference in data retrieval from memory
- It depends on the physical proximity to the CPU and the underlying technology used to implement them.
	- Reasons:
		- 1. Limitations of electrical signals 
			- Limitations of electrical signals and the physical properties of the components involved in data transfer.
		- 2. The complexity and design of the memory interface
			- Register access is tightly integrated into the CPU's execution pipeline, allowing for direct and immediate access to the data. In contrast, accessing data from external memory involves more complex procedures, such as sending memory addresses, initiating read or write commands, and waiting for the data to be retrieved or stored. 
- The ordering of physical proximity (depends on the level):
	- Registers > Cache > Main / RAM > secondary storage (HDDs, SSDs) > Tertiary storage (removable stuffs )
		- Registers
			- Since registers are physically integrated into the CPU chip, the distance the electrical signals need to travel is extremely short, resulting in near-instantaneous access times.
		- RAM / secondary storage
			-  external memory modules like RAM are physically separate from the CPU. The memory bus connects the CPU to the RAM modules, and the data signals need to travel along this bus to reach the desired memory location. 



---
### `new` keyword
- In C++, the `new` keyword is used for dynamic memory allocation. It is used to allocate memory for a single object or an array of objects, on the heap, which is a region of memory separate from the stack where local variables are stored. 

### Dynamic arrays
- Unlike static arrays, which have a fixed size determined at compile time, dynamic arrays offer flexibility in managing memory and storing data.
- Dynamic arrays are implemented using pointers. To create a dynamic array, you use the new keyword to allocate memory on the heap, and the array elements are stored consecutively in that memory space. 

- example:
	- Initialize `array` so that it points to a contiguous block of memory large enough to hold three `double` 
```cpp
// prototype
dataType* arrayName = new dataType[size];

// example
double *array = new double[3]

// to deallocate memory in runtime:
delete[] dynamicArray;
```
	- `double *array = new double[3]`


### Destructor
- a destructor is a special member function of a class that is used to clean up resources and perform necessary tasks when an object of that class is destroyed or goes out of scope. 
- Key points:
	- 1. Destructors do not take any arguments and do not return any value, not even void.
	- 2. A class can have only one destructor, and it cannot be overloaded with different parameter lists.
	- 3. Destructors can be explicitly called for an object using the object name followed by the destructor operator (~), but this is rarely needed and should be avoided in most cases.

- Example:
	- Demonstrates the usage of a destructor
```cpp
#include <iostream>

class MyClass {
public:
    MyClass() {
        std::cout << "Constructor called" << std::endl;
    }

    ~MyClass() {
        std::cout << "Destructor called" << std::endl;
    }
};

int main() {
    MyClass obj;  // Create an object of MyClass

    // Rest of the code...

    return 0;  // Object obj goes out of scope and its destructor is automatically called
}
```

---



### Hierarchal structure of memory
- $10^9$ bytes = 1GB
- In modern computers, memory is typically organized in a hierarchical structure, consisting of different levels such as 
	- registers, 
	- cache, 
	- main memory (RAM), and 
	- secondary storage (hard disk drives, solid-state drives). 
- Each level has its own "addressing scheme" and "characteristics", but the basic principles of memory addressing remain the same. 
- Memory addressing involves two key components: 
	- an address
		- The address represents a unique identifier or location within the memory system, and the data value is the information stored at that particular address.
		- Representations:
			- The memory addresses are typically represented as numerical values, often in binary format. 
		- Capability of an address
			- The size of the address determines the total number of unique memory locations that can be accessed. For example, with a 32-bit address, a computer can address 2^32 (4,294,967,296) distinct memory locations.
	- a data value 
		-  the data value is the information stored at that particular address.

### Memory addresses
- In computing, memory addressing refers to the process of identifying and accessing specific locations in a computer's memory system.
	- It enables the retrieval and storage of data within a computer's memory.
- Within the memory system of a typical computer, every byte is identified by a numeric address. 
	- eg: The memory address in a tiny 64KB computer would begin with a byte numbered `0`, and end with a type numbered `65535`.
	- Given that addresses are closely tied to the internal structure of the hardware, it is more more common to think about address as beginning at address `0000` and ending with `FFFF`.

### Memory addressing process
- Different addressing modes and techniques exist to optimize memory access based on factors like data size, caching, and efficiency. 
- Types:
	- Direct addressing
	- Indirect addressing
	- Indexed addressing
	- Relative addressing
- General steps:
	- Step 1 - Address calculation
		- Based on the type of memory access (read or write) and the specific operation being performed.
		- It may involves calculations based on offsets, indexes or pointers. 
		- Example of address calculation
			- Declaration and initialization
				- `int array[] = {10,20,30,40,50};`
			- Address calculation:
				- Index = `2`
				- Element size = `4` bytes
				- Start address = `1000`
				- Then, address for index=2 element =` Start address + (Index x element size)`
			- Accessing the memory:
				- Once we have calculated the address, we can access the memory location to read the data. When we accessing `index=2` element of that array, we would access the memory location at address `1008` to retrieve the value `30`. 
	- Step 2 - Address translation
		- The memory address generated by the CPU needed to be addressed into the physical address of the memory location. 
		- This translation is typically handled by computers memory management unit (MMU), which maps virtual addresses to physical addresses. 
		- Example of "address translation"
			- Suppose we have a computer with a virtual memory system using a 16-bit address space.
			- Virtual address space range from 0 to 65535 ($2^{16}-1$)
			- Physical address space consists of main memory address from 0 to 32767 ($2^{15}-1$)
			- The memory management unit (MMU) handles the address translation between the victual and physical addresses. 
			- When translating, the MMU translates the virtual address $x$ to the physical address $y$. 
			- The CPU uses the physical address $y$ to access the actual memory location in the main memory. 
	- Step 3 - Accessing the memory
		- Once the physical address is determined, the computer can access the memory location to read or write the data.
- Example of address calculation


### Byte addressing and word addressing
- Byte addressing 
	- It is a memory addressing scheme where each byte of memory has a unique address.
- Word addressing
	- It is a memory addressing scheme where memory is organized and accessed based on the size of a "word."
	- A word typically represents the unit of data that a computer's processor can handle in a single operation. The size of a word varies depending on the computer architecture but is often 2, 4, or 8 bytes.
	- In word addressing, the basic unit of memory addressing is still 1 byte. However, the memory addresses are typically aligned to the word boundary.
	- Example:
		- Word 0 - address 0
		- Word 1 - address 4
		- Word 2 - address 8
	- Advantage:
		- Word addressing provides a way to access larger chunks of data at once, which can be beneficial for certain operations. It is particularly useful for processors that have specific instructions designed to work with words or for optimizing memory access when dealing with larger data structures.

- Figure:
	- This figure sketch how memory is organized in a typical C++ program.
	- The instruction in the program, which are represented internally as bit patterns stored in memory words, and global variables tend to be stored in low-numbered address near the beginning of the address 
	- The highest addresses in memory are used for stack frames. 
		- Each time your program calls a function or a method, the computer creates a new stack frame in this memory region.
		- When that function returns, the stack frame is discarded leaving the memory free to be used for stack frames of subsequent calls. 
![[Pasted image 20230529153956.png]]


---

# Lecture 15  pointers

### Assigning memory to variable
- Analogy of computer's memory when computer accessing it
	- Memory can be thought of simply as a long row of boxes, with each box having a value in it, and an index associated with it. 
	- The boxes can hold different types, but the numbers associated with each box is just a number, one after the other. 
- Steps that computer register address for elements:
	- 1. Declaration of variable
	- 2. Assignment of values to the variable
		- `const double PI = 3.14159`
	- 3. The memory allocated to a variable depends on its data type. 
		- If it is a double, then it will reserves eight bytes of memory somewhere in the low-address region of memory. 
	- 4. Computer determine the starting address to the variable
	- 5. Computer put elements into the chain of memory unit byte by byte, from the starting address, and put the remaining elements sequentially. 
	- 6. Image `PI` is stored in the virtual address `200`. 


![[Pasted image 20230605114506.png|500]]
![[Pasted image 20230605114528.png|500]]

### Methods to store variables
- Pointers
	- Pointers are variables that store the memory address of another variable. They provide a way to indirectly access and manipulate data stored in memory. 
	- Pointers allow for dynamic memory allocation and facilitate efficient data structures and algorithms. 
	- By using pointers, you can create complex data structures like linked lists, trees, and graphs.
- Stacks
	- The stack is a region of memory used for local variables and function call information. Variables stored on the stack are automatically allocated and deallocated as functions are called and return.
- Heap
	- The heap is a region of memory used for dynamic memory allocation. Variables stored on the heap are allocated manually and can persist beyond the scope of a function.
- Registers
	- Registers are small, high-speed storage areas within the CPU. They are used to store frequently accessed data or intermediate results. However, the number of available registers is limited.
- Global variables
	- Global variables are declared outside of any function and can be accessed by all functions within a program. They are stored in a global data segment and persist throughout the execution of the program.
- Constants
	- Constants are fixed values that are hardcoded directly into the program. 
	- They are typically stored in the program's code segment and cannot be modified during runtime.
- Caches
	- Caches are small, high-speed memory units located closer to the CPU than main memory. They are used to temporarily store frequently accessed data to improve the overall performance of the system.
- File storages
	- Variables can also be stored in files on disk or other external storage devices. This allows data to be saved and accessed across different program executions.

---
### How computer memory involved during the process of powering up the computer

- Power on
	- 1. Setting up the memory controller 
	- 2. Configuring memory timings 
	- 3. Performing a memory self-test to ensure memory modules are functional.
- Firmware execution
	- After memory is initialized, the firmware executes its initialization code from a specific address in memory. This code typically resides in 

---

### Not all variables need to be stored with a pointer.


### Pointers
- Pointers are just a memory address
	- We do not care the actual memory address numbers themselves. Most often when we draw the pointer visually to show that a variable points to another variable, we do not write the address number of the target block.
- What is the benefit of it?
	- 1. Pointers allow you to use indirect access and manipulate data by referring to their memory addresses. 
		- This is useful for scenarios such as 
			- dynamic memory allocation
			- passing large data structures efficiently between functions
			- implementing data structures like linked lists or tree
			- or the case when we need to modify the value of a variable indirectly
- How we describe pointers:
	- We generally use an arrow to "point" from a pointer, to the address it points to.
	- `petPointer` $\rightarrow$ `pet`

- Points to learn:
	- 1. Every location in memory, and therefore every variable, has an address.
	- 2. Every address corresponds to a unique location in memory.
	- 3. The computer knows the address of every variable in your program.
	- 4. Given a memory address, the computer can find out what value is stored at that location.
	- 5. While addresses are just numbers, C++ treats them as a separate type. This allows the compiler to catch cases where you accidentally assign a pointer to a numeric variable and vice versa (which is almost always an error).
- We need to specify the data type for the pointer for several reasons:
	- Variables:
		- Specify data type to the variable determine what kind of values it can hold.
	- Pointer:
		- Pointer does not store the actual value directly, but rather the address of the value, it requires information about the data type of the variable it points to. 


- Example
	- `(type_of_data)*` operator: 
		- It puts after the data type, denote that the following variable will be a pointer.
	- `&(variable)` operator:
		- Putting `&` before a variable, would assign the address of the variable, instead of the value of the variable to the left hand side. 
```cpp
// To declare a pointer of a particular type, use asterisk symbol
string* petPtr;  // declare a pointer (which will hold a memory address) to a string
int* agePtr;     // declare a pointer to an int
char* letterPtr; // declare a pointer to a char

//To get the address of another variable, use "&" (ampersand) symbol
string pet = "cat"; // a string variable, pretend it is at memory location 10
petPtr = &pet; // petPtr now holds the address of pet

// To get value of the variable a pointer points to, use `*` character
cout << *petPtr << endl; // prints out "cat"
```

- Example: print out the variable address
	- `0x`: This prefix denote the following number is written in hexadecimal (base-16) notation. 
```cpp
#include <stdio.h>

int main() {
    int age = 25;
    int* agePtr = &age;

    printf("Address of age variable: %p\n", &age); // Address of age variable: 0x7fff12345678
    printf("Value stored in agePtr: %p\n", agePtr); // Value stored in agePtr: 0x7fff12345678

    return 0;
}
```

- Q: 
	- Variable value are stored in some addresses that a pointer is holding. But how the computer holds these addresses? 
- A: 
	- Memory address are stored in registers or in memory itself.
	- The CPU uses registers to hold frequently accessed memory addresses for faster execution. 
		- When a pointer is created and assigned an address, the address is typically stored in a register. This allows the CPU to directly access the memory location without having to access RAM every time.
		- However, if the number of memory addresses exceeds the capacity of available registers, the remaining addresses will be stored in RAM. 
	- The specific mechanisms and organization of memory vary across different computer architectures and operating systems. 


### Linked list
- linked list is a data structure used to store and manage a collection of elements called nodes.
- Properties:
	- 1.Unlike arrays or lists, where elements are stored sequentially in memory, a linked list consists of nodes that are linked together through pointers.
		- Each node consists of:
			- 1. The value of that node
			- 2. The memory address of the next node
- How to insert / delete elements 
	- 1. Create a new node
	- 2a. If the Linked list is empty, find the position you want to insert the new node.
	- 2b. If the linked list is not empty, find the position where you want to insert the new node.
	- 3. Adjust the pointers to insert new node.
		- Set `next` pointer of the new node to the point to the node currently at the desired position,
		- Set `next` pointer of the node before the desired position to the point to the new node.
	- 4.If you want to insert new node at the beginning of the linked list, update the head node, to point to the new node. 
- How to traverse elements 
	- Unlike arrays, linked list do not provide direct access to elements using indices. 
	- 1. Start at the head of the linked list
	- 2. While the current node is not null, read, modify or printing the data of the node, move to the next node in the list following the address provided in the current node.
	- 3. Repeat step 2, until certain condition is met or reaching the end of the list. 

- Advantages:
	- 1. Dynamic allocation of memory
		- Unlike arrays, where the size is fixed, linked lists can grow or shrink as needed. 
		- This properties allow efficient insertion and deletion operations at any position within the list. 
	- 2. Effective insertion 
		- When we use array and we want to put a new element in between the array, we need to move all elements by 1 time. That operation can be costly for large dataset. 
- Disadvantage:
	- 1. Random access is not possible in a linked list
	- 2. Accessing an element requires iterating through the list sequentially
	- 3. Generally require more memory than arrays to store the same list of elements.
		- Unlike array, we only need the starting address to access the whole array. Each node of the linked list 

- sometimes you can use different kind of data structure, which has different internal storage, and they have different pros and cons.


- example 
```c++
LinkedList<int> list;
for (int i=1; i<=8; i++){
	list.add(10*i); // {10,20,230,40,50,60,70,80}
}
```



---
# Lecture 16 Implementing `stackint`

### Hermit crab analogy
- 1. Grow a bit until the shell is outgrown
- 2. Find another shell
	- The program requests additional memory from the operating system. 
- 3. Move all their stuffs into the other shell
	- The program transfer its existing data to the newly allocated memory space
- 4. Leave old shell on the sea floor. 
	- The previous memory space becomes unused and deallocated or freed. 
- 5. Update their address with the Hermit Post office
	- The program informs the necessary data structures (such as pointers, or references) about the new memory addresses. 
- 6. Update the capacity of their new shell on their web page
	- The program updates any relevant metadata, or records to reflect the new size of capacity of the allocated memory. 


### Dynamic array expansion

- Steps:
	- 1. Check capacity
	- 2. Expand capacity
	- 3. Copy elements
	- 4. Update references
	- 5. Add new element

---
# Lecture 17 Guest lecture 

---
# Lecture 18 Heaps

### Heap property
- Properties
	- 1. For a max heap, the value of each node is greater than or equal to the values of its children.
	- 2. For a min heap, the value of each node is less than or equal to the values of its children.
		- Typically stored in an array, where the parent-child relationship of the tree is determined by the indices of the elements in the array. 
			- Root of the heap: 
				- Index 0
			- Any elements:
				  Index i
			  Its left child
				  index 2i + 1
			  its right child
				  index 2i + 2
- Perfect binary tree
	- In the tree, all the levels are completely filled.
	- If some levels of the tree is not filled (or, to branches extending outward), then the structure is not following heap structure
- Almost complete binary tree
	- Leaves should be present only at the last and 2nd last levl
	- Leaves at the same level should be filled from left to right

### Heap
- It is a specialized tree-based data structure that satisfies the heap property.
- often implemented as a binary tree and is commonly known as binary heap.
- Implementations:
	- Binary heaps
	  - Binary max heap 
		  - 
- Advantages:
	- Efficiently maintaining and retrieving the maximum or minimum element from a collection of elements. 

- Figure: Tree and array representation of a binary heap
![[Pasted image 20230608133059.png]]

### Heap operations
- peek()
- enqueue()
- dequeue()

### Priority queue
- where elements with higher priority can be accessed and removed first. 
- real-life applications
	- professor office hours
	- the sequence of getting on an airplane


---
# Lecture 19 Sorting 

### Insertion sort

### Selection sort

### Merge sort

### Quicksort



---
# Lecture 20,21 Linked list

---
# Lecture 22 Trees

### Trees
- What is it?
	- A tree is a hierarchical data structure consisting of nodes connected by edges. It has a root node that serves as the starting point, and each node can have zero or more child nodes. 
	- Nodes with no children are called leaf nodes. The relationship between nodes in a tree is often referred to as a parent-child relationship.
- Relationship with linked list
	- A linked list can be considered as a special case of a tree where the maximum connectivity of each node is 1
- properties
	- 1. inherently recursive
		- A tree a collection of nodes, which can be empty.
		- recursion is a programming technique in which a function calls itself, either directly or indirectly, to solve a problem by reducing it to a smaller instance of the same problem. 
		- Manifestation of recursive:
			- 1. Breaking down tasks
			- 2. Traversing or processing a tree into smaller, manageable steps
			- 3. The structure of a tree can be defined recursively
	- 2. One parent, no cycle
	- 3. Left child has lower value than right child
	- 4. The parent node are not necessary describe the property of their child nodes. 
- Characteristics
	- Path
		- The sequence from a parent to its children
	- Length of path
	- Depth
		- The length from the root
	- Height
		- The longest path from the node to a leaf
- Traversing a tree
	- Depth-first search (discuss later)

- Some tree structure in life, the parent node describes the properties of the child node. 
	- However! It is not commonly used in standard tree data structure. 
![[Screenshot 2023-06-11 190722 - Copy.png|300]]

- Further classification regarding to the presence of parent node descriptions:
	- 1. Pure hierarchical structures
		- the nodes represent elements in a hierarchical relationship, but the parent nodes do not necessarily describe the properties of their child nodes. 
	- 2. Attribute-based structures
		- Some tree structures incorporate attributes or metadata in the nodes that provide additional information about the elements or relationships. These attributes can be used to describe properties of the child nodes indirectly.
		- These structures can be seen as having a form of parent node descriptions, as the attributes provide context or details about the child nodes.
		- Examples:
			- XML
			- JSON
	- 3. Metadata-driven structures
		- the parent nodes may explicitly describe the properties or characteristics of their child nodes through dedicated metadata fields. These structures are designed specifically to capture relationships between nodes and their properties.
		- Nodes represent concepts or entities
		- Edges represent relationships between nodes 
		- The parent nodes in these structures often describe the properties of the child nodes through defined metadata fields or properties.
		- examples:
			- ontology
			- knowledge graph

---
- Q: How computer can make use of attribute-based tree to facilitate the searching
- A:
	- 1. Filtering and selection: attributes associated with nodes in an attribute-based tree can be used to filter and select nodes based on specific criteria.
	- 2. Indexing and efficiency: Attribute-based trees can be indexed to optimize search efficiency. By indexing attributes, the computer can create data structures like hash tables or search trees that allow for faster retrieval of nodes based on their attribute values. This indexing can significantly speed up search operations, especially when dealing with large amounts of data.
	- 3. Semantic Search: Attribute-based trees can support semantic search, where the meaning or context of the search query is taken into account. By leveraging attributes that describe properties or relationships, computers can perform more intelligent searches. 
	- 4. Faceted search:  In some attribute-based tree structures, nodes can have multiple attributes that describe different facets or aspects of the data. Faceted search allows users to navigate the tree structure by selecting specific attribute values across different facets. 

---

- My interpretation:
	- Metadata linking to objects, would helping algebra/reasoning between entities


---
- The following part discusses how to prepare an optimized tree data structure for an agent to search
	- Balance binary search tree
		- These trees ensure the heights of the left and right subtrees by at most one, resulting in efficient searching operations. 
	- Trie (prefix tree):
		- A specialized tree data structure that is commonly used for efficient searching of strings or sequences. It is useful for autocomplete or dictionary-based searching. 
	- Heaps
		- Specialized trees that satisfy the heap property, which allows for efficient extraction of the min or max element. 
		- Commonly used in priority queues or heap-based sorting algorithms. 
	- K-D trees:
		- K-D trees are used for multidimensional searching, especially in computational geometry or nearest neighbors searches. 
		- They partition the space based on the values of different dimensions, enabling efficient searches in high-dimensional spaces. 

---
- The following part discusses different way of map/graph traversal: 

### Random walk
- properties:
	- Completeness
		- A random walk may never stumble upon the correct path, leading to an incomplete or unsuccessful solution
	- Not systematic
		- This approach does not ensure no path is left unexplored
	- No memory
		- While DFS / BFS uses a stack to keep track of visited nodes, random walks does not maintain any memory of the path taken.
	- Non Optimality
		- DFS can find a path but does not guarantee finding the shortest path. However, if the maze exists solution, DFS will find it. Random walks often wander aimlessly without approaching the goal.
	- Non-deterministic behavior
		- DFS follows a predefined set of rules, this predictability makes it easier to debug. 

### Depth-first traversal
- We explore the deepest nodes of the tree, before moving on to shallower levels. 
- A. Pre-order
	- Do something, go left, go right
	- root-left-right.
- B. In-order
	- Go left, do something, go right
	- left-root-right.
- C. Post-order
	- Go left, go right, do something
	-  left-right-root.

### D. Level-order/ Breadth-first traversal
- We visit all the nodes at the same level before moving on to the next level. This traversal uses a queue data structure to keep track of the nodes to visit. The order of operations is from left to right at each level.
- Steps:
	- Enqueue the root node into a queue
	- While the queue is not empty
		- Dequeue a node
		- Do something with the node
		- Enqueue the left child if exists
		- Enqueue the right child if exists

- Other traversal frameworks:
	- 1. Dijkstra's algorithm
		- It explores nodes in other of their distance from the start node. 
	- 2. Best-first search
		- It uses a heuristic function to evaluate nodes and selects the most promising node based on the heuristic value. 
	- 3. Depth-limited search, and Iterative Deepening Depth-First Search (IDDFS):
		- DLS is similar to DFS but limits the depth of exploration. It stops the search when a specified depth is reached, preventing infinite search in graphs with cycles.
		- It performs a series of depth-limited searches with increasing depth limits until the goal is found.
		- IDDFS combines the advantages of both BFS and DFS. 

---
# Lecture 23 Binary search trees

### Binary search tree
- Property
	- In a binary search tree, the values stored in the nodes are organized in a specific way. For any given node in the tree, all the values in its left subtree are less than the value in the node, and all the values in its right subtree are greater than the value in the node. This property is known as the binary search property.
- Advantages:
	- enables us to perform efficient search operations. 
		- When searching for a specific value in a binary search tree, we start at the root node and compare the target value with the value in the current node. Based on the comparison, we can determine whether the target value is in the left subtree or the right subtree. 
		- By recursively applying this process, we can quickly narrow down the search to the desired node or determine that the value does not exist in the tree.
- Depth versus breadth analysis of choosing $2$ as the base of tree
	- Say we have $N$ nodes. 
	- If we construct a tree with "$1$ parent - $2$ child" structure, then total levels would be $\frac{N}{2^k} \leq 1 \implies log_2 N \leq k$
	- The average 

---
# Lecture 24 Huffman coding


---
# Lecture 26 Graphs

### Graphs
- Graphs capture complex relationships and enable analysis and traversal across diverse connections.
- Types:
	- Weighted/unweighted graphs 
	- Directed/undirected graphs
- Properties:
	- Connectivity
		- While tree has a rule where "each node has exactly one parent, and - or more child nodes. and there are no cycles or loops in a tree structure"
		- Graphs can have multiple edges and cycles. Nodes can be connected to any other node, allowing for more complex and arbitrary relationships between elements. 
	- Directionality
		- Tree usually considered as directed acyclic graphs.
		- Graphs can be either directed or undirected
	- Root and leaves:
		- Root serves as the starting point for traversing the structure
		- Graphs does not have a concept of root node or a leaf node, since they are not required to have a specific starting or ending point.
	- Connectivity constraints
		- Trees have specific connectivity constraints, ensuring hierarchal structures. Each node, except the root has one parent, and there are no cycles. These constraints facilitates efficient searching, insertion and deletion. 
- More features
	- Node
	- Vertex
	- Edge
	- Path
	- Path length
	- Neighbor / adjacent
	- Loops / cycles 
	- Reachability / connectedness
- Applications
	- Tree:
		- Used in hierarchies structures, such as file systems, decision trees or binary search trees. They excel at organizing data in hierarchal manner. 
	- Graphs:
		- They are more versatile and find applications in a wide range of scenarios, like social networks, transportation networks, recommendation system, dependency management. 

