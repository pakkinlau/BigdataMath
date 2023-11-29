- 21/6/2023 added

# Lecture 1

- 6.5B web searches every day
- Text-based information retrieval is likely the most frequently used piece of software in the world
- Sentiment analysis in 900k Yelp review
- social network
- chatbot
- recommendation engine
- resolving ambiguity is hard
	- `The chef made her duck`
		- 7 possible interpretations
- models and tools
	- regular expressions
	- edit distance and alignment
	- neural word embeddings
	- machine learning classifiers
		- naive bayes
		- logistic regression
		- neural networks
	- neural language model (aka foundation models)
	- network algorithms
	- recommendation algorithms
	- linguistic tools
	- The GUS chatbot architecture
	- neural chatbots
- Core of model NLP - neural word embeddings
	- A word's meaning is a point in, say, 300-dimensional space


- leaning goals
	- write efficient regular expressions to solve any kind of text-based extraction tasks
	- apply the edit distance algorithm to all sorts of sequence problems
	- build a supervised classifier to solve problems like sentiment classification
	- build a neural network and train it using stochastic gradient descent
	- build a search engine
	- build a recommendation engine
	- build a computational model of word meaning (using lexicons and neural word embeddings)
	- build a chatbot
	- understand and implement PageRank and other social network functions
	- understand neural language models and be able to reason both about what they can do, and also their social implications

---
# Lecture 2 - Unix for poets

- why it is related to machine learning
	- Including a step of Unix command text processing before training a machine learning model can help improve the quality of the training data. 
	- By
		- clean and preprocess the data
		- extract relevant information
		- transform the text
		- engineer effective features
	- Possible actions
		- Data cleaning
		- Text normalization
			-  Converting text to lowercase, removing punctuation marks, expanding contractions, or handling special characters to standardize the data.
		- Stop word removal
			- Stop word removal: Removing commonly occurring words that do not contribute much to the overall meaning or predictive power of the text, such as "the," "and," "is," etc.
		- Tokenization
			- Splitting the text into individual words or tokens to create a bag-of-words representation.
		- Lemmatization
			- Reducing words to their base or root form to handle variations (e.g., "running" and "ran" to "run").
		- Feature extraction 
			- Extracting relevant information from the text, such as extracting keywords, named entities, or specific patterns that can be used as features for training the machine learning model.

- motivation:
	- While it is true that training a text machine learning model typically involves feeding a large text corpus. There are still several reasons why learning text processing Unix commands can be valuable:
		- 1. Data preprocessing
			- They can help you clean and format your data, extract relevant information, remove unwanted characters, and perform various text transformations that can improve the quality of your training data.
		- 2. Data exploration
			- Unix commands like grep allow you to search for specific patterns or keywords within a text corpus, helping you gain insights into the data. By exploring the data, you can identify potential issues, anomalies, or patterns that may impact the training process or require special handling.
		- 3. Feature engineering
			- In many cases, the performance of machine learning models depends on the quality of the features used for training. Unix commands provide convenient ways to extract and manipulate features from text data.
			- For example, you can use tools like sed or awk to extract specific fields from a structured text file or to transform the text in a way that enhances the predictive power of the features.
		- 4. Integration with pipelines and scripts
			- Unix commands are designed to work well with command-line interfaces and can be easily integrated into pipelines or scripts. This allows you to automate text processing tasks, perform batch operations on large datasets, or incorporate text processing steps into larger data processing workflows. 
		- 5. Efficiency and performance
			- While machine learning models can handle text processing tasks to some extent, they might not always be the most efficient solution. Unix commands are optimized for text processing and can often perform operations much faster than a general-purpose machine learning model.

- tools
	- grep
	- sort
	- uniq -c
	- tr
	- wc
	- sed
	- cat
	- echo
	- cut
	- paste
	- head
	- tail
	- rev
	- comm
	- join

- prerequisite
	- ubuntu in the machine

- task 1: count words in a text
	- algorithm
		- tokenize
		- sort
		- count duplicates
- task 2: merge upper and lower case by downcasing everything

- sorting and reversing liners of text
	- sort
	- sort -f
	- sort -n
	- sort -r
	- sort 0nr
	- echo "Hello" |rev

- counting and sorting exercise
	- task 1: fins the 50 most common words in the NYT
	- task 2: find the words in the NYT that end in "zz"

- tips
	- 1. piping commands together can be simple and powerful and Uninx
	- 2. It gives flexibility

### Bigrams
- They are word pairs and their counts
- Algorithms
	- 1. tokenize by word
	- 2. create two almost-duplicate files of words, off by one line, using tail
	- 3. paste them together so as to get $word_i$ and $word_{i+1}$ on the same line.
	- 4. count
- Exercise: find the 10 most common bigrams
	- For you to look at, what part-of-speech pattern are most of them?
	- solution: `tr 'A-Z' 'a-z' < nyt.bigrams | sort | uniq -c | sort -nr | head -n 10`
- Exercise: find the 10 most common trigrams
	- solution:
		- `tail -n +3 nyt.words > nyt.thirdwords`
		- `paste nyt.words nyt.nextwords nyt.thirdwords > nyt.trigrams`
		- `cat nyt.trigrams | tr "[:upper:]" "[:lower:]" | sort | uniq -c | sort -rn | head -n 10`

### Grep
- Grep finds patterns specified as regular expressions
	- It stands for "globally search for regular expression and print"
- Grep is a filter, you keep only some lines of the input
	- `grep gh` keep lines containing ‘"gh’"
	- `grep '^con'` keep lines beginning with "con"
	- `grep 'ing$'` keep lines ending with ‘‘ing
	- `grep -v gh` keep lines NOT containing “gh
- Grep versus egrep (grep -E)
- Exercise: finding words ending in `-ing`
	- `grep 'ing$' nyt.words |sort | uniq –c`

### Sed
- sed is used when you need to make systematic changes to strings in a file (larger changes than `tr`)
- it is line based, you optionally specify a line, by regex or line numbers, and specific a regex substitution to make
- eg:
	- to change all cases of George to Jane
	- `sed 's/George/Jane/' nyt_200811.txt | less`
- exercise
	- count frequency of word initial consonant sequences
		- `tr "[:upper:]" "[:lower:]" < nyt.words | sed 's/[aeiou].*$//' | sort | uniq -c`
	- count word final consonant sequences
		- `tr "[:upper:]" "[:lower:]" < nyt.words | sed 's/^.*[aeiou]//' | sort | uniq -c | sort -rn | less`

---
# Lecture 3 regular expression 


---
# Lecture 4 minimum edit distance

---
# Lecture 5 Introduction to N-grams

- goal: assign a probability to a sentence
	- Machine translation
	- Spell correction
	- Speech recognition

---
# Lecture 6  Text classification and naive bayes

### Text classification
- definition
	- input - a document $d$, 
	- a fixed set of classes $C = \{ c_1, c_2, \dots, c_j \}$
- output:
	- a predicted class $c \in C$

### Classification methods
- hand-coded rules 
- supervised machine learning
	- any kind of classifier
		- naive bayes
		- logistic regression
		- support-vector machines
		- k-nearest neighbors


### naive bayes classifier
- bag of word representation

### multinomial naive bayes independence assumptions
- naive bayes -- learning
	- parameter estimation

### sentiment classification

### generative model for multinomial naive bayes

### confusion matrix

### per class evaluation measures
- Recall
	- fraction of docs in class $i$ classified correctly
- Precision
	- fraction of docs assigned class $i$ that are actually about class $i$
- Accuracy
	- fraction of docs classified correctly


---
# Lecture 7 - logistic regression

- baseline supervised machine learnign tool for classification

- naive bayes is a generative classifier
- logistic regression is a discriminative classifer

### Generative classifier

### Discriminative classifier 

### Probabilistic machine learning classifier

### Learning --- cross-entropy loss

### Stochastic gradient descent

### hyperparameters








---
# Lecture 8 - Introduction to information retrieval

### Information retrieval
- collection - a set of documents
- goal: retrieve documents with information that is relevant to the user's information need and helps the user complete a task

- Unstructured versus structured data in nineties and today

- figure: the classic search model
![[Pasted image 20230621190825.png|400]]

- how good are the retrieved docs?
	- precision: fraction of retrieved docs are relevant to the user's information need
	- recall: fraction of relevant docs in collections are retrieved

### Term-document incidence matrices

### Inverted index
- It is the key data structure underlying modern information retrieval (IR)

### Query processing with an inverted index


### Boolean retrieval model 


### Extended Boolean models

### Phrase queries

### Positional indexes


---
# Lecture 9 Introducing ranked retrieval

### Scoring with the Jaccard coefficient

### Term frequency weighting

### Document frequency weighting

### tf-idf weighting

### vector space model (VSM)

### tf-idf cosine scores
- sdsd
- calculating tf-idf cosine scores in an IR system
	- ...
	- ...

### Using many features to determine relevance

### Evaluating search engines
- Measurable (speed/size)
	- How fast does it index
	- How fast does it search
	- Expressiveness of query language
	- Uncluttered UI
	- Is it free?
- User happiness
- Evaluating ranked results
	- If we have:
		- a benchmark document collection
		- a benchmark set of queries
		- assessor judgment of whether documents are relevant to queries
	- then we can use precision/recall/F measure as before
	- The system can return any number of results

### Precision-recall curve
- By taking various numbers of the top returned documents, the evaluator can produce a precision-recall curve

### Averaging over queries


### Interpolated precision

---
# Lecture 10 Word meaning

### Desiderata

### Lemma

### Sense

### Synonymy
- Relations between senses

### Linguistic principle of contrast
- Difference in form --> difference in meaning


### Similarity relation

### Word relatedness relation 


### Semantic field


### Antonymy relations

### Connotation (sentiment)

### Vector semantics


### Computational model of word meaning
- Ideas:
	- 1. Defining meaning by linguistic distribution
	- 2. Meaning as a point in space (Osgood et al. 1957)
		- 3 affective dimensions for a word
			- valence
			- arousal 
			- dominance

### Embeddings
- Every modern NLP algorithms uses embeddings as the representation of word meaning
- why vectors?
	- with words, a feature is a word identity
	- with embeddings
		- feature is a word vector
		- the previous word was a vector
		- now in the test set we might see a similar vector
		- we can generalize to similar but unseen words
- kinds of embeddings
	- 1. tf-idf
	- 2. word2vec

### Computing word similarity


### Skip-gram

### Skip-gram classifier

### Learning the classifier


### Properties of embeddings
- Kinds 
	- Small windows
	- Large windows
- Analogical relations


---
# Lecture 11 Part of speech tagging


---
# Lecture 12 Units in neural networks

---

# Lecture 13 Git tutorial

---
# Lecture 14 Introduction to chatbots and dialogue systems

---
# Lecture 15 Introduction to recommender systems

---
# Lecture 16 Web graphs, Links, and PageRank

---
# Lecture 17 Social Networks 

















