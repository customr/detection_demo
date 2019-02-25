del /f run.sh
del /f install.sh
python3 -m venv flask_env
flask_env\Scripts\activate
pip3 install -r requirements.txt
export FLASK_ENV=flask_env
cd app/src/yolov3
START model_weights/get_pretrained_coco_weights.bat


