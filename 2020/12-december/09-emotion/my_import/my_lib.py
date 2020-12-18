#dieu
import numpy as np
import pandas as pd
import string
from collections import defaultdict
from time import time
# Sklearn
from sklearn.feature_extraction.text import CountVectorizer , TfidfVectorizer , TfidfTransformer
from sklearn.model_selection import ShuffleSplit
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.metrics import recall_score , precision_score ,f1_score
from sklearn import metrics , svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier, LogisticRegression, LogisticRegressionCV
from sklearn.naive_bayes import MultinomialNB, CategoricalNB, ComplementNB, BernoulliNB
from sklearn.svm import SVC, LinearSVC
#vis
# import matplotlib
# import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import plotly.graph_objs as go
import plotly as py
from plotly.offline import init_notebook_mode, iplot, plot
#NLP ISSUE WITH HEROKU
# # # import nltk   
# # # from nltk.corpus import stopwords , wordnet as wn    
# # # from nltk import wordpunct_tokenize , WordNetLemmatizer ,sent_tokenize ,  word_tokenize
# # # from nltk.stem import PorterStemmer , LancasterStemmer
# # # from nltk.stem.snowball import SnowballStemmer  
#Dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
