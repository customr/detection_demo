import os.path
import time
import tensorflow as tf
import numpy as np
from app.src.yolov3.models.yolo_v3 import yolo_v3
from app.src.yolov3.utils.utils import process_image, get_anchors, get_classes, convert_box_coordinates, non_max_suppression, draw_boxes

def main(**args):
    h = 416
    w = 416
    anchors = get_anchors('app/src/yolov3/utils/anchors.txt')
    classes = get_classes('app/src/yolov3/utils/coco_classes.txt')
    save_as = args['save_as']

    image, original_im = process_image(args['path_to_input_image'], h, w)
    tf.reset_default_graph()

    with tf.variable_scope('x_input'):
        X = tf.placeholder(dtype=tf.float32, shape=[None, h, w, 3])
    
    yolo_outputs = yolo_v3(inputs=X, num_classes=len(classes), anchors=anchors, h=h, w=w, training=False) # output

    with tf.variable_scope('obj_detections'):
        raw_outputs = tf.concat(yolo_outputs, axis=1)

    # pass image through model
    with tf.Session() as sess:
        writer = tf.summary.FileWriter('app/src/yolov3/tensorboard/tensorboard_detect/',sess.graph)
        writer.close()
        saver = tf.train.Saver()
        saver.restore(sess, save_path='app/src/yolov3/model_weights/coco_pretrained_weights.ckpt')
        start = time.time()
        ro = sess.run(raw_outputs, feed_dict={X:[np.array(image, dtype=np.float32)]})
        end = time.time()
        total_time = end-start
    
    # convert box coordinates, apply nms, and draw boxes
    boxes = convert_box_coordinates(ro)
    filtered_boxes = non_max_suppression(boxes, confidence_threshold=0.5,iou_threshold=0.4)
    draw_boxes(save_as,'app/src/yolov3/utils/coco_classes.txt',filtered_boxes,original_im, image)
    
    return save_as
