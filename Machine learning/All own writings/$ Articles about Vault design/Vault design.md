- 9/4/2023

# Mission:
- Reader prioritized, not writer prioritized
	- toolbox that on the side of decoder / reader / human-learner, which prioritize the speed of information retrieval for solving problems, rather than courses / books that prioritize the speed of the encoder / writer. In other words, the functionality of the software should be all related to how the reader retrieve his previous writings. 
	- My hypothesis is, ALL data formats, excluding natural plain text articles, are the way of enhancing the reader-side experience. Particularly computer file formats.
- Enhancing the odds the entity being discovered 
	- The style of writing is prioritized on how to lift up the possibility of the sentence will be discovered in the future.
	- Existing methods:
		- 1. Unlinked mentions (for exact matches):
			- This method forces the writer to reduce their vocabulary, such that the software could link up separate notes, as far as the writer keep using the same exact word. 
		- 2. Aliases (for not exact matches)
	- New creating methods:
		- 1. Auto-linkage suggestion
			- When writing a new notes, the app would loop through each words, and displays suggestions of linkage, in the end of the block of words, to search whether there are some existing entities mentioned. 
		- 2. Edge-centered note-writing
		- 3. Multi-typed notes file format
			- File formats enable users and the software to make constraints on the content
		- 4. Context-based ML-learned  entity or attributes odds scoring 
			- 4 kinds of probability:
				- 1. That word is a named entity (E)
				- 2. That word is an attribute for another entity (A)
				- 3. That word is a pronoun, which could be simplified to be another E or A.
				- 4. That word is a part of A.
			- The probability is based on the context of the article. 
				- Say if we are talking about 

# User interaction 
### Discovery

### Onboarding


### Creating a new vault


### Creating a new note 


### 

# Success indicator
1. Discoverable
	- Detect the possibility of each word is whether rich meaning and the possibility of each entity could be linked up with other entity
	- Unlinked mentions, alias (which are already available in the market)
	- Auto-linkage suggestion:
		- Alleviate the workload for the content creator to link up the existing content while writing. 
	- Existence of constraints:
		- 
1. Computable
	- On comparison
		- Supports comparison between same class of concepts, which might be accomplished by hierarchical structure of types, learned by ML algorithms.  
	- On linking
		- Creating a score for predicting how probable a word is going to be linked. 
			- Say each word would have a score that indicate how informative it is, and we use unsupervised learning to learn that. 
				- Named entity recognition 
					- use machine learning algorithm to automatically identify entities such as people, organizations and locations in a text. 
				- Latent Dirichlet allocation
					- to identify the main topic in each note.
				- Semantic similarity
					- The idea is, words that have similar meanings tend to occur in similar contexts, and have similar relationships with other words. 
					- Wu-Plamer similarity
						- measures the similarity of two synsets based on their depth in the WordNet hierarchy and the depth of tehir most specific common ancestor. 
					- Word embeddings:
						- Represent words as vectors in a high-dimensional space based on their co-occurrence patterns. 
2. Context are linked but could be optionally hided 
3. Edge-centered writing 
4. Types-extraction and avoid writing the same thing as much as possible
5. Information entropy maximized note typing structure
	- 

# 