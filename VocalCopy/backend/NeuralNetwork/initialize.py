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

    def __init__(self, x_domain, layers, functions, output_function):
        if None in (x_domain, layers, functions, output_function):
            raise ValueError("None is not a valid argument for Settings.__init__")
        self.x_domain = x_domain
        self.layers = layers
        self.functions = functions
        self.output_function = output_function

class Prediction:
    def __init__(self, prediction: float):
        self.prediction = prediction

class BinaryClassificationPrediction(Prediction):
    def classify(self, threshold):
        return self.prediction > threshold

def initialize(settings: Settings):
    return NeuralNetwork(
        settings.layers, settings.x_domain, settings.funnel_function, settings.functions)