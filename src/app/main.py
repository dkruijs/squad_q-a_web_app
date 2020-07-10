# -*- coding: utf-8 -*-
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import tensorflow as tf

from .init_model import init_BERT

# TODO attribute all sources
# TODO object-oriented structure; make one class with a data transformer method and an infer method
# TODO embed in a simple web app, input-output
# TODO dockerize
# TODO check other requirements
# TODO clean up gitignore, other files 

# TODO turn into class
def main():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    # TODO: fill in logger
    logger = logging.getLogger(__name__)
    logger.info('Initializing model serving.')

    model, tokenizer = init_BERT()



    question = "Paris is the capital of France."
    answer_text = "Of which country is Paris the capital?"

    input_dict = tokenizer(question, answer_text, return_tensors='tf')
    start_scores, end_scores = model(input_dict)

    all_tokens = tokenizer.convert_ids_to_tokens(input_dict["input_ids"].numpy()[0])
    answer = ' '.join(all_tokens[tf.math.argmax(start_scores, 1)[0]: tf.math.argmax(end_scores, 1)[0] + 1])
    print("answer:")
    print(answer)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
