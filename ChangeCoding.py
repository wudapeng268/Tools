#coding=utf-8
import os
import sys
import codecs
##第一个参数是需要转码的文件的原编码格式 e.g gbk GB18303 GB2312 
##第二个参数是需要转码的目标编码格式e.g utf-8
##第三个参数是待转码文件的路径,请写文件夹的路径,会读取文件夹下所有文件
##第四个参数是写入文件的路径,请写成文件夹
argument = sys.argv
filenames = os.listdir(argument[3])
print filenames
for filename in filenames:
    if filename.startswith("."):
        continue
    context=""
    with open(argument[3]+"/"+filename) as fin:
        for line in fin:
            context = context + line
        # print context
        if not os.path.exists(argument[4]):
            os.makedirs(argument[4])
        out=file(argument[4]+"/"+filename,"w")
        out.write(context.decode(argument[1]).encode(argument[2]))
        out.close()