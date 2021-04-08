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
    # three_precise = [[1.0, 0.9285714285714286, 1.0],[0.9042553191489362, 0.9900990099009901, 1.0],\
    #                  [0.9274193548387096, 0.9292035398230089, 1.0],[0.9413489736070382, 0.8837209302325582, 0.8863636363636364],\
    #                  [0.8736059479553904, 0.944206008583691, 0.967741935483871]]
    # three_precise = [[426.7037862000001,891.5890271,3178.1495494],[10274.7325741,10819.2379265,13170.1219843],\
    #                  [47983.3081783,48500.3794513,50727.5763556],[3376.6669303999997,4050.7318622,8042.715062099998],\
    #                  [522.5266335,968.1393223,3298.7447880000004],[35116.1679848,35616.2371611,37915.40542829999],\
    #                  [628.368223,1897.9358915,2247.3452148]]
    
    # 召回率
    three_precise =  [[0.275, 0.31875, 0.25, 0.20, 0.23],
                      [0.505, 0.525, 0.50625, 0.50125, 0.50555555555556],
                      [0.27777777777777776, 0.10216346153846154,0.12154696132596685,0.10501606127996046,0.0770106475590973],
                      [0.605,0.58,0.60625,0.56,0.60555555555556],
                      [0.955,0.932,0.923,0.912,0.914]]
    
    # 精确率
    # three_precise =  [[0.2522, 0.38403614457831325, 0.22, 0.19, 0.25],
    #                   [0.754, 0.753, 0.752, 0.757,0.75138896605366],
    #                   [0.34, 0.25, 0.24, 0.16, 0.152],
    #                   [0.67, 0.61, 0.69, 0.65, 0.70],
    #                   [0.95045, 0.94, 0.93, 0.921, 0.908]]


    myfont=FontProperties(fname='C:\Windows\Fonts\simhei.ttf',size=10)
    sns.set(font=myfont.get_name(),style='ticks')
    # sns.set_style('darkgrid',{"axes.facecolor": ".9"})
    # sns.set_style("white",{"axes.facecolor": ".9"})
    # sns.set_style("white")
##    sns.set_palette('Set2')
    # sns.set_context('paper',font_scale=1.5,rc={"lines.linewidth": 1.7})
    # sns.set(font=myfont.get_name())
    # sns.set(font_scale=1.5,font='Times New Roman')
    # sns.set_style("ticks")
    # plt.style.use('ggplot')
    # plt.figure(figsize=(9,7))
    # plt.ylim((0.9, 1))
    # plt.title('对比算法的精确率和召回率')
    # plt.title('precise of this algorithm when recall is 1')
##    fig,ax = plt.subplots()
    # x_data = ['617','3611','8202','12872','19411']
    # x_data = ['DJ-Cluster', 'K-Means', 'hierCluster', 'DBSCAN', 'FDCC']
    x_data = ['数据集A','数据集B', '数据集C','数据集D', '数据集E']
    # x_data = ['data set A', 'data set B', 'data set C', 'data set D', 'data set E']
    # x_data = ['3611','8202','12872','19411','58233','77644','97055','116466']
    # color_set = ['salmon', 'amber', 'baby poop green','aqua', 'windows blue', 'baby purple','bubblegum pink']
    # color_set = ['indianred', 'peru', 'olivedrab', 'cadetblue']
    # color_set = ['darkred', 'darkorange', 'darkblue', 'darkgreen']
    color_set = ['white','black','white','white','gray']
    # color_set = ['teal','olive', 'steelblue', 'peru', 'none']
    # color_set = ['rouge', 'dark orange', 'baby poop', 'dark blue', 'dark green']
    # color_set = ['darkblue','darkorange','darkgreen','black']
    # color_set = ['blue', 'green', 'yellow','black', 'gray', 'baby purple','bubblegum pink']
    # legend_set = ['ASUWO', 'BSVM', 'MSSVM', 'multitrain', 'ssoSMOTEsso','VBensembles','wdchange']
##    fig,ax = plt.subplots()
    # for index in range(len(three_all_recall_precise)):
    width = 0.15
    all_recall_precise = np.array(three_all_recall_precise)
    # plt.bar(x_data, all_recall_precise[:,2])
    # plt.xticks(x_data)
    # plt.xlabel('data set')
    # plt.ylabel('precision')
    # plt.show()
    
    three_precise = np.array(three_precise)
    # plt.figure(figsize=(12,10))
    fig, ax = plt.subplots(figsize=(8, 6))
    

    
    x = np.arange(len(x_data))
    print(x)
    # rects1 = ax.bar(x - width*2, three_precise[0,:], width, label='DJ-Cluster', zorder=1,facecolor = color_set[0],linewidth=1, linestyle = '-')
    rects1 = ax.bar(x - width*2, three_precise[0,:], width, label='DJ-Cluster', zorder=1,facecolor = color_set[0],linewidth=1, linestyle = '-',edgecolor = 'black', hatch = '/')
    rects2 = ax.bar(x - width, three_precise[1,:], width, label='K-Means', zorder=1, facecolor = color_set[1], edgecolor = 'white')
    rects3 = ax.bar(x, three_precise[2,:], width, label='hierCluster', zorder=2, facecolor = color_set[2],linewidth=1, linestyle = '-',edgecolor = 'black', hatch = '-')
    rects4 = ax.bar(x + width, three_precise[3,:], width, label='DBSCAN', zorder=2, facecolor = color_set[3],linewidth=1, linestyle = '-',edgecolor = 'black')
    rects5 = ax.bar(x + width*2, three_precise[4,:], width, label='FDCC', zorder=1, facecolor = color_set[4],linewidth=1)
    
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
    # autolabel(rects1)
    # autolabel(rects2)
    # autolabel(rects3)
    



    # plt.xticks(x_data)
    ax.set_xticklabels(('0', 'Data A','Data B', 'Data C','Data D', 'Data E'),fontsize=14)
    # ax.set_yticklabels(('0', 'data set A', 'data set B', 'data set C', 'data set D', 'data set E'))
    # ax.set_yticklabels(('0', '1', '0.75', '0.5', '0.25', '0', '0.25', '0.5', '0.75', '1'),fontsize=13)
    # ax.set_yticklabels((0, 0.92, 0.94, 0.96, 0.98, 1),fontsize=13)
    # ax.set_yticks(np.linspace(0,1,11))
    ax.set_yticklabels((0.0, 0.2,0.4,0.6,0.8,1.0), fontsize=14)
    plt.ylim(0,1.0)
    plt.xlabel('数据集',fontsize=14)
    plt.ylabel('召回率',fontsize=14)
    # plt.ylabel('准确率',fontsize=14)
    
    labels = ['各算法:', 'DJ-Cluster', 'K-Means', 'hierCluster', 'DBSCAN', 'FDCC']
    linestyles = ['-','-','-','-','-','-']
    edgecolors = ['none','black','none','black','black','none']
    color_set = ['none','white','black','white','white','gray']
    hatch_set = ['none','/','none','-','/','none']
    patches = [mpatches.Patch( 
                              label='{:s}'.format(labels[i]),
                              linewidth=1,
                              linestyle=linestyles[i],
                              facecolor=color_set[i],
                              edgecolor=edgecolors[i],
                              hatch=hatch_set[i]) for i in range(len(labels))]
    # patches = [mpatches.Rectangle(width=20,height=20,xy=(10,10), 
    #                           label='{:s}'.format(labels[i]),
    #                           linewidth=1,
    #                           linestyle=linestyles[i],
    #                           facecolor=color_set[i],
    #                           edgecolor=edgecolors[i],
    #                           hatch=hatch_set[i]) for i in range(len(labels))]
    # patches.insert(0, '对比数据集:')
    ax = plt.gca()
    box = ax.get_position()
    # print('box:',box)
    ax.set_position([box.x0, box.y0, box.width , box.height*0.8])
    ax.legend(handles=patches, bbox_to_anchor=(0.99, 1.07), ncol=6, edgecolor='white', handlelength=1, fontsize=10)
    # ax.legend(handles=patches, bbox_to_anchor=(0.95, 1.12), ncol=3)
    
    fig.subplots_adjust(hspace=0.8)

    #plt.savefig('C:/Users/yzzyq/Desktop/pic/amountOfData-2.eps', dpi = 600, format = 'eps')
    

    plt.show()
