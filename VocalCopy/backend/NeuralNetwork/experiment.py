from argparse import ArgumentError
from multiprocessing.sharedctypes import Value
from initialize import Prediction, BinaryClassificationPrediction, initialize, Settings
import typing
import sys

def prepare(settings : Settings = Settings()):
    return initialize(settings)

def run_one(nn, inputs) -> BinaryClassificationPrediction:
    return BinaryClassificationPrediction(nn.propagate(inputs))

def run_all(nn, inputs) -> typing.List[BinaryClassificationPrediction]:
    return list(map(lambda input: run_one(nn, input), inputs))

def train(nn, samples):
    run_all(nn, inputs)

def test(nn, samples):
    run_all(nn, inputs)

def predict(nn, inputs):
    run_one(nn, inputs)
    #TODO: parse the prediction

def main(settings : Settings = Settings()):
    nn = prepare(settings)
    #TODO: implement running samples

if __name__ == "__main__":
    if len(sys.argv) > 2:
        main(Settings(
            x_domain = sys.argv[1],
            layers = sys.argv[2],
            functions = sys.argv[3],
            output_function = sys.argv[4]
        ))
    else:
        # If you are not running using a launch configuration
        # nor command line arguments, define the desired settings here.
        # To use default settings, use "default" as a command line argument.
        my_x_domain = None
        my_layers = None
        my_functions = None
        my_output_function = None
        try:
            main(Settings(
                my_x_domain,
                my_layers,
                my_functions,
                my_output_function
            ))
        except ValueError :
            if sys.argv[1] == "default":
                main()
            else:
                raise ArgumentError()
