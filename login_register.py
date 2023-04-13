from flask import jsonify,make_response,request
from flask_restful import Resource
import uuid
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import create_access_token
from courses.models import User
from courses import db,api



# Register user    
class CrateUser(Resource):
    def post(self):  
        check_name = User.query.filter_by(name = request.json['name']).first()
        if request.json['name']=="" or request.json['email']=="" or request.json['password']=="" or request.json['password']=="":
            return make_response('Please check your inputs',404)
        else:
            if check_name is None:
                hased_password  = generate_password_hash(request.json['password'],method='sha256') 
                new_user = User(id = str(uuid.uuid4()),
                                name = request.json['name'],
                                email = request.json['email'],
                                phone = request.json['phone'],
                                password  = hased_password,
                                
                                )
                db.session.add(new_user)
                db.session.commit()
                return make_response("Registration succeeded",200)
            else:
                return make_response(f"Name ({request.json['name']}) already exist please change name",404)


# Login                
class Login(Resource):
    def post(self):
        check_name = User.query.filter_by(name = request.json['name']).first()
        if request.json['name']==""  or request.json['password']=="":
                return make_response('Please check your inputs',404)
        else:
            if check_name is None:
                return make_response("Please check your name or password ",404)
            else:
                check_password = check_name.password
                if check_password_hash(f"{check_password}",f"{request.json['password']}"):
                    access_token = create_access_token(identity=request.json['name'])
                    img ='./static/img/'+check_name.img
                    return make_response(jsonify({'token':access_token,'text_name':check_name.name,'photo':img,'email':check_name.email,'phone':check_name.phone}))
                else:
                    return make_response("Please check your name or password ",404)
                
                
api.add_resource(CrateUser,'/newuser')                 
api.add_resource(Login,'/login')                  