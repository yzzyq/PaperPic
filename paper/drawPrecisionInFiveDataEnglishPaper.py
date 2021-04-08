import copy
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import xlwt
import os
from matplotlib.font_manager import FontProperties
import matplotlib.patches as mpatches



if __name__ == '__main__':
    
    # three_all_recall_precise = [
    #                             [[617,1,1],[3611,1,0.966],[8202,1,0.947],[12872,1,0.925],[19411,1,0.959],[38822,1,0.916],[58233,1,0.918],[77644,1,0.911],[97055,1,0.917],[116466,1,0.909]]
    #                             ]

    # three_all_recall_precise = [
    #                             [[3611,1,0.966],[8202,1,0.947],[12872,1,0.925],[19411,1,0.959],[58233,1,0.918],[77644,1,0.911],[97055,1,0.917],[116466,1,0.909]]
    #                             ]
    three_all_recall_precise = [[617,1,0.96296],[3611,1,0.9494],[8202,1,0.9322],[12872,1,0.9093],[19411,1,0.90994]]
    three_precise = [[1.0, 0.9285714285714286, 1.0],[0.9042553191489362, 0.9900990099009901, 1.0],\
                     [0.9274193548387096, 0.9292035398230089, 1.0],[0.9413489736070382, 0.8837209302325582, 0.8863636363636364],\
                     [0.8736059479553904, 0.944206008583691, 0.967741935483871]]
    
    # myfont=FontProperties(fname='C:\Windows\Fonts\simhei.ttf',size=14)
    # sns.set(font=myfont.get_name())
    # sns.set_style('darkgrid',{"axes.facecolor": ".9"})
    # sns.set_style("white",{"axes.facecolor": ".9"})
    # sns.set_style("white")
##    sns.set_palette('Set2')
    sns.set_context('paper',font_scale=1.6,rc={"lines.linewidth": 1.7})
    # sns.set(font=myfont.get_name())
    sns.set(font_scale=1.6,font='Times New Roman')
    sns.set_style("ticks")
    # plt.style.use('ggplot')
    # plt.figure(figsize=(9,7))
    # plt.ylim((0.9, 1))
    # plt.title('对比算法的精确率和召回率')
    # plt.title('precise of this algorithm when recall is 1')
##    fig,ax = plt.subplots()
    # x_data = ['617','3611','8202','12872','19411']
    x_data = ['data set A', 'data set B', 'data set C', 'data set D', 'data set E']
    # x_data = ['3611','8202','12872','19411','58233','77644','97055','116466']
    # color_set = ['salmon', 'amber', 'baby poop green','aqua', 'windows blue', 'baby purple','bubblegum pink']
    # color_set = ['indianred', 'peru', 'olivedrab', 'cadetblue']
    # color_set = ['darkred', 'darkorange', 'darkblue', 'darkgreen']
    color_set = ['teal','olive', 'steelblue', 'peru', 'none']
    # color_set = ['rouge', 'dark orange', 'baby poop', 'dark blue', 'dark green']
    # color_set = ['darkblue','darkorange','darkgreen','black']
    # color_set = ['blue', 'green', 'yellow','black', 'gray', 'baby purple','bubblegum pink']
    # legend_set = ['ASUWO', 'BSVM', 'MSSVM', 'multitrain', 'ssoSMOTEsso','VBensembles','wdchange']
##    fig,ax = plt.subplots()
    # for index in range(len(three_all_recall_precise)):
    width = 0.2
    all_recall_precise = np.array(three_all_recall_precise)
    # plt.bar(x_data, all_recall_precise[:,2])
    # plt.xticks(x_data)
    # plt.xlabel('data set')
    # plt.ylabel('precision')
    # plt.show()
    
    three_precise = np.array(three_precise)
    # plt.figure(figsize=(12,10))
    fig, ax = plt.subplots(figsize=(10, 8))
    

    
    x = np.arange(len(x_data))
    # print(x)
    rects0 = ax.bar(x, all_recall_precise[:,2], width*3, facecolor = 'none', zorder=2, linewidth=1, linestyle = '--', edgecolor = 'black')
    rects1 = ax.bar(x - width, three_precise[:,0], width, label='0 < SNR < 10', zorder=1,facecolor = color_set[1], edgecolor = 'white')
    rects2 = ax.bar(x, three_precise[:,1], width, label='10 < SNR < 50', zorder=1, facecolor = color_set[2], edgecolor = 'white')
    rects3 = ax.bar(x + width, three_precise[:,2], width, label='SNR > 50', zorder=1, facecolor = color_set[3], edgecolor = 'white')
    
    # 在柱状图上显示数值
    # for x,y in zip(x, all_recall_precise[:,2]):
    #     ax.text(x + 0.5, y, '%.2f' % y, ha = 'center', va = 'bottom')

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            # height = format()
            ax.annotate('{:.2f}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 0.1),  # 3 points vertical offset
                        fontsize=11,
                        textcoords="offset points",
                        ha='center', va='bottom')
    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)
    



    # plt.xticks(x_data)
    ax.set_xticklabels(('0', 'data set A', 'data set B', 'data set C', 'data set D', 'data set E'),fontsize=13)
    # ax.set_yticklabels(('0', 'data set A', 'data set B', 'data set C', 'data set D', 'data set E'))
    # ax.set_yticklabels(('0', '1', '0.75', '0.5', '0.25', '0', '0.25', '0.5', '0.75', '1'),fontsize=13)
    # ax.set_yticklabels((0, 0.92, 0.94, 0.96, 0.98, 1),fontsize=13)
    ax.set_yticks(np.linspace(0,1,11))
    ax.set_yticklabels((0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1), fontsize=13)
    # plt.ylim(-1.2,1.2)
    plt.xlabel('data set',fontsize=18)
    plt.ylabel('precision',fontsize=18)
    
    labels = ['0 < SNR < 10', '10 < SNR < 50', 'SNR > 50', 'average']
    linestyles = ['-','-','-','--']
    edgecolors = ['none','none','none','black']
    patches = [mpatches.Patch(
                            #   color=color_set[i+1], 
                              label='{:s}'.format(labels[i]),
                              linewidth=1,
                              linestyle=linestyles[i],
                              facecolor=color_set[i+1],
                              edgecolor=edgecolors[i]) for i in range(len(labels))]
    print(patches)
    ax = plt.gca()
    box = ax.get_position()
    print('box:',box)
    ax.set_position([box.x0, box.y0, box.width , box.height*0.8])
    ax.legend(handles=patches, bbox_to_anchor=(0.9, 1.07), ncol=4, edgecolor='white', handlelength=0.8, fontsize=13)

    
    fig.subplots_adjust(hspace=0.8)

    # plt.savefig('C:/Users/yzzyq/Desktop/pic/amountOfData-2.eps', dpi = 1200, format = 'eps')
    

    plt.show()
