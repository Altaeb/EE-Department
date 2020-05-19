import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from app import create_app
from database.models import setup_db, Sheet, Subject

assistant_token = os.environ['ASSISTANT_TOKEN']
director_token = os.environ['DIRECTOR_TOKEN']
producer_token = os.environ['PRODUCER_TOKEN']


class EE_DepartmentTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ['TEST_DATABASE_URL']
        self.headers_assistant = {'Content-Type':'application/json', 'Authorization': assistant_token}
        self.headers_director = {'Content-Type':'application/json', 'Authorization': director_token}
        self.headers_producer = {'Content-Type':'application/json', 'Authorization': producer_token}
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            #create all tables
            self.db.create_all()
        self.new_subject = {
                        "name": "EE304",
                        }
        self.new_sheet = {
	                    "title": "Degital",
	                    "release_date": "09-05-2020"
                        }


    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_404_subjects_not_found_get_subjects(self):
        Subject.query.delete()
        res = self.client().get('/subjects', headers=self.headers_producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Not Found")


    def test_404_sheets_not_found_get_sheets(self):
        Sheet.query.delete()
        res = self.client().get('/sheets', headers=self.headers_producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Not Found")


    def test_get_subjects(self):
        self.client().post('/subjects', headers=self.headers_producer, json = self.new_subject)
        res = self.client().get('/subjects', headers=self.headers_producer)
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['subjects'])

    def test_get_sheets(self):
        self.client().post('/sheets', headers=self.headers_producer, json = self.new_sheet)
        res = self.client().get('/sheets', headers=self.headers_producer)
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['sheets'])

    def test_post_subjects(self):
        res = self.client().post('/subjects', headers=self.headers_producer, json = self.new_subject)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(len(data['new subject added']))

    def test_post_sheets(self):
        res = self.client().post('/sheets', headers=self.headers_producer, json = self.new_sheet)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(len(data['new sheet added']))


    def test_422_if_post_subjects_failed(self):
        res = self.client().post('/subjects',headers=self.headers_producer, json ={})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['message'], "Unprocessable")
        self.assertEqual(data['success'], False)

    def test_422_if_post_sheets_failed(self):
        res = self.client().post('/sheets',headers=self.headers_producer, json ={})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['message'], "Unprocessable")
        self.assertEqual(data['success'], False)

    def test_delete_subject(self):
        res = self.client().delete('/subjects/12', headers=self.headers_producer)
        data = json.loads(res.data)

        subject = Subject.query.filter(Subject.id == 12).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 12)
        self.assertEqual(subject, None)

    def test_delete_sheet(self):
        res = self.client().delete('/sheets/3', headers=self.headers_producer)
        data = json.loads(res.data)

        sheet = Sheet.query.filter(Sheet.id == 3).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 3)
        self.assertEqual(sheet, None)

    def test_404_if_subject_is_none(self):
        res = self.client().delete('/subjects/3', headers=self.headers_producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], "Not Found")
        self.assertEqual(data["success"], False)

    def test_404_if_sheet_is_none(self):
        res = self.client().delete('/sheets/3', headers=self.headers_producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], "Not Found")
        self.assertEqual(data["success"], False)

    def test_patch_subjects(self):
        res = self.client().patch('/subjects/13', headers=self.headers_producer, json = self.new_subject)
        data = json.loads(res.data)
        subject = Subject.query.filter(id==13).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['updated'], 13)

    def test_patch_sheets(self):
        res = self.client().patch('/sheets/4', headers=self.headers_producer, json = self.new_sheet)
        data = json.loads(res.data)
        sheet = Sheet.query.filter(id==3).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['updated'], 4)

    def test_404_if_subject_is_none_patch_subjects(self):
        res = self.client().patch('/subjects/1000', headers=self.headers_producer, json = self.new_subject)
        data = json.loads(res.data)
        subject = Subject.query.filter(id==1000).one_or_none()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Not Found")

    def test_404_if_sheet_is_none_patch_sheets(self):
        res = self.client().patch('/sheets/1000', headers=self.headers_producer, json = self.new_sheet)
        data = json.loads(res.data)
        sheet = Sheet.query.filter(id==1000).one_or_none()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Not Found")

    def test_patch_subject_not_permitted(self):
        res = self.client().delete('/subjects/15', headers=self.headers_assistant)
        data = json.loads(res.data)

        subject = Subject.query.filter(Subject.id == 15).one_or_none()
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permission not found")

    def test_post_subject_not_permitted(self):
        res = self.client().post('/subjects', headers=self.headers_assistant, json = self.new_subject)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permission not found")

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()