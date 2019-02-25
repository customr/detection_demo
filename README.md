# DETECTION_DEMO

## Getting Started

This is my graduate project for [DLSchool](https://www.dlschool.org).
It is a demo-server where you can make predictions of specific classes by neural detector YoloV3.
Image as input, returns the same image with detection boxes on it.


## Installation

First of all you must be in directory, where this repository does. 

```
cd /your/path/to/detection_demo
```

After that just run installation file simply like that
```
./install.sh
```

That's all what you need for server installation. From this moment you can go to the local server 127.0.0.1:5000 and check it by yourself!

## Usage

If you complete installation above, you do not need to lauch that code everytime. Installed server can be started like that:

```
cd your/path/to/detection_demo
```

```
./run.sh
```

The server based on **127.0.0.1:5000**

## Built With

* [YoloV3](https://github.com/akozd/tensorflow_yolo_v3) - The neural detector
* [flask](http://flask.pocoo.org) - microframework for Python Servers
* [flask_uploads](https://pythonhosted.org/Flask-Uploads/) - Used to make input image form


## Authors

* **Maxim Shipitsin**

## Contacts

* **Canvas** name - max_ship
* **Slack**_name - moks
* **shipicin_max@mail.ru**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details