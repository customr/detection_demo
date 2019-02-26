# DETECTION_DEMO
#### **only for linux users or windows-professionals**
## Getting Started

This is my graduate project for [DLSchool](https://www.dlschool.org).
It is a demo-server where you can make predictions of specific classes by neural detector YoloV3.
Image as input, return the same image with detection boxes on it.
![alt text](https://i.ytimg.com/vi/BNHJRRUKMa4/maxresdefault.jpg)

## Installation

First of all you must be in directory, where this repository does. 

### For Linux users:
```
cd /your/path/to/detection_demo
```
After that you can run installation script:
```
bash install.sh
```

That's all what you need for server installation. From this moment you can go to the local server **127.0.0.1:5000** and check detector by yourself!

## Usage

If you have complete installation above, you do not need to relauch this code everytime. Installed server can be started like that:

### For Linux users:
```
cd /your/path/to/detection_demo
```
```
bash run.sh
```

The server based on address **127.0.0.1:5000**

## Built With

* [YoloV3](https://github.com/akozd/tensorflow_yolo_v3) - Used as neural detector
* [flask](http://flask.pocoo.org) - microframework for Python Servers
* [flask_uploads](https://pythonhosted.org/Flask-Uploads/) - Used to make input image form


## Authors

* **Maxim Shipitsin**

## Contacts

* **Canvas** name - max_ship
* **Slack** name - moks
* **shipicin_max@mail.ru**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
