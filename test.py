import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import Flask;
from flaskext.mysql import MySQL;
from flask import request, session;
import json;

app = Flask(__name__);

#초기 설정
app.secret_key = "secret"
login_manager = LoginManager()
mysql = MySQL();
login_serializer = URLSafeTimedSerializer(app.secret_key);
app.config['MYSQL_DATABASE_USER'] = 'secret';
app.config['MYSQL_DATABASE_PASSWORD'] = 'secret';
app.config['MYSQL_DATABASE_DB'] = 'secret';

login_manager.init_app(app);
mysql.init_app(app);

#DB관련 함수

#connectDB
#	mysql db 에 접근하여 cursor를 리턴한다.
#	접근할 db 명, 계정, 비밀번호는 위의 초기설정 부분에서 app.config로 정의
def connectDB():
	cursor = mysql.connect().cursor();
	return cursor;


#User 클래스와 관련 함수
class User(UserMixin):
	#User class
	#  Variables
	#    email : string (encoding UTF-8)
	#    password : string (encoding UTF-8, encrypted by using sha1)
	#    active, authenticate, anonymous : bool
	#    loginDate :  datetime (datetime.utcnow)
	def __init__(self, email, password):
		self.email = email.encode('utf8');
		self.password = password;
		
		if email == "":
			self.anonymous = True;
		else:
			self.anonymous = False;
		self.active = False;
		self.authenticate = False;
		self.loginDate = datetime.datetime.utcnow();

	def is_active(self):
		return self.active;
	def is_authenticated(self):
		return self.authenticate;
	def is_anonymous(self):
		return self.anonymous;
	def get_id(self):
		return self.email;
	def get_auth_token(self):
		userToken = [self.email,self.password];
		data = login_serializer.dumps(userToken);
		return data;
	@staticmethod
	def getUserFromDB(cursor,email):
		cursor.execute("select * from USER where email='"+email+"'");
		data = cursor.fetchone();
		if data != None:
			user = User(email,data[1]);
			user.active = True;
			user.authenticate = True;
			user.anonymous = False;
			return user;
		else:
			return None;

@login_manager.user_loader
def load_user(email):
	cursor = connectDB();
	return User.getUserFromDB(cursor,email);


@app.route('/setBookFirst', methods=['post'])

def setBookFirst():
	cursor = connectDB();
	cursor.execute("select name,author,cover_img from BOOKINFO where book_num='"+L0004+"'")

	result = [];

	colums = tuple([d[0] for d in cursor.description])

	for row in cursor:
		result.append(dict(zip(colums,row)))

	print(reuslt)

	return jason.dumps(result)


if __name__ == "__main__":
	app.run(debug=True, host='10.73.45.83', port=5012);