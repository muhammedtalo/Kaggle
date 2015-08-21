import sys
import csv
from sklearn.feature_extraction.text import CountVectorizer

f = open(sys.argv[1])
reviews = []
for rows in f:
    try:
        reviews.append(rows.split('\t')[2])
    except:
        pass

vectorizer = CountVectorizer(min_df=1, stop_words='english')
X = vectorizer.fit_transform(reviews)
print vectorizer.get_feature_names()
print (X.toarray().transpose())
