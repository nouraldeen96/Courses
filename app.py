from courses import app
from courses.user_api import * 
from courses.course_api import * 
from courses.teacher_api import * 
from courses.user_and_course_api import * 
from courses.login_register import * 
from courses.enroll import * 

if __name__ == '__main__':
    app.run(debug=True,port=3300)
    
 
    
    

   