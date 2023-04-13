from flask import jsonify,make_response,request
from flask_restful import Resource
from courses.models import Course,Teacher
from courses import db,save_imge,api



class AddTeacher(Resource):
    def post(self): 
        img1 = save_imge(request.files.get("img"),'default_user.png')
        
        teacher = Teacher(  name = request.form.get('name'),
                            email = request.form.get('email'),
                            phone = request.form.get('phone'),
                            description= request.form.get('description'),
                            img = img1
                            )
        if teacher.name == "" or teacher.email == "" or teacher.phone == "" or teacher.description == "" : 
            return  make_response("Please fill all data",404)
        else:
            db.session.add(teacher)
            db.session.commit()
            return make_response("Added",200)
        
            

class GetTeachers(Resource):
    def get(self):    
        teachers = Teacher.query.all()
        teacher_list = []
        for teacher in teachers:
            img ='./static/img/'+teacher.img
            teacher_data = {"id":teacher.id,
                            "name":teacher.name,
                            "email":teacher.email,
                            "phone":teacher.phone,
                            "description":teacher.description,
                            "img":img,
                        }  
            teacher_list.append(teacher_data)
        return {"teachers": teacher_list},200
class GetTeacherByName(Resource):
    def get(self,name):
        teacher = Teacher.query.filter_by(name = name).first()
        if teacher is None:
            return {"message":'No Teacher Found'},404
        else:
            img ='./static/img/'+teacher.img
            return jsonify({
                "id":teacher.id,
                "name":teacher.name,
                "email":teacher.email,
                "phone":teacher.phone,
                'description':teacher.description,
                "img":img
            })   
            
class CourseTeachers(Resource): 
 def get(self,title):
        course = Course.query.filter_by(title = title).first()
        teachers = course.teachers
        teachers_info = []
        for teacher in teachers:
            img ='./static/img/'+teacher.img
            teacher_info = {
                            "id":teacher.id,
                            "name":teacher.name,
                            'description':teacher.description,
                            "img":img
                           }
            teachers_info.append(teacher_info)
        
        return {"teachers": teachers_info},200 
    
class UpdateTeacher(Resource):      
    def put(self,name):  
        teacher = Teacher.query.filter_by(name = name).first()
        img1 = teacher.img
        teacher.name =request.form.get('name')
        teacher.email = request.form.get('email')
        teacher.phone =request.form.get('phone')
        teacher.description =request.form.get('description')
        if request.files.get("img")== None:
            teacher.img = img1
        else:    
            teacher.img = save_imge(request.files.get("img"),'default_user.png')
            
        db.session.commit()
        return make_response('Updated',200)
    
class DeleteTeacher(Resource):      
    def put(self,name):  
        teacher = Teacher.query.filter_by(name = name).first()
        db.session.delete(teacher)
        db.session.commit()
        return make_response('Deleted',200 )    
    
            
api.add_resource(AddTeacher,'/addteacher')  
api.add_resource(GetTeachers,'/getteachers')  
api.add_resource(GetTeacherByName,'/getteacherByname/<name>')  
api.add_resource(CourseTeachers,'/courseteacher/<title>')  
api.add_resource(UpdateTeacher,'/updateteacher/<name>')  
api.add_resource(DeleteTeacher,'/deleteteacher/<name>')  