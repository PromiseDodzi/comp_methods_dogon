import pandas as pd
from lingpy import *
from lingpy.compare.util import  mutual_coverage_subset
from collections import defaultdict
import matplotlib.pyplot as plt
from tabulate import tabulate


#Getting language coverage illustration
wl=Wordlist("notebook_4_1.tsv")
coverage_series = pd.Series(wl.coverage().values(), index=wl.coverage().keys())
ax = coverage_series.plot(kind='bar')

plt.title("Language coverage in data")
plt.savefig('coverage_plot.png')  

plt.show()

#get data statistics
retain = []
for language, coverage in wl.coverage().items():
    if coverage > 288:
        retain += [language]

new_wl = {0: [c for c in wl.columns]}
for idx, language in wl.iter_rows("doculect"):
    if language in retain:
        new_wl[idx] = wl[idx]
new_wl = Wordlist(new_wl)

print("New Wordlist has {0} Languages and {1} concepts".format(new_wl.width,new_wl.height))
table = []
for language, coverage in new_wl.coverage().items():
    table += [[language, coverage, coverage /new_wl.height]]
print("\n")
print(tabulate(table, headers=["language", "items","coverage"],floatfmt=".2f"))

#get mutual coverage
number_of_languages=[]
perc_of_languages=[]
number_of_concepts=[]
perc_of_concepts=[]
mut_cov_num=[]
for i in range(800, 0, -1):
    count, results = mutual_coverage_subset(new_wl, i)
    coverage, languages = results[0]
    number_of_languages.append(count)
    perc_of_languages.append((count/new_wl.width)*100)
    number_of_concepts.append(coverage)
    perc_of_concepts.append((coverage/new_wl.height)*100)
    mut_cov_num.append(i)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 7))

scatter1 = axes[0].scatter(number_of_concepts, number_of_languages, c=mut_cov_num, alpha=0.6)
axes[0].set_ylabel("Number of languages")
axes[0].set_xlabel("Number of concepts")
axes[0].set_title("Mutual coverage in data")


scatter2 = axes[1].scatter(perc_of_concepts, perc_of_languages, c=mut_cov_num, alpha=0.6)
axes[1].set_ylabel("Percentage of languages")
axes[1].set_xlabel("Percentage of concepts")
axes[1].set_title("Mutual coverage in data")

plt.subplots_adjust(wspace=0.5)
plt.colorbar(scatter1, ax=axes[0], label='Mutual Coverage Number') 
plt.colorbar(scatter2, ax=axes[1], label='Mutual Coverage Number')
plt.savefig("mutual_coverage")
plt.show()

