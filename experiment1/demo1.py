# -*- coding: utf-8 -*-
import datetime
import json
import math
import operator

def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4E00' and uchar <= u'\u9FA5':
        return True
    else:
        return False


def count_chinese_word(filepath, encoding):

    _dict = {}
    dict = {}
    account = 0
    try:
        with open(filepath, 'r') as txt_file:
            for line in txt_file:
                ustr = line.decode(encoding)
                for uchar in ustr:
                    if is_chinese(uchar):
                        account += 1
                        if _dict.has_key(uchar):
                            _dict[uchar] = _dict[uchar] + 1
                        else:
                            _dict[uchar] = 1
    except IOError as ioerr:
        print "文件", filepath, "不存在"
    print "词数：",account,"词"
    sorted_dict = sorted(_dict.iteritems(), key=lambda d: d[1], reverse=True)   # 排序

    print "---",type(sorted_dict)
    return sorted_dict,account

def cal_chinese_word_top100(_dict,_account):
    i = 0
    print _account
    _list = [[1 for x in range(2)] for y in range(100)]
    while i<100:

        _list[i][0]=_dict[i][0]
        _list[i][1]=float(_dict[i][1])/float(_account)
        i += 1

    return _list
def cal_chinese_word_7(_dict,_account):
    fruency1 = 0
    fruency20 = 0
    fruency100 = 0
    fruency600 = 0
    fruency2000 = 0
    fruency3000 = 0
    fruency6000 = 0
    i = 0
    newAccount = 0.0
    fruency1 = float(_dict[0][1])/float(_account)
    while i<20:
        newAccount = newAccount + _dict[i][1]
        i += 1
    fruency20 = float(newAccount)/float(_account)
    newAccount = 0.0
    i = 0
    while i<100:
        newAccount = newAccount + _dict[i][1]
        i += 1
    fruency100 = float(newAccount)/float(_account)
    newAccount = 0.0
    i = 0
    while i<600:
        newAccount = newAccount + _dict[i][1]
        i += 1
    fruency600 = float(newAccount)/float(_account)
    newAccount = 0.0
    i = 0
    while i<2000:
        newAccount = newAccount + _dict[i][1]
        i += 1
    fruency2000 = float(newAccount)/float(_account)
    newAccount = 0.0
    i = 0
    while i<3000:
        newAccount = newAccount + _dict[i][1]
        i += 1
    fruency3000 = float(newAccount)/float(_account)
    newAccount = 0.0
    i = 0
    fruency6000 = fruency3000
    #使用的语料没有超出3000个生字
    # while i<6000:
    #     newAccount = newAccount + _dict[i][1]
    #     i += 1
    # print newAccount,_account
    # fruency6000 = float(newAccount)/float(_account)
    # newAccount = 0.0
    return fruency1, fruency20, fruency100, fruency600, fruency2000, fruency3000, fruency6000
#计算熵
def cal_entropy(_list):

    entropy = 0.0
    i = 0
    while i<100:

        entropy += -math.log(_list[i][1])
        i +=1
    return entropy

if __name__ == '__main__':

    begin = datetime.datetime.now()
    _dict,_account = count_chinese_word('test.txt', 'GBK')

    """给出前100个汉字高频字的频率统计结果"""
    _list = cal_chinese_word_top100(_dict, _account)
    print "前100的词频：", json.dumps(_list, encoding="utf-8", indent=2, ensure_ascii=False)
    """给出前1、20、100、600、2000、3000、6000汉字的字频总和"""
    fruency1, fruency20, fruency100, fruency600, fruency2000, fruency3000, fruency6000 = cal_chinese_word_7(_dict,_account)
    print "前1、20、100、600、2000、3000、6000汉字的字频总和：",fruency1,fruency20,fruency100,fruency600,fruency2000,fruency3000,fruency6000
    print "------------------"
    """计算汉字的熵值"""
    entropy = cal_entropy(_list)
    print "汉字熵值为：",entropy
    end = datetime.datetime.now()
    print '运行用时',end - begin