#encoding=utf8
import sys
import os
import csv
reload(sys)
sys.setdefaultencoding( "utf-8" )

with open('../../../kaggle_data/toxic_comment_classify/data/unzip_data/train.csv','rb') as csvfile:
    reader = csv.DictReader(csvfile)
    column = [row for row in reader]
print column[1]['comment_text']
"""
file = open('','rb')
#file1 = open('/data/cisuser/yuanbo/project/chinese_comment_multi_generate/label_model/tingting_jieshu1_label.txt','rb')
lines = file.readlines()
count = 0
for line in lines:
    filename1 = "./lock_data/%s.txt" % str(count)
    filename2 = "./lock_data/%s.lab" % str(count)
    line_list = line.replace('\n','').split(',')
    file1 = open(filename1,'wb')
    file2 = open(filename2,'wb')
    file1.write(line_list[1].strip().decode('utf-8'))
    file2.write(line_list[0].strip().decode('utf-8'))
    file1.close()
    file2.close()
    count += 1
"""
