# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

import os
import json
import pandas


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath='../data/raw', output_filepath='../data/processed'):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    # TODO: fill in logger
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    in_file = os.path.join(input_filepath, "train-v2.0.json")
    with open(in_file) as f:
        train = json.load(f)

    import pprint 
    pp = pprint.PrettyPrinter()
    pp.pprint(train['data'][3])
    out_file = os.path.join(output_filepath, "test.json")
    with open(out_file, 'w+') as f:
        f.write(json.dumps(train['data'][3], indent=4))

    # TODO: decide on tabular? structure    

    # ---> more todos in features


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
