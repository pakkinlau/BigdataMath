- 12-10-2022: created

- UD specifies a complete morpho-syntactic representation that can be applied cross-linguistically. This effectively means that grammatical notions may be indicated via word forms (morphologically) or via dependency relations (syntactically). The morphological specification of a (syntactic) word in the UD scheme consists of three levels of representation:
	- A lemma representing the semantic content of the word.
	- A part-of-speech tag representing the abstract lexical category associated with the word.
	- A set of [[feature]] representing lexical and grammatical properties that are associated with the particular word form.

- Lemmas are typically determined by language-specific dictionaries and lexica. In contrast, the part-of-speech tags and grammatical properties are taken from two universal inventories defined below.

- Unlike in various language-specific tagsets, the universal tags and features do not include means to mark fused words (a word that is result of merging two other words, which are syntactically independent and belong to different parts of speech): Czech dělals (dělal + jsi … main verb + auxiliary); proň (pro + něj … preposition + pronoun); German zum (zu + dem … preposition + article); Spanish dámelo (da + me + lo … verb + clitics) etc. The only truly general approach to fused words in UD is to exploit the distinction between tokens and (syntactic) words, and to apply a language-specific processing step that splits tokens into syntactic words where necessary. Every syntactic word then gets its own part-of-speech tag and features. See also Tokenization and Format.


- Website: https://universaldependencies.org/u/overview/morphology.html#morphology-general-principles