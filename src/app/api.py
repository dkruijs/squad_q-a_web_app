from flask import Flask, make_response, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import sys

from .serve.main import BertQAModel

app = Flask(__name__)
api = Api(app)

cors = CORS(app, resources={r"/": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


class BertApi(Resource):
    def __init__(self):
        """The first call of the API will initialize the BERT model in memory,
           speeding up subsequent inference calls.
        """
        self.bert = BertQAModel()

    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def post(self):
        """Performs inference on JSON-formatted question and answer data received in a
           POST-request's body.
        """
        webform_data = request.get_json(force=True)

        try:
            input_data = self.bert.transform_input_data(question=webform_data['question'],
                                                        answer_text=webform_data['answer_text'])
            answer = self.bert.run_inference(input_data)
            response = jsonify({"answer": answer})
            return make_response(response, 200)
        except:
            return make_response(f"Unexpected error during inference: {sys.exc_info()[0]}", 500)


api.add_resource(BertApi, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
