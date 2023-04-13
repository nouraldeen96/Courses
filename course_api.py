from flask import jsonify,make_response,request
from flask_restful import Resource
from courses.models import Course,Teacher
from courses import db,save_imge,api


########## Courses ###########           
# Get All Courses
class GetCourse(Resource):
    def get(self):
        courses = Course.query.all()
        course_list = []
        for course in courses:
            img ='./static/img/'+course.img
            course_data = {"id":course.id,
                            "title":course.title,
                            "description":course.description,
                           "week":course.week,
                           "hours_week":course.hours_week,
                           "cost":course.cost,
                           "subject":course.subject,
                           "level":course.level,
                           "prerequisites":course.prerequisites,
                           "language":course.language,
                           "what_learn":course.what_learn,
                           "img":img,
                           }
            course_list.append(course_data)
        return {"courses": course_list},200
    
# Get Course By Title    
class GetCourseByTitle(Resource):
    def get(self,title):
        course = Course.query.filter_by(title = title).first()
        img ='./static/img/'+course.img
        if course is None:
            return {'error':'Not found'},404
        else:
            return jsonify({
                            "id":course.id,
                            "title":course.title,
                            "description":course.description,
                            "week":course.week,
                            "hours_week":course.hours_week,
                            "cost":course.cost,
                            "subject":course.subject,
                            "level":course.level,
                            "prerequisites":course.prerequisites,
                            "language":course.language,
                            "what_learn":course.what_learn,
                            "img":img,
                        })

# Add New Course    
class AddCourse (Resource):
    def post(self): 
     
        teacher1 = request.form.getlist("teacher1")
        course_title = request.form.get('title')
        teachers =teacher1[0].split(",")
        course = Course(title =request.form.get('title'),
                        description = request.form.get('description'),
                        week =request.form.get('week'),
                        hours_week = request.form.get('hours_week'),
                        cost = request.form.get('cost'),
                        subject = request.form.get('subject'),
                        level = request.form.get('level'),
                        prerequisites= request.form.get('prerequisites'),
                        language = request.form.get('language'),
                        what_learn = request.form.get('what_learn'),
                        img = save_imge(request.files.get("img"),'default_course.jpg')
                        )
        if course.title=="" or course.description== "" or course.week=="":
            return make_response("Please fill all data",404)
        else:
            db.session.add(course)
            db.session.commit()
        if teachers[0] != "":
            for teacher_name in  teachers :
                teacher = Teacher.query.filter_by(name = teacher_name).first()
                course = Course.query.filter_by(title = course_title).first()
                teacher.studying.append(course) 
                db.session.commit()
                  
            
            
        return make_response(jsonify({"id":course.id,
                    "title":course.title,
                    "description":course.description,
                    "week":course.week,
                    "hours_week":course.hours_week,
                    "cost":course.cost,
                    "subject":course.subject,
                    "level":course.level,
                    "prerequisites":course.prerequisites,
                    "language":course.language,
                    "what_learn":course.what_learn,
                    "img":course.img}),200)
    
       

# Update Course
class UpdateCourse (Resource):        
    def put(self,title):  
        course = Course.query.filter_by(title = title).first()
        teacher1 = request.form.getlist("teacher1")
        teachers =teacher1[0].split(",")
        img1 = course.img
        course.title =request.form.get('title')
        course.description = request.form.get('description')
        course.week =request.form.get('week')
        course.hours_week = request.form.get('hours_week')
        course.cost = request.form.get('cost')
        course.subject = request.form.get('subject')
        course.level = request.form.get('level')
        course.prerequisites= request.form.get('prerequisites')
        course.language = request.form.get('language')
        course.what_learn = request.form.get('what_learn')
        if request.files.get("img")== None:
            course.img = img1
        else:    
            course.img = save_imge(request.files.get("img"),'default_course.jpg')
            
        getoldteachers = course.teachers
        oldteachers=[]
        for i in getoldteachers:
              oldteachers.append(i.name)    
            
        if teachers[0] != "":
            if len(oldteachers)== 0 :
                for teacher_name in  teachers :
                    teacher = Teacher.query.filter_by(name = teacher_name).first()
                    teacher.studying.append(course) 
                    db.session.commit()
            else:
                for i in teachers:
                    for j in oldteachers:
                        if i==j:
                            teachers.remove(i)
                            oldteachers.remove(i)
            
            if len(teachers) > 0:                
                for teacher_name in  teachers :
                        teacher = Teacher.query.filter_by(name = teacher_name).first()
                        teacher.studying.append(course) 
                        db.session.commit()
            
            if len(oldteachers) > 0:
                for teacher_name in  oldteachers :
                    teacher = Teacher.query.filter_by(name = teacher_name).first()
                    teacher.studying.remove(course) 
                    db.session.commit() 
           
        
        db.session.commit()
        return 'Update',200
       
# Delete Course
class DeleteCourse (Resource):        
    def put(self,title):  
        course = Course.query.filter_by(title = title).first()
        check_users = course.enrolled
        # check_teachers = course.teachers
        
        
        
        
        if len(check_users) > 0:
            return make_response('You cannot delete because there are registered students',404)
        
        else:
            db.session.delete(course)
            db.session.commit()
            return f'{title} is Delete',200




api.add_resource(GetCourse,'/allcourses')            
api.add_resource(GetCourseByTitle,'/getcoursebytitle/<title>')            
api.add_resource(AddCourse,'/add')            
api.add_resource(UpdateCourse,'/update/<title>')            
api.add_resource(DeleteCourse,'/delete/<title>') 