# -*- coding: utf-8 -*-
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import tensorflow as tf

from transformers import TFBertForQuestionAnswering
from transformers import BertTokenizer


# TODO error catching, logging
# TODO all todos
# TODO docstrings


class BertQAModel:
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    def __init__(self):
        # TODO: fill in logger
        logger = logging.getLogger(__name__)
        logger.info('Initializing model.')

        self.model, self.tokenizer = self.init_bert()

    @staticmethod
    def init_bert():
        """ Runs data processing scripts to turn raw data from (../raw) into
            cleaned data ready to be analyzed (saved in ../processed).
        """
        logger = logging.getLogger(__name__)
        logger.info('Initializing BERT model and tokenizer.')

        tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
        model = TFBertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

        return model, tokenizer

    def transform_input_data(self, question, answer_text):
        """Tokenizes the input question text and contextual answer text into a dictionary
           containing token_ids, an attention map and XXXXXXXXXXXXXXXXXXXXX
        """
        input_dict = self.tokenizer(question, answer_text, return_tensors='tf')
        return input_dict

    def run_inference(self, input_dict):
        """Runs inference on the model using the input data, and returns a
           human-readable answer.
        """
        start_scores, end_scores = self.model(input_dict)
        all_tokens = self.tokenizer.convert_ids_to_tokens(input_dict["input_ids"].numpy()[0])
        answer_string = ' '.join(all_tokens[tf.math.argmax(start_scores, 1)[0]: tf.math.argmax(end_scores, 1)[0] + 1])
        # Combine sub-word tokens into one
        answer_string = answer_string.replace(" ##", "")
        return answer_string


if __name__ == '__main__':

    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    bert = BertQAModel()

    question = "What happens to ice cream as its temperature increases?"
    answer_text = "Ice cream (derived from earlier iced cream or cream ice) is a sweetened frozen \
    food typically eaten as a snack or dessert. It may be made from dairy milk or cream and is flavoured \
    with a sweetener, either sugar or an alternative, and any spice, such as cocoa or vanilla. \
    Colourings are usually added, in addition to stabilizers. The mixture is stirred to incorporate \
    air spaces and cooled below the freezing point of water to prevent detectable ice crystals from \
    forming. The result is a smooth, semi-solid foam that is solid at very low temperatures (below \
    2 °C or 35 °F). It becomes more malleable as its temperature increases."

    input_data = bert.transform_input_data(question=question, answer_text=answer_text)

    answer = bert.run_inference(input_data)

    print(answer)
