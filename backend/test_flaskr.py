import os 
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from models import setup_db, Book 
from flaskr import create_app 

#Define the test case class for the application (or section of the application, for larger applications).

class BookTestCase(unittest.TestCase):
    #Define and implement the setUp function. It will be executed before each test and is where you should initialize the app and test client, as well as any other context your tests will need. The Flask library provides a test client for the application, accessed as shown below.
    def setUp(self):
        """Define test variables and initialize app."""
        self.client = app.test_client
        pass
    #Define the tearDown method, which is implemented after each test. It will run as long as setUp executes successfully, regardless of test success.
    def tearDown(self):
        """ Executed after each test """
        pass 
    
    #Define your tests. All should begin with "test_" and include a doc string about the purpose of the test. In defining the tests, you will need to:
    #1. Get the response by having the client make a request
    #2. Use self.assertEqual to check the status code and all other relevant operations.
    def test_given_behavior(self):
        """Test ____________ """
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)