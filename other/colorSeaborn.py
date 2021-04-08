#seaborn色彩查看

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib.font_manager import FontProperties


if __name__ == '__main__':
    dataSet = np.array([[1.78,2.52,0,1],
                        [2.532,1.235,-45,1],
                        [0.21,2.10,-133,-1],
                        [0.945,1.23,-52,-1],
                        [5.21,6.123,-123,1],
                        [0,5.23,0,-1]])
    dataSet_pd = pd.DataFrame(dataSet,columns=['itself','line','around','class'])
    

    print(dataSet[:,0])
##    sns.distplot(dataSet[0,:],bins=3)
    #基本的散点图，适合数据量小的情况
    myfont=FontProperties(fname='C:\Windows\Fonts\simhei.ttf',size=14)
    sns.set(font=myfont.get_name())
    sns.set_style('darkgrid',{"axes.facecolor": ".9"})
    sns.set_palette('Set2')
    sns.set_context('paper',font_scale=1,rc={"lines.linewidth": 1.5})
    sns.set(font=myfont.get_name())
    f,(ax1,ax2) = plt.subplots(1,2,figsize=(10,6),sharex=True)
##    plt.figure(figsize=(7,5))
##    plt.title('数据的信噪比50以上,权重1-0.5-0.5下阈值的大小与召回、精确的关系')
##    plt.subplot(1,2,1)
    sns.boxplot(x = 'class',y = 'line',data = dataSet_pd,ax=ax1,palette="Set2")
    sns.swarmplot(x = 'class',y = 'line',data = dataSet_pd,ax=ax1,color='.25')
##    plt.subplot(1,2,2)
    sns.swarmplot(x = 'class',y = 'around',data = dataSet_pd,ax=ax2,alpha=.5,color='w')
    sns.violinplot(x = 'class',y = 'around',data = dataSet_pd,ax=ax2,inner=None,palette="Set2")
##    sns.pointplot(x = 'itself',
##                  y = 'class',
##                  data = dataSet_pd,
##                  color = 'm',
##                  markers='*')
##    sns.pointplot(x = 'itself',
##                  y = 'around',
##                  data = dataSet_pd,
##                  color = 'g',
##                  linestyles='--')
##    sns.stripplot(x = 'class',
##                  y = 'itself',
##                  data = dataSet_pd,
##                  color='w',
##                  alpha=.5)
##    sns.violinplot(x = 'class',
##                  y = 'itself',
##                  data = dataSet_pd,
##                   inner=None)
##    sns.violinplot(x = 'itself',
##                  y = 'around',
##                  data = dataSet_pd)
    plt.show()

