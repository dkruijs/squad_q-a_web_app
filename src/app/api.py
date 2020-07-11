from flask import Flask, make_response, request
from flask_restful import Resource, Api
import sys

from .serve.main import BertQAModel

app = Flask(__name__)
api = Api(app)


class BertApi(Resource):
    def __init__(self):
        """The first call of the API will initialize the BERT model in memory,
           speeding up subsequent inference calls.
        """
        self.bert = BertQAModel()

    def post(self):
        """Performs inference on JSON-formatted question and answer data received in a
           POST-request's body.
           :return:
        """
        data = request.get_json(force=True)
        try:
            input_data = self.bert.transform_input_data(question=data['question'], answer_text=data['answer_text'])
            answer = self.bert.run_inference(input_data)
        except:
            return make_response(f"Unexpected error during inference: {sys.exc_info()[0]}", 500)
        return make_response(answer, 200)


api.add_resource(BertApi, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
