from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity,jwt_required
from courses.models import Course,User
from courses import api

#The student's Courses        
class Mycourses(Resource):
    @jwt_required(refresh=False)
    def get(self):
        user_name = get_jwt_identity()
        user = User.query.filter_by(name = user_name).first()
        mycourses = user.enrolling
        course_list = []
        for course in mycourses:
            img ='./static/img/'+course.img
            course_data = {"id":course.id,
                            "title":course.title,
                            "img":img,
                           }
            course_list.append(course_data)
       
        
        return {"courses": course_list},200        
                       

#students enroled in a course
class Registereduser(Resource):
    def get(self,title):
        course_title =title
        course = Course.query.filter_by(title = course_title).first()
        registered_user = course.enrolled
        user_info = []
        for user in registered_user:
            user_data = {"name"  :user.name,
                         "email" :user.email,
                         "phone" :user.phone,
                         "course_title":title
                        }
            user_info.append(user_data)
        
        return {"users":  user_info},200        
    
api.add_resource(Mycourses,'/mycourses')   
api.add_resource(Registereduser,'/showstudents/<title>') 

      


             
                                                                                                                                                                                                        


