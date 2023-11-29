### Base LLM
- Predicts the next word, based on text training data
- eg:
	- greedy algorithm that just feed the largest probability next-word. So there is not much logic at all. 

### Instruction tuned LLM
- Tries to follow instructions
- Fine-tune on instructions and good attempts at following those instructions. 
- eg:
	- question-answering
	- RLHS: Reinforcement learning with human feedback

---
# Guidelines

### Principles 
- 1. Write clear and specific instruction
	- You should express what you want a model to do by providing instructions that are as clear and specific as you can.
	- Longer prompts actually provide more clarity and context for the model, which can actually lead to more detailed and relevant outputs. 
		- That could guide the model and reduce the chance of getting incorrect responses. 
	- Tactics:
		- 1. Use delimiters: `""`, (backticks) , `---`, `<>` `<tag>`. 
			- Avoid prompt injection
				- This is the way to avoid "prompt injection". Like, you can use delimiter to quote the text that would be just the data involved, but not the part of the instruction.
		- 2. Ask for structured output
			- Make parsing the output easier. It can be helpful to ask for a structured output like HTML and JSON.
		- 3. Check whether conditions are satisfied.
			- First assumptions first. If it's not, indicate this then stop the full task completion attempt. 
- 2. Give the model time to think
	- Which means spending more computation effort on the task. 
	- Tactic 1: specify the steps to complete a task
		- eg: step 1,2,3, ... 
	- Tactic 2: Instruct the model to work out its own solution before rushing to a conclusion
		- eg: determine some statement is true or not. 
			- instead of let the AI to skim the text, you force the AI to have its own solution first. 
- Model limitations
	- 1. Hallucination 
		- It can make statements that sound plausible but are not true.
		- To reduce hallucinations:
			- 1. Find relevant information first
			- 2. Answer the question based on the relevant information.

- Figure: example way of specifying the output
![[Pasted image 20230629141903.png]]
![[Pasted image 20230629141916.png]]

---
### Iterative prompt development
- Writing application with LLM. 
- If you have a good process to iteratively make your prompt better, then you will be able to come to something that works well for the task you want to achieve.
- To be iterative, try something, analyze where the result does not give what you want, and then clarify instructions, give more time to think. Refine prompts with a batch of examples. 
- Looping steps of MLOps:
	- 1. Idea
	- 2. Implementation (code / data)
		- We use prompt to execute this step
	- 3. Experimentational result
	- 4. Error analysis
	- Repeat 1 - 4
- Example:
	- Writing a marketing plan
	- You provide:
		- 1. Fact sheet
		- 2. Prompt + embed the fact sheet. 
	- So you have first run. And see is it good enough.
	- If it can be improved. Rewrite the prompt and add that concern.

---
### Summarize
- Trial 1:
	- In X words
- Trial 2:
	- Focus on some aspect
- Chain up the summarization task
	- Step 1: Ask chatGPT to generate a list of articles. Each article could be very lengthy.
	- Step 2: Use a for-loop to force the AI to summarize each article one by one.

---
### Inferring
- Say you have an article "review of a product"
- You can ask AI to:
	- 1. Sentiment analysis
	- 2. Identify certain items (eg: item purchased, 2. Company that made that item) from the article, and write it as JSON. 
		- As boolean
		- As positive / negative
		- As string
		- As numerical value
	- 3. Topic (each item one or two words long) are being discussed in the article (topic modeling?)
	- 4. Given a list of topics, which topic is covered in the article, return true / false for each item.

---
### Transforming
- Use cases
	- 1. Use loops to iterate a list of sentences, pass it to the API, to get the response.
	- 2. Translate from slang to a business letter.
	- 3. Translate between JSON / HTML / XML / markdown ... 
	- 4. Checking a review
		- `from redlines importRedlines`
		- `diff = Redlines(text,response)`
	- 5. Proofread + APA style, ask for markdown format output

---
### Expanding
- Taking a shorter task of text, and having LLM generating longer text. 
- Use case:
	- 1. Given an article of "review", given the sentiment of that "review"
		- If the sentiment is positive, generate a reply to thank.
		  If the sentiment is negative, generate a reply to apologize.
	- 2. Use "Temperature" parameter to change the variety of model's responses. Which is a parameter in the `get_completion()` function, or `openai.ChatCompletion.create()` function.
		- When using a lower temperature, the model make a more focused and deterministic response.
		- When temperature = 1 or above, it increases the randomness of the sampling process. The model is more likely to explore less probable options, leading to more creative and diverse response. 

---
# building systems with the ChatGPT API

- Tokens:
	- chatGPT consider words as tokens, in their prediction. And it don't see individual characters. 
	- So it cannot reverse the task of "reversing the word `lollipop`.
	- Different models have different limits on the number of tokens can be processed. 

- System, user and assistant messages
	- 