.PHONY: all prepare_data statistics cognates clusters
all: prepare_data statistics cognates clusters
prepare_data:
	python scripts/cleaning_data.py  
statistics:
	python scripts/data_statistics.py  
cognates:
	python scripts/cognates_alignments.py  
clusters:
	python scripts/clustering.py



