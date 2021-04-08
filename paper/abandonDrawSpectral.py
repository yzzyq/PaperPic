# 根据数据画出所需要的光谱图象
import matplotlib.pyplot as plt
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

def drawPic(data):
    wave,flux = data[0],data[1]
    # gap = (max(flux) - min(flux))/30
    # max_y = max(flux) + gap
    # min_y = min(flux) - gap
    max_y = 0.9
    min_y = 0
    text_pos = 0.85
    print('wave:', wave)
    print('flux:', flux)
    plt.figure(figsize=(9,7))
    plt.ylim(min_y, max_y)
    plt.xlim(6500,6770)
    plt.xlabel('Wavelength')
    plt.ylabel('Flux')
    plt.plot(wave, flux, c='black', linewidth=0.8)
    # 画6564的标识线
    plt.vlines(6564.61, min_y, max_y, colors = 'blue', linewidth=1.0, linestyles = ':')
    plt.text(6568, text_pos, r'$H\alpha$')
    
    # Hbeta的标识线
    plt.vlines(4862.68, min_y, max_y, colors = 'blue', linewidth=1.0, linestyles = ':')
    plt.text(4866, text_pos, r'$H\beta$')

    # 下面是俩个NII
    plt.vlines(6549.86, min_y, max_y, colors = 'blue', linewidth=1.0, linestyles = ':')
    plt.text(6553, text_pos, r'NII')

    plt.vlines(6585.27, min_y, max_y, colors = 'blue', linewidth=1.0, linestyles = ':')
    plt.text(6590, text_pos, r'NII')

    # 下面是俩个SII
    plt.vlines(6718.29, min_y, max_y, colors = 'blue', linewidth=1.0, linestyles = ':')
    plt.text(6721, text_pos, r'SII')

    plt.vlines(6732.67, min_y, max_y, colors = 'blue', linewidth=1.0, linestyles = ':')
    plt.text(6735, text_pos, r'SII')
    # plt.grid(True)

    # 放大某段区间
    plt.axes([0.45,0.15,0.25,0.25])
    plt.plot(wave, flux, c='black', linewidth=0.8)
    plt.ylim(0.2, 0.9)
    plt.xlim(4850, 4874)
    # plt.xlabel('Wavelength')
    # plt.ylabel('Flux')

    # plt.vlines(4862.68, min_y, max_y, colors = 'blue', linewidth=1.0, linestyles = ':')
    plt.vlines(4862.68, 0.2, 0.9, colors = 'blue', linewidth=1.0, linestyles = ':')
    plt.text(4863.5, 0.85, r'Hb')
    # plt.text(4860, 35, r'Hb')

    # plt.grid(True)
    plt.show()





if __name__ == '__main__':
    # 依赖主信息的文件
    # data = readfits('oldSpectral','spec-56618-EG000954N044957B01_sp07-137.fits.gz')
    # data = readfits('oldSpectral','spec-55892-GAC_082N27_M1_sp10-204.fits.gz')
    # data = readfits('oldSpectral','spec-57018-EG004632N152831B01_sp07-188.fits')
    # data = readfits('oldSpectral','spec-55893-F9302_sp07-249.fits.gz')
    # data = readfits('oldSpectral','spec-57785-HD023750N350938V02_sp10-029.fits')
    # data = readfits('oldSpectral', 'spec-57760-HD021554N364614B01_sp16-168.fits')
    # data = readfits('oldSpectral', 'spec-57760-HD021554N364614B01_sp15-096.fits')
    # data = readfits('oldSpectral', 'spec-57659-EG012217N184057M01_sp02-100.fits')
    # data = readfits('oldSpectral', 'spec-56202-EG012535N233041V01_sp07-004.fits')
    data = readfits('oldSpectral','spec-57756-M31029N37B1_sp07-112.fits')
    drawPic(data)
    print()

    




4
