import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(dirname(abspath(__file__)))))

from api.libs.happy_face import PredictHappyFace


class PredictBuilder:
    """
    Builder predictor
    """

    def __init__(self, name_predictor):
        self.name_predictor = name_predictor  # name predictor 

    def build(self):
        if self.name_predictor == "happy_face":
            return PredictHappyFace()
        else:
            return f"Not found models with name {self.name_predictor}"
