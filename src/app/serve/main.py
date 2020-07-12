# -*- coding: utf-8 -*-
import logging
import tensorflow as tf

from transformers import TFBertForQuestionAnswering
from transformers import BertTokenizer


class BertQAModel:
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info('Initializing model.')

        self.model, self.tokenizer = self.init_bert()

    def init_bert(self):
        """ Runs data processing scripts to turn raw data from (../raw) into
            cleaned data ready to be analyzed (saved in ../processed).
        """
        self.logger = logging.getLogger(__name__)
        self.logger.info('Initializing BERT model and tokenizer.')

        tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
        model = TFBertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

        return model, tokenizer

    def transform_input_data(self, question, answer_text):
        """Tokenizes the input question text and contextual answer text into a dictionary
           containing token_ids, an attention mask and token type IDs (see https://huggingface.co/transformers/glossary.html#model-inputs).
        """
        self.logger = logging.getLogger(__name__)
        self.logger.info('Transforming raw input data into tokenized input data.')

        input_dict = self.tokenizer(question, answer_text, return_tensors='tf')
        return input_dict

    def run_inference(self, input_dict):
        """Runs inference on the model using the input data, and returns a
           human-readable answer.
        """
        self.logger = logging.getLogger(__name__)
        self.logger.info('Running inference on the model and returning human-readable answer.')

        start_scores, end_scores = self.model(input_dict)
        all_tokens = self.tokenizer.convert_ids_to_tokens(input_dict["input_ids"].numpy()[0])
        answer_string = ' '.join(all_tokens[tf.math.argmax(start_scores, 1)[0]: tf.math.argmax(end_scores, 1)[0] + 1])
        # Combine sub-word tokens into one and remove unnecessary spaces
        answer_string = answer_string.replace(" ##", "")
        answer_string = answer_string.replace(" , ", ", ")
        answer_string = answer_string.replace(" . ", ".")
        return answer_string


if __name__ == '__main__':
    """This main() function is purely here for demonstrational purposes, and can be used
       to show a usual workflow for the codebase. 
    """

    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    logger = logging.getLogger(__name__)

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
    logger.info(f'Answer: {answer}')

