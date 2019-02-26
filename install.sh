python3 -m venv flask_env
source flask_env/bin/activate
pip3 install -U -r requirements.txt
export FLASK_ENV=flask_env
cd app/src/yolov3/model/weights
./get_pretrained_coco_weights.sh
cd ../../../../..
python3 detection_demo.py
rm requirements.txt
rm install.sh
