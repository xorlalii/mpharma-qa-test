# mPharma QA Test

Test is written in Python 3.7 using selenium webdriver

## Install Pipenv

Follow link to install [pipenv](https://pypi.org/project/pipenv/)


## Install project dependencies

    pipenv install


## Run tests

### With HTML report

    pytest tests/ --html=report.html --self-contained-html


### With XML report

    pytest tests/ --junitxml=unit.xml


