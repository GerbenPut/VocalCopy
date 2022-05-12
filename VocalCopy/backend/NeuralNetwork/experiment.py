from initialize import Prediction, BinaryClassificationPrediction, initialize, Settings
import typing

def prepare(settings : Settings = Settings()):
    return initialize(settings)

def run_one(nn, inputs) -> BinaryClassificationPrediction:
    return BinaryClassificationPrediction(nn.propagate(inputs))

def run_all(nn, inputs) -> typing.List[BinaryClassificationPrediction]:
    return list(map(lambda input: run_one(nn, input), inputs))

def train(nn, samples):
    inputs = get_input(sampl)
    run_all(nn, inputs)

def test(nn, samples):
    run_all(nn, inputs)

def predict(nn, inputs):
    run_one(nn, inputs)