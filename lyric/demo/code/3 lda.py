# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 23:22:31 2016

@author: QingLing

YOU MUST USE Python3 !!!
"""

import pandas as pd
from gensim import corpora,models

inputfile = 'vae_cut.txt'
stoplist = 'stoplist.txt'

data = pd.read_csv(inputfile,encoding = 'utf-8', header =None)
stop = pd.read_csv(stoplist, encoding = 'utf-8', header = None, sep = 'tipdm',engine='python')
stop = [' ', ''] + list(stop[0])

data[1] = data[0].apply(lambda s: s.split(' ')) #定义一个分割函数，然后用apply广播
data[2] = data[1].apply(lambda x: [i for i in x if i not in stop]) #逐词判断是否停用词，思路同上


data_dict = corpora.Dictionary(data[2])
data_corpus = [data_dict.doc2bow(i) for i in data[2]]
data_lda = models.LdaModel(data_corpus, num_topics=3, id2word=data_dict)

for i in range(3):
    data_lda.show_topic(i) #输出每个主题


"""
data_lda.show_topic(0)

[('一个', 0.01337413294048086),
 ('做', 0.0086063464749015599),
 ('江南', 0.0079807473174709227),
 ('梦境', 0.0077907314132819117),
 ('一天', 0.0074494574476564853),
 ('熟悉', 0.0063196215037977007),
 ('想', 0.0059114604367196599),
 ('心', 0.0057991125557976851),
 ('前', 0.0055810621179508135),
 ('继续', 0.0054994154627434708)]
 
 '0.013*一个 + 0.009*做 + 0.008*江南 + 0.008*梦境 + 0.007*一天 + 
 0.006*熟悉 + 0.006*想 + 0.006*心 + 0.006*前 + 0.005*继续'

data_lda.show_topic(1)

[('天上', 0.012831787333501505),
 ('出现', 0.010989822992194734),
 ('从前', 0.0080820497830311911),
 ('遥远', 0.0080037841633056207),
 ('爱', 0.0075236663972912702),
 ('回到', 0.006009291177056752),
 ('穿', 0.0055107300146477077),
 ('离别', 0.0054726122328166314),
 ('奇迹', 0.0054635025273411459),
 ('一分钟', 0.0052939208418974967)]

'0.013*天上 + 0.011*出现 + 0.008*从前 + 0.008*遥远 + 0.008*爱 + 
0.006*回到 + 0.006*穿 + 0.005*离别 + 0.005*奇迹 + 0.005*一分钟'

data_lda.show_topic(2)

[('爲', 0.011713958266369007),
 ('爱', 0.0070329844044813112),
 ('感情', 0.006415102585026383),
 ('是不是', 0.0062907833029337366),
 ('街上', 0.0059741034146154545),
 ('浪漫', 0.0056755325820853257),
 ('人群', 0.00567016656711322),
 ('逆向', 0.00567016656711322),
 ('只', 0.0046613330445985013),
 ('画面', 0.0043284871289807139)]
 
 '0.012*爲 + 0.007*爱 + 0.006*感情 + 0.006*是不是 + 0.006*街上 + 
 0.006*浪漫 + 0.006*人群 + 0.006*逆向 + 0.005*只 + 0.004*画面'
"""