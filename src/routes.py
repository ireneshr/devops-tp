from flask import Flask, jsonify, request, abort, render_template
from db import empDB
import os

app = Flask(__name__)

@app.route('/employee', methods=['GET'])
def getAllEmp():
    return jsonify(empDB)

@app.route('/employee/<empId>', methods=['GET'])
def getEmp(empId):
    employee = next((emp for emp in empDB if emp['id'] == empId), None)

    if employee:
        return render_template('employee.html', employee=employee)
    else:
        return "Empleado no encontrado"

@app.route('/employee/<empId>', methods=['PUT'])
def updateEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]
    if 'name' in request.json :
        em[0]['name'] = request.json['name']
    if 'phone' in request.json:
        em[0]['phone'] = request.json['phone']
    return jsonify(em[0])


@app.route('/employee', methods=['POST'])
def createEmp():
    dat = {
    'id':request.json['id'],
    'name':request.json['name'],
    'phone':request.json['phone']
    }
    empDB.append(dat)
    return jsonify(dat)


@app.route('/employee/<empId>', methods=['DELETE'])
def deleteEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]
    if len(em) == 0:
        abort(404)
    empDB.remove(em[0])
    return jsonify({'response':'Success'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
