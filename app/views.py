from flask import jsonify

from app import app
from app.mock_data.students import student_data

@app.route("/api/students", methods=["GET"])
def getStudentsList():
    return jsonify(student_data), 200

@app.route("/api/students/<id>", methods=["GET"])
def getStudentDetail(id):
    return jsonify(next((item for item in student_data if item["id"] == int(id)), None)), 200