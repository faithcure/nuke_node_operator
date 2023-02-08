import nuke
from node_operator_mainwindow import *
import os

class nodes_operator_read_node_tab(QWidget, Ui_Form):
    def __init__(self):
        super(nodes_operator_read_node_tab, self).__init__()
        self.read_meta_table.setSortingEnabled(True)

    def missing_frames(self, knob_name):
        def get_current_index():
            nuke.selectedNodes()
            for i in nuke.selectedNodes():
                nodeClass = i.Class()
                if nodeClass == "Read":
                    i[knob_name].setValue(self.missing_frame_combo.currentText())
        self.missing_frame_combo.currentIndexChanged.connect(get_current_index)

    def localization_policy(self, knob_name):
        self.localisation_on_off.addItems(["off", "on", "onDemand", "fromAutoLocalizePath"])
        def get_current_index():
            for i in nuke.selectedNodes():
                nodeClass = i.Class()
                if nodeClass == "Read":
                    i[knob_name].setValue(self.localisation_on_off.currentText())
        self.localisation_on_off.currentIndexChanged.connect(get_current_index)

    def update_node(self, knob_name):
        def get_current_index():
            for i in nuke.selectedNodes():
                    nodeClass = i.Class()
                    if nodeClass == "Read":
                        i[knob_name].execute()
        self.update_btn.clicked.connect(get_current_index)

    def reload_node(self, knob_name):
        def get_current_index():
            for i in nuke.selectedNodes():
                    nodeClass = i.Class()
                    if nodeClass == "Read":
                        i[knob_name].execute()
        self.reload_btn.clicked.connect(get_current_index)

    def premulty(self, knob_name):
        def get_current_index(state):
            for c in nuke.selectedNodes():
                    nodeClass = c.Class()
                    if nodeClass == "Read":
                        if state == Qt.Checked:
                            c[knob_name].setValue(1)
                        else:
                            c[knob_name].setValue(0)
        self.premulty.stateChanged.connect(get_current_index)

    def auto_alpha(self, knob_name):
        def get_current_index(state):
            for c in nuke.selectedNodes():
                    nodeClass = c.Class()
                    if nodeClass == "Read":
                        if state == Qt.Checked:
                            c[knob_name].setValue(1)
                        else:
                            c[knob_name].setValue(0)
        self.auto_alpha.stateChanged.connect(get_current_index)

    def raw_data(self, knob_name):
        def get_current_index(state):
            for c in nuke.selectedNodes():
                    nodeClass = c.Class()
                    if nodeClass == "Read":
                        if state == Qt.Checked:
                            c[knob_name].setValue(1)
                        else:
                            c[knob_name].setValue(0)
        self.raw_data.stateChanged.connect(get_current_index)

    def format_settings(self):
        def add_formats():
            format_list = []
            for f in nuke.formats():
                format_list.append(f.name())
            self.format_box.addItems(format_list)
        add_formats()

        def get_current_index():
            for c in nuke.selectedNodes():
                nodeClass = c.Class()
                if nodeClass == "Read":
                    c["format"].setValue(self.format_box.currentText())
        self.format_box.currentIndexChanged.connect(get_current_index)
        #self.format_size_label.setText("Sure your root Format(s)")

    def frame_range(self):
        def add_first_frame():
            for c in nuke.selectedNodes():
                nodeClass = c.Class()
                if nodeClass == "Read":
                    c["first"].setValue(int(self.first_frame_range_line.text()))

        def add_last_frame():
            for c in nuke.selectedNodes():
                nodeClass = c.Class()
                if nodeClass == "Read":
                    c["last"].setValue(int(self.last_frame_range_line.text()))

        def change_before():
            for c in nuke.selectedNodes():
                nodeClass = c.Class()
                if nodeClass == "Read":
                    c["before"].setValue(self.set_frame_before.currentText())

        def change_after():
            for c in nuke.selectedNodes():
                nodeClass = c.Class()
                if nodeClass == "Read":
                    c["after"].setValue(self.set_frame_after.currentText())

        self.first_frame_range_line.textChanged.connect(add_first_frame)
        self.last_frame_range_line.textChanged.connect(add_last_frame)
        self.first_frame_range_line.returnPressed.connect(add_first_frame)
        self.last_frame_range_line.returnPressed.connect(add_last_frame)
        self.set_frame_before.currentIndexChanged.connect(change_before)
        self.set_frame_after.currentIndexChanged.connect(change_after)

    def frame_offset(self,
                    knob_name,
                    frame):

        def get_current_index():
            for c in nuke.selectedNodes():
                nodeClass = c.Class()
                if nodeClass == "Read":
                    c[knob_name].setValue(self.frame_mode_combo.currentText())

        def set_current_frame():
            for c in nuke.selectedNodes():
                nodeClass = c.Class()
                if nodeClass == "Read":
                    c[frame].setValue(self.set_frame_lineedit.text())

        self.frame_mode_combo.currentIndexChanged.connect(get_current_index)
        self.set_frame_lineedit.returnPressed.connect(set_current_frame)
        self.set_frame_lineedit.textChanged.connect(set_current_frame)

    def original_range(self,
                       orig_first,
                       orig_last):

        def original_first():
            for c in nuke.selectedNodes():
                nodeClass = c.Class()
                if nodeClass == "Read":
                    c[orig_first].setValue(int(self.original_range_in.text()))

        def original_last():
            for c in nuke.selectedNodes():
                nodeClass = c.Class()
                if nodeClass == "Read":
                    c[orig_last].setValue(int(self.orginal_range_out.text()))
        self.original_range_in.textChanged.connect(original_first)
        self.orginal_range_out.textChanged.connect(original_last)

    def colorspace(self, knob_name):
        colorspaces = nuke.root()["monitorLut"].values()
        self.color_space.addItems(colorspaces)
        def get_colorspaces():
            for c in nuke.selectedNodes():
                nodeClass = c.Class()
                if nodeClass == "Read":
                    c[knob_name].setValue(self.color_space.currentText())
        self.color_space.currentIndexChanged.connect(get_colorspaces)

    def loadDataReadNode(self):
        bit_depth = "input/bitsperchannel" # Bit depth
        created_time = "input/ctime" # Created time
        path_file_name = "input/filename" # path of the read node
        codec_info = "quicktime/codec_name" # codec info
        file_size = "input/filesize" # file sz (?? > MB!)
        file_extension = "input/filereader" # File extension info
        row = 0

        readCountList = []
        for n in nuke.allNodes("Read"):
            readCountList.append(n.name())
            self.read_meta_table.setRowCount(len(readCountList))
            self.read_meta_table.setItem(row, 0, QTableWidgetItem(n.name()))

            localizedBox = QCheckBox()
            #localizedBox.setText("True")
            localizedBox.setEnabled(False)

            exploreBtn = QPushButton()
            exploreBtn.setText("Explore")

            if n.metadata("input/height") == None:
                self.read_meta_table.setItem(row, 1, QTableWidgetItem("None"))
            else:
                self.read_meta_table.setItem(row, 1, QTableWidgetItem(n.metadata(file_extension)))

            self.read_meta_table.setCellWidget(row, 2, localizedBox)

            extension = ["exr", "jpg", "tga", "raw", "dpx", "png", "targa", "jpeg", "tiff", "xpm", "yuv", "null", None]

            if n.metadata(file_size) != None:
                get_file_size_from_meta = float(n.metadata(file_size) / 1024 / 1024)

                if n.metadata(file_size) == None:
                    self.read_meta_table.setItem(row, 7, QTableWidgetItem(str(get_file_size_from_meta)[:6] + " MB"))

                if self.read_meta_table.item(row, 1).text() in extension:
                    self.read_meta_table.setItem(row, 7, QTableWidgetItem(str(get_file_size_from_meta)[:6] + " MB / Frame"))

                else:
                    self.read_meta_table.setItem(row, 7, QTableWidgetItem(str(get_file_size_from_meta)[:6] + " MB"))

            else:
                self.read_meta_table.setItem(row, 7, QTableWidgetItem(str("Error")))
                nuke.message("Some read nodes are incorrect. Please check!" + "(Added as " + self.read_meta_table.item(row ,7).text() + ")")

            aspect_size =  str(n.metadata("input/width")) + " x " +  str(n.metadata("input/height") )

            if n.metadata("input/height") == None:
                self.read_meta_table.setItem(row, 3, QTableWidgetItem(str("None")))
            else:
                self.read_meta_table.setItem(row, 3, QTableWidgetItem(aspect_size))

            if n.metadata(codec_info) == None:
                self.read_meta_table.setItem(row, 4, QTableWidgetItem("None"))
            else:
                self.read_meta_table.setItem(row, 4, QTableWidgetItem(n.metadata(codec_info)))

            to_node = nuke.toNode(self.read_meta_table.item(row, 0).text())

            if to_node["localizationPolicy"].value() == "on":
                localizedBox.setChecked(True)
                localizedBox.setText("True")

            else:
                self.read_meta_table.cellWidget(row, 2).setStyleSheet("background-color: #512f00")
                localizedBox.setCheckable(False)
                localizedBox.setText("False")

            def explore_file():
                get_path = self.read_meta_table.item(self.read_meta_table.currentRow(), 6).text().split("/")[:-1]
                os.startfile("/".join(get_path))
            if n.metadata(created_time) != None:
                self.read_meta_table.setItem(row, 5, QTableWidgetItem(n.metadata(created_time)))
            else:
                self.read_meta_table.setItem(row, 5, QTableWidgetItem("Error"))

            if n.metadata(path_file_name) != None:
                self.read_meta_table.setItem(row, 6, QTableWidgetItem(n.metadata(path_file_name)))
            else:
                self.read_meta_table.setItem(row, 6, QTableWidgetItem("Error"))

            self.read_meta_table.setCellWidget(row, 8, exploreBtn)
            exploreBtn.clicked.connect(explore_file)
            row = row + 1

            # get file path from table
            # get_path = nuke.toNode(self.read_meta_table.item(row, 0).text())["file"].value().split("/")[:4]
            # pp = os.path.normpath("/".join(get_path))

        # get file from file knob
        def check_files_root():
            for allnodes in nuke.allNodes("Read"):
                get_path = os.path.normpath("/".join(allnodes["file"].value().split("/")[:4]))
                # print (allnodes.name() ,get_path)

                PATH_ALT_1 = nuke.root()["project_directory"].value().split("/")[:1]
                PATH_ALT_2 = nuke.root()["project_directory"].value().split("/")[:2]
                PATH_ALT_3 = nuke.root()["project_directory"].value().split("/")[:3]
                PATH_ALT_4 = nuke.root()["project_directory"].value().split("/")[:4]
                PATH_ALT_5 = nuke.root()["project_directory"].value().split("/")[:5]

                path_one = os.path.normpath("/".join(PATH_ALT_1))
                path_two = os.path.normpath("/".join(PATH_ALT_2))
                path_three = os.path.normpath("/".join(PATH_ALT_3))
                path_four = os.path.normpath("/".join(PATH_ALT_4))
                path_five = os.path.normpath("/".join(PATH_ALT_5))

                if get_path not in path_five and path_one and path_three and path_two:
                    self.warning_read_tab.setText("Some nodes not in the project directory please check.")
                    allnodes["tile_color"].setValue(4278190847)

                else:
                    allnodes["tile_color"].setValue(0)

        self.checl_warning.clicked.connect(check_files_root)
