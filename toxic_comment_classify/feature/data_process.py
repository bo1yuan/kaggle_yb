#encoding=utf8
"""
导入一些必要模块
"""
import sys
import os
import xgboost as xgb
import numpy as np
import pandas as pd

#本脚本用来进行数据预处理。包括一些可视化数据操作
# pylint: enable=R0201

class DataProcess(object):

    """
    该类为数据处理模块，具体对toxic数据进行各种标准化，归一化及可视化处理

    """
    def __init__(self):
        self.input_file = "input_file"


    def run(self):
        """
        类执行函数run
        """
        self.load_data("a")
        print "ok"


    #@staticmethod
    def load_data(self, input_file="aa"):
        """
        此函数负责导入数据
        """
        print input_file
        print "load data"
        return input_file

    #@staticmethod
    def data_visual(self, dataframe="bb"):
        """
        数据可视化专用函数
        """
        print dataframe
        return dataframe






if __name__ == "__main__":
    OBJ = DataProcess()
    OBJ.load_data("aa")
    OBJ.run()
