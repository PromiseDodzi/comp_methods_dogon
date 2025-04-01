import os
from functions import lexstatExperiment, alignmentExperiment

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    files_dir = os.path.join(base_dir, '..', 'files')
    data_file = os.path.join(base_dir, '..', 'files', 'cleaned_data.tsv')

    # Ensure the files directory exists
    os.makedirs(files_dir, exist_ok=True)

    # Run experiments
    lexstatExperiment(data_file, 288, f"{files_dir}/lexstat")
    alignmentExperiment(f"{files_dir}/lexstat.tsv", f"{files_dir}/alignment")

if __name__ == "__main__":
    main()
