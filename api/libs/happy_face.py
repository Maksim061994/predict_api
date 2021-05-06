import sys
from os.path import dirname, abspath
import pickle
import numpy as np
from keras.preprocessing import image
from io import BytesIO
from PIL import Image
from keras.applications.imagenet_utils import preprocess_input


sys.path.append(dirname(abspath(__file__)))

from api.libs.handle_logs import get_console_logger
from api.libs.tensorflow_predicter import SystemFuncPredict


class PredictHappyFace(SystemFuncPredict):
    """
    Builder predictor by happy model
    """

    def __init__(self):
        super().__init__()
        self.url_predict = "localhost"
        self.feature = None  # features for model
        self.logger = get_console_logger("Happy face predictor")
        self.curr_uri = "/v1/models"
        self.target_size = (64, 64)

    def generate_features(self,
                          input_feature: list = None,
                          model: str = None,
                          version: int = None,
                          type_input: str = "json"):
        """
        Feature generation
        :param input_feature: list with input features
        :param model: name model
        :param version: version model
        """
        self.logger.info("Generate features for model")
        if input_feature is None:
            input_feature = []
        if type_input == "json":
            # TODO: for specific task
            self.feature = {"inputs": input_feature}
        if type_input == "file":
            in_memory_file = BytesIO()
            input_feature.save(in_memory_file)
            image = Image.open(in_memory_file)
            image = image.resize(self.target_size, Image.ANTIALIAS)
            img_array = np.array(image)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)
            self.feature = {"inputs": {"images": img_array.tolist()}}

    def generate_output_predict(self, result_processing):
        """
        Get output predict
        :param result_processing: результат расчетов нейронной сети
        :return: расстояния между входных и выходным (из нейронной сети) вектором
        """
        print("result_processing", result_processing)
        str_output = "Почему не улыбаешься?"
        if result_processing["outputs"][0][0] == 1: # TODO: костыль
            str_output = "Красивая улыбка!"
        # output = {"predicts": result_processing}
        return str_output

    def compute_predict(self, path_model):
        """
        Compute predict for model
        :param path_model: path to model
        """
        out = []
        self.logger.info("Compute features for model")
        params = path_model.split("/")
        uri = f"{self.curr_uri}/{params[-2]}/versions/{params[-1]}:predict"
        if self.feature:
            predicts = self.send_to_api(self.feature, uri)
            out = self.generate_output_predict(predicts)
        return out
