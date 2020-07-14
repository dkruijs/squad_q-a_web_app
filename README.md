SQuAD Q&A web app
==============================

A deployable Q&A web app based on a version of Google's [BERT](https://github.com/google-research/bert) pretrained on the [SQuAD dataset](https://rajpurkar.github.io/SQuAD-explorer/), specifically [Huggingface transformers](https://huggingface.co/transformers/)' `TFBertForQuestionAnswering` model, for answering reading comprehension questions. This is my capstone project for the [Udacity Machine Learning Nanodegree](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t).

Problem statement
-----------------
The SQuAD dataset consists of 100,000 excerpts from high-quality Wikipedia articles ranging from celebrities to abstract concepts, combined with multiple reading comprehension questions per excerpt. It follows a structure such that the answers to the questions can be found in the excerpts as a span of text, either single or multiple words, entities or no:

![](https://rajpurkar.github.io/mlx/qa-and-squad/example-squad.png)
(image source: [blog by one of the dataset's maintainers on the reasoning behind and background of the SQuAD dataset](https://rajpurkar.github.io/mlx/qa-and-squad/))

My goal in this project is to create an end-to-end deep learning product based on Google's [BERT](https://github.com/google-research/bert) but not using the given pre-training scripts in Google's repo, only using the model artifacts and my own TensorFlow code. Of course, I do look at the ALBERT repo's code and other examples on the internet for conceptual inspiration, but I will cite all such influences via in-line comments.

The project being 'end-to-end' refers to an added goal that it (or an inference-ready trained production model setup) should be easily deployable right after cloning the repo, using docker or some other solution either locally or on a preferred cloud platform. 

Documentation
------------
_Coming soon_

Getting started
------------

**Running the web app**:

Build and run the docker images (run command in root folder) -- build will take a while the first time!
```
docker-compose up
```

Then open a browser window on your host to the address `localhost:80` to see the web app. When you first run the model (by entering a question and pressing the 'Submit' button) it will download some model artifacts, this will take a while too.

**Validating model results**

The module `src/validate/validate.py` can be used to validate model results relative to given SQuAD answers. 
```
python -m src.validate.validate
```

**Recreating the development environment**:

* Create a virtual environment and activate it: 
``` 
virtualenv -p python3.7 venv
source /venv/bin/activate
```
or, on Windows hosts (Git bash):
`source /venv/Scripts/activate`

* Once inside the virtual environment, install requirements: 
``` 
pip install -r requirements.txt
```

Requirements
------------
This project uses the following external Python libraries (see `requirements.txt`):

```
click==7.1.2
python-dateutil==2.8.1
pytz==2020.1
six==1.15.0
python-dotenv==0.13.0
tensorflow==2.2.0
scikit-learn==0.23.1
sentencepiece==0.1.91
Flask==1.1.2
Flask-RESTful==0.3.8
flask_cors
transformers==3.0.1
```

Sources consulted
-----------------
I consulted the following online sources to arrive at this code product: 

* [Deploy a servable BERT QA model using Tensorflow Serving](https://medium.com/@joyceye04/deploy-a-servable-bert-qa-model-using-tensorflow-serving-d848f9797d9)
* [Question answering with a fine-tuned BERT](https://mccormickml.com/2020/03/10/question-answering-with-a-fine-tuned-BERT/)
* [Serve models fast with Flask](https://medium.com/datalab-log/serve-models-fast-with-flask-371726521591)
* [Serve static files from docker via nginx](https://www.linkedin.com/pulse/serve-static-files-from-docker-via-nginx-basic-example-arun-kumar/)
* [Stack Overflow -- Nginx doesn't communicate with flask rest api](https://stackoverflow.com/questions/47739828/nginx-doesnt-communicate-with-flask-rest-api-docker)
* For the `index.html` file that contains the web app, I used the `index.html` file from the Nanodegree SageMaker notebooks as a base for the HTML structure (I replaced the JavaScript code entirely). 

License
------------
This project is copyright © 2020 Daan Kruijs. It is free software, and may be redistributed under the terms specified in the LICENSE file (GNU-GPLv3 license).


Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── notebooks          <- Jupyter notebooks for EDA and analysis. 
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    ├── docker-compose.yml <- The docker confiuguration. Start all with `docker-compose up`.
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module.
    │   │
    |   ├── app           <- Code for the deployment web app.
    │   │   ├── serve     <- Backend code for serving the model, called by the api.  
    │   │   ├── website   <- HTML file for the web app.
    │   │   ├── flask     <- Dockerfile for Flask.
    │   │   ├── nginx     <- Dockerfile and configuration for nginx. 
    │   │   └── api.py    <- Code for the API.
    │   │
    │   └── validate      <- Code for validating the model results.
    │   
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project structure based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
