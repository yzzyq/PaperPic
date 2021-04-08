import copy
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import xlwt
import os
from matplotlib.font_manager import FontProperties


if __name__ == '__main__':
    
    three_all_recall_precise = [
                                [[617,1,1],[3611,1,0.966],[8202,1,0.947],\
                                 [12872,1,0.925],[19411,1,0.959]]
                                 #[38822,1,0.916],[58233,1,0.918],[77644,1,0.911],[97055,1,0.917],[116466,1,0.909]]
                                ]
    
    #myfont=FontProperties(fname='C:\Windows\Fonts\simhei.ttf',size=14)
    # sns.set(font=myfont.get_name())
    # sns.set_style('darkgrid',{"axes.facecolor": ".9"})
    # sns.set_style("white",{"axes.facecolor": ".9"})
    # sns.set_style("white")
##    sns.set_palette('Set2')
    sns.set_context('paper',font_scale=1.5,rc={"lines.linewidth": 1.7})
    # sns.set(font=myfont.get_name())
    sns.set(font_scale=1.5,font='Times New Roman')
    sns.set_style("ticks")
    # plt.style.use('ggplot')
    plt.figure(figsize=(9,7))
    # plt.title('对比算法的精确率和召回率')
    # plt.title('precise of this algorithm when recall is 1')
##    fig,ax = plt.subplots()
    x_data = ['617','3611','8202','12872','19411']
    #x_data = ['617','3611','8202','12872','19411','38822','58233','77644','97055','116466']
    color_set = ['salmon', 'amber', 'baby poop green','aqua', 'windows blue', 'baby purple','bubblegum pink']
    color_set = ['black']
    # legend_set = ['ASUWO', 'BSVM', 'MSSVM', 'multitrain', 'ssoSMOTEsso','VBensembles','wdchange']
##    fig,ax = plt.subplots()
    for index in range(len(three_all_recall_precise)):
        all_recall_precise = np.array(three_all_recall_precise[index])
#         plt.scatter(x_data,
# ##                    all_recall_precise[:,0],
#                     all_recall_precise[:,1],
#                     c = sns.xkcd_rgb[color_set[index]],
#                     marker = '*',
#                     alpha=0.5)
#         plt.plot(x_data,
#                  all_recall_precise[:,1],
#                  label= legend_set[index] + ' recall',
#                  c = sns.xkcd_rgb[color_set[index]],
#                  linestyle=':',
#                  marker='|')
        plt.scatter(x_data,
                    all_recall_precise[:,2],
                    c = sns.xkcd_rgb[color_set[index]],
                    alpha=0.5)
        plt.plot(x_data,
                 all_recall_precise[:,2],
                #  label= legend_set[index] + ' precise',
                 c = sns.xkcd_rgb[color_set[index]])
##    plt.legend(loc='best')
    # ax = plt.gca()
    # box = ax.get_position()
    # ax.set_position([box.x0, box.y0, box.width*0.85 , box.height])
    # plt.legend(bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0,fontsize = 9,
    #            handleheight = 3)
    plt.xticks(['617','3611','8202','12872','19411'])
    #plt.xticks(['617','3611','8202','12872','19411','38822','58233','77644','97055','116466'])
    plt.xlabel('the number of test data')
    # plt.grid(True)
    

    plt.show()
