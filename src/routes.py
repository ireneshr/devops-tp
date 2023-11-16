from flask import Flask, jsonify, request, abort, render_template
from db import empDB
from ddtrace import tracer
import logging

tracer.configure(
    hostname='datadog-agent',
    port=8126,
)

app = Flask(__name__)

@app.route('/employee', methods=['GET'])
@tracer.wrap(service="all_employees")
def getAllEmp():
    logging.info('employees.all')
    return jsonify(empDB)

@app.route('/employee/<empId>', methods=['GET'])
@tracer.wrap(service="get_employee")
def getEmp(empId):
    employee = next((emp for emp in empDB if emp['id'] == empId), None)
    logging.info('employees.get')
    if employee:
        return render_template('employee.html', employee=employee)
    else:
        return abort(400, description='Empleado no encontrado')

@app.route('/employee/<empId>', methods=['PUT'])
@tracer.wrap(service="update_employee")
def updateEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]
    if 'name' in request.json :
        em[0]['name'] = request.json['name']
    if 'phone' in request.json:
        em[0]['phone'] = request.json['phone']
    logging.info('employee.updated')
    return jsonify(em[0])


@app.route('/employee', methods=['POST'])
@tracer.wrap(service="create_employee")
def createEmp():
    dat = {
    'id':request.json['id'],
    'name':request.json['name'],
    'phone':request.json['phone']
    }
    empDB.append(dat)
    logging.info('employee.created')
    return jsonify(dat)


@app.route('/employee/<empId>', methods=['DELETE'])
@tracer.wrap(service="delete_employee")
def deleteEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]
    if len(em) == 0:
        abort(404)
    empDB.remove(em[0])
    logging.info('employee.removed')
    return jsonify({'response':'Success'})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)