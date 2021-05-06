import sys
from os import path
sys.path.append(path.join(path.dirname(__file__), '../'))
from api.libs.handle_logs import get_console_logger
import json
import requests


class SystemFuncPredict:
    """
    System func by predict
    """
    def __init__(self, url_predict="localhost", port_predict=8501):
        self.url_predict = url_predict  # host tf-serving
        self.port_predict = port_predict  # port tf-serving
        self.logger = get_console_logger("Base tensorflow predictor")

    def send_to_api(self, data, uri):
        """
        Отправка данных для расчёта
        :param data - json с данными для content
        :param url - адрес запроса
        :param port - порт
        :param uri - версия модели
        """
        headers = {"Content-Type": "application/json"}
        # self.logger.info(f"Get predict from tensorflow for features {data} and model {uri}")
        resp = requests.post(f"http://{self.url_predict}:{self.port_predict}{uri}",
                             data=json.dumps(data), headers=headers, verify=False)
        return json.loads(resp.text)

    @staticmethod
    def generate_output_predict(result):
        """
        Интерпретация результов предсказания
        """
        return {"predicts": list(result)}
