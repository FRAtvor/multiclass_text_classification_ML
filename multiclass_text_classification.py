import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC


def category_extract (text):
    """
    exctract category from url
    splitted by "/"
    category in 4th position after split
    """       
    category = text.split("/")[3]
    # alternatively
    # category = re.sub(r"\/", " ", url).split("/")[2]
   
    return category


def clean_text(text):
    """    
    text pre-processing 
    - remove char [/], ['] and ["]
    - remove punctuation
    - lowercase text
    """      
        
    # replace punctuation char with spaces    
    filters='!"\'#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'
    translate_dict = dict((c, " ") for c in filters)
    translate_map = str.maketrans(translate_dict)
    text = text.translate(translate_map)

    # lowercase    
    text = text.lower()

    return text    


# data import
dataset = pd.read_csv('dataset_rss.csv')

#check data
print(dataset.head(10))
print(dataset.tail(10))

# DATA PREPROCESSING
# category_extract call in dataset column 'url'
dataset['url'] = dataset['url'].apply(lambda x: category_extract(x))

# rename column url -> category
dataset.rename(columns = {'url':'category'}, inplace=True)

categories = dataset.category.unique()

# check categories
print(categories)

# drop unwanted categoreis
dataset=dataset[dataset['category'].str.contains(".php")==False]
dataset=dataset[dataset['category'].str.contains("2009")==False]
dataset=dataset[dataset['category'].str.contains("2014")==False]

print(dataset.tail(10))

categories = dataset.category.unique()
print(categories)

# split dataset - train / test by title, 80/20
# used title as data. In perex are too much confusing words without stop words defined.
train_data, test_data, train_labels, test_labels = train_test_split(dataset['title'], dataset['category'], test_size=0.20)


# vectorizing text 
# (+ possible stop words, but my_list need to be defined according list of words counts in texts - TBC, better accuracy expected) 
# + clean text
vectorizer = CountVectorizer(
    # stop_words = my_list,
    preprocessor = clean_text)

train_data_vect = vectorizer.fit_transform(train_data)    
test_datat_vect = vectorizer.transform(test_data)


# Naive Bayes multinominal, easy&fast 
# instantiate model
model_nb = MultinomialNB()

# trainig model
model_nb.fit(train_data_vect, train_labels)
pred_nb = model_nb.predict(test_datat_vect)

# accuracy evaluation
acc_score_nb = accuracy_score(test_labels, pred_nb)
print(acc_score_nb*100)

# SVC try, should scale better to large numbers of samples
# instantiate model
model_SVC = LinearSVC()

# model training
model_SVC.fit(train_data_vect, train_labels)
pred_SVC = model_SVC.predict(test_datat_vect)

# accuracy evaluation
acc_score_SVC = accuracy_score(test_labels, pred_SVC)
print(acc_score_SVC*100)