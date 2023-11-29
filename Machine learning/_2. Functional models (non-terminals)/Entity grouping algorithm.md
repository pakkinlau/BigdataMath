-25-9-2022: created

- Related paper: [[(Paper) an integrated framework of learning and evidential reasoning for user profiling using short texts]]
- From this paper:
- Input: text corpus U, user dictionary, distant function d, threshold e.
	- for each [[document]] for each word, calculate sim() to each distinct element. 
		- if sim> e, replace element with 'omega' in d. 
		- abstract corpus accept 'omega'
	- return abstract corpus