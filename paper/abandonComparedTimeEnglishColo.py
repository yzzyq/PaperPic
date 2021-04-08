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
    legend_set = ['ASUWO', 'BSVM', 'MSSVM', 'multitrain', 'ssoSMOTEsso','VBensembles','wdchange']
    time_all = [['ASUWO','3611',426.7037862000001],
                ['ASUWO','8202',891.5890271],
                ['ASUWO','19411',3178.1495494],
                ['BSVM','3611',10274.7325741],
                ['BSVM','8202',10819.2379265],
                ['BSVM','19411',13170.1219843],
                ['MSSVM','3611',47983.3081783],
                ['MSSVM','8202',48500.3794513],
                ['MSSVM','19411',50727.5763556],
                ['multitrain','3611',3376.6669303999997],
                ['multitrain','8202',4050.7318622],
                ['multitrain','19411',8042.715062099998],
                ['ssoSMOTEsso','3611',522.5266335],
                ['ssoSMOTEsso','8202',968.1393223],
                ['ssoSMOTEsso','19411',3298.7447880000004],
                ['VBensembles','3611',35116.1679848],
                ['VBensembles','8202',35616.2371611],
                ['VBensembles','19411',37915.40542829999],
                ['wcrank','3611',98.2074937],
                ['wcrank','8202',424.29736790000004],
                ['wcrank','19411',2004.5705459]]
    time_pd = pd.DataFrame(time_all,columns=['algorithm_name','number','time'])
    data_num = [3611,8202,19411]
    sns.set_style('darkgrid',{"axes.facecolor": ".10"})
    sns.set_context('paper',font_scale=1.3,rc={"lines.linewidth": 1.7})
    sns.set(font_scale=1.2,font='Times New Roman')
    sns.set_style("ticks")
    plt.figure(figsize=(10,7))
    #plt.title('all algorithms time')
    plt.xlim((0,51000))
    sns.barplot(x = 'time',y = 'algorithm_name',hue = 'number',linewidth = 1.5,data =time_pd,palette='Set2')
##    sns.barplot(x = '3611',y = 'algorithm_name',linewidth = 2.5,data =time_pd )
    
##    ax = plt.gca()
##    box = ax.get_position()
##    ax.set_position([box.x0, box.y0, box.width*0.85 , box.height])
##    plt.legend(bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0,fontsize = 9,
##               handleheight = 3)
    plt.grid(True)
    

    plt.show()
