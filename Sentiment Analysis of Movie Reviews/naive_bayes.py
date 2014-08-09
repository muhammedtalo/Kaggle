import csv
import sys
from sklearn.feature_extraction.text import CountVectorizer

reviews = []
with open(sys.argv[1]) as tsv:
    reader = csv.reader(tsv)
    for line in reader:
        reviews.append(line[0].split('\t')[2])

vectorizer = CountVectorizer(min_df=1)
vectorizer.fit(reviews)
x = vectorizer.transform(reviews)
x = x.toarray()
print x

