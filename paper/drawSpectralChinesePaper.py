# 根据数据画出所需要的光谱图象
import matplotlib.pyplot as plt
from matplotlib import gridspec
from astropy.io import fits
import os
import copy
import numpy as np
import random

#对单个光谱数据的处理
def readfits(path,fileName):
    dfu = fits.open(path + '/'+fileName)
    #初始波长
    beginWave = dfu[0].header['COEFF0']
    #步长
    step = dfu[0].header['CD1_1']
    #光谱中的流量 
    flux = dfu[0].data[0]
    #求出波长,求出与流量对应的波长
    wave = np.array([10**(beginWave + step*j) for j in range(len(flux))])
    data = [wave,flux]
    #-------------------------------------------
    # return data,poistion
    return data

# 取其中一部分波长和流量
def chooseSpectralData(data):
    # 截取的范围
    choose_wave = []
    choose_flux = []
    wave, flux = data[0], data[1]
    length = len(wave)
    for index in range(length):
        if 3900 < wave[index] < 6800:
            choose_wave.append(wave[index])
            choose_flux.append(flux[index])
    # print(choose_wave[:35])
    return [choose_wave, choose_flux]

#数据文件中的光谱数据
def exractData(fileName):
    listFile = os.listdir(fileName)
    dataSet = []
    allPoistion = []
    for file in listFile:
        dfu = fits.open(fileName + '/'+file)
        #读出数据并且保存
        data,poistion = readfits(fileName,file)
        dataSet.append(data)
        allPoistion.append(poistion)
    #os.chdir(os.pardir)
    return dataSet,np.array(allPoistion)

def drawPic(data, word):
    wave,flux = data[0],data[1]
    gap = (max(flux) - min(flux)) / 8
    max_y = max(flux) + gap
    min_y = min(flux) - gap
    text_pos = max(flux)
    # print('wave:', wave)
    # print('flux:', flux)
    fig = plt.figure(figsize=(9,7))
    plt.ylabel('flux (relative)', fontsize=15)


    # 画4105的标识线
    plt.vlines(4101.734, min_y, max_y, colors = 'gray', linewidth=1.0, linestyles = ':')
    plt.text(4105, text_pos, r'$H\delta$')

    # Hbeta的标识线
    plt.vlines(4861.325, min_y, max_y, colors = 'gray', linewidth=1.0, linestyles = ':')
    plt.text(4866, text_pos, r'$H\beta$')

    # OIII的标识线
    # 适合A5
    # plt.vlines(4958.911, min_y, max_y, colors = 'gray', linewidth=1.0, linestyles = ':')
    # plt.text(4962, text_pos-1500, r'OIII')

    # 适合K5
    plt.vlines(4958.911, min_y, max_y, colors = 'gray', linewidth=1.0, linestyles = ':')
    plt.text(4962, text_pos-4500, r'OIII')

    plt.vlines(5006.843, min_y, max_y, colors = 'gray', linewidth=1.0, linestyles = ':')
    plt.text(5010, text_pos, r'OIII')

    # 画5875.67的标识线
    plt.vlines(5875.67, min_y, max_y, colors = 'gray', linewidth=1.0, linestyles = ':')
    plt.text(5780, text_pos, r'Hel')

    # 画OI的标识线
    plt.vlines(6300.304, min_y, max_y, colors = 'gray', linewidth=1.0, linestyles = ':')
    plt.text(6305, text_pos, r'OI')

    # 下面是NII
    plt.vlines(6548.040, min_y, max_y, colors = 'gray', linewidth=1.0, linestyles = ':')
    plt.text(6453, text_pos, r'NII')

    # 画6564的标识线
    # 适合A5
    # plt.vlines(6562.800, min_y, max_y, colors = 'gray', linewidth=1.0, linestyles = ':')
    # plt.text(6568, text_pos-1500, r'$H\alpha$')
    # 适合K5
    plt.vlines(6562.800, min_y, max_y, colors = 'gray', linewidth=1.0, linestyles = ':')
    plt.text(6568, text_pos-4500, r'$H\alpha$')


    plt.vlines(6583.460, min_y, max_y, colors = 'gray', linewidth=1.0, linestyles = ':')
    plt.text(6590, text_pos, r'NII')

    # 下面是SII
    plt.vlines(6716.440, min_y, max_y, colors = 'gray', linewidth=1.0, linestyles = ':')
    plt.text(6721, text_pos, r'SII')

    # 下面是Ca
    plt.vlines(3933.66, min_y, max_y, colors = 'gray', linewidth=1.0, linestyles = ':')
    plt.text(3800, text_pos, r'CaK')

    plt.vlines(3968.45, min_y, max_y, colors = 'gray', linewidth=1.0, linestyles = ':')
    plt.text(3972, text_pos, r'CaH')
    
    # 下面是Na
    plt.vlines(5891.94, min_y, max_y, colors = 'gray', linewidth=1.0, linestyles = ':')
    plt.text(5897, text_pos, r'NaD')

    plt.xlabel('wavelength ('+word+')', fontsize=15)
    plt.plot(wave, flux, c='black', linewidth=0.8)
    
    
    plt.show()





if __name__ == '__main__':
    # data = readfits('newSpectral/A5V','spec-55889-F8906_sp01-122.fits.gz')
    # data = readfits('newSpectral/A5V','spec-55903-B90304_sp03-132.fits.gz')
    # data = readfits('newSpectral/K5','spec-56199-EG000313N173308V_1_sp02-001.fits.gz')
    data = readfits('newSpectral/K5','spec-56200-EG004228N273834V_1_sp06-148.fits.gz')
    word = 'A'   
    with open('word.txt', 'r', encoding='utf-8') as f:
        word = f.read()
    # print(word)

 
    choose_data = chooseSpectralData(data)
    drawPic(choose_data,word)
    print()

    



