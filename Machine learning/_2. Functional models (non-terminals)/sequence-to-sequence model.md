---
alias: [seq2seq]
---

- 12-10-2022: created

- superset:
	- [[model]]

- Sequence to Sequence (often abbreviated to seq2seq) models is a special class of [[Recurrent|RNN]] architectures that we typically use (but not restricted) to solve complex Language problems like [[Machine Translation]], [[Question answering]], creating [[Chatbot]], [[Text Summarization]], etc.

- Components of seq2seq (R2)
	- 1. Encoder 
		- The complete input sequence is read by LSTM, with one word being sent into the encoder at each timestep. (R2)
		- The information is processed at each timestep, and the contextual info existing in the input sequence is captured. (R2)
	- 2. [[Decoder]]
		- [[Decoder]] is likewise an [[LSTM]] that analyses the whole target sequences word-by-word, and predict a sequence that is one timestep delayed.  (R2)

---
## Techniques

- [[attention]]
- [[beam search]]
- [[bucketing]]


- Related: [[Multi-word token expansion]]

---
## Reference
1. Vidhya's blog: 
https://www.analyticsvidhya.com/blog/2020/08/a-simple-introduction-to-sequence-to-sequence-models/#:~:text=Sequence%20to%20Sequence%20(often%20abbreviated,Chatbots%2C%20Text%20Summarization%2C%20etc.
2. Analytic steps blog: https://www.analyticssteps.com/blogs/what-text-summarization-nlp