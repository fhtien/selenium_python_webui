import json
import os





def read_json_file(fielname):
    '''
    读取文件。返回以json格式的数据
    #反序列读取
    :param fielname:
    :return:
    '''
    with open(fielname,'r+') as f:

        data = json.load(f)
        print(type(data))


    return data


def write_file_json(filename):
    '''
    数据写成json格式的文件
    序列化写成json格式的文件也可以写成txt单里面保存的数据是json格式
    :param filename: 要写成文件的名字
    data 是你序列化写的数据
    :return:
    '''
    data = {'name':'邓旭东'}
    with open(filename+'.txt','w+') as f:
        json.dump(data,f)

# write_file_json('测试一下')
a = read_json_file('测试一下.txt')
print(a)