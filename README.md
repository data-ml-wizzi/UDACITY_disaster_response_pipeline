# Project "DISASTER RESPONSE PIPELINE"
This Project ist part of my "Data Science" Nanodegree on Udacity.

# Table of Contents

1. [Project Motivation](#motivation)
2. [Installations](#installations)
2. [Data](#data)
3. [File Descriptions](#files)
4. [Instructions](#instructions)
5. [Results](#results)
6. [Licensing](#licensing)


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
The Data was provided bith Appen (former Figure8). Their datasets include roughly 26k messages of disasters all around the world as well as their categorization. 

</br>
The following two CSV files are provided:

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



# Results <a name="results"></a>

# Licensing <a name="licensing"></a>



To run ETL pipeline that cleans data and stores in database
python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db


To run ML pipeline that trains classifier and saves
python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl