import copy
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import xlwt
import os
from matplotlib.font_manager import FontProperties




if __name__ == '__main__':

    three_all_recall_precise = [[[1, 1.3000485],[2, 1.33955214],
                                 [3, 1.36206945],[4, 1.3375444],
                                 [5, 1.44723436],[6, 1.36206945]],
                                
                                [[1, 1.37745842],[2, 1.31472052],
                                 [3, 1.28737261],[4, 1.35418987],
                                 [5, 1.37124068],[6, 1.35323641]],

                                [[1, 1.39158136],[2, 1.38781867],
                                 [3, 1.46514307],[4, 1.45344138],
                                 [5, 1.39084316],[6, 1.38781867]]
                                ]
    
    myfont=FontProperties(fname='C:\Windows\Fonts\simhei.ttf',size=14)
    sns.set(font=myfont.get_name(),style='ticks')
    sns.set_context('paper',font_scale=1.5,rc={"lines.linewidth": 1.7})

    plt.figure(figsize=(11,8))
    x_data = ['1','2','3','4','5','6']
    # x_data = ['data set A', 'data set B', 'data set C', 'data set D', 'data set E']
    # x_data = ['3611','8202','12872','19411','58233','77644','97055','116466']
    # color_set = ['salmon', 'amber', 'baby poop green','aqua','black']
    # color_set = ['grey','grey','grey','grey','grey','grey','black']
    color_set = ['black','grey','black']
    line_width_set = [2, 2, 2, 1, 3]
    legend_set = ['2000', '8000', '16000']
##    fig,ax = plt.subplots()
    use_markers = ['+', '*', 'o', '^', 'D', 'X', '_']
    use_linestyle = ['-','-','--']
    # plt.ylim((0, 1))
    for index in range(len(three_all_recall_precise)):
        all_recall_precise = np.array(three_all_recall_precise[index])
        plt.plot(x_data,
                 all_recall_precise[:,1],
                #  label= legend_set[index] + ' recall',
                 label= legend_set[index],
                 c = sns.xkcd_rgb[color_set[index]],
                 linestyle=use_linestyle[index],
                 linewidth=line_width_set[index])
                #  marker=use_markers[index],markersize=6)
    plt.legend(loc='best')
    ax = plt.gca()
    box = ax.get_position()
    # ax.set_position([box.x0, box.y0, box.width*0.85 , box.height])
    # plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0, fontsize = 12, edgecolor='black', handleheight = 3)
    # plt.legend()
    plt.xlabel('迭代次数')
    plt.ylabel('fitness值')
    sns.despine()


    plt.show()
