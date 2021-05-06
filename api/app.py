from flask import Flask, jsonify, request
from libs.builder_model import PredictBuilder
import yaml

app = Flask(__name__)

_PATH_CONFIG = "./api/config.yml"
_ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
_CONTENT_MODELS = ["happy_face"]

with open(_PATH_CONFIG, "r") as ymlfile:
    config = yaml.load(ymlfile)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in _ALLOWED_EXTENSIONS


@app.route('/models', methods=["GET"])
def models():
    """
    Get list worker models
    """
    return jsonify(config)

 
@app.route('/<string:model>/v<int:version>/predict', methods=["POST"])
def get_predict(**kwargs):
    """
    Get predict:
    :param model - name model
    :param version - version model
    """
    input_data = dict()
    type_input = "json"
    # process input data
    if kwargs["model"] in _CONTENT_MODELS:
        input_data["data"] = request.files['file']
        type_input = "file"
    else:
        input_data = request.get_json(force=True)  
    # compute feature and predict
    predictor = PredictBuilder(name_predictor=kwargs["model"]).build()
    # features
    predictor.generate_features(
        input_feature=input_data["data"],
        model=kwargs["model"],
        version=kwargs["version"],
        type_input=type_input
    )
    # predict
    result_predict = predictor.compute_predict(f'./models/{kwargs["model"]}/{kwargs["version"]}')
    return jsonify(result_predict)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4444)