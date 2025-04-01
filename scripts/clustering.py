import os
from functions import getdistanceandtaxa, treeConstructor, getHeatmap

def get_tree_and_cluster():

    base_dir = os.path.dirname(os.path.abspath(__file__))
    files_dir = os.path.join(base_dir, '..', 'files')
    illustrations_dir = os.path.join(base_dir, '..', 'illustrations')

    # Create the illustrations directory if it doesn't exist
    if not os.path.exists(illustrations_dir):
        os.makedirs(illustrations_dir)

  
    distance, taxa = getdistanceandtaxa(f"{files_dir}/lexstat.tsv")

    # Generate tree and save it in illustrations directory
    treeConstructor(distance, taxa, f"{illustrations_dir}/tree", "Phylogenetic relationship among Dogon languages")

    # Generate heatmap and save it in illustrations directory
    getHeatmap(distance, taxa, "Heatmap of Dogon languages cognate detection", f"{illustrations_dir}/heatmap")


if __name__ == "__main__":
    get_tree_and_cluster()


