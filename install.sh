python3 -m venv flask_env
source flask_env/bin/activate
echo Installing requirements. Please wait.
pip3 install -q -r requirements.txt
export FLASK_ENV=flask_env
cd app/src/yolov3
echo load model weights
bash model_weights/get_pretrained_coco_weights.sh
cd ../../..
python3 detection_demo.py
rm requirements.txt
rm install.sh
