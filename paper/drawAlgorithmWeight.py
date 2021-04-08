import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.font_manager import FontProperties

# 提取出我们需要的权重数据
def extractWeights(file_name):
    all_weights_data = []
    before_weight = 0
    with open(file_name, 'r') as f:
        for index,line_data in enumerate(f.readlines()):
            # one_weight_data = [index]
            tep = line_data.split('[')[1].split(']')[0]
            temp_weight = tep.split(',')
            temp_weight = [float(weight) for weight in temp_weight]
            if abs(temp_weight[0] - before_weight) > 0.1:
                one_weight_data = [index,'primary weight',temp_weight[0]]
                all_weights_data.append(one_weight_data)
                one_weight_data = [index,'secondary weight',temp_weight[1]]
                all_weights_data.append(one_weight_data)
                before_weight = temp_weight[0]
            if index >= 77:
                break
            # one_weight_data.extend(temp_weight.split(','))
            # one_weight_data = [float(weight) for weight in one_weight_data]
            # print(one_weight_data)
            # all_weights_data.append(one_weight_data)
    return all_weights_data 


if __name__ == '__main__':
    # file_name = '5.txt'
    # file_name = '4.txt'
    file_name = '3.txt'
    # 提取出我们需要的权重数据
    weights = extractWeights(file_name)
    weights_pd = pd.DataFrame(weights, columns = ['number of iterations', 'weight class', 'weight values'])
    print(weights_pd)
    # 画出图像
    # myfont = FontProperties(fname='C:\Windows\Fonts\simhei.ttf', size=14)
    # sns.set(font=myfont.get_name(), style="whitegrid", color_codes=True)
    sns.set(style="whitegrid", color_codes=True)
    sns.set_context('paper', font_scale=1.5, rc={"lines.linewidth":1.7})
    plt.figure(figsize=(10,8))
    plt.ylim((0, 1))
    # sns.pointplot(x = 'number of iterations' , y = 'weight value', hue = 'weight class', data = weights_pd, 
    #               palette = {'primary weight':'g', 'secondary weight':'m'},
    #               markers = ['^','o'], linestyles = ['-', '--'])
    sns.pointplot(x = 'number of iterations' , y = 'weight values', hue = 'weight class', data = weights_pd, 
                  palette = {'primary weight':'g', 'secondary weight':'m'},
                  markers = ['^','o'], linestyles = ['-', '--'])
    # 保存图片
    #plt.savefig('C:/Users/yzzyq/Desktop/pic/0-10-weight-change.eps', dpi = 1200, format = 'eps')
    plt.show()
    




