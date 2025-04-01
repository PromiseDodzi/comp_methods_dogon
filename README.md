# compt_methods_dogon

This repository accompanies the paper "Adopting a computer-assisted approach to historical language comparison: defining early steps in a Dogon languages comparative work" by Promise Dodzi Kpoglu. The repository contains both the data and the source code used in the paper's experiments. The code, files, and illustrations are available on the `master` branch of this repository.

## Data

All data used for experiments are stored in the `files` folder.

### Original Data

The original data, as curated by the field linguist, is named `original_data.tsv`. This data is also available on the Dogon and Bangime Linguistics project site, accessible via [this link](https://dogonlanguages.info/). The data has been curated in CLDF (Cross-Linguistic Data Format) and is publicly available via [this link](https://github.com/languageorphans/heathdogon).

### Processed Data

The processed data, after manual processing, is named `data.tsv`. Each row represents a word, and the columns are as follows:

| Column            | Info                                                                 |
|-------------------|----------------------------------------------------------------------|
| ID                | Unique identifier                                                   |
| VARID             | Variant form identifier                                             |
| DOCULECT          | Language name                                                       |
| GLOSS             | Meaning of the form as used by language users                       |
| FRENCH            | Gloss translation in French                                         |
| ENGLISH_SHORT     | Reduced gloss in English                                            |
| FRENCH_SHORT      | Reduced gloss in French                                             |
| ENGLISH_CATEGORY  | Categorization of reduced gloss into designated categories          |
| FRENCH_CATEGORY   | Categorization of reduced gloss in French into designated categories|
| VALUE_ORG         | Original form noted by field-linguist                               |
| SINGULAR          | Singular form of the word, where necessary                          |
| PLURAL            | Plural form of the word, where necessary                            |
| FORM              | 'Consensus' form chosen for verbs                                   |
| PARSED_FORM       | Proposed segmentation of 'consensus' form                           |
| RECONSTRUCTION    | Proposed reconstruction                                             |
| CONCEPT           | Standardized reference of gloss                                     |
| POS               | Part of speech of the word                                         |

### Cleaned Data

This is the data obtained after semi-manual processing. Each row represents a word, and the columns are as follows:

| Column    | Info                                                                 |
|-----------|----------------------------------------------------------------------|
| DOCULECT  | Language name                                                       |
| GLOSS     | Meaning of the form as used by language users                       |
| IPA       | Standardized representation of the word in IPA                       |

## Scripts

The `scripts` folder contains all the Python scripts needed to obtain the results reported in the paper.

- `utils.py`: Contains various classes defined to help clean and segment words.
- `functions.py`: Calls on classes defined in `utils.py` and defines various functions to clean the original data.
- `cleaning_data.py`: Calls various functions in `functions.py` to clean the original data and outputs `cleaned_data.tsv`.
- `data_statistics.py`: Analyzes various components of the data and outputs results to the `illustrations` folder.
- `cognates_alignments.py`: Automatically determines cognates in the data and performs alignment analysis. Outputs files into the `files` folder.
- `clustering.py`: Accepts the results of `cognates_alignments.py` and performs clustering and analysis. Results are outputted into the `illustrations` folder.

## Illustrations

This folder contains:

- `coverage_plot.png`: The result of the analysis carried out on the data.
- `mutual_coverage.png`: The result of the mutual coverage analysis of the data.
- `heatmap.png`: A heatmap illustrating the weighted distances between languages.
- `tree.png`: A phylogenetic tree illustrating the relationships between the various Dogon languages.

## Commands

To obtain the same results reported in the paper:

1. Clone this repository and run `pip install -r requirements.txt`.
2. Switch to the `master` branch by running the command `git checkout master`.

There are two ways to obtain the results:

- Run `make all` on the command line to automatically run all scripts.
- Run the scripts manually:
  - `python cleaning_data.py`: Runs the segmentation rules in `utils.py` on the manually processed data `data.tsv` by calling various functions in `functions.py`.
  - `python data_statistics.py`: Produces an analysis of `cleaned_data.tsv`, outputting `coverage_plot.png`, a graph of every language's coverage, `mutual_coverage.png`, which gives an idea of length and breadth coverage in the data, and the number of items on the command line.
  - `python cognates_alignments.py`: Outputs `lexstat.tsv` and `alignment_2.html`, which are cognate clustering results and alignment results, respectively.
  - `python clustering.py`: Takes `lexstat.tsv` as input to output `tree.png`, a phylogenetic relationship based on cognacy, and `heatmap.png`, a heatmap of aggregated pairwise distances between languages.



