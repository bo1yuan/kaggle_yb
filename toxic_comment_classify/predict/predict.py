#encoding=utf8
import xgboost as xgb
import numpy as np
import pandas as pd
import sys
import os

"""
本类用来对test.csv进行预测，输出对应的predict.csv文件，标准格式跟sample_submission.csv
"""

class PredictModel(object):
    """
    本程序用来预测最后的输出，需要用到model文件夹中的训练好的model
    """

    def __init__(self):
        """
        初始化函数
        """
        self.output_dir = "../../../kaggle_data/toxic_comment_classify/data/predict_data/"
        self.output_filename = "predict_output_file.csv"

    def run(self):
        """
        执行函数
        """
