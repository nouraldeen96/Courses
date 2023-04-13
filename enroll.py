from flask import make_response,request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity,jwt_required
from courses.models import Course,User
from courses import db,api



########## Enroll ###########
class Checkenroll(Resource):
    @jwt_required(refresh=False)
    def post(self):
        course_id =request.json.get('course_id')
        user_name = get_jwt_identity()   
        user = User.query.filter_by(name = user_name).first()
        mycourses = user.enrolling
        course_list = []
        for course in mycourses:
            course_data = course.id
            course_list.append(course_data)
        if course_id in course_list:
            return {"status":"enroll"},200
        else:
            return {"status":"unenrolled"},200
        
        
class Enroll(Resource):
    @jwt_required(refresh=False)
    def post(self):
        course_id =request.json.get('course_id')
        user_name = get_jwt_identity()
        user = User.query.filter_by(name = user_name).first()
        course = Course.query.get(course_id)
        user.enrolling.append(course) 
        db.session.commit()
        
        return make_response('Successfully registered',200)

class Unenrolled(Resource):
    @jwt_required(refresh=False)
    def post(self):
        course_id =request.json.get('course_id')
        user_name = get_jwt_identity()                      
        user = User.query.filter_by(name = user_name).first()
        course = Course.query.get(course_id)
        user.enrolling.remove(course)
        db.session.commit()
        
        return make_response('Registration has been cancelled',200)


api.add_resource(Enroll,'/enroll')  
api.add_resource(Checkenroll,'/checkenroll')  
api.add_resource(Unenrolled,'/unenrolled') 