from courses import db


user_course = db.Table('user_course',
                       db.Column('user_id',db.String(50),db.ForeignKey('user.id')),
                       db.Column('course_id',db.Integer,db.ForeignKey('course.id')))

teacher_course = db.Table('teacher_course',
                       db.Column('teacher_id',db.Integer,db.ForeignKey('teacher.id')),
                       db.Column('course_id',db.Integer,db.ForeignKey('course.id'))) 
   



class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    week = db.Column(db.String(80), nullable=False)
    hours_week = db.Column(db.String(80), nullable=False)
    cost = db.Column(db.String(80), nullable=False)
    subject = db.Column(db.String(80), nullable=False)
    level = db.Column(db.String(80), nullable=False)
    prerequisites = db.Column(db.String(80), nullable=False)
    language = db.Column(db.String(80), nullable=False)
    what_learn = db.Column(db.Text, nullable=False)
    img = db.Column(db.Text,unique = False,nullable = False,default='default_course.jpg')
    def __repr__(self):
        return f"{self.title}:[ {self.week},{self.hours_week},{self.cost},{self.subject},{self.prerequisites},{self.language},{self.what_learn}] "
    
class User(db.Model):
    id = db.Column(db.String(50), primary_key=True,unique = True)
    name = db.Column(db.String(50),nullable=False,unique=True) 
    email = db.Column(db.String(125),nullable=False)
    phone =  db.Column(db.String(20),nullable=False)  
    password = db.Column(db.String(80),nullable=False)
    img = db.Column(db.Text,unique = False,nullable = False,default='default_user.png')
    enrolling = db.relationship('Course',secondary = user_course,backref = 'enrolled')
    
    def __repr__(self):
        return f"{self.name}:[{self.email},{self.phone},{self.password}]"

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True,unique = True)
    name = db.Column(db.String(50),nullable=False,unique=True) 
    email = db.Column(db.String(125),nullable=False)
    phone =  db.Column(db.String(20),nullable=False)
    description = db.Column(db.Text, nullable=False)  
    img = db.Column(db.Text,unique = False,nullable = False,default='default_user.png')
    studying = db.relationship('Course',secondary = teacher_course,backref = 'teachers')
    
    def __repr__(self):
        return f"{self.name}:[{self.email},{self.phone},{self.img}]"
