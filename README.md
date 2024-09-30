# compt_methods_dogon
This repository accompanies the paper Adopting a computer-assisted approach to historical language comparison: defining early steps in a Dogon languages comparative wor by Promise Dodzi Kpoglu. 
The repository contains both the data and the source code used in the paper's experiment.

# Data
All data used for experiments are stored as .tsv files

## Original data
The orginal data as the field linguist curated is named original_data.tsv
The same data has been put on the Dogon and Bangime Linguistics project [site]([url](https://dogonlanguages.info/))

## Processed data
The processed data, after manual process is data.tsv
Each row is a word and the columns are as follows:
| Column | Info |
| --------------- | --------------- | 
| ID    | unique identifier    | 
| VARID    | variant form identifier    | 
| DOCULECT    | language name    | 
| GLOSS    | the meaning of the form as used by language users    |
| FRENCH    | the gloss translation in French    |
| ENGLISH_SHORT    | the reduced gloss in English    |
| FRENCH_SHORT    | the reduced gloss in French    |
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


