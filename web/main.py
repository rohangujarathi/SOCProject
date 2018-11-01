from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HumorDetector(Resource):
    def get(self, sentence):
        return {'flag': self.model(sentence)}
        
    def model(self, sentence):
        if 'joke' in sentence:
            return True
        else:
            return False
        
api.add_resource(HumorDetector, '/hm/<string:sentence>')

if __name__ == '__main__':
    app.run(debug=True)
