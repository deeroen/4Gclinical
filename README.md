# Challenge 4G clinical

This is a python (>3.8) application providing a solution to the test provided by 4G clinical.
This app involves a minimal frontend. The app was developed using Flask, and the 
documentation was tested using doctest.

### Directory layout

    .
    ├── app.py                  # The Flask app
    ├── requirements.txt        # Packages used
    ├── script                   # Classe(s) and useful functions
        └── phone.py            
        └── solver.py  
    ├── Dockerfile     
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

The app will then be running on [http://localhost:80/](http://localhost:8080/)


## Deploy with Docker

    docker build -t python-4gc .

    docker run  -p 80:80 python-4gc
