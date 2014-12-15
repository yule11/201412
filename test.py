import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import Flask;
from flaskext.mysql import MySQL;
from flask import request, session;
import json;

app = Flask(__name__);

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