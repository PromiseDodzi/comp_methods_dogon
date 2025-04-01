from utils import NounParser,VerbParser,AdjectiveNumeralParser
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from lingpy import *
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceMatrix, DistanceTreeConstructor


#Instantiating parser objects
noun_parser=NounParser()
verb_parser=VerbParser()
adj_num_parser=AdjectiveNumeralParser()


def prior_forms(row):
    """
    puts all forms that have been parsed into a single column
    """
    if pd.isna(row["POS"]):  
        return None
    elif row["POS"] in ["noun", "numeral", "adjective"]:
        form = str(row["SINGULAR"]) if isinstance(row["SINGULAR"], str) else ""
        return form
    elif row["POS"] == "verb":
        verb = row["FORM"]
        if pd.isna(verb):
            return None
        else:
            return verb
    else:
        form = str(row["SINGULAR"]) if isinstance(row["SINGULAR"], str) else ""
        return form




def parsing_data(row):
    """
    puts all forms that have been parsed into a single column
    """
    if pd.isna(row["POS"]):  
        return None
    elif row["POS"]=="noun":
        noun=row["BEFORE_PARSE"]
        if pd.isna(noun):
            return None
        else:
            noun=(noun_parser.identified_suffixes(
            noun_parser.hyphen_space(
                noun_parser.nasalized_stops(
                    noun_parser.cvcv_segmentation(
                            noun_parser.parse_off_final_nasals(
                                noun_parser.existing_parses(
                                    adj_num_parser.y_suffixes(noun.strip("()/_"))))))))) if (noun.endswith("y") or (noun.endswith("ⁿ") and noun[-2]=="y")) else \
                            (noun_parser.identified_suffixes(
                                noun_parser.hyphen_space(
                                    noun_parser.nasalized_stops(
                                        noun_parser.cvcv_segmentation(
                                                noun_parser.parse_off_final_nasals(
                                                    noun_parser.existing_parses(noun.strip("()/_"))))))))
            return noun
            
    elif row["POS"] == "numeral" or row["POS"] == "adjective":
        form = row["BEFORE_PARSE"]
        if pd.isna(form):
            return None
        else:
            form=adj_num_parser.miscellaneous(
            adj_num_parser.switch_hyphen_position(
                adj_num_parser.replace_hyphens_keep_last(
                    adj_num_parser.y_suffixes(
                        adj_num_parser.isolating_suffixes(
                                adj_num_parser.existing_parses(form.strip("()/_")))))))
            return form
    elif row["POS"] == "verb":
        verb = row["BEFORE_PARSE"]
        if pd.isna(verb):
            return None
        else:
            verb=verb_parser.post_editing_short_strings(
            verb_parser.segment_cvcs(
                    verb_parser.existing_parses(verb.strip(")(_"))))
            return verb
    else:
        form = str(row["BEFORE_PARSE"]) if isinstance(row["BEFORE_PARSE"], str) else ""
        return form


def remove_spaces(word):
    if word is None:
        return None
    new_word=""
    for letter in word:
        if letter==" ":
            new_word += ""
        else:
            new_word += letter
    return new_word

def lexstatExperiment(input_file, coverage_num, lexstat_output):
    """
    Takes an input file and outputs a lexstat cluster
    input_file: any_name
    coverage_num: coverage number
    lexstat_output:any_name
    """
    wl = Wordlist(input_file)
    retain = []
    for language, coverage in wl.coverage().items():
        if coverage > coverage_num:
            retain.append(language)
    
    new_wl = {0: [c for c in wl.columns]}
    for idx, language in wl.iter_rows("doculect"):
        if language in retain:
            new_wl[idx] = wl[idx]
    new_wl = Wordlist(new_wl)
    
    lex = LexStat(new_wl)
    lex.get_scorer(runs=10000)
    lex.cluster(method='lexstat', threshold=0.55, ref='cogid')
    
    return lex.output('tsv', filename=lexstat_output)

def alignmentExperiment(input_name, output_name, output_type="html"):
    """
    returns a nexus file of alignments.
    Arguments:
    input_name= a tsv lexstat cluster
    output_name= name to be given to nexus file
    """
    lex=LexStat(input_name)
    alm = Alignments(lex, ref='cogid')
    alm.align()
    return alm.output(output_type, filename=output_name)

def getHeatmap(distance, taxa, title, heatmap_name):
    """
    returns a heatmap. It accepts a distance matrix and a list of languages
    Args:
        distance=distance matrix
        taxa=languages
        title=title of heatmap
        heatmap_name=name to be used to save heatmap
    """
    fig=plt.figure(figsize=(12, 8))  # Adjust the width and height as needed
    sns.heatmap(pd.DataFrame(distance, taxa, columns=taxa), annot=True)
    plt.title(title)
    plt.show()
    return fig.savefig(heatmap_name)

def getdistanceandtaxa(lexstat_cluster):
    "returns distances and languages that must be assigned a variable. Accepts a lextstat clustered tsv file"
    lex=LexStat(lexstat_cluster)
    alm=Alignments(lex)
    alm.align()
    distance=alm.get_distances()
    taxa=alm.taxa
    return distance, taxa

def treeConstructor(distance, language, tree_name,title):
    """
    returns a phylogenetic tree. It accepts a distance matrix and a list of languages
    Args:
        distance=distance matrix
        language=languages
        tree_name=name to be used to save heatmap
        title=title of heatmap
    """
    
    df =  pd.DataFrame(distance, language, columns=language)
    
    # Convert the DataFrame to a lower triangular matrix format
    def to_lower_triangle(matrix):
        lower_triangle = []
        for i in range(len(matrix)):
            row = []
            for j in range(i+1):
                row.append(matrix[i][j])
            lower_triangle.append(row)
        return lower_triangle
    
    matrix = to_lower_triangle(df.values)
    labels = df.index.tolist()
    
    # Create a DistanceMatrix object
    distance_matrix = DistanceMatrix(names=labels, matrix=matrix)
    
    # Construct the tree using UPGMA (you can also use 'nj' for Neighbor-Joining)
    constructor = DistanceTreeConstructor()
    tree = constructor.upgma(distance_matrix)
    
    # Draw the tree using matplotlib and save to a PNG file
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(1, 1, 1)
    plt.title(title)
    Phylo.draw(tree, do_show=False, axes=ax)
    plt.show()
    
    # Save the figure as a PNG file
    return fig.savefig(tree_name)

def getHeatmap(distance, taxa, title, heatmap_name):
    """
    returns a heatmap. It accepts a distance matrix and a list of languages
    Args:
        distance=distance matrix
        taxa=languages
        title=title of heatmap
        heatmap_name=name to be used to save heatmap
    """
    fig=plt.figure(figsize=(12, 8))  # Adjust the width and height as needed
    sns.heatmap(pd.DataFrame(distance, taxa, columns=taxa), annot=True)
    plt.title(title)
    plt.show()
    return fig.savefig(heatmap_name)