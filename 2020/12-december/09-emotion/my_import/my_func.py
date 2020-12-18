from my_import.my_lib import *

def get_top_n_words(corpus,d,n=None):
    vec = CountVectorizer().fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in     vec.vocabulary_.items()]
    if d == "up" :
        words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
        return words_freq[:n]
    elif d == "down" :
        words_freq=sorted(words_freq, key = lambda x: x[1], reverse=False)
        return words_freq[:n]

def tokenize(corpus):
    #text = ''.join([ch for ch in text if ch not in dataEF["Text"]])
    tokens = nltk.word_tokenize()
    lemma = WordNetLemmatizer()
    stemmer = SnowballStemmer("english")
    # tokens = [lemmatizer.lemmatize(token) for token in tokens] 
    #OR
    # tokens = [lemma.lemmatize(lemma.lemmatize(lemma.lemmatize(w,'v'),'n'),'a')for w in tokens]
    return [stemmer.stem(token) for token in tokens]

def run_pipes(pipes, splits=10, test_size=0.2, seed=42):  
    res = defaultdict(list)
    spliter = ShuffleSplit(n_splits=splits, test_size=test_size, random_state=seed)
    for idx_train, idx_test in spliter.split(corpus):
        for pipe in pipes:
            # name of the model
            name = "-".join([x[0] for x in pipe.steps])
            
            # extract datasets
            X_train = corpus[idx_train]
            X_test = corpus[idx_test]
            y_train = targets[idx_train]
            y_test = targets[idx_test]
            
            # Learn
            start = time()
            pipe.fit(X_train, y_train)
            fit_time = time() - start
            
            # predict and save results
            y = pipe.predict(X_test)
            res[name].append([
                fit_time,
                f1_score(y_test, y, average = 'micro'),
                precision_score(y_test, y, average = 'micro'),
                recall_score(y_test, y, average = 'micro')
])
    return res

def print_table(res):
    # Compute mean and std
    final = {}
    for model in res:
        arr = np.array(res[model])
        final[model] = {
            "time" : arr[:, 0].mean().round(2),
            "f1_score": [arr[:,1].mean().round(5),arr[:,1].std().round(5)],
            "Precision": arr[: 2].mean().round(5).round(5),
            "Recall": arr[: 3].mean().round(5).round(5)
                    }

    df = pd.DataFrame.from_dict(final, orient="index").round(3)
    return df