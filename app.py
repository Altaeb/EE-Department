import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from database.models import setup_db, Sheet, Subject
from auth.auth import AuthError, requires_auth


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    
    # End points
    @app.route('/')
    def welcome():
        return "welcome to EE-Department"

    @app.route('/sheets')
    @requires_auth('get:sheets')
    def get_sheets(payload):
        selection = Sheet.query.order_by(Sheet.id).all()
        sheets = [sheet.format() for sheet in selection]

        return jsonify({
            'success': True,
            'sheets': sheets,
            'totalSheets': len(Sheet.query.all())
        })

    @app.route('/sheets/<int:sheet_id>', methods=['DELETE'])
    @requires_auth('delete:sheets')
    def delete_sheet(payload, sheet_id):
        sheet = Sheet.query.filter(Sheet.id == sheet_id).one_or_none()
        
        if sheet is None:
            abort(404)

        try:
            sheet.delete()
            selection = Sheet.query.order_by(Sheet.id).all()
            sheets = [sheet.format() for sheet in selection]

            return jsonify({
                'success': True,
                'deleted': int(sheet_id),
                'sheets': sheets,
                'totalSheets': len(Sheet.query.all())
            })

        except:
            abort(422)

    @app.route('/sheets', methods=['POST'])
    @requires_auth('post:sheets')
    def create_sheet(payload):
        body = request.get_json()
        title = body.get('title', None)
        release_date = body.get('release_date', None)

        try:
            sheet = Sheet(
                title=title,
                release_date=release_date,
                )

            sheet.insert()
            selection = Sheet.query.order_by(Sheet.id).all()
            sheets = [sheet.format() for sheet in selection]

            return jsonify({
                'success': True,
                'created': sheet.id,
                'sheets': sheets,
                'totalSheets': len(Sheet.query.all())
            })

        except:
            abort(422)

    @app.route('/sheets/<int:sheet_id>', methods=['PATCH'])
    @requires_auth('patch:sheets')
    def update_sheet(payload, sheet_id):
        sheet = Sheet.query.filter(Sheet.id == sheet_id).one_or_none()
        if sheet is None:
            abort(404)

        try:
            body = request.get_json()
            title = body.get('title', None)
            release_date = body.get('release_date', None)

            sheet.title = title
            sheet.release_date = release_date
            selection = Sheet.query.order_by(Sheet.id).all()
            sheets = [sheet.format() for sheet in selection]

            return jsonify({
                'success': True,
                'updated': sheet.id,
                'sheets': sheets,
                'totalSheets': len(Sheet.query.all())
            })

        except:
            abort(422)

    @app.route('/subjects')
    @requires_auth('get:subjects')
    def get_subjects(payload):
        selection = Subject.query.order_by(Subject.id).all()
        subjects = [subject.format() for subject in selection]

        return jsonify({
            'success': True,
            'subjects': subjects,
            'totalSubjects': len(Subject.query.all())
        })

    @app.route('/subjects/<int:subject_id>', methods=['DELETE'])
    @requires_auth('delete:subjects')
    def delete_subject(payload, subject_id):
        subject = Subject.query.filter(Subject.id == subject_id).one_or_none()
        
        if subject is None:
            abort(404)

        try:
            subject.delete()
            selection = Subject.query.order_by(Subject.id).all()
            subjects = [subject.format() for subject in selection]

            return jsonify({
                'success': True,
                'deleted': subject_id,
                'subjects': subjects,
                'totalSubjects': len(Subject.query.all())
            })

        except:
            abort(422)

    @app.route('/subjects', methods=['POST'])
    @requires_auth('post:subjects')
    def create_subject(payload):
        body = request.get_json()
        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)

        try:
            subject = Subject(
                name=name,
                age=age,
                gender=gender
                )

            subject.insert()
            selection = Subject.query.order_by(Subject.id).all()
            subjects = [subject.format() for subject in selection]

            return jsonify({
                'success': True,
                'created': subject.id,
                'subjects': subjects,
                'totalSubjects': len(Subject.query.all())
            })

        except:
            abort(422)

    @app.route('/subjects/<int:subject_id>', methods=['PATCH'])
    @requires_auth('patch:subjects')
    def update_subject(payload, subject_id):
        subject = Subject.query.filter(Subject.id == subject_id).one_or_none()
        if subject is None:
            abort(404)

        try:
            body = request.get_json()
            name = body.get('name', None)
            age = body.get('age', None)
            gender = body.get('gender', None)

            subject.name = name
            subject.age = age
            subject.gender = gender

            selection = Subject.query.order_by(Subject.id).all()
            subjects = [subject.format() for subject in selection]

            return jsonify({
                'success': True,
                'updated': subject.id,
                'subjects': subjects,
                'totalSubjects': len(Subject.query.all())
            })

        except:
            abort(422)

    # Error Handling
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
                        "success": False,
                        "error": 422,
                        "message": "unprocessable"
                        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
                        "success": False,
                        "error": 404,
                        "message": "resource not found"
                        }), 404


    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
                        "success": False,
                        "error": AuthError,
                        "message": "resource not found"
                        }), AuthError
        

    return app

app = create_app()

if __name__ == '__main__':
    app.run()