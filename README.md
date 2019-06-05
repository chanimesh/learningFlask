# learningFlask
To create a virtual env run the following command

`python3 -m venv <virtualen_name>`


This has a virtual env for flask to activate use the following command

`. <virtualen_name>/bin/activate`


also to deactivate the virtual env 

`deactivate`

To run the application <br>
First export the application environment variable<br>
`export FLASK_APP=hello.py`

then

you can either use the flask command 
`flask run`

or python's -m switch with flask
`python -m flask run`


####To active debugger 
`export FLASK_ENV=development`<br>
`flask run`
