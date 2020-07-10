import click
import logging
import tensorflow as tf
from pathlib import Path
from dotenv import find_dotenv, load_dotenv


# todo refactor
max_seq_length = 384
batch_size = 16
albert_config_file = '../../models/raw/albert_base/albert_config.json'
with open(albert_config_file, "w") as f:
    run_config = f.read()
EXPORT_PATH = '../../models/trained/albert_untuned/2'

@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main():

    # Define input function for served model

    # This function is based on example from:
    # https://medium.com/@joyceye04/deploy-a-servable-bert-qa-model-using-tensorflow-serving-d848f9797d9
    def serving_input_receiver_fn():
        feature_spec = {
            "unique_ids": tf.FixedLenFeature([], tf.int64),
            "input_ids": tf.FixedLenFeature([max_seq_length], tf.int64),
            "input_mask": tf.FixedLenFeature([max_seq_length], tf.int64),
            "segment_ids": tf.FixedLenFeature([max_seq_length], tf.int64),
        }

        serialized_tf_example = tf.placeholder(dtype=tf.string,
                                               shape=[batch_size],
                                               name='input_example_tensor')
        receiver_tensors = {'examples': serialized_tf_example}
        features = tf.parse_example(serialized_tf_example, feature_spec)
        return tf.estimator.export.ServingInputReceiver(features, receiver_tensors)

    estimator = tf.contrib.tpu.TPUEstimator(
        use_tpu=False,
        model_fn=model_fn,
        config=run_config,
        train_batch_size=6,
        predict_batch_size=8)
    estimator._export_to_tpu = False  ## !!important to add this
    estimator.export_saved_model(
        export_dir_base=EXPORT_PATH,
        serving_input_receiver_fn=serving_input_receiver_fn)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()