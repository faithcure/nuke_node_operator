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

zigzag_expression = "/zigzag_gif.gif"
wiggle_expression = "/wiggle.gif"
w_bounce_expression = "/W_Bounce.gif"
scale_up_down_expression = "/scale_up_down.gif"
heart_expression = "/Heart.gif"
h_bounce_expression = "/H_Bounce.gif"
drift_expression = "/drift.gif"
cw_ellipse_expression = "/CW_Ellipse.gif"
cw_circle_expression = "/CW_Circle.gif"
ccw_ellipse_expression = "/CCW_Ellipse.gif"
ccw_circle_expression = "/CCW_Circle.gif"
blink_expression = "/Blink.gif"

zigzag_nk = "/zig_zag_exp.nk"
wiggle_nk = "/wiggle_exp.nk"
w_bounce_nk = "/v_bounce_exp.nk"
scale_up_down_nk = "/scale_up_down_exp.nk"
heart_nk = "/heart_exp.nk"
h_bounce_nk = "/h_bounce_exp.nk"
drift_nk = "/drift_exp.nk"
cw_ellipse_nk = "/cw_ellipse_exp.nk"
cw_circle_nk = "/CW_circle_exp.nk"
ccw_ellipse_nk = "/CCW_Ellipse_exp.nk"
ccw_circle_nk = "/CCW_circle_exp.nk"
blink_nk = "/blink_exp.nk"


class ready_to_expressions(QWidget, Ui_Form):
    def __init__(self):
        super(ready_to_expressions, self).__init()

    def if_result_empty(self):
        self.create_text_node_btn.setEnabled(0)
        self.create_stick_node_btn.setEnabled(0)
        self.add_label_btn.setEnabled(0)
        self.create_backd_btn.setEnabled(0)

        def if_result_empty_def():
            if self.expression_reslt.text():
                self.create_text_node_btn.setEnabled(1)
                self.create_stick_node_btn.setEnabled(1)
                self.add_label_btn.setEnabled(1)
                self.create_backd_btn.setEnabled(1)
            else:
                self.create_text_node_btn.setEnabled(0)
                self.create_stick_node_btn.setEnabled(0)
                self.add_label_btn.setEnabled(0)
                self.create_backd_btn.setEnabled(0)

        self.expression_reslt.textChanged.connect(if_result_empty_def)

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

    def text_expressions(self):
        # root_name = nuke.root().name().split("/").pop()
        proj_dir_expression = " [value root.project_directory] "
        format_expression = " [value root.format] "
        colorspace_expression = " [value colorspace] "
        # script_name_expression = " root_name "
        frame_range_expression = " [value root.first_frame] - [value root.last_frame] "
        script_path_extension = " [value root.name] "
        fps_extension = " [value root.fps] "
        monitorLut = " [value root.monitorLut] "
        current_frame_extension = " [value frame] "
        colorManagement_extension = " [value root.colorManagement] "
        file_extension_expression = " [file extension [knob [topnode].file]] "
        value_size_expression = " [value size] "
        value_mix_expression = " [value mix] "
        value_input_name_expression = " [value input.name] "
        gui_expression = " $gui "
        first_frame_expression = " [value root.first_frame] "
        last_frame_expression = " [value root.last_frame] "
        all_input_name_expression = """ [python {"\n".join(["Input: %s" % node.name() for node in nuke.thisNode().dependencies()])}] """
        main_values_of_node_expression = " [values this] "
        all_values_of_node_expression = " [values -a this] "
        input_this_expression = " [inputs this] "

        def proj_dir_check(state):
            before = self.expression_reslt.text()
            if state == Qt.Checked:
                self.expression_reslt.insert(proj_dir_expression)
            else:
                if proj_dir_expression in self.expression_reslt.text():
                    self.expression_reslt.setText(before.replace(proj_dir_expression, ""))
                else:
                    pass

        def add_format_check(state):
            before = self.expression_reslt.text()
            if state == Qt.Checked:
                self.expression_reslt.insert(format_expression)
            else:
                if format_expression in self.expression_reslt.text():
                    self.expression_reslt.setText(before.replace(format_expression, ""))
                else:
                    pass

        def color_space_check(state):
            before = self.expression_reslt.text()
            if state == Qt.Checked:
                self.expression_reslt.insert(colorspace_expression)
            else:
                if colorspace_expression in self.expression_reslt.text():
                    self.expression_reslt.setText(before.replace(colorspace_expression, ""))
                else:
                    pass

        """
        def script_name_check(state):
            before = self.expression_reslt.text()
            if state == Qt.Checked:
                self.expression_reslt.insert(text_04)
            else:
                if text_04 in self.expression_reslt.text():
                    self.expression_reslt.setText(before.replace(text_04, ""))
                else:
                    pass
        """

        def frame_range_check(state):
            before = self.expression_reslt.text()
            if state == Qt.Checked:
                self.expression_reslt.insert(frame_range_expression)
            else:
                if frame_range_expression in self.expression_reslt.text():
                    self.expression_reslt.setText(before.replace(frame_range_expression, ""))
                else:
                    pass

        def script_path_check(state):
            before = self.expression_reslt.text()
            if state == Qt.Checked:
                self.expression_reslt.insert(script_path_extension)
            else:
                if script_path_extension in self.expression_reslt.text():
                    self.expression_reslt.setText(before.replace(script_path_extension, ""))
                else:
                    pass

        def fps_check(state):
            before = self.expression_reslt.text()
            if state == Qt.Checked:
                self.expression_reslt.insert(fps_extension)
            else:
                if fps_extension in self.expression_reslt.text():
                    self.expression_reslt.setText(before.replace(fps_extension, ""))
                else:
                    pass

        def monitorlut_check(state):
            before = self.expression_reslt.text()
            if state == Qt.Checked:
                self.expression_reslt.insert(monitorLut)
            else:
                if monitorLut in self.expression_reslt.text():
                    self.expression_reslt.setText(before.replace(monitorLut, ""))
                else:
                    pass

        def current_frame_check(state):
            before = self.expression_reslt.text()
            if state == Qt.Checked:
                self.expression_reslt.insert(current_frame_extension)
            else:
                if current_frame_extension in self.expression_reslt.text():
                    self.expression_reslt.setText(before.replace(current_frame_extension, ""))
                else:
                    pass

        def color_management_check(state):
            before = self.expression_reslt.text()
            if state == Qt.Checked:
                self.expression_reslt.insert(colorManagement_extension)
            else:
                if colorManagement_extension in self.expression_reslt.text():
                    self.expression_reslt.setText(before.replace(colorManagement_extension, ""))
                else:
                    pass

        def extension_check(state):
            before = self.expression_reslt.text()
            if state == Qt.Checked:
                self.expression_reslt.insert(file_extension_expression)
            else:
                if file_extension_expression in self.expression_reslt.text():
                    self.expression_reslt.setText(before.replace(file_extension_expression, ""))
                else:
                    pass

        def value_size_check(state):
            before = self.expression_reslt.text()
            if state == Qt.Checked:
                self.expression_reslt.insert(value_size_expression)
            else:
                if value_size_expression in self.expression_reslt.text():
                    self.expression_reslt.setText(before.replace(value_size_expression, ""))
                else:
                    pass

        def value_mix_check(state):
            before = self.expression_reslt.text()
            if state == Qt.Checked:
                self.expression_reslt.insert(value_mix_expression)
            else:
                if value_mix_expression in self.expression_reslt.text():
                    self.expression_reslt.setText(before.replace(value_mix_expression, ""))
                else:
                    pass

        def value_input_name_check(state):
            before = self.expression_reslt.text()
            if state == Qt.Checked:
                self.expression_reslt.insert(value_input_name_expression)
            else:
                if value_input_name_expression in self.expression_reslt.text():
                    self.expression_reslt.setText(before.replace(value_input_name_expression, ""))
                else:
                    pass

        def gui_check(state):
            before = self.expression_reslt.text()
            if state == Qt.Checked:
                self.expression_reslt.insert(gui_expression)
            else:
                if gui_expression in self.expression_reslt.text():
                    self.expression_reslt.setText(before.replace(gui_expression, ""))
                else:
                    pass

        def firs_frame_check(state):
            before = self.expression_reslt.text()
            if state == Qt.Checked:
                self.expression_reslt.insert(first_frame_expression)
            else:
                if first_frame_expression in self.expression_reslt.text():
                    self.expression_reslt.setText(before.replace(first_frame_expression, ""))
                else:
                    pass

        def last_frame_check(state):
            before = self.expression_reslt.text()
            if state == Qt.Checked:
                self.expression_reslt.insert(last_frame_expression)
            else:
                if last_frame_expression in self.expression_reslt.text():
                    self.expression_reslt.setText(before.replace(last_frame_expression, ""))
                else:
                    pass

        def all_input_name_check(state):
            before = self.expression_reslt.text()
            if state == Qt.Checked:
                self.expression_reslt.insert(all_input_name_expression)
            else:
                if all_input_name_expression in self.expression_reslt.text():
                    self.expression_reslt.setText(before.replace(all_input_name_expression, ""))
                else:
                    pass

        def main_values_of_nodes_check(state):
            before = self.expression_reslt.text()
            if state == Qt.Checked:
                self.expression_reslt.insert(main_values_of_node_expression)
            else:
                if main_values_of_node_expression in self.expression_reslt.text():
                    self.expression_reslt.setText(before.replace(main_values_of_node_expression, ""))
                else:
                    pass

        def all_values_of_nodes_check(state):
            before = self.expression_reslt.text()
            if state == Qt.Checked:
                self.expression_reslt.insert(all_values_of_node_expression)
            else:
                if all_values_of_node_expression in self.expression_reslt.text():
                    self.expression_reslt.setText(before.replace(all_values_of_node_expression, ""))
                else:
                    pass

        def input_this_check(state):
            before = self.expression_reslt.text()
            if state == Qt.Checked:
                self.expression_reslt.insert(input_this_expression)
            else:
                if input_this_expression in self.expression_reslt.text():
                    self.expression_reslt.setText(before.replace(input_this_expression, ""))
                else:
                    pass

        self.ex_proj_dir_check.stateChanged.connect(proj_dir_check)
        self.exp_add_format_check.stateChanged.connect(add_format_check)
        self.exp_cc_check.stateChanged.connect(color_space_check)
        # self.exp_scriptname_check.stateChanged.connect(script_name_check)
        self.exp_framerange_check.stateChanged.connect(frame_range_check)
        self.exp_script_path_check.stateChanged.connect(script_path_check)
        self.exp_fps_check.stateChanged.connect(fps_check)
        self.exp_monitor_lut_check.stateChanged.connect(monitorlut_check)
        self.exp_frame_current_check.stateChanged.connect(current_frame_check)
        self.exp_colormanagement_check.stateChanged.connect(color_management_check)
        self.exp_extension_check.stateChanged.connect(extension_check)
        self.exp_value_size_check.stateChanged.connect(value_size_check)
        self.exp_value_mix_check.stateChanged.connect(value_mix_check)
        self.exp_value_input_check.stateChanged.connect(value_input_name_check)
        self.exp_gui_check.stateChanged.connect(gui_check)
        self.exp_first_frame_check.stateChanged.connect(firs_frame_check)
        self.exp_last_frame_check.stateChanged.connect(last_frame_check)
        self.exp_all_input_check.stateChanged.connect(all_input_name_check)
        self.exp_main_values_check.stateChanged.connect(main_values_of_nodes_check)
        self.exp_all_values_check.stateChanged.connect(all_values_of_nodes_check)
        self.exp_node_count_check.stateChanged.connect(input_this_check)

    def create_nodes(self):
        def create_text_node():
            text_node = nuke.createNode("Text")
            text_node["message"].setValue(self.expression_reslt.text())

        def create_backdrop():
            backdrop = nuke.createNode("BackdropNode")
            backdrop["label"].setValue(self.expression_reslt.text())

        def create_stcik_note():
            stick_note = nuke.createNode("StickyNote")
            stick_note["label"].setValue(self.expression_reslt.text())

        def add_label():
            """Add as label to selected Node(s)"""
            add_label = nuke.selectedNodes()
            for i in add_label:
                i["label"].setValue(self.expression_reslt.text())

        self.create_text_node_btn.clicked.connect(create_text_node)
        self.create_backd_btn.clicked.connect(create_backdrop)
        self.create_stick_node_btn.clicked.connect(create_stcik_note)
        self.add_label_btn.clicked.connect(add_label)
        self.create_def_water.setEnabled(False)

    def animation_expression(self):
        """Animation expression definition"""

        # zigzag animation
        zigzag_exp_movie = QMovie(get_relative_path + zigzag_expression)
        self.Zigzag_expression_lbl.setMovie(zigzag_exp_movie)
        zigzag_exp_movie.start()

        def create_zigzag_anim():
            """Create zigzag setup"""
            nuke.nodePaste(get_relative_path + zigzag_nk)

        # wiggle animation
        wiggle_exp_movie = QMovie(get_relative_path + wiggle_expression)
        self.wiggle_expression_lbl.setMovie(wiggle_exp_movie)
        wiggle_exp_movie.start()

        def create_wiggle_anim():
            """Create wiggle setup"""
            nuke.nodePaste(get_relative_path + wiggle_nk)

        # w_bounce animation
        w_bounce_exp_movie = QMovie(get_relative_path + w_bounce_expression)
        self.w_bounce_lbl.setMovie(w_bounce_exp_movie)
        w_bounce_exp_movie.start()

        def v_bounce_anim():
            """Create vertical bounce setup"""
            nuke.nodePaste(get_relative_path + w_bounce_nk)

        # scale up-down animation
        scale_up_down_movie = QMovie(get_relative_path + scale_up_down_expression)
        self.scale_up_expression_lbl.setMovie(scale_up_down_movie)
        scale_up_down_movie.start()

        def scale_updown_anim():
            """Create scale up and down setup"""
            nuke.nodePaste(get_relative_path + scale_up_down_nk)

        # heart attack animation
        heart_attack_movie = QMovie(get_relative_path + heart_expression)
        self.heart_expression_lbl.setMovie(heart_attack_movie)
        heart_attack_movie.start()

        def heart_anim():
            """Call heart like setup"""
            nuke.nodePaste(get_relative_path + heart_nk)

        # H_Bounce animation
        h_bounce_movie = QMovie(get_relative_path + h_bounce_expression)
        self.h_bounce_expression_lbl.setMovie(h_bounce_movie)
        h_bounce_movie.start()

        def h_bounce_anim():
            """Call Horizontal bounce setup"""
            nuke.nodePaste(get_relative_path + h_bounce_nk)

        # drift animation
        drift_movie = QMovie(get_relative_path + drift_expression)
        self.drift_expression_lbl.setMovie(drift_movie)
        drift_movie.start()

        def drift_anim():
            """Call drift setup"""
            nuke.nodePaste(get_relative_path + drift_nk)

        # cw ellipse animation
        cw_ellipse_movie = QMovie(get_relative_path + cw_ellipse_expression)
        self.CW_Ellipse_expression_lbl.setMovie(cw_ellipse_movie)
        cw_ellipse_movie.start()

        def cw_ellipse_anim():
            """Call cw ellipse setup"""
            nuke.nodePaste(get_relative_path + cw_ellipse_nk)

        # cw circle animation
        cw_circle_movie = QMovie(get_relative_path + cw_circle_expression)
        self.CW_Circle_expression_lbl.setMovie(cw_circle_movie)
        cw_circle_movie.start()

        def cw_circle_anim():
            """Call cw circle setup"""
            nuke.nodePaste(get_relative_path + cw_circle_nk)

        # ccw ellipse animation
        ccw_ellipse_movie = QMovie(get_relative_path + ccw_ellipse_expression)
        self.CCW_Ellipse_expression_lbl.setMovie(ccw_ellipse_movie)
        ccw_ellipse_movie.start()

        def ccw_ellipse_anim():
            """Call CCW ellipse setup"""
            nuke.nodePaste(get_relative_path + ccw_ellipse_nk)

        # ccw circle animation
        ccw_circle_movie = QMovie(get_relative_path + ccw_circle_expression)
        self.CCW_Circle_expression_lbl.setMovie(ccw_circle_movie)
        ccw_circle_movie.start()

        def ccw_circle_anim():
            """Call CCW cirlce setup"""
            nuke.nodePaste(get_relative_path + ccw_circle_nk)

        # blink animation
        blink_movie = QMovie(get_relative_path + blink_expression)
        self.blink_expression_lbl.setMovie(blink_movie)
        blink_movie.start()

        def blink_anim():
            """Call blink setup"""
            nuke.nodePaste(get_relative_path + blink_nk)

        # Animation button signals
        self.wiggle_btn.clicked.connect(create_wiggle_anim)
        self.zigzag_btn.clicked.connect(create_zigzag_anim)
        self.w_bounce_btn.clicked.connect(v_bounce_anim)
        self.scale_up_btn.clicked.connect(scale_updown_anim)
        self.heart_btn.clicked.connect(heart_anim)
        self.drift_btn.clicked.connect(drift_anim)
        self.cw_circle_btn.clicked.connect(cw_circle_anim)
        self.ccw_elipse_btn.clicked.connect(ccw_ellipse_anim)
        self.blink_btn.clicked.connect(blink_anim)
        self.ccw_circle_btn.clicked.connect(ccw_circle_anim)
        self.CW_elipse_btn.clicked.connect(cw_ellipse_anim)
        self.h_bounce_btn.clicked.connect(h_bounce_anim)