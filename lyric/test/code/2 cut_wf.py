# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 10:04:54 2016

@author: QingLing
"""

import pandas as pd
import jieba

inputfile = 'wangfeng_clean.txt'
outputfile = 'wangfeng_cut.txt'

data = pd.read_csv(inputfile, encoding='utf=8', header=None)
# define the cut function
mycut = lambda s: ' '.join(jieba.cut(s))
# Use space' ' to join the cutted results
data = data[0].apply(mycut)
# data #cutted prefect
data.to_csv(outputfile, index=False, header=False, encoding='utf-8')
