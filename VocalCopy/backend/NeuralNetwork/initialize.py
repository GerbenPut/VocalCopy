from network import NeuralNetwork

class Settings:
    class Defaults:
        x_domain = (0, 3*10**4)
        layers = 1
        functions = []
        output_function = None

    def __init__(self):
        self.x_domain = Settings.Defaults.x_domain
        self.layers = Settings.Defaults.layers
        self.functions = Settings.Defaults.functions
        self.output_function = Settings.Defaults.output_function

class Prediction:
    def __init__(self, prediction: float):
        self.prediction = prediction

class BinaryClassificationPrediction(Prediction):
    def classify(self, threshold):
        return self.prediction > threshold

def initialize(settings: Settings):
    return NeuralNetwork(
        settings.layers, settings.x_domain, settings.funnel_function, settings.functions)