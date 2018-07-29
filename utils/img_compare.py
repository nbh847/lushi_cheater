from PIL import Image
import math
import operator
import functools

def compare(pic1,pic2):
    '''
    :param pic1: 图片1路径
    :param pic2: 图片2路径
    :return: 返回对比的结果, True or False
    !!! 相差10个百分点以内就算相似
    '''
    image1 = Image.open(pic1)
    image2 = Image.open(pic2)

    histogram1 = image1.histogram()
    histogram2 = image2.histogram()

    differ = math.sqrt(functools.reduce(operator.add, list(map(lambda a,b: (a-b)**2,histogram1, histogram2)))/len(histogram1))
    print (differ)

    if differ <= 15:
        return True
    else:
        return False

# pic_1 = 'D:\Python27\workspace\lushi_cheater\screen_shut_file\\skill_ok.jpg'
# pic_2 = 'D:\Python27\workspace\lushi_cheater\screen_shut_file\\skill_no.jpg'
# compare(pic_1, pic_2)
