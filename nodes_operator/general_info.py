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
import psutil
import platform
from node_operator_mainwindow import *
import socket
import webbrowser


class general_infos(QWidget, Ui_Form):
    def __init__(self):
        super(general_infos, self).__init()

    def set_web_links(self):
        # set web links
        def get_more_info_link():
            webbrowser.open("https://learn.foundry.com/nuke/content/comp_environment/organizing_scripts/using_profile_node.html")
        def tutorial_link():
            webbrowser.open("www.fatihunal.net")
        self.more_prf_link.clicked.connect(get_more_info_link)
        self.app_tuts.clicked.connect(tutorial_link)

    def get_spec_system(self):
        avaliable_ram = round(psutil.virtual_memory().available/1000000000, 2)
        total_ram = round(psutil.virtual_memory().total/1000000000, 2)
        ram_used = round(psutil.virtual_memory().used/1000000000, 2)
        ram_used_percent = psutil.virtual_memory().percent
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            #print(f"Core {i}: {percentage}%")
            pass
        cpu_percent = psutil.cpu_percent()

        cpu_type = platform.machine()
        pysical_cores = psutil.cpu_count(logical=False)
        pysical_cores_logical = psutil.cpu_count(logical=True)
        pc_name = socket.gethostname()


        self.mem_free_label.setText(str(avaliable_ram) + " / " + str(total_ram) + "Gb ~")
        self.mem_usage_lbl.setText(str(ram_used) + "Gb" + " / " + str(ram_used_percent)+ "% ~")
        self.cpu_core_lbl.setText(str(pysical_cores) + " (" + str(pysical_cores_logical) + ")" + " - " + str(cpu_type) + " / " + "Total CPU Usage: " + str(cpu_percent) + "%")
        self.pc_name_lbl.setText(str(pc_name))
        
        
    def get_link_contact(self):
        """Create web site link for the general tab"""
        self.label_61.setText('''<a href='http://www.fatihunal.net', 
                                 style=color:white >www.fatihunal.net</a>''')
        self.label_61.setOpenExternalLinks(True)
        self.label_63.setText('''<a href='http://www.cameroncarson.com', 
                                 style=color:white >www.cameroncarson.com (expressions)</a>''')
        self.label_63.setOpenExternalLinks(True)
        self.gitup.setText('''<a href='https://github.com/faithcure/', 
                                style=color:white >GitHub Page</a>''')
        self.gitup.setOpenExternalLinks(True)
        self.youtube.setText('''<a href='https://www.youtube.com/@viewportpro', 
                                style=color:white >Youtube Page</a>''')
        self.youtube.setOpenExternalLinks(True)
        self.nukepedia_lbl.setText('''<a href='https://www.nukepedia.com/search?filter=1&query=faithcure', 
                                style=color:white >Nukepedia results</a>''')
        self.nukepedia_lbl.setOpenExternalLinks(True)
                                
    def get_node_count(self):
        allNodes = str(len(nuke.allNodes()))
        if allNodes == 0:
            self.node_count_label.setText("0")
        else:
            self.node_count_label.setText(allNodes + " with Viewer node(s)")
    
    def get_selected_node_count(self):
        sN = nuke.selectedNodes()
        if sN:
            self.selected_node_cnt_lbl.setText(str(len(sN)))

    def get_read_count(self):
        readNodes = str(len(nuke.allNodes("Read")))
        self.read_node_count_lbl.setText(readNodes)
    
    def get_write_count(self):
        writeNodes = str(len(nuke.allNodes("Write")))
        self.write_node_count_lbl.setText(writeNodes)

    def get_project_dir(self):
        """if: there is no path than return None"""
        proj_dir = nuke.root()["project_directory"].value().split("/")[3:]
        get_prj_dir = "/".join(proj_dir)
        if proj_dir:
            self.project_dir_lbl.setText(".../"+get_prj_dir)
        else:
            self.project_dir_lbl.setText("Project name is not set.")

    def get_project_name(self):
        """if: there is no name than return None"""
        proj_name = nuke.root()["name"].value()
        get_prj_name = proj_name.split("/")[-1]
        if proj_name:
            self.project_name_lbl.setText(get_prj_name)
        else:
            self.project_name_lbl.setText("Project directory is not set.")

    def get_nuke_env(self):
        nuke_env = "nuke_env"
        if nuke.env["ple"] == True:
            nuke_env = "PLE"
        elif nuke.env["indie"] == True:
            nuke_env = "Indie"
        elif nuke.env["nukex"] == True:
            nuke_env = "NukeX"
        elif nuke_env["hieroStudio"] == True:
            nuke_env = "Hiero Studio"
        elif nuke.env["hiero"] == True:
            nuke_env = "Hiero"
        elif nuke.env["assist"] == True:
            nuke_env = "Assist"
        elif nuke.env["nc"] == True:
            nuke_env = "Non Commercial"
        elif nuke.env["nukex"] == True:
            nuke_env = "NukeX"
        elif nuke_env["studio"] == True:
            nuke_env = "Nuke Studio"
        else:
            nuke_env = "Unknow Environment"

        nukeVersionString = "Nuke " + nuke.env["NukeVersionString"] + " > " + "(" + nuke_env + ")"      
        self.nuke_env_lbl.setText(nukeVersionString)
    
    def open_close_pf(self):
        """open and close performance timers. return: on/off"""
        def enable_disable_state(state):
            if state == Qt.Checked:
                nuke.startPerformanceTimers()
            else:
                nuke.stopPerformanceTimers()
        self.checkBox.stateChanged.connect(enable_disable_state)

    def check_state_pf(self):
        """return: using performance timers check"""
        if nuke.usingPerformanceTimers() == False:
            self.checkBox.setChecked(0)
        else:
            self.checkBox.setChecked(1)

    def get_performence_timer(self):
        """General profiling strings are here"""
        cpu_core = nuke.env ["numCPUs"]
        memory_size = None
        return None
