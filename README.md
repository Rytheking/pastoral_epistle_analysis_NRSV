# pastoral_epistle_analysis_NRSV
All biblical translations sourced from https://ebible.org/eng-asv/oldindex.htm

To set up run
```shell
python3 -m venv venv
source venv/bin/activate  # (or venv\Scripts\activate on Windows)
```

Install needed dependencies
```shell
pip install nltk matplotlib textstat matplotlib-venn pandas seaborn
python -m nltk.downloader punkt, stopwords
```