rm run.bat
rm install.bat
python3 -m venv flask_env
source flask_env/bin/activate
pip3 install -r requirements.txt
export FLASK_ENV=flask_env
cd app/src/yolov3
bash model_weights/get_pretrained_coco_weights.sh 
cd ../../../
rm requirements.txt
rm install.sh

