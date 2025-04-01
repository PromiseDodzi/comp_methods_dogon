import os
import pandas as pd
import numpy as np
from functions import prior_forms, parsing_data, remove_spaces
from segments.tokenizer import Tokenizer
from sys import argv

def main():
    # Define input file path
    input_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "files"))
    input_file = os.path.join(input_dir, "data.tsv")
    
    # Check if the file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return
    
    # Loading data
    data = pd.read_csv(input_file, sep="\t", encoding="utf-8")
    
    # Dropping unwanted columns
    list_to_drop = ["ID", "FRENCH", "ENGLISH_SHORT", "FRENCH_SHORT", "ENGLISH_CATEGORY", "FRENCH_CATEGORY", "PARSED FORM", "RECONSTRUCTION"]
    data = data.drop(columns=list_to_drop, errors='ignore')
    
    # Pulling necessary data together
    data["BEFORE_PARSE"] = data.apply(prior_forms, axis=1)
    
    # Segmenting data
    data["PARSED"] = data.apply(parsing_data, axis=1)
    
    # Using orthography profile
    tk = Tokenizer('files/orthography.tsv')
    data["IPA"] = data["PARSED"].apply(lambda x: tk(x, column="IPA") if isinstance(x, str) else x)
    
    # Cleaning spaces
    data["IPA"] = data["IPA"].apply(remove_spaces)
    data = data[["DOCULECT", "GLOSS", "IPA"]].dropna(subset=["DOCULECT", "GLOSS", "IPA"])
    
    # Drop empty columns and specific entries
    data.replace("", np.nan, inplace=True)
    data = data.dropna(subset=["IPA"])
    data = data.drop(data.loc[(data["GLOSS"] == "(1Pl subject pronominal)") & (data["DOCULECT"] == "Mombo")].index)
    
    # Define output directory and file path
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "files"))
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "cleaned_data.tsv")
    
    # Save cleaned and formatted data
    data.to_csv(output_file, index=False, encoding="utf-8", sep='\t')
    print(f"Cleaned data outputted to '{output_file}'")

if __name__ == "__main__":
    main()
