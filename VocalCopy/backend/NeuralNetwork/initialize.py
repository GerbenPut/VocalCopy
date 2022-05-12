from network import NeuralNetwork

class Settings:
    class Defaults:
        x_domain = (0, 3*10**4)
        layers = 1
        functions = []
        funnel_function = None

    def __init__(self):
        self.x_domain = Settings.Defaults.x_domain
        self.layers = Settings.Defaults.layers
        self.functions = Settings.Defaults.functions
        self.funnel_function = Settings.Defaults.funnel_function

class Prediction:
    def __init__(self, prediction: float):
        self.prediction = prediction

class BinaryClassificationPrediction(Prediction):
    def classify(self, threshold):
        return self.prediction > threshold

def initialize(settings: Settings):
    return NeuralNetwork(layers, x_domain, funnel_function, functions)