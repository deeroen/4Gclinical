# Challenge 4G clinical

This is an application providing a solution to the test provided by 4G clinical.
This app involves a minimal frontend. The app was developed using Flask, and the 
documentation was tested using doctest.

### A typical top-level directory layout

    .
    ├── app.py                  # The Flask app
    ├── requirements.txt        # Packages used
    ├── scipt                   # Classe(s) and usefull functions
        └── phone.py            
        └── solver.py           
    └── README.md

A flask application is contained within the `app.py` file.

### Within the script directory:
`solver.py` contains the functions used to find the solution to the challenge.

`phone.py` is a file used to define the PhoneNumber class. This class contains 
a method used to assess the validity of the phone number

## Install 

    pip install -r requirements.txt
    

## Run the app

    python app.py

## Use the app

The app will then be running on [http://localhost:8080/](http://localhost:8080/)


## Deploy with Docker

    docker build -t python-4gc .

    docker run python-4gc