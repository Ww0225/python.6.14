# 使用Numpy、PIL等库将本校的校徽LOGO（下图）转换为Ndarray数组，并使用matplotlib重新绘制图像输出显示
from PIL import Image
import numpy
image = Image.open('image/学校Logo.png')
nd = numpy.asarray(image)
print(nd)
from matplotlib import pyplot
pyplot.imshow(nd)
pyplot.show()