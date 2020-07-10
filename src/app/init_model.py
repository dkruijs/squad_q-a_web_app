# -*- coding: utf-8 -*-
import logging

from transformers import TFBertForQuestionAnswering
from transformers import BertTokenizer


def init_BERT():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('Initializing BERT model and tokenizer.')

    tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
    model = TFBertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

    return model, tokenizer

