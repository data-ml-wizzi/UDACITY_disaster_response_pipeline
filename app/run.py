# import packages
import json
import plotly
import pandas as pd
import re
from sqlalchemy import create_engine
import joblib
from plotly.graph_objs import Bar

# import nltk stuff
import nltk

nltk.download(['punkt','stopwords', 'wordnet', 'punkt_tab'])

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

# import flask stuff
from flask import Flask
from flask import render_template, request, jsonify


app = Flask(__name__)

def tokenize(text):
    
    #Normalize Text
    url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    detected_urls = re.findall(url_regex, text)
    for url in detected_urls:
        text = text.replace(url, "urlplaceholder")

    #Tokenize Text
    tokens = word_tokenize(text)

    #Remove Stopwords
    words = [t for t in tokens if t not in stopwords.words("english")]

    #Lemmatize
    clean_tokens = []
    for word in words:
        clean_tok = WordNetLemmatizer().lemmatize(word).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

# load data
engine = create_engine('sqlite:///data/DisasterResponse.db')
df = pd.read_sql_table('TAB_DR', engine)

# load model
model = joblib.load("models/classifier.pkl")


# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    # extract data needed for visuals
    # TODO: Below is an example - modify to extract data for your own visuals
    genre_counts = df.groupby('genre').count()['message']
    genre_names = list(genre_counts.index)

    # Message counts for ALL messages (categorical):
    cat =  df[df.columns[4:]] # select categories within DataFrame
    cat_counts = (cat.shape[0] * cat.mean()).sort_values(ascending=True)
    cat_names = list(cat_counts.index)  
    
    # Top five categories count
    top_cat_count = df.iloc[:,4:].sum().sort_values(ascending=False)[0:5]
    top_cat_names = list(top_cat_count.index)
    
    # create visuals
    # TODO: Below is an example - modify to create your own visuals
    graphs = [
        {
            'data': [
                Bar(
                    x=genre_names,
                    y=genre_counts
                )
            ],

            'layout': {
                'title': 'Distribution of Message Genres',
                'yaxis': {
                    'title': "Message Counts"
                },
                'xaxis': {
                    'title': "Genre"
                }
            }
        },
        {    'data': [
                Bar(
                    x=cat_counts,
                    y=cat_names,
                    orientation = 'h'
                )
            ],

            'layout': {
                'title': 'Message Category Distribution - ALL messages',
                'yaxis': {
                    'title': ""
                },
                'xaxis': {
                    'title': "Message Counts"
                }
            }
        },        
        {    'data': [
                Bar(
                    x=top_cat_names,
                    y=top_cat_count
                )
            ],

            'layout': {
                'title': 'Top FIVE Categories',
                'yaxis': {
                    'title': "Message Counts"
                },
                'xaxis': {
                    'title': "Category"
                }
            }
        } 
    
    ]
    
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(host='0.0.0.0', port=3000, debug=True)


if __name__ == '__main__':
    main()