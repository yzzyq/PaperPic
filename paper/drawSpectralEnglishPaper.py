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
    #读出数据中的位置
    #位置
    # ra = dfu[0].header['ra']
    # dec = dfu[0].header['DEC']
    # snrr_stn = dfu[0].header['snrr']
    # snri_stn = dfu[0].header['snri']
    # poistion = [float(ra),float(dec)]
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
        if 4842 < wave[index] < 4882 or 6530 < wave[index] < 6750:
            choose_wave.append(wave[index])
            choose_flux.append(flux[index])
    print(choose_wave[:35])
    return [choose_wave, choose_flux]

#数据文件中的光谱数据
def exractData(fileName):
    listFile = os.listdir(fileName)
    dataSet = []
    allPoistion = []
    for file in listFile:
        dfu = fits.open(fileName + '/'+file)
        # data_class = dfu[0].header['class']
        # print('数据的类别是：',data_class)
        # red = 0
        # if data_class == 'GALAXY':
            # red = searchRedshift(file,redshift,fileName)
        #print(file)
        #读出数据并且保存
        data,poistion = readfits(fileName,file)
        dataSet.append(data)
        allPoistion.append(poistion)
    #os.chdir(os.pardir)
    return dataSet,np.array(allPoistion)

# def drawPic(data):
#     wave,flux = data[0],data[1]
#     # gap = (max(flux) - min(flux))/30
#     # max_y = max(flux) + gap
#     # min_y = min(flux) - gap
#     max_y = 0.9
#     min_y = 0
#     text_pos = 0.85
#     print('wave:', wave)
#     print('flux:', flux)
#     plt.figure(figsize=(9,7))
#     plt.ylim(min_y, max_y)
#     # plt.xlim(6490,6750)
#     plt.xlim(6530,6750)
#     # plt.xticks(range(len(wave)), wave)
#     plt.xlabel('Wavelength')
#     plt.ylabel('Flux')
#     plt.plot(wave, flux, c='black', linewidth=0.8)
#     # 画6564的标识线
#     plt.vlines(6564.61, min_y, max_y, colors = 'blue', linewidth=1.0, linestyles = ':')
#     plt.text(6568, text_pos, r'$H\alpha$')
    
#     # Hbeta的标识线
#     plt.vlines(4862.68, min_y, max_y, colors = 'blue', linewidth=1.0, linestyles = ':')
#     plt.text(4866, text_pos, r'$H\beta$')

#     # 下面是俩个NII
#     plt.vlines(6549.86, min_y, max_y, colors = 'blue', linewidth=1.0, linestyles = ':')
#     plt.text(6553, text_pos, r'NII')

#     plt.vlines(6585.27, min_y, max_y, colors = 'blue', linewidth=1.0, linestyles = ':')
#     plt.text(6590, text_pos, r'NII')

#     # 下面是俩个SII
#     plt.vlines(6718.29, min_y, max_y, colors = 'blue', linewidth=1.0, linestyles = ':')
#     plt.text(6721, text_pos, r'SII')

#     plt.vlines(6732.67, min_y, max_y, colors = 'blue', linewidth=1.0, linestyles = ':')
#     plt.text(6735, text_pos, r'SII')
#     # plt.grid(True)

#     # 放大某段区间
#     # plt.axes([0.45,0.15,0.25,0.25])
#     plt.axes([0,0.11,0.3,0.77])
#     # plt.axes.figsize
#     # plt.axes.figure(figsize = (9,7))
#     plt.plot(wave, flux, c='black', linewidth=0.8)
#     # plt.plot(wave, flux, c='black', linewidth=50)
#     # plt.ylim(0.2, 0.9)
#     plt.ylim(min_y, max_y)
#     plt.xlim(4842, 4882)
#     # plt.xlabel('Wavelength')
#     # plt.ylabel('Flux')

#     # plt.vlines(4862.68, min_y, max_y, colors = 'blue', linewidth=1.0, linestyles = ':')
#     plt.vlines(4862.68, 0.2, 0.9, colors = 'blue', linewidth=1.0, linestyles = ':')
#     plt.text(4863.5, 0.85, r'Hb')
#     # plt.text(4860, 35, r'Hb')

#     # plt.grid(True)
#     plt.show()

def drawPic(data, word):
    wave,flux = data[0],data[1]
    # max_y = 0.9
    # min_y = 0
    gap = (max(flux) - min(flux)) / 8
    max_y = max(flux) + gap
    min_y = min(flux) - gap
    text_pos = max(flux)
    print('wave:', wave)
    print('flux:', flux)
    fig = plt.figure(figsize=(9,7))
    gs = gridspec.GridSpec(1,2, width_ratios = [1,3], wspace=0.1)
    # fig,axes = plt.subplots(1,2,figsize=(9,7),sharey=True)
    # print(len(axes))
    ax0 = fig.add_subplot(gs[0])
    ax1 = fig.add_subplot(gs[1], sharey = ax0)
    plt.setp(ax1.get_yticklabels(), visible=False)
    ax0.set_ylabel('flux (relative)', fontsize=15)
    ax0.set_ylim(min_y,max_y)
    ax0.vlines(4862.68, min_y, max_y, colors = 'cornflowerblue', linewidth=1.0, linestyles = '--')
    ax0.text(4863.5, text_pos, r'Hb', fontsize=15)
    # ax0.text(4860, 35, r'Hb')
    ax0.plot(wave[:35], flux[:35], c='black', linewidth=0.8)
    # ax0.set_yticks(size=15)
    
    ax0.tick_params(axis='both',which='both',labelsize=15)


    # 画6564的标识线
    ax1.vlines(6564.61, min_y, max_y, colors = 'cornflowerblue', linewidth=1.0, linestyles = '--')
    ax1.text(6568, text_pos, r'$H\alpha$', fontsize=15)

    # 下面是俩个NII
    ax1.vlines(6549.86, min_y, max_y, colors = 'cornflowerblue', linewidth=1.0, linestyles = '--')
    ax1.text(6551, text_pos, r'NII', fontsize=15)

    ax1.vlines(6585.27, min_y, max_y, colors = 'cornflowerblue', linewidth=1.0, linestyles = '--')
    ax1.text(6588, text_pos, r'NII', fontsize=15)

    # 下面是俩个SII
    ax1.vlines(6718.29, min_y, max_y, colors = 'cornflowerblue', linewidth=1.0, linestyles = '--')
    ax1.text(6721, text_pos, r'SII', fontsize=15)

    ax1.vlines(6732.67, min_y, max_y, colors = 'cornflowerblue', linewidth=1.0, linestyles = '--')
    ax1.text(6735, text_pos, r'SII', fontsize=15)

    ax1.set_xlabel('wavelength ('+word+')', fontsize=15, position=(0.3,0))
    ax1.plot(wave[36:], flux[36:], c='black', linewidth=0.8)
    ax1.tick_params(axis='both',which='both',labelsize=15)
    plt.subplots_adjust(wspace=0)
    # plt.yticks(size = 15)
    # plt.xticks(size = 15)
   
    # plt.savefig('C:/Users/yzzyq/Desktop/pic/Halpha-perfect.eps', dpi = 1200, format = 'eps')
    # plt.savefig('C:/Users/yzzyq/Desktop/pic/primary-data-Hb.eps', dpi = 1200, format = 'eps')
    # plt.savefig('C:/Users/yzzyq/Desktop/pic/primary-data-NII-Hb.eps', dpi = 1200, format = 'eps')
    # plt.savefig('C:/Users/yzzyq/Desktop/pic/primary-data-none.eps', dpi = 1200, format = 'eps')
    # plt.savefig('C:/Users/yzzyq/Desktop/pic/primary-data-SII.eps', dpi = 1200, format = 'eps')

    # plt.savefig('C:/Users/yzzyq/Desktop/pic/secondary-data-NII-NII-SII-SII.eps', dpi = 1200, format = 'eps')
    # plt.savefig('C:/Users/yzzyq/Desktop/pic/secondary-data-NII-NII-SII.eps', dpi = 1200, format = 'eps')
    # plt.savefig('C:/Users/yzzyq/Desktop/pic/secondary-data-NII-NII.eps', dpi = 1200, format = 'eps')
    #plt.savefig('C:/Users/yzzyq/Desktop/pic/secondary-data-NII-SII.eps', dpi = 1200, format = 'eps')
    
    
    plt.show()





if __name__ == '__main__':
    # 完美的数据，发射线都存在的
    # data = readfits('spectral','spec-55892-GAC_082N27_M1_sp10-204.fits')
    # data = readfits('spectral', 'spec-56202-EG012535N233041V01_sp07-004.fits')



    # 依赖主信息的文件
    # 一条
    # data = readfits('spectral','spec-57785-HD023750N350938V02_sp10-029.fits')

    # # 俩条
    # data = readfits('spectral','spec-56618-EG000954N044957B01_sp07-137.fits')
    # # 三条
    # data = readfits('spectral', 'spec-57357-EG011407N160800B01_sp14-074.fits')
    # # 四条
    # data = readfits('spectral','spec-57698-KP010142N094445B01_sp16-188.fits')



    # # 依赖于次要信息的文件
    # # 三条
    # data = readfits('spectral','spec-55893-F9302_sp07-249.fits')
    # data = readfits('spectral','spec-57018-EG004632N152831B01_sp05-111.fits')
    # # 可以认为四条
    # data = readfits('spectral','spec-57756-M31029N37B1_sp07-112.fits')
    data = readfits('spectral','spec-56601-EG003603N070921M01_sp15-176.fits')
    word = 'A'   
    with open('word.txt', 'r', encoding='utf-8') as f:
        word = f.read()
    print(word)

 
    choose_data = chooseSpectralData(data)
    drawPic(choose_data,word)
    print()

    



