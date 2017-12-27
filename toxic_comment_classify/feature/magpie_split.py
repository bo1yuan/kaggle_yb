#encoding=utf8
import sys
import os
import csv
reload(sys)
sys.setdefaultencoding( "utf-8" )

with open('../../../kaggle_data/toxic_comment_classify/data/unzip_data/train.csv','rb') as csvfile:
    reader = csv.DictReader(csvfile)
    column = [row for row in reader]
#print column[1]['comment_text']
dim_list = ['toxic','severe_toxic','obscene','threat','insult','identity_hate']
count = 0
for col_num in xrange(len(column)):
    row = column[col_num]
    label_list = []
    for i in xrange(len(dim_list)):
        if int(row.get(dim_list[i],-1)) >= 1:
            label_list.append(dim_list[i])
    print "*****"
    if label_list:
        filename1 = "../../../kaggle_data/toxic_comment_classify/data/train_data/magpie_data/%s.txt" % str(count)
        filename2 = "../../../kaggle_data/toxic_comment_classify/data/train_data/magpie_data/%s.lab" % str(count)
        file1 = open(filename1,'wb')
        file2 = open(filename2,'wb')
        file1.write(row.get('comment_text'))
        file2.write("\n".join(label_list))
        file1.close()
        file2.close()
        count += 1
