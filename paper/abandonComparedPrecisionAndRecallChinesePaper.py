import copy
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import xlwt
import os
from matplotlib.font_manager import FontProperties




if __name__ == '__main__':

    three_all_recall_precise = [[[2000,0.275,0.2522],[8000,0.31875,0.38403614457831325],
                                 [16000,0.25,0.22],[18000,0.20,0.19],
                                 [20000,0.23,0.25]],
                                
                                [[2000,0.505,0.754],[8000,0.525,0.753],
                                 [16000,0.50625,0.752],[18000,0.50125,0.757],
                                 [20000,0.50555555555556,0.75138896605366]],

                                [[2000,0.27777777777777776,0.34],[8000,0.10216346153846154,0.25],
                                 [16000,0.12154696132596685,0.24],[18000,0.10501606127996046,0.16],
                                 [20000,0.0770106475590973,0.152]],

                                [[2000,0.605,0.67],[8000,0.58,0.61],
                                 [16000,0.60625,0.69],[18000,0.56,0.65],
                                 [20000,0.60555555555556,0.70]],

                                [[2000,0.955,0.95045],[8000,0.932, 0.94],
                                 [16000,0.923, 0.93],[18000, 0.912, 0.921],
                                 [20000,0.914,0.908]]

                    
                                ]
    
    myfont=FontProperties(fname='C:\Windows\Fonts\simhei.ttf',size=14)
    sns.set(font=myfont.get_name(),style='ticks')
    # sns.set_style('darkgrid',{"axes.facecolor": ".9"})
##    sns.set_palette('Set2')
    sns.set_context('paper',font_scale=1.5,rc={"lines.linewidth": 1.7})
    # sns.set(font=myfont.get_name())
    # sns.set(font_scale=1.5,font='Times New Roman',style='ticks')
    # plt.style.use('ggplot')
    # sns.set_style("ticks")
    plt.figure(figsize=(11,8))
    # plt.title('对比算法的精确率和召回率')
    # plt.title('recall and precise of all algorithms')
##    fig,ax = plt.subplots()
    x_data = ['2000','8000','16000','18000','20000']
    # x_data = ['data set A', 'data set B', 'data set C', 'data set D', 'data set E']
    # x_data = ['3611','8202','12872','19411','58233','77644','97055','116466']
    # color_set = ['salmon', 'amber', 'baby poop green','aqua','black']
    # color_set = ['grey','grey','grey','grey','grey','grey','black']
    color_set = ['black','black','black','black','black','black','black']
    line_width_set = [1, 1, 1, 1, 3]
    legend_set = ['DJ-Cluster', 'K-Means', 'hierCluster', 'DBSCAN', 'FDCC']
##    fig,ax = plt.subplots()
    use_markers = ['+', '*', 'o', '^', 'D', 'X', '_']
    plt.ylim((0, 1))
    for index in range(len(three_all_recall_precise)):
        all_recall_precise = np.array(three_all_recall_precise[index])
#         plt.scatter(x_data,
# ##                    all_recall_precise[:,0],
#                     all_recall_precise[:,1],
#                     c = sns.xkcd_rgb[color_set[index]],
#                     marker = '*',
#                     alpha=0.5)
        plt.plot(x_data,
                 all_recall_precise[:,1],
                #  label= legend_set[index] + ' recall',
                 label= legend_set[index] + '召回率',
                 c = sns.xkcd_rgb[color_set[index]],
                 linestyle=':',
                 linewidth=line_width_set[index],
                 marker=use_markers[index],markersize=6)
        # plt.scatter(x_data,
        #             all_recall_precise[:,2],
        #             c = sns.xkcd_rgb[color_set[index]],
        #             alpha=0.5)
        plt.plot(x_data,
                 all_recall_precise[:,2],
                #  label= legend_set[index] + ' precision',
                 label= legend_set[index] + '精确率',
                 linewidth=line_width_set[index],
                 c = sns.xkcd_rgb[color_set[index]]
                 ,marker=use_markers[index],markersize=6)
##    plt.legend(loc='best')
    ax = plt.gca()
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width*0.85 , box.height])
    # plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0, fontsize = 12,
    #            handleheight = 3)
    plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0, fontsize = 12, edgecolor='black', handleheight = 3)
    # plt.legend(bbox_to_anchor=(1, 1.02))
    # plt.xticks(['617','3611','8202','12872','19411','38822','58233','77644','97055','116466'])
    # plt.xticks(['617','3611','8202','12872','19411'])
    # plt.xticks(['3611','8202','12872','19411','58233','77644','97055','116466'])
    plt.xlabel('五种不同数据量')
    plt.ylabel('精确率和召回率')
    # plt.grid(True)
    sns.despine()
    # plt.savefig('C:/Users/yzzyq/Desktop/pic/all-algorithm-2.eps', dpi = 600, format = 'eps')

    plt.show()
