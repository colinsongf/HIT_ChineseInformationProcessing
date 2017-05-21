# -*- coding: utf-8 -*-
#载入文件中词语于集合中，遍历求得词语的最大长度
def file_fun():
    filename = './emma_lexicon/lexicon.dic'
    f = open(filename,encoding = 'utf-8')
    word_set = set()
    length = 1
    for line in f:
        line = line.strip()
        word_set.add(line)
        if len(line) > length:
            length = len(line)
    return length,word_set

#遍历分割begin-end最大长度词是否在集合中，在集合中则加入列表，break,begin = end
#不在列表中，继续for循环判断最大长度-1词是否在集合中
def split_word(sentence,max_len,word_set):
    begin = 0
    words = []
    while begin < len(sentence):
        for end in range(min(begin + max_len,len(sentence)),begin,-1):
            if sentence[begin:end] in word_set or end == begin + 1:
                words.append(sentence[begin:end])
                break
        begin = end
    return words

#获取最大长度和词典集合
max_len,word_set = file_fun()
#正向最大匹配分词
word_list = split_word(input('请输入一句话：'),max_len,word_set)
#输出分割后的词语
for word in word_list:
    print(word)