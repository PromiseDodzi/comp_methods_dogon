# compt_methods_dogon
This repository accompanies the paper `Adopting a computer-assisted approach to historical language comparison: defining early steps in a Dogon languages comparative work` by Promise Dodzi Kpoglu. 
The repository contains both the data and the source code used in the paper's experiment.

# Data
All data used for experiments are stored as .tsv files

### Original data
The orginal data as the field linguist curated is named original_data.tsv
The same data has been put on the Dogon and Bangime Linguistics project site which is accessible by this link
https://dogonlanguages.info/.
The data has also been curated in CLDF (cross Linguistic Data Format), and it is publicly available via this link:
https://github.com/languageorphans/heathdogon

### Processed data
The processed data, after manual process is data.tsv
Each row is a word and the columns are as follows:
| Column | Info |
| --------------- | --------------- | 
| ID    | unique identifier    | 
| VARID    | variant form identifier    | 
| DOCULECT    | language name    | 
| GLOSS    | meaning of the form as used by language users    |
| FRENCH    | gloss translation in French    |
| ENGLISH_SHORT    | reduced gloss in English    |
| FRENCH_SHORT    | reduced gloss in French    |
| ENGLISH_CATEGORY    | categorization of reduced gloss into designated categories    |
| FRENCH_CATEGORY    | categorization of reduced gloss in French into designated categories    |
| VALUE_ORG    | original form noted by field-linguist    |
| SINGULAR    | singular form of word,where neccesary. form used if available (except for verbs)    |
| PLURAL    | plural form of word, where neccesary    |
| FORM    | 'consensus' form chosen for verbs    |
| PARSED_FORM    | proposed segmentation of 'consensus' form    |
| RECONSTRUCTION    | proposed reconstruction    |
| CONCEPT    | standardized reference of gloss    |
| POS    | part of speech of word    |

### notebook_4_1
Data obtained after semi-manual processing
Each row is a word and the columns are as follows
|Column | Info |
|--------------- | --------------- |
| DOCULECT    | language name    |
| GLOSS    | meaning of the form as used by language users    |
| IPA    | standardized representation of the word in IPA    |

# Commands
Prior to running the following commands, clone this repository and run `pip install -r requirements.txt`
* `python cleaning_data_1.py data.tsv` runs the segmentation rule 'utils.py' on manually processed data 'data.tsv' by calling on various functions in 'functions.py'.
this outputs `notebook_4_1`, which is the final processed data ready for automatic cognate detection to be run
* `python illustrations.py` produces analysis of the `notebook_4_1`, outputting 'coverage_plot.png', a graph of every language's coverage, `mutual_coverage.png`, which gives an idea of length and breath coverage in data, and number of items on the command line
* `python cognates_alignments_2.py` outputs `notebook_4_lexstat.tsv` and `notebook_4_alignment_2.html` which are cognate clustering results and alignments results respectively.
* `python clustering_3.py` takes `notebook_4_lexstat.tsv` as input to output 'tree_notebook_4', a phylogenetic relationship based on cognacy, and `heatmap_notebook_4`, a heatmap of agregated pairwise distances between languages.



