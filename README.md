SQuAD Q&A web app
==============================

A deep learning-based model based on Google's [ALBERT](https://github.com/google-research/ALBERT) and trained on the [SQuAD dataset](https://rajpurkar.github.io/SQuAD-explorer/) for answering reading comprehension questions, deployable as a web app. This is my capstone project for the [Udacity Machine Learning Nanodegree](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t).

***Currently a work in progress!*** To check out a thorough project description and to get a feel for the scope of this project, check out the [capstone project proposal (PDF)](docs/Capstone_proposal.pdf) I wrote as part of the Nanodegree.


Documentation
------------
_Coming soon_

Getting started
------------
* Install `pipenv` and its dependency `pyenv`: 
``` 
pip install pipenv pyenv
```
* Install all requirements in the Pipfile into a new pipenv virtual environment (please execute this command in the folder containing the Pipfile):
```
pipenv install 
```

**Note**: The virtual environment management is based on pipenv; this means you can both install this package in its development version (in order to extend it for your own uses) and its non-development version (in order to simply run/use it). Use `pipenv install` for the non-development version, `pipenv install --dev` for the development version.


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
