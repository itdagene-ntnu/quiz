# itdagene-quiz

Quiz app for itDAGENE. Segregated from the main project since 2014.

## Getting set up

### Dependencies

* Virtualenv
* bower
* Grunt
* PostgreSQL

#### Clone the repo

    $ git clone https://github.com/itdagene-ntnu/quiz.git

#### Set up a virtual environment

    $ cd quiz
    $ virtualenv venv
    $ source venv/bin/activate

#### Run make-target setup

    $ make setup

Before you do this step, you should have a look at the
[`quiz/settings/local.py.example`](https://github.com/itdagene-ntnu/quiz/blob/master/quiz/settings/local.py.example)
file to ensure that the database settings correspond with your local setup.

If everything went according to plan, you can now start the development server
with `make run`.
