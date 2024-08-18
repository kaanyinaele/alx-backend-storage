This repository contains educational resources and exercises focused on understanding NoSQL databases, particularly MongoDB, and how to interact with them using Python. The project covers key concepts, including querying, inserting, updating, and deleting data in MongoDB.
Learning Objectives

By the end of this project, you should be able to explain the following concepts without external references:

    What NoSQL means and its differences from SQL
    The principles of ACID (Atomicity, Consistency, Isolation, Durability)
    What document storage is and the different types of NoSQL databases
    The benefits of using a NoSQL database
    How to query, insert, update, and delete information in a NoSQL database using MongoDB

Resources

The following resources are recommended to assist your learning:

    NoSQL Databases Explained
    What is NoSQL?
    MongoDB with Python Crash Course - Tutorial for Beginners
    MongoDB Tutorial 2: Insert, Update, Remove, Query
    Aggregation
    Introduction to MongoDB and Python
    mongo Shell Methods
    Mongosh

Requirements
MongoDB Command Files

    Files should be interpreted on Ubuntu 18.04 LTS using MongoDB version 4.2.
    Each file should start with a comment line // my comment and end with a newline.
    Ensure files are checked for length using wc.

Python Scripts

    Scripts should be compatible with Python 3.7 and PyMongo 3.10.
    Files must start with #!/usr/bin/env python3 and comply with pycodestyle guidelines (version 2.5.*).
    Include documentation for all modules and functions.
    Code should be executed only when run directly, not when imported.

Installation Instructions

To set up MongoDB 4.2 on Ubuntu 18.04, follow these commands:

bash

wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo service mongod start

Check if MongoDB is running:

bash

sudo service mongod status

To install the required Python package:

bash

pip3 install pymongo

This repository includes both MongoDB command files and Python scripts to provide hands-on experience with NoSQL databases.
