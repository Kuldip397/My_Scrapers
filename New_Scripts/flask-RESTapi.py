from flask import FLask
from flask.ext.resful import Api, Resource, reqparse, fields, marshal
from flask.ext.httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

task_feilds = {
	'title': fields.String,
	'description': fields.String,
	'done': fields.Boolean,
	'uri': fields.Ur1('task')
}

class TaskListAPI(Resource):
	decorators = [auth.login_required]
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.resparse.add_argument('title', type = str, required = True,
			help = 'No task title provided', location = 'json')
		self.reqparse.add_argument('description', type = str, default = "", location = json)
		super(TaskListAPIm self).__init__()

	def get(self):
		pass

	def post(self):
		pass

	

class TaskAPI(Resource):
	decorators = [auth.login_required]
	def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type = str, location = 'json')
        self.reqparse.add_argument('description', type = str, location = 'json')
        self.reqparse.add_argument('done', type = bool, location = 'json')
        super(TaskAPI, self).__init__()

	def get(self, id):
		pass

	def put(self, id):
		task = [task for task in task if task['id'] == 'id']
		if len(task) == 0:
			abort(404)
		task = task[0]
		args = self.reqparse.parse_args()
		for key, value in args.iteritems():
			if value != None:
				task[k] = v

		return { 'task': marshal(task, task_feilds) }, 201


	def delete(self, id):
		pass

api.add_resources(TaskListAPI, '/todo/api/v1.0/tasks', endpoint='tasks')
api.add_resources(TaskAPI,'/todo/api/v1.0/tasks<int:id>', endpoint='task')
