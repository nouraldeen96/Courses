from flask import jsonify,make_response,request
from flask_restful import Resource
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import get_jwt_identity,jwt_required
from courses.models import User
from courses import db,save_imge,api

########## Users ###########
# get all users
class GetUsers(Resource):
    def get(self):    
        users = User.query.all()
        user_list = []
        for user in users:
            user_data = {"id":user.id,
                        "name":user.name,
                        "email":user.email,
                        "phone":user.phone,
                        }  
            user_list.append(user_data)
        return {"Users": user_list},200

 

        

# Get User By Name        
class GetUserByName(Resource):
    def get(self,name):
        user = User.query.filter_by(name = name).first()
        if user is None:
            return {"message":'No User Found'},400
        else:
            return jsonify({
                "id":user.id,
                "name":user.name,
                "email":user.email,
                "phone":user.phone,
                "password":user.password
               
            })

                                
class UpdateUser (Resource):
    @jwt_required(refresh=False)       
    def put(self):  
        user_name = get_jwt_identity()
        user = User.query.filter_by(name = user_name).first()
        img1 = user.img
        if request.form.get('name')!="" and request.form.get('email')!= "" and request.form.get('phone') != "":
            user.name =request.form.get('name')
            user.email = request.form.get('email')
            user.phone =request.form.get('phone')
            if request.files.get("img")== None:
                user.img = img1
            else:    
                user.img = save_imge(request.files.get("img"),'default_user.png')
                
            db.session.commit()
            return make_response('Updated',200)    
        else:
               return make_response('Please fill all feilds',400)     
 
        
    
class UpdateUserPassword (Resource):
    @jwt_required(refresh=False)       
    def put(self):  
        user_name = get_jwt_identity()
        user = User.query.filter_by(name = user_name).first()
        check_password =  user.password
        if check_password_hash(f"{check_password}",f"{request.form.get('oldPassword')}"):
            hased_password  = generate_password_hash(request.form.get('newPassword'),method='sha256')
            user.password = hased_password 
            db.session.commit()
            return make_response('Updated password',200) 
        else:
            return make_response('Please check your old password',400)
        

            
              
api.add_resource(GetUsers,'/getusers')            

api.add_resource(GetUserByName,'/getuserByname/<name>')  

api.add_resource(UpdateUser,'/updateuser')  
api.add_resource(UpdateUserPassword,'/updateuserpassword')                