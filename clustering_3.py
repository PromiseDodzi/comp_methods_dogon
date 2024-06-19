from functions import getdistanceandtaxa,treeConstructor,getHeatmap


distance_notebook_4, language_notebook_4=getdistanceandtaxa("notebook_4_lexstat.tsv")

treeConstructor(distance_notebook_4, language_notebook_4, "tree_notebook_4","Phylogenetic relationship among Dogon languages")

getHeatmap(distance_notebook_4, language_notebook_4, "Heatmap of Dogon languages cognate detection", "heatmap_notebook_4")
