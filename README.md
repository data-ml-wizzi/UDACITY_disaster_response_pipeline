# Project "DISASTER RESPONSE PIPELINE"
This Project ist part of my "Data Science" Nanodegree on Udacity.

# Table of Contents

1. [Project Motivation](#motivation)
2. [Installations](#installations)
2. [Data](#data)
3. [File Descriptions](#files)
4. [Instructions](#instructions)
5. [Results](#results)


# Project Motivation <a name="motivation"></a>
As part of the "Data Science" Nanodegree on Udacity we shall show our skills with creating an ETL Pipeline, attach an ML Pipeline, make the tool usable via an flask frontend and also make it available on GitHub.

During a Disaster usually time and human ressources are a critical ressource. So a keyword search on thousands of messages to filter out the right ones is not practical. Therefore the goal of this specific project ist to optimize the process of message processing and forwarding, so the right information gets to the right recipient fast in order to activate the right countermeassures.

To achieve this first NLP (Natural Language Processing) has to be used to preprocess the text data in order to train a machine learning algorithm for classifying the messages.

# Installations <a name="installations"></a>

<ul>
    <li>pandas          == 2.2.3
    <li>numpy           == 2.2.2
    <li>ipykernel       == 6.29.5
    <li>sqlalchemy      == 2.0.37
    <li>nltk            == 3.9.1
    <li>scikit-learn    == 1.6.1
    <li>plotly          == 5.24.1
    <li>flask           == 3.1.0
</ul>

# Data <a name="data"></a>
The Data was provided bith Appen (former Figure8). Their datasets include roughly 26k messages of disasters all around the world as well as their categorization. </br>

The following two CSV files are provided:</br>

<ul>
  <li>messages.csv: ~ 26k messages
  <li>categories.csv: 36 disaster categories 
</ul>

# File Descriptions <a name="files"></a>

```
app
 |--- templates
 |       |---go.html                    <- Classification results page of the web app
 |       |---master.html                <- Main page of the web app
 |--- run.py                            <- flask file that runs the app

 data
 |--- categories.csv                    <- 36 categories for the ~26k messages
 |--- messages.csv                      <- ~26k messages
 |--- DisasterResponse.db               <- SQL Database for storing the cleaned data
 |--- process_data.py                   <- script to process the data

 jupyter                                <- Juypter Notebooks with the ETL and ML Pipelines

 models
 |--- classifier.pkl                    <- saved model
 |--- train_classifier.py               <- script to train the classifier model
 ```

# Instructions <a name="instructions"></a>

1. Clone or download the repo, open the terminal and navigate to the project folder

2. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database</br>

        `python data/process_data.py data/messages.csv data/categories.csv data/DisasterResponse.db`

    - To run ML pipeline that trains classifier and saves</br>
        
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

3. Run your web app: `python app/run.py`

4. Click the `PREVIEW` button to open the homepage via http://loclhost:3000 or http://127.0.0.1:3000


# Results <a name="results"></a>
In the web app (Figure 1) the user can enter messages at the top, which are then classified based on the stored model. Below, various statistical evaluations of the training data are also shown:

- Distribution of all messages according to genres ('news', 'direct', 'social') that where used for the training of the model
- Distribution of all messages according to the 36 categories that where used for the training of the model
- Distribution of the top five categories for all messages that where used for the training of the model

<br>
    <div align="center">
	    <img src="https://github.com/data-ml-wizzi/UDACITY_disaster_response_pipeline/blob/main/app/app_screeni.png">
    </div>
    <div align="center">
	    <i>Figure 1 – Screenshot of the Web-App</i>
    </div>
<br>

