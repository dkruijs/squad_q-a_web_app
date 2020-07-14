import sys
import logging
import pprint
import os
import json
import pandas as pd

from ..app.serve.main import BertQAModel


def load_data(in_path, in_file):
    in_file = os.path.join(in_path, in_file)
    with open(in_file) as f:
        data = json.load(f)
    return data


def validate(data, output_file_path, output_file_name, num_titles):
    """Performs inference on JSON-formatted question and answer data from the SQuAD dataset,
       registers the result and whether it matches the specified answer.
    """
    # initialize the model
    model = BertQAModel()
    # create a header row
    header = ["Title", "Question", "Answer", "y_true", "Prediction", "Match", "y_pred", "PartialMatch"]
    # initialize a variable to hold our data, with the header row to start
    out_df = pd.DataFrame(columns=header)

    # parse number of items up to `num_titles`
    for item in data['data'][0:num_titles]:
        for i in range(len(item['paragraphs'])):
            context = item['paragraphs'][i]['context']
            for q in item['paragraphs'][i]['qas']:

                try:
                    q['answers'][0]['text']
                # if we've run out of data, move to the next QA pair
                except IndexError:
                    continue

                # tokenize input data and run inference
                input_data = model.transform_input_data(question=q['question'], answer_text=context)
                answer = model.run_inference(input_data)

                # F1_1 `y_true` dummy value
                f1_1 = "1"

                line = [item['title'], q['question'], q['answers'][0]['text'].strip().lower(), f1_1, answer]

                # full match
                if q['answers'][0]['text'].strip().lower() == answer:
                    line.append("1")
                    line.append("1")  # y_true dummy
                else:
                    line.append("0")
                    line.append("0")  # y_pred dummy
                # partial match
                if q['answers'][0]['text'].strip().lower() in answer or \
                        answer in q['answers'][0]['text'].strip().lower():
                    line.append("1")
                else:
                    line.append("0")

                # append line to DF
                out_df.loc[len(out_df)] = line

    out_df.to_csv(os.path.join(output_file_path, output_file_name), index=False)


if __name__ == '__main__':
    """This script performs validation of the model by running the whole SQuAD dataset through it
        and recording the results.
        """

    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    logger = logging.getLogger(__name__)

    input_file_name = "dev-v2.0.json"
    input_file_path = "./data/raw"
    output_file_path = "./data/processed"
    output_file_name = "validate.csv"

    data = load_data(input_file_path, input_file_name)

    validate(data, output_file_path, output_file_name, num_titles=3)


