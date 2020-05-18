import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from database.models import db_drop_and_create_all, setup_db, Sheet, Subject
from auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

db_drop_and_create_all()

@app.route('/sheets')
@requires_auth('get:sheets')
def get_sheets(payload):
    selection = Sheet.query.order_by(Sheet.id).all()
    sheets = [sheet.format() for sheet in selection]
    
    return jsonify({
        'success': True,
        'sheets': sheets,
        'totalsheets': len(Sheet.query.all())
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
        sheets = [Sheet.format() for Sheet in selection]

        return jsonify({
            'success': True,
            'deleted': Sheet_id,
            'sheets': sheets,
            'totalsheets': len(Sheet.query.all())
        })

    except:
        abort(422)

@app.route('/sheets', methods=['POST'])
@requires_auth('post:Sheets')
def create_Sheet(payload):
    body = request.get_json()
    title = body.get('title', None)
    release_date = body.get('release_date', None)

    try:
        Sheet = Sheet(
            title=title,
            release_date=release_date,
            )

        Sheet.insert()
        selection = Sheet.query.order_by(Sheet.id).all()
        sheets = [Sheet.format() for Sheet in selection]

        return jsonify({
            'success': True,
            'created': Sheet.id,
            'sheets': sheets,
            'totalsheets': len(Sheet.query.all())
        })

    except:
        abort(422)

@app.route('/sheets/<int:Sheet_id>', methods=['PATCH'])
@requires_auth('patch:Sheets')
def update_Sheet(payload, Sheet_id):
    Sheet = Sheet.query.filter(Sheet.id == Sheet_id).one_or_none()
    if Sheet is None:
        abort(404)

    try:
        body = request.get_json()
        title = body.get('title', None)
        release_date = body.get('release_date', None)

        Sheet.title = title
        Sheet.release_date = release_date
        selection = Sheet.query.order_by(Sheet.id).all()
        sheets = [Sheet.format() for Sheet in selection]

        return jsonify({
            'success': True,
            'updated': Sheet.id,
            'sheets': sheets,
            'totalsheets': len(Sheet.query.all())
        })

    except:
        abort(422)

@app.route('/Subjects')
@requires_auth('get:Subjects')
def get_Subjects(payload):
    selection = Subject.query.order_by(Subject.id).all()
    Subjects = [Subject.format() for Subject in selection]

    return jsonify({
        'success': True,
        'Subjects': Subjects,
        'totalSubjects': len(Subject.query.all())
    })

@app.route('/Subjects/<int:Subject_id>', methods=['DELETE'])
@requires_auth('delete:Subjects')
def delete_Subject(payload, Subject_id):
    Subject = Subject.query.filter(Subject.id == Subject_id).one_or_none()

    if Subject is None:
        abort(404)

    try:
        Subject.delete()
        selection = Subject.query.order_by(Subject.id).all()
        Subjects = [Subject.format() for Subject in selection]

        return jsonify({
            'success': True,
            'deleted': Subject_id,
            'Subjects': Subjects,
            'totalSubjects': len(Subject.query.all())
        })

    except:
        abort(422)

@app.route('/Subjects', methods=['POST'])
@requires_auth('post:Subjects')
def create_Subject(payload):
    body = request.get_json()
    name = body.get('name', None)
    age = body.get('age', None)
    gender = body.get('gender', None)

    try:
        Subject = Subject(
            name=name,
            age=age,
            gender=gender
            )

        Subject.insert()
        selection = Subject.query.order_by(Subject.id).all()
        Subjects = [Subject.format() for Subject in selection]

        return jsonify({
            'success': True,
            'created': Subject.id,
            'Subjects': Subjects,
            'totalSubjects': len(Subject.query.all())
        })

    except:
        abort(422)

@app.route('/Subjects/<int:Subject_id>', methods=['PATCH'])
@requires_auth('patch:Subjects')
def update_Subject(payload, Subject_id):
    Subject = Subject.query.filter(Subject.id == Subject_id).one_or_none()
    if Subject is None:
        abort(404)

    try:
        body = request.get_json()
        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)

        Subject.name = name
        Subject.age = age
        Subject.gender = gender

        selection = Subject.query.order_by(Subject.id).all()
        Subjects = [Subject.format() for Subject in selection]

        return jsonify({
            'success': True,
            'updated': Subject.id,
            'Subjects': Subjects,
            'totalSubjects': len(Subject.query.all())
        })

    except:
        abort(422)

return app

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