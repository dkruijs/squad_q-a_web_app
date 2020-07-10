from flask import Flask, make_response
from flask_restful import Resource, Api
import os
import glob

app = Flask(__name__)
api = Api(app)


def get_dataset(data_path):
    """Retrieves a CSV dataset from the given location, by taking the first CSV
       file found and returning its contents as a string.
    """
    try:
        os.chdir(data_path)
    except:
        return False
    filenames = glob.glob('*.csv')
    if len(filenames) == 0: 
        return False
    data = ""
    with open(filenames[0]) as f:
        data += f.read()
    return data

@app.route('/process_dataset')
def process_dataset():
    os.system("sh submit.sh")
    return make_response("Processing was completed.", 200)


@app.route('/force_reprocess_dataset')
def force_reprocess_dataset():
    spark_args = os.environ['SPARK_APPLICATION_ARGS'].split(" ")
    spark_args.append("reprocess") 
    os.environ['SPARK_APPLICATION_ARGS'] = " ".join(spark_args)
    try: 
        os.system("sh submit.sh")
    except:
        return make_response("Processing errored out.", 500)
    return make_response("Processing was completed.", 200)


@app.route('/force_calculate_heat_waves')
def force_calculate_heat_waves():
    spark_args = os.environ['SPARK_APPLICATION_ARGS'].split(" ")
    spark_args.append("calculate_heat_waves") 
    os.environ['SPARK_APPLICATION_ARGS'] = " ".join(spark_args)
    os.system("sh submit.sh")
    return make_response("Processing was completed.", 200)


@app.route('/retrieve_heat_waves')
def retrieve_heat_waves():
    data = get_dataset(os.path.join(os.environ['SPARK_APPLICATION_ARGS']\
        .split(' ')[2], "heat_waves.csv"))
    if data:
        response = make_response(data, 200)
        response.mimetype = "text/plain"
        return response
    else:
        response = make_response("No data was found.", 400)
        response.mimetype = "text/plain"
        return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')