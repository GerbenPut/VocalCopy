import numpy as np
import math
import typing
from functions import functions as operations

class NeuralNetwork:
    __param_generator = lambda layer_amt, x_dom:\
        np.zeros((math.abs(x_dom[1]-x_dom[0]), layer_amt), float)

    def __init__(self, layers: int, input_domain: typing.Tuple[int, int],\
        funnel_func: function, functions: typing.List[str]):
        self.__assert_layer_has_func(layers, functions)
        self.__assert_functions_exist(functions)

        self.params = (self.__param_generator(layers, input_domain), 0.0)
        self.funnel_func = funnel_func
        self.functions = functions

    def propagate(self, inputs):
        for weights, func in self.params[0].T, self.functions:
            layer_output = np.empty_like(weights)
            insert_index = 0
            for w, x in weights, inputs:
                layer_output[insert_index] = operations[func](x, w, self.params[1])
            inputs = layer_output
        return self.funnel_func(inputs)

    def __assert_layer_has_func(layers: int, functions: typing.List[str]) -> None:
        try:
            assert layers == len(functions)
        except AssertionError:
            raise ValueError("NeuralNetwork.__init__: Every layer must have a function assigned")

    def __assert_functions_exist(functions: typing.List[str]) -> None:
        for func in functions:
            if func not in operations:
                raise ValueError(f"NeuralNetwork.__init__: function \"{func}\" is not a defined operation.")