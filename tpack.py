#!/usr/bin/python
# -*- coding: UTF-8 -*-
#author: dkcao by 2018-06-08

import os, sys
import commands

#from PyTexturePacker import Packer #pip install PyTexturePacker
 
print "###########start#####################"

TP="TexturePacker"

curpath = raw_input("Please intput dir:")
if curpath == "":
	curpath = os.getcwd()
print curpath


name1 = raw_input("Please intput name:")
output = os.path.join(curpath,"tmp/")
outfile = os.path.join(output,name1)
outPlist = os.path.join(output,name1)

if not os.path.exists(output):
 os.mkdir(output)

filelist = " "

dirs = os.listdir( curpath )
it = iter(dirs)
while True:
    try:
        x = next(it)
        if os.path.isfile(os.path.join(curpath,x)):
	    	filelist += " "
    		filelist += os.path.join(curpath,x)
    except StopIteration:
        break

# cmd = "TexturePacker --sheet {} --data {} --allow-free-size --no-trim --max-size 1024 --format cocos2d {}".format(outfile, outPlist, filelist)
# print cmd
# (status, output) = commands.getstatusoutput(cmd)
# print status,output

# --trim-sprite-names  去除png等后缀  
# --multipack 多图片打包开起，避免资源图太多，生成图集包含不完全，开起则会生成多张图集。  
# --maxrects-heuristics macrect的算法  参数 Best ShortSideFit LongSideFit AreaFit BottomLeft ContactPoint  
# --enable-rotation 开起旋转，计算rect时如果旋转将会使用更优的算法来处理，得到更小的图集  
# --border-padding 精灵之间的间距  
# --shape-padding 精灵形状填充  
# --trim-mode Trim 删除透明像素，大下使用原始大小。 参数 None Trim Crop CropKeepPos Polygon  
# --basic-sort-by Name  按名称排序  
# --basic-order Ascending 升序  
# --texture-format 纹理格式  
# --data 输出纹理文件的信息数据路径 plist  
# --sheet 输出图集路径 png  
# --scale 1 缩放比例 主要用于低分辨率的机子多资源适配。  
# --max-size 最大图片像素 一般我是用的2048，超过2048以前的有些android机型不支持。  
# --size-constraints 结纹理进行大小格式化，AnySize 任何大小 POT 使用2次幂 WordAligned  
# --replace 正则表达式，用于修改plist加载后的名称  
# --pvr-quality PVRTC 纹理质量  
# --force-squared 强制使用方形  
# --etc1-quality ETC 纹理质量  
def pack_textures(inputPath, outputPath, opt, scale, maxSize, sheetSuffix, textureFormat, sizeConstraints, sheetName, otherParams, fileNameSuffix):  
    packCommand = TP + \
        " --multipack" \
        " --format cocos2d" \
        " --maxrects-heuristics best" \
        " --enable-rotation" \
        " --shape-padding 2" \
        " --border-padding 0" \
        " --trim-mode Trim" \
        " --basic-sort-by Name" \
        " --basic-order Ascending" \
        " --texture-format {textureFormat}" \
        " --data {outputSheetNamePath}{fileNameSuffix}.plist" \
        " --sheet {outputSheetNamePath}{fileNameSuffix}.{sheetSuffix}" \
        " --scale {scale}" \
        " --max-size {maxSize}" \
        " --opt {opt}" \
        " --size-constraints {sizeConstraints}" \
        " {inputPath}" \
        " {otherParams}"  
  
  
    # win 和 mac 上处理正则表达式结果不一样  
    if sys.platform == "win32":  
        packCommand = packCommand + " --replace (.png)$=" \
            " --replace \\b={sheetName}_" \
            " --replace {sheetName}_$=.png"  
    else:  
        packCommand = packCommand + " --replace ^={sheetName}_"  
  
  
    packCommand = packCommand.format(  
        textureFormat=textureFormat,  
        outputSheetNamePath=os.path.join(outputPath,sheetName) + "_{n}",  
        sheetName=sheetName,  
        sheetSuffix=sheetSuffix,  
        scale=scale,  
        maxSize=maxSize,  
        opt=opt,  
        sizeConstraints=sizeConstraints,  
        inputPath=inputPath,  
        otherParams=otherParams,  
        fileNameSuffix=fileNameSuffix)  
    os.system(packCommand)  

if __name__ == '__main__':  
	pack_textures(curpath,output,'RGBA8888',1,2048,'png',"png","AnySize",name1,"--png-opt-level 7", "")

	print "###########end#####################"

