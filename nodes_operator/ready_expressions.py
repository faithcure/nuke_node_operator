import nuke
import os
from node_operator_mainwindow import *

file_path = os.path.dirname(__file__)
get_relative_path = os.path.normpath(file_path + "/assets/")

random = "/random.png"
noise = "/noise.png"
sinus = "/sinus.png"
tris = "/tris.png"
square = "/sqr.png"
saw_right_inner = "/saw_right_inner.png"
saw_right = "/saw_right.png"
saw_right_curve = "/saw_right_curve.png"
saw_left_curve = "/saw_left_curve.png"
boing = "/boing.png"
blip = "/blip.png"
sin_blip = "/snie_blip.png"

class ready_to_expressions(QWidget, Ui_Form):
    def __init__(self):
        super(ready_to_expressions, self).__init()

    def tab_widgets(self):
       self.randm_img.setPixmap(QPixmap(get_relative_path + random))
       self.noise_img.setPixmap(QPixmap(get_relative_path + noise))
       self.sinus_img.setPixmap(QPixmap(get_relative_path + sinus))
       self.tris_img.setPixmap(QPixmap(get_relative_path + tris))
       self.sqr_img.setPixmap(QPixmap(get_relative_path + square))
       self.saw_right_inner_img.setPixmap(QPixmap(get_relative_path + saw_right_inner))
       self.saw_right_img.setPixmap(QPixmap(get_relative_path + saw_right))
       self.saw_right_curve_img.setPixmap(QPixmap(get_relative_path + saw_right_curve))
       self.saw_left_curve_img.setPixmap(QPixmap(get_relative_path + saw_left_curve))
       self.boing_img.setPixmap(QPixmap(get_relative_path + boing))
       self.blip_img.setPixmap(QPixmap(get_relative_path + blip))
       self.sine_blip_img.setPixmap(QPixmap(get_relative_path + sin_blip))