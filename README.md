### API for model

start: `bash start.sh`

check cnt: `docker ps -a`

check tf-serving: GET `http://HOST:8501/v1/models/happy_face/versions/1/metadata`

chekc api: GET `http://HOST:4444/models`