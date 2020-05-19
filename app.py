import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from database.models import setup_db, Sheet, Subject
from auth.auth import AuthError, requires_auth


#----------------------------------------------------------------------------#
#                                  App Setup
#----------------------------------------------------------------------------#
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
#----------------------------------------------------------------------------#
#                                  Endpoints
#----------------------------------------------------------------------------#
    @app.route('/')
    def welcome():
        return "welcome to EE-Department"

    @app.route('/sheets', methods=['GET'])
    @requires_auth('get:sheets')
    def get_sheets(payload):
        sheets = Sheet.query.all()

        if len(sheets) == 0:
            abort(404)

        data = []
        for sheet in sheets:
            sheets_data = {
                'title': sheet.title,
                'release date': sheet.release_date.isoformat()
                }
            data.append(sheets_data)

        result = {
                  'success': True,
                  'sheets': data
                  }
        return jsonify(result)


    @app.route('/sheets/<int:id>', methods=['DELETE'])
    @requires_auth('delete:sheets')
    def delete_sheet(payload, id):
        sheet = Sheet.query.filter_by(id=id).first()

        if sheet is None:
            abort(404)
        else:
            sheet.delete()
        return jsonify({
                      'success': True,
                      'deleted': id
                      })

    @app.route('/sheets', methods=['POST'])
    @requires_auth('post:sheets')
    def create_sheet(payload):
        body = request.get_json()
        try:
            title, release_date = body['title'], body['release_date']
            sheet = Sheet(title=title, release_date=release_date)
            sheet.insert()
            sheet_data = {
                'title': sheet.title,
                'release_date': sheet.release_date.isoformat()
                }
            return jsonify({
                'success': True,
                'new sheet added': sheet_data
                })
        except:
            abort(422)

    @app.route('/sheets/<int:id>', methods=['PATCH'])
    @requires_auth('patch:sheets')
    def update_sheet(payload, id):
        sheet = Sheet.query.filter_by(id=id).first()
        if sheet is None:
            abort(404)
        else:
            body = request.get_json()
            sheet.title = body['title']
            sheet.release_date = body['release_date']
            sheet.update()
            return jsonify({
                'success': True,
                'updated': id
                })

    @app.route('/subjects', methods=['GET'])
    @requires_auth('get:subjects')
    def get_subjects(payload):
        subjects = Subject.query.all()

        if len(subjects) == 0:
            abort(404)

        data = []
        for subject in subjects:
            subjects_data = {
                'name': subject.name,
                }
            data.append(subjects_data)

        result = {
              'success': True,
              'subjects': data
            }
        return jsonify(result)

    @app.route('/subjects/<int:id>', methods=['DELETE'])
    @requires_auth('delete:subjects')
    def delete_subject(payload, id):
        subject = Subject.query.filter_by(id=id).first()

        if subject is None:
            abort(404)
        else:
            subject.delete()
        return jsonify({
                      'success': True,
                      'deleted': id
                      })

    @app.route('/subjects', methods=['POST'])
    @requires_auth('post:subjects')
    def create_subject(payload):
        body = request.get_json()
        try:
            name = body['name']
            subject = Subject(name=name)
            subject.insert()
            subject_data = {
                'name': subject.name,
                }
            return jsonify({
                'success': True,
                'new subject added': subject_data
                })
        except:
            abort(422)

    @app.route('/subjects/<int:id>', methods=['PATCH'])
    @requires_auth('patch:subjects')
    def update_subject(payload, id):
        subject = Subject.query.filter_by(id=id).first()
        if subject is None:
            abort(404)
        else:
            body = request.get_json()
            subject.name = body['name']
            subject.update()
            return jsonify({
                'success': True,
                'updated': id
            })

#----------------------------------------------------------------------------#
#                                Error Handlers
#----------------------------------------------------------------------------#
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
                      "success": False,
                      "error": 422,
                      "message": "Unprocessable"
                      }), 422

    @app.errorhandler(404)
    def notfound(error):
        return jsonify({
                        "success": False,
                        "error": 404,
                        "message": "Not Found"
                        }), 404

    @app.errorhandler(405)
    def notallowed(error):
        return jsonify({
                        "success": False,
                        "error": 405,
                        "message": "Method Not Allowed"
                        }), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
          "success": False,
          "error": 500,
          "message": "Internal Server Error"
          }), 500

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
            }), 400

    @app.errorhandler(AuthError)
    def auth_error(errors):
        return jsonify({
            "success": False,
            "error": errors.status_code,
            "message": errors.error['description']
            }), errors.status_code
    return app

app = create_app()

if __name__ == '__main__':
    app.run()