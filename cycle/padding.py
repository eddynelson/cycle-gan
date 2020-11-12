from tensorflow import pad
from tensorflow.keras.layers import Layers

class ReflectionPadding2D(Layer):
    '''
    Padding docs: https://www.machinecurve.com/index.php/2020/02/10/using-constant-padding-reflection-padding-and-replication-padding-with-keras/#reflection-padding
    '''
    def __init__(self, padding=(1, 1), **kwargs):
        super(ReflectionPadding2D, self).__init__(**kwargs)
        self.padding = padding
    
    def call(self, input_tensor):
        padding_width, padding_height = self.padding
        
        padding_matrix = [
            [0, 0],
            [padding_height, padding_height],
            [padding_width, padding_width],
            [0, 0]
        ]
        
        return pad(input_tensor, padding_matrix, mode='REFLECT')