- 29-9-2022: created


---
## Prerequsite and applicable area of category theory

- Typically you need to master a lot of fields, before teaching category theory. Because people they use examples from every branch of mathematics because it’s like a theory that abstracts over all other branches of mathematics.
- Mathematics is all about structure. 
- How people interact with other things that you already know or other things of the same type, is very much what we do in programming. 

---
## Category theory in programming

- We define things and then we describe them by how they interact with other things. Like in object-oriented programming. Okay, I mean mostly category theory is used in functional programming, but object-oriented programming also has very rigid structure, right? So you do things like data hiding for instance.
- What does it mean to hide your data? It means that you want to describe your object, not by how it’s implemented, but how it interacts with other objects. Namely its methods.
- What are messages, like what kind of messages can you send to this object and how it will respond to these messages by sending other messages and so on. 
- you have objects that interact with each other by sending messages, for instance – that’s like the essence of category theory.
- A category is just a bunch of objects and arrows between them. That’s all. And this is perfect model for programming.


---
- Turing School of Thought that says: “Well the computer is just a device that has like a sort of like a printing head and the reader and so on, and it just moves the tape and infinite tape and moves them.” So this is a very mechanical kind of approach.
- there is this very abstract approaching mathematics. Or like what is computation? Because normally in math you define things like functions and you say, “well function is just a value that is related to the argument of the function.” So there’s argument and there is value. You know, its like function is defined and this is argument. This is value. Give me an argument, I’ll give you a value. It doesn’t ask you, you know “well, but how long will it take you to calculate this value?” Right? No, it’s just there.
- well if I want the value I’ll have to derive it from the argument somehow and I have to go through some steps. Right? And so I have to decompose this bigger question into smaller question. And just answer every single smaller question and then combine them into one big result.
- being able to decompose bigger problems into smaller problems and then combine the solutions. That’s essentially the description of "programmer / mathematician /physicist".
	- you always split things into smaller pieces, right? And then sometimes when you work in a team, right, you have to split, your work into individual tasks
	- And then if you have like a huge, huge problem, you want to split it into smaller problems. Like if you want to prove Fermat’s Last Theorem, right? It’s not just like you think for a moment and then you say, oh, I got it, right? No.
	- You said, you know, I have to study first elliptic curves. And there was this theorem in elliptic curves that I have to prove. Oh, and somebody tried to prove it, but they failed because they couldn’t prove a certain lemma.

---
### **what does category theory bring to the table?**

-  category theory essentially studies all the different ways in which things can be composed and decomposed.
- the goal of category theory, you know, it’s like it says like what is the structure of things? So what is a structure? Structure is like what parts something has and how these parts interact.
- we don’t even ask ourselves these questions like what is structure? But it’s an obvious thing, right? But it is structure is that you can decompose something into smaller pieces and you can describe how they interact that structure.

---
## **Why does categories theory seem to… Or why is it more used in the world of functional programming? Why not imperative programming or object oriented programming?**

- because functional programming is much more restricted, less hacky. I mean, I came from imperative programming. I mean I programming C++ the last four years, so you know, I’m familiar with this stuff and I can do that. 
- But things in imperative programming are not very well defined. It’s like they don’t really have this nice mathematical structure.  It’s more of an expert system programming.
- Now in functional programming, it’s more like there is a mathematical structure behind it and let’s just stick to it, right? And if you have this mathematical structure, then you don’t have to slap people over the head and say don’t do that because it’s impossible to do certain things.

---
## Why we need something that models thing abstractly when they execute concretely

-  because there is this other thing on the other side of the computer and that’s the human programmer. Okay? So programming is not just about the computer, it’s about the interaction between the human and the computer. And the computer doesn’t really care about, you know, how structured your code is. Why do we avoid goto’s? You know, it’s like computers love goto’s. Give me goto’s. Yeah, I can execute them. I mean it’s like the processor has one of the basic instructions jump, right? 
- Why not let me jump all the time. Right? So why do we avoid goto’s? Not because computers don’t like goto’s, right? It’s because we humans, if we have too many goto’s, we just lose track of stuff and start making mistakes.
- So I don’t think this is like the requirement, you know, for the computer architecture or the programming language should reflect the architecture of the computer. I think the computer language should reflect the architecture of the human mind and the human mind works differently. 
- The computer doesn’t understand things, but we have to, right? We have to understand things and understanding again, it means that we have to like divide problems into smaller things. Give them names

- Human library vs Amazon warehouse
	- Human way: Have a Dewey decimal system where people can locate where books are.
	- Warehouse: Just put things whereever and just remember where they put them. It's a computer, so they don't need human memory structure. 

---
## Category theory for human, not for computers

- You’re not supposed to look inside objects or arrows. They are just the basic thing. you’ve described them not by what they are, but how they behave. 
- 1. if you have an arrow from A to B and an arrow from B to C, then there’s automatically an arrow from A to C. Which is a composition of these arrows. And that’s the principle of category theory. That things are composable.
- 2. there has to be an identity arrow for every object. Which means it’s an arrow that when you compose with some other arrow, you get back that arrow again.
- 3. have to be able to compose arrows. There has to be a unit arrow for every object that the identity arrow and also the composition has to be **associative** so that you don’t have to parentheses. --- Did they first compose these two and then compose it with the third one or did I do it in that different.

---

## Example of a category where that has some meaning

- Objects (in programming are called types)
- Arrows (in programming are called functions)
- So you are automatically in category theory if you are coding functional scripts. 

---
## Category is not just about structure study

-  You can add additional structure to the category or you can discover additional structure in this category.
- in programming we are dealing with data structures, right? So what are data structures? Again, you know you have to start with some elementary types, right? And then from these types you form more complex types.
- Product type
	- you put them into one bigger type that combines them. That’s called a product category theory.
- sum type
	- Or you do things like creating a data structure in which I either have a string or an integer like a union type or something. That also can be describing in a category theory as as a sum type and so on.
---
## Limitation of functional programming?

- functional programming is that the terminology can be confusing, right? That it can be not friendly to newcomers that we call it Algebraic data types and some types of product types. And do you think that’s like a valid criticism?
- No
- there are some cultures in the programming that invent languages and libraries where they come up with weird names that are supposed to be easier to understand than the ones they get from mathematics. But then it’s sort of like blocks you from going back to mathematics and trying to learn what’s the theory behind that
- you go to a mathematical paper and they use completely different language and you don’t know what is that? I don’t know what the sum is, what the, what our product is.
- Anyways if I call something, you know like in object oriented programming, if I call something an object that’s so meaningful, right? Just try to define what you mean by an object in a programming language.
	- Just because you took a word from English language that everybody thinks they understand, that doesn’t mean that an object in C++ for instance, is immediately obvious.

- Functor is mappable
- Monad is bindable. 

---
## How to get to writing category theory from doing C++ development

- I was always interested in… How do you write good programs, right? How do you make your programs reliable and that made me interested in the theory behind programming.
- I was always interested in exploring the boundaries. Like what is the hardest thing in C++ that you can think of? Well, I guess template method programming. 

---
## a way to understanding functional programming was like a shortcut for you to be able to understand template method programming. **Being able to think in Haskell but write in C++ was your advantage.**

-  if you program in C++, it’s a good idea to learn some Haskell and maybe use it as pseudo-code.

---
## How you get from Haskell to category theory?

-  they use these terms, the functor, monad and so on. So I was curious where do these terms come from and what’s the meaning of that.
-  I started looking into mathematical foundation on that, trying to understand. And then again, you know, it’s like, I know I don’t do much programming, mostly just testing some ideas, mostly testing the types, do they work together and so on.
- Because even the Haskell is too constraining but there are certain ideas in math that are difficult to translate to Haskell.
-  So again, I’m finding the boundaries of what can be expressed in Haskell and then going beyond them as category theory. There is a whole area in between which is dependent types. 