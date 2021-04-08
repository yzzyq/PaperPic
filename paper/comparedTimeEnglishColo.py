import copy
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import xlwt
import os
from matplotlib.font_manager import FontProperties





if __name__ == '__main__':
    color_set = ['salmon', 'amber', 'baby poop green','aqua', 'windows blue', 'baby purple','bubblegum pink']
    legend_set = ['ASUWO', 'BSVM', 'MSSVM', 'multitrain', 'ssoSMOTEsso','VBensembles','WEDA']
    time_all = [['ASUWO','data set B',426.7037862000001],
                ['ASUWO','data set C',891.5890271],
                ['ASUWO','data set E',3178.1495494],
                ['BSVM','data set B',10274.7325741],
                ['BSVM','data set C',10819.2379265],
                ['BSVM','data set E',13170.1219843],
                ['MSSVM','data set B',47983.3081783],
                ['MSSVM','data set C',48500.3794513],
                ['MSSVM','data set E',50727.5763556],
                ['multitrain','data set B',3376.6669303999997],
                ['multitrain','data set C',4050.7318622],
                ['multitrain','data set E',8042.715062099998],
                ['ssoSMOTEsso','data set B',522.5266335],
                ['ssoSMOTEsso','data set C',968.1393223],
                ['ssoSMOTEsso','data set E',3298.7447880000004],
                ['VBensembles','data set B',35116.1679848],
                ['VBensembles','data set C',35616.2371611],
                ['VBensembles','data set E',37915.40542829999],
                ['WEDA','data set B',628.368223],
                ['WEDA','data set C',1897.9358915],
                ['WEDA','data set E',2247.3452148]]
    time_pd = pd.DataFrame(time_all,columns=['the name of algorithm','data set','time (s)'])
    # data_num = [3611,8202,19411]
    data_num = ['data set B', 'data set C', 'data set E']
    sns.set_style('darkgrid',{"axes.facecolor": ".10"})
    sns.set_context('paper',font_scale=1.5,rc={"lines.linewidth": 1.7})
    sns.set(font_scale=1.2,font='Times New Roman')
    sns.set_style("ticks")
    color = ['darkblue','darkorange','darkgreen']
    sns.color_palette(color)
    plt.figure(figsize=(10, 7))
    #plt.title('all algorithms time')
    plt.xlim((0,51000))
    sns.barplot(x = 'the name of algorithm',y = 'time (s)',hue = 'data set',linewidth = 1.7,data =time_pd, palette = 'Set2')

    plt.grid(True)
    # plt.savefig('C:/Users/yzzyq/Desktop/pic/all-time-3.eps', dpi = 1200, format = 'eps')

    plt.show()
