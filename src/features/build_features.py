import click
import logging


class Tokenizer:
    pass


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main():


    # TODO: remove irrelevant characters (i.e. non-alphanumeric) & convert lowercase

    # TODO: tokenize by separating into separate words  (word2vec?)

    # TODO: lemmatize using common tool 

    # TODO: how to input into model? one sentence from context & one question at a time? 
    # or whole context and a question at a time? Look at SageMaker proj for solution?
    # --> sentence piece tokenization (inspired on the `run_squad_v2.py` script in the ALBERT repo).



if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
