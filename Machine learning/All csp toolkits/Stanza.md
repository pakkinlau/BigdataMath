---
created: 11-10-2022 23:50
category: [library]
alias: []
tags: []
cssclass: []
---

- Superset: []
- Subset functions: []

- Section 0a: What is Stanza? 
	- A python NLP toolkit for many human language
	- Same as [[CoreNLP]], this toolkit is also comes from stanford university. 
	- When the CoreNLP client is instantiated, Stanza will automatically start the CoreNLP server as a local process.  (R1)

- Section 0b: Similarities and differences of this package comparing with another packages

- [[(Comparison) spaCy versus Stanza]]


- Section 0c: All projects that is already using this package to accomplish tasks

---

- Section 1: General functionalities
	- Running stanza locally / online 
	- Neural pipeline interface
	- Document instance 
	- CoreNLP client interface


- Section 2: Detailed steps
	- (ALL examples could be found on Attachments/Detailed steps/Stanza.ipynb)






---
- Example 1: running stanza locally 

```python
import stanza
stanza.download('en') # download English model
nlp = stanza.Pipeline('en') # initialize English neural pipeline

doc = nlp("Considering using Stanza on English biomedical or clinical text? Consider using our biomedical models. Visit Stanza's biomedical demo page for a try of these models.") # run annotation over a sentence

print(doc)
print(doc.entities)

```

- Printout -- annotation of each word:
	- xpos: treeban[[part of speech]]
```
  [
    {
      "id": 1,
      "text": "Considering",
      "lemma": "consider",
      "upos": "VERB",
      "xpos": "VBG",
      "feats": "VerbForm=Ger",
      "head": 0,
      "deprel": "root",
      "start_char": 0,
      "end_char": 11,
      "ner": "O",
      "multi_ner": [
        "O"
      ]
```

- Printout -- identified entities in the text
```
[{
  "text": "Stanza",
  "type": "PRODUCT",
  "start_char": 18,
  "end_char": 24
}, {
  "text": "English",
  "type": "LANGUAGE",
  "start_char": 28,
  "end_char": 35
}, {
  "text": "Stanza",
  "type": "ORG",
  "start_char": 109,
  "end_char": 115
}]
```



---
- Example 2: Online demonstration of stanza:
	- http://stanza.run/

![[Pasted image 20221012170934.png|500x700]]
- Figure: some trial runs of the stanza online demo.
	- [[part of speech]]
	- [[Lemmatization|lemma]]
	- [[named entity recognition]]
	- [[Universal dependencies]]



---
1.  Neural pipeline interface (class object)
	- Stanza's NLP pipeline can be intialized with `pipeline` class, taking language name as an argument.
	- All processors will be loaded and run over the input text.

- Example: (R1) Shows a minimal usage of Stanza for downloading Chinese model, annotating a sentence with customized processors, and printing out all annotations. 
```python
import stanza
# download Chinese model
stanza.download(’zh’)
# initialize Chinese neural pipeline
nlp = stanza.Pipeline(’zh’, processors=’tokenize,
pos,ner’)
# run annotation over a sentence
doc = nlp(’斯坦福是一所私立研究型大学。’)
print(doc)
```


2.  Document instance
	- After all processors are run, a `Document` instance will be returned, which stores all annotation results. 
	- Within `Document`, annotations are further stored in `Sentence`, `Token`, `Word` instance in a top-down fashion.

- Example:
```python
# print the text and POS of all words  
for sentence in doc.sentences:  
for word in sentence.words:  
print(word.text, word.pos)  
# print all entities in the document  
print(doc.entities)
```

3. CoreNLP client interface

- Stanza is designed in a way that the actual communication with the backend CoreNLP server is transparent to the user.

```python
from stanza.server import CoreNLPClient
# start a CoreNLP client
with CoreNLPClient(annotators=[’tokenize’,’ssplit
’,’pos’,’lemma’,’ner’,’parse’,’coref’]) as
client:
# run annotation over input
ann = client.annotate(’Emily said that she
liked the movie.’)
# access all entities
for sent in ann.sentence:
print(sent.mentions)
# access coreference annotations
print(ann.corefChain)
```




- NLP [[tasks]]

- Figure: (R1) Comparison from R1
	- What is "fully neural"? "Fully neural, [[language-agnostic]]", which allows us to release models supporting 66 languages. 
	- Why it has "state-of-the-art" performance? --> Need to research 
	- What is "each step of the pipeline"?
![[Pasted image 20221011184800.png]]



- Advantages
	- 1. From raw text to annotations
	- 2. [[Multilingual]]
	- 3. [[State-of-the-art]] [[performance]]
		- For 112 datasets, its neural pipeline adapts well to text of different genres, achieving ... or competitive [[performance]] at each step of the pipeline.
	- 4. It has a pythonic interface to java coreNLP package, access to additional tools eg: coreference resolution, and relation extraction. 


---

- Architecture
	- 1. Neurl multilingual NLP pipeline

---
## Reference

1. [[(Paper) Qi, P., Zhang, Y., Zhang, Y., Bolton, J., & Manning, C. (2020). Sta n z a -- A Python Natural Language Processing Toolkit for Many Human Languages.]]












---
## Reference

1. 