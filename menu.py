# -*- coding: utf-8 -*-
import nuke
import node_operator_main_v01
import importlib


toolbar = nuke.menu("Nodes")
i = toolbar.addMenu("Studio", icon='STUDIO.png')

# development node operator
def start_NOP():
    # node operator
    importlib.reload(node_operator_main_v01)
    node_operator_main_v01.start()
i.addCommand("Node Operator v0.1", "start_NOP()")
