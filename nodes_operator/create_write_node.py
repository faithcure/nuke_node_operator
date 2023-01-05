# -*- coding: utf-8 -*-

################################################################################
## Node operator for Nuke 11+
##
## Created by: Fatih ünal
## WebSite: wwww.fatihunal.net
## e-Mail: fatihunal1989@gmail.com
################################################################################

import nuke
import os
from node_operator_mainwindow import *

class write_settings_tab(QWidget, Ui_Form):
    def __init__(self):
        super(write_settings_tab, self).__init()
    
    def base_name(self, 
                  name, 
                  Proxy, 
                  DN, 
                  Type, 
                  Empty, 
                  Digits, 
                  Directory,
                  Node_name):
        self.location_line_edit.setDisabled(True)
        self.type = self.file_type_combo.currentText()
        self.write_node_name.setEnabled(False)
        if nuke.root()[name].value() == "":
            self.current_locatipn_label.setText("Not matching script name, please save this script.")
            self.current_locatipn_label.setStyleSheet("background-color: red")
        else:
            self.script_name = "".join(nuke.root()[name].value().split("/").pop().split(".")[:1])
            self.current_locatipn_label.setText(self.script_name)
            self.label_16.setText("Denoise: OFF")
            self.label_18.setText(Type.upper())
            if self.label_20 == "":
                self.label_20.setText(Empty.upper())
            else:
                pass

            if "Main" in self.script_name:
                self.script_name = self.script_name.replace("Main", Proxy)
                self.last_name_of_render = self.script_name + Digits + self.file_type_combo.currentText()
                self.label_13.setText(self.last_name_of_render)
            else:
                self.label_13.setText("comp_" +self.script_name + Digits + self.type)

        if nuke.root()[Directory].value() == "":
            self.last_path_label.setText("There is no directory of the project. Please set directory or input specific path.")
            self.last_path_label.setStyleSheet("background-color: red")
        else:
            self.script_directory = "/".join(nuke.root()[Directory].value().split("/"))
            self.for_short_name = self.script_directory + "/Comp/" + "Inputs/" + "Proxy_Render/"
            if len(self.for_short_name.split("/")) > 7:
                self.short_dir_path = "/".join(self.for_short_name.split("/")[8:])
                self.last_path_label.setText("../" + self.short_dir_path)
                #print (self.short_dir_path, "short")
            else:
                self.long_dir_path = "/".join(self.for_short_name.split("/"))
                self.last_path_label.setText(self.long_dir_path)


        def if_denoie_checked(ifDenoiseActive):
            if ifDenoiseActive == Qt.Checked:
                if Proxy in self.script_name:
                    self.if_dn_name = self.script_name.replace(Proxy, DN) + Digits + self.type
                    #self.last_path_label.setText( "../" + self.short_dir_path + self.script_name.replace(Proxy, DN) + Digits + self.type)
                    
                else:
                    self.if_dn_name = "comp_" + self.script_name + "_" + DN + Digits + self.type
                    #self.last_path_label.setText( "../" + self.short_dir_path + self.script_name)
                    
                self.label_13.setText(self.if_dn_name)
                self.suffix_line_edit.setEnabled(False)
                self.suffix_line_edit.setPlaceholderText("Disabled for DN")
                self.label_20.setText(Empty.upper())
                self.label_16.setText("Denoise: ON")
                
            else:
                self.suffix_line_edit.setEnabled(True)
                self.for_short_name = self.script_directory + "/Comp/" + "Inputs/" + "Proxy_Render/" + self.label_13.text()
                if Proxy not in self.script_name:
                    self.if_dn_name = "comp_" + self.script_name + Digits + self.type
                else:
                    self.if_dn_name = self.script_name.replace(DN, Proxy) + Digits + self.type
                self.label_13.setText(self.if_dn_name)
                self.if_dn_name = "comp_" + self.script_name + Digits + self.type
                self.suffix_line_edit.setPlaceholderText("")
                self.label_16.setText("Denoise: OFF")
                self.label_20.setText(Empty.upper())
                self.suffix_line_edit.clear()
                self.last_path_label.setText( "../" + self.short_dir_path )
        self.is_denoise.stateChanged.connect(if_denoie_checked)
        
        def if_suffix_changed():
            if self.suffix_line_edit.text() == "":
                 self.label_13.setText(self.script_name + Digits + self.type)
                 self.label_20.setText(Empty.upper())
            else:
                if Proxy in self.script_name:
                    self.label_13.setText(self.script_name.replace(Proxy, self.suffix_line_edit.text()) + Digits + self.type)
                    self.label_20.setText(self.suffix_line_edit.text())
                else:
                    self.label_13.setText("comp_" + self.script_name + "_" + self.suffix_line_edit.text() + Digits + self.type)
                    self.label_20.setText(self.suffix_line_edit.text())

        self.suffix_line_edit.textChanged.connect(if_suffix_changed)

        def change_file_type():
            self.type = self.file_type_combo.currentText()
            new_name = ".".join(self.label_13.text().split(".")[:-1])
            self.label_13.setText(new_name + "." + self.type)
            self.label_18.setText(self.type.upper())
        self.file_type_combo.currentIndexChanged.connect(change_file_type)

        def get_file_name():
            self.get_file_browser_path = nuke.getFilename('Get File Contents')
            
            self.location_line_edit.setText(self.get_file_browser_path)
            self.last_path_label.setText(self.get_file_browser_path)
            self.location_line_edit.setEnabled(True)
        self.select_btn.clicked.connect(get_file_name)
        
        def new_name_check(state):
            if state == Qt.Checked:
                self.write_node_name.setEnabled(True)
            else:
                self.write_node_name.setEnabled(False)
        self.write_node_name_check.stateChanged.connect(new_name_check)

        def create_write():
            self.last_selection_path = self.for_short_name +  self.label_13.text()
            self.selected_path = self.location_line_edit.text() + self.label_13.text()
            self.wNode = nuke.createNode("Write")
            if not self.location_line_edit.text():
                self.wNode["file"].setValue(self.last_selection_path)
            else:
                self.wNode["file"].setValue(self.selected_path)
            nonde_inst = 1
            spec_inst = 1
            while nuke.exists(Node_name + "_" + str(nonde_inst)):
                nonde_inst +=1
            while nuke.exists(self.write_node_name.text() + "_" + str(spec_inst)):
                spec_inst += 1
            self.wNode["create_directories"].setValue(True)
            self.wNode["tile_color"].setValue(16777215)

            if self.write_node_name_check.isChecked():
                if self.write_node_name.text():
                    self.wNode[name].setValue(self.write_node_name.text()  + "_" + str(spec_inst))
                else:
                    nuke.message("Please enter node a node name.")
            else:
                self.wNode[name].setValue(Node_name  + "_" + str(nonde_inst))

        self.create_write_node_btn.clicked.connect(create_write)
            
        def create_matte_node():
            self.last_selection_path = self.for_short_name + self.script_name + Digits + self.type
            self.selected_path = self.location_line_edit.text() + self.script_name + Digits + self.type
            matte_node = nuke.createNode("Write")
            matte_node_name = "Matte_Node"
            matte_node_inst = 1
            while nuke.exists(matte_node_name + "_" + str(matte_node_inst)):
                matte_node_inst += 1
            matte_node[name].setValue(matte_node_name + "_" + str(matte_node_inst))

            if not self.location_line_edit.text():
                matte_node["file"].setValue(self.last_selection_path.replace(Proxy, "Matte"))
            else:
                matte_node["file"].setValue(self.selected_path.replace(Proxy, "Matte"))
     
            matte_node["tile_color"].setValue(4294967295)
            matte_node["channels"].setValue("alpha")
            matte_node["file_type"].setValue("exr")
            matte_node["create_directories"].setValue(True)
        self.default_btn.clicked.connect(create_matte_node)