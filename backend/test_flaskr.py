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
        self.app = create_app() 
        self.client = self.app.test_client
        self.database_name = "bookshelf_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('dina','dina','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        
        self.new_book = {
            'title': 'Anansi Boys',
            'author': 'Neil Gaiman',
            'rating': 5
        }
        #binds the app to the current context 
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all() 
            
    #Define the tearDown method, which is implemented after each test. It will run as long as setUp executes successfully, regardless of test success.
    def tearDown(self):
        """ Executed after each test """
        pass 
    
    #Define your tests. All should begin with "test_" and include a doc string about the purpose of the test. In defining the tests, you will need to:
    #1. Get the response by having the client make a request
    #2. Use self.assertEqual to check the status code and all other relevant operations.
    # def test_given_behavior(self):
    #     """Test ____________ """
    #     res = self.client().get('/')
    #     self.assertEqual(res.status_code, 200)
    
    
    # @TODO: Write at least two tests for each endpoint - one each for success and error behavior.
    #        You can feel free to write additional tests for nuanced functionality,
    #        Such as adding a book without a rating, etc. 
    #        Since there are four routes currently, you should have at least eight tests. 
    # Optional: Update the book information in setUp to make the test database your own! 
    
    # test retrive_books
    def test_get_paginated_books(self):
        res = self.client().get('/books')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_books'])
        self.assertTrue(len(data['books']))
    
    #test retrive books requesting beyon valid page
    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client().get('/books?page=1000')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')  
                  
    # @TODO: Write tests for search - at minimum two
    #        that check a response when there are results and when there are none
    
    # test the updata_book method 
    def test_update_book_rating(self):
        res = self.client().patch('/books/5', json={'rating':1})
        data = json.loads(res.data)
        book = Book.query.filter(Book.id == 5).one_or_none() 
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(book.format()['rating'], 1)
        
    #test the failed update 
    def test_400_for_failed_update(self):
        res = self.client().patch('/books/5')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')
      
    # test the delete method 
    def test_delete_book(self):
        res = self.client().delete('/books/1')
        data = json.loads(res.data)
        
        book = Book.query.filter(Book.id == 1).one_or_none()
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)
        self.assertTrue(len(data['books']))  
        self.assertTrue(data['total_books'])
        self.assertEqual(book,None)
    
    # Tes delete method with non exist book 
    def test_422_if_book_does_not_exist(self):
        res = self.client().delete('/books/1000')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'unprocessable')
        
    
#Run the test suite, by running python test_file_name.py from the command line.
if __name__ == "__main__":
    unittest.main()