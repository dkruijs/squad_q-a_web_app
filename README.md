SQuAD Q&A web app
==============================

A deep learning-based model based on Google's [ALBERT](https://github.com/google-research/ALBERT) and trained on the [SQuAD dataset](https://rajpurkar.github.io/SQuAD-explorer/) for answering reading comprehension questions, deployable as a web app. This is my capstone project for the [Udacity Machine Learning Nanodegree](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t).

***Currently a work in progress!*** To check out a thorough project description and to get a feel for the scope of this project, check out the [capstone project proposal (PDF)](docs/Capstone_proposal.pdf) I wrote as part of the Nanodegree.


**Sources**:
https://medium.com/@joyceye04/deploy-a-servable-bert-qa-model-using-tensorflow-serving-d848f9797d9
https://mccormickml.com/2020/03/10/question-answering-with-a-fine-tuned-BERT/
https://medium.com/datalab-log/serve-models-fast-with-flask-371726521591
https://www.linkedin.com/pulse/serve-static-files-from-docker-via-nginx-basic-example-arun-kumar/

Problem statement
-----------------
The SQuAD dataset consists of 100,000 excerpts from high-quality Wikipedia articles ranging from celebrities to abstract concepts, combined with multiple reading comprehension questions per excerpt. It follows a structure such that the answers to the questions can be found in the excerpts as a span of text, either single or multiple words, entities or no:

![](https://rajpurkar.github.io/mlx/qa-and-squad/example-squad.png)
(image source: [blog by one of the dataset's maintainers on the reasoning behind and background of the SQuAD dataset](https://rajpurkar.github.io/mlx/qa-and-squad/))

My goal in this project is to create an end-to-end deep learning product based on Google's [ALBERT](https://github.com/google-research/ALBERT) but not using the given pre-training scripts in Google's repo, only using the model artifacts and my own TensorFlow code. Of course, I do look at the ALBERT repo's code and other examples on the internet for conceptual inspiration, but I will cite all such influences via in-line comments.

The project being 'end-to-end' refers to an added goal that it (or an inference-ready trained production model setup) should be easily deployable right after cloning the repo, using docker or some other solution either locally or on a preferred cloud platform. 

Documentation
------------
_Coming soon_

Getting started
------------

**run**:

Build the docker image, then run it:
```
build --rm -t dkruijs/qa_bert .
docker run --name qa_bert 
```

misc
```
docker run --name qa_bert -d -p 8080:80 dkruijs/qa_bert
docker run -it --entrypoint /bin/bash dkruijs/qa_bert
```

Then open a browser window on your host to the address `localhost:8080` to see the web app.

**development**:

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
_Coming soon_

More information
------------
_Coming soon_

Contributing
------------
_Coming soon_

License
------------
This project is copyright © 2020 Daan Kruijs. It is free software, and may be redistributed under the terms specified in the LICENSE file (GNU-GPLv3 license).


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    |   ├── app           <- Code for the deployment web app
    │   │   └── ...
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
