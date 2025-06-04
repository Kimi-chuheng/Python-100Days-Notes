#Python处理图像
from PIL import Image

# 读取图像获得Image对象
image = Image.open('1.png')
# 通过Image对象的format属性获得图像的格式
print(image.format) # JPEG
# 通过Image对象的size属性获得图像的尺寸
print(image.size)   # (500, 750)
# 通过Image对象的mode属性获取图像的模式
print(image.mode)   # RGB
# 通过Image对象的show方法显示图像
image.show()


from PIL import ImageFilter

# 使用Image对象的filter方法对图像进行滤镜处理
# ImageFilter模块包含了诸多预设的滤镜也可以自定义滤镜
image.filter(ImageFilter.CONTOUR).show()