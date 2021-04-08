import copy
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import xlwt
import os
from matplotlib.font_manager import FontProperties





if __name__ == '__main__':
    
    myfont=FontProperties(fname=r'C:\Windows\Fonts\simhei.ttf',size=20)

    color_set = ['salmon', 'amber', 'baby poop green','aqua', 'windows blue', 'baby purple','bubblegum pink']
    legend_set = ['DJ-Cluster', 'K-Means', 'hierCluster', 'DBSCAN', 'CH-CCFDAC']
    time_all = [['DJ-Cluster','2000',61.0291597],
                ['DJ-Cluster','16000',410.0025457],
                ['DJ-Cluster','20000',600.1495494],
                ['K-Means','2000',13.078463000000001],
                ['K-Means','16000', 79.8131372],
                ['K-Means','20000',86.3447208],
                ['hierCluster','2000',8.4250221],
                ['hierCluster','16000',171.1488256],
                ['hierCluster','20000',379.9984246],
                ['DBSCAN','2000',11.253993499999998],
                ['DBSCAN','16000',108.76235630000001],
                ['DBSCAN','20000',136.9092218],
                ['CH-CCFDAC','2000',5.525],
                ['CH-CCFDAC','16000',70.0067505999999999955],
                ['CH-CCFDAC','20000',81.005444999999999978]]
    time_pd = pd.DataFrame(time_all,columns=['算法名称的缩写','数据集的大小','时间 (s)'])
    # data_num = [2000,16000,20000]
    data_num = ['2000', '16000', '20000']
    sns.set_style('darkgrid',{"axes.facecolor": ".10"})
    sns.set_context('paper',font_scale=1.3,rc={"lines.linewidth": 1.7})
    #sns.set(font_scale=1.2,font='Times New Roman')
    sns.set_style("ticks")
    sns.set(font_scale=1.4,font=myfont.get_name(),style = 'ticks')
    
    color = ['darkblue','darkorange','darkgreen']
    sns.color_palette(color)
    plt.figure(figsize=(10,7))
    #plt.title('all algorithms time')
    plt.xlim((0,51000))
    sns.barplot(x = '算法名称的缩写',y = '时间 (s)',hue = '数据集的大小',linewidth = 1.5, data =time_pd, palette = 'Set2')
##    sns.barplot(x = '3611',y = 'algorithm_name',linewidth = 2.5,data =time_pd )
    
##    ax = plt.gca()
##    box = ax.get_position()
##    ax.set_position([box.x0, box.y0, box.width*0.85 , box.height])
##    plt.legend(bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0,fontsize = 9,
##               handleheight = 3)
    plt.grid(True)
    #plt.savefig('C:/Users/yzzyq/Desktop/pic/all-time-3.eps', dpi = 600, format = 'eps')

    plt.show()
