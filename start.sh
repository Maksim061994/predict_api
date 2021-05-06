# Upload tensorflow-serving image
docker run -d -p 8501:8501 -p 8500:8500 -v ${PWD}/data_science/models/serving:/models -e MODEL_NAME=happy_face --name tf-loco-serving -t tensorflow/serving -i-model_config_file=/models/models.config --model_config_file_poll_wait_seconds=60;
# Run API
docker-compose down --rmi all
docker-compose build .;
docker-compose up -d;
