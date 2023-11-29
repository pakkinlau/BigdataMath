---
alias: [NER, named entity tagging]
---

- 12-10-2022: created

- Superset:
	- [[NLP tasks]]

- Dependency:
	- [[Tokenization]]. [[Multi-word token expansion|MWT]]


- For NER we adopt the contextualized string representation based sequence tagger from Akbik et al. (2018). (R1)
- Viewed from a [[semantics|semantic]] perspective, these proper nouns refer to different kinds of entities: Janet is a person, Stanford University is an organization, and Colorado is a location.
	- eg: 
		- PER
		- LOC
		- ORG
		- GPE
	- named entity is commonly extended to include things that aren't entities per se, eg dates, times, or other temporal expressions.

- Applications
	- Sentiment analysis (consumers towards certain entity)
	- First stage in [[Question answering]]
	- Linking text to information in structured knowledge source like wikipedia
	- Central to natural language understanding tasks of building [[semantics|semantic]] representations, like extracting events and the relationship between participants. 

- Difficulties:
	- 1. the ambiguity of segmentation. 
		-  We need to decide what's an entity, and where the boundaries are.
		- Indeed, most words in a text will not be named entities.
	- 2. Type ambiguity
		- `JFK` can refer to a person, the airport in New York, or any number of schools.


![[Pasted image 20221017151300.png]]
- Fig: example of the NER tagger. 

---
## Reference
1. [[(Paper) Qi, P., Zhang, Y., Zhang, Y., Bolton, J., & Manning, C. (2020). Sta n z a -- A Python Natural Language Processing Toolkit for Many Human Languages.]]
2. [[(Book) Speech and language processing - Daniel Jurafsky (Stanford university)]]