from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/api/submit', methods=['POST'])
def submit_student_list():
    data = request.get_json()

    if 'students' not in data:
        return jsonify({
            'status': 'error',
            'message':'Lack in student information'
        }),400

    required_information = ['student_id', 'name', 'age', 'gender']
    students = data['students']
    for student in students:
        if type(student) is not dict:
            return jsonify({
                'status':'error',
                'message': 'Please check the input format'
            }),400
        for x in student:
            if x not in required_information:
                return jsonify({
                    'status' : 'error',
                    'message' : 'Please check if all input information is complete'
                }),400
        if not isinstance(student['age'], int) or student['age'] <= 0:
            return jsonify({
                'status':'error',
                'message': 'Age must be a positive integer'
            }),400
        if student['gender'] not in ['male', 'female']:
            return jsonify({
                'status': 'error',
                'message': 'Gender must be "male" or "female"'
            }), 400




    duplicate_students=[]
    seen_students=[]
    unchecked_students=[]

    for student in students:
        id_student = student['student_id']
        if id_student in seen_students:
            duplicate_students.append(student)
        else:
            unchecked_students.append(student)
            seen_students.append(id_student)

    checked_students = []
    for student in unchecked_students:
        if int(student['age']) <= 22:
            checked_students.append(student)
    response = {
    'status': 'success',
    'message': 'The list has been processed successfully',
    'total_students': len(checked_students),
    'duplicate_students': duplicate_students,
    'student_eligible_for_free_ticket': checked_students
    }
    return jsonify(response),200


if __name__ == '__main__':
    app.run(debug=True)
