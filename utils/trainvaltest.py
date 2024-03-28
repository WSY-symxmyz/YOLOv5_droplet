# 导入所需的库
import os
import random
import shutil
import numpy as np

# 定义图片和label的原始路径
image_dir = "../dataset/datas"  # 图片文件夹的路径
label_dir = "../dataset/labels"  # label文件夹的路径

# 定义划分后的输出路径
output_image_dir = "../dataset/image"  # 输出文件夹的路径
output_label_dir = "../dataset/label"
train_image_dir = os.path.join(output_image_dir, "train")  # train文件夹的路径
val_image_dir = os.path.join(output_image_dir, "val")  # val文件夹的路径
test_image_dir = os.path.join(output_image_dir, "test")  # test文件夹的路径
train_label_dir = os.path.join(output_label_dir, "train")  # train文件夹的路径
val_label_dir = os.path.join(output_label_dir, "val")  # val文件夹的路径
test_label_dir = os.path.join(output_label_dir, "test")  # test文件夹的路径

# 定义划分的比例
train_ratio = 0.7  # train的比例
val_ratio = 0.2  # val的比例
test_ratio = 0.1  # test的比例

# 创建输出文件夹
os.makedirs(output_image_dir, exist_ok=True)
os.makedirs(output_label_dir, exist_ok=True)
os.makedirs(train_image_dir, exist_ok=True)
os.makedirs(val_image_dir, exist_ok=True)
os.makedirs(test_image_dir, exist_ok=True)
os.makedirs(train_label_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)
os.makedirs(test_label_dir, exist_ok=True)

# 获取图片和label的文件名列表
image_files = np.array(os.listdir(image_dir))  # 转换为numpy数组
label_files = np.array(os.listdir(label_dir))  # 转换为numpy数组

# 对文件名列表进行排序
image_files = sorted(image_files, key=lambda x: int(x[0:5]), reverse=False)  # 按照图片文件名中的数字部分升序排序
label_files = sorted(label_files, key=lambda x: int(x[0:5]), reverse=False)  # 按照label文件名中的数字部分升序排序

# 找出没有对应label的image
image_files_len = len(image_files)
label_files_len = len(label_files)

no_label_images = image_files[label_files_len:]
image_files = image_files[0:label_files_len]
"""
# 检查图片和label的文件名是否对应，并将没有label的图片单独存放在一个列表中
for image_file, label_file in zip(image_files, label_files):
    # 去掉文件名的后缀，比较是否相同
    if image_file[:-4] != label_file[:-4]:
        # 如果不相同，说明图片没有对应的label，将图片文件名添加到no_label_images列表中
        no_label_images.append(image_file)
        # 同时，从image_files列表中删除该图片文件名，避免重复处理
        image_files = np.delete(image_files, np.where(image_files == image_file))
"""

new_image_files_len = len(image_files)
new_label_files_len = len(label_files)
print(new_image_files_len == new_label_files_len)

# 设置相同的随机数种子

for image_file, label_file in zip(image_files, label_files):
    # 去掉文件名的后缀，比较是否相同
    assert image_file[:5] == label_file[:5], "打乱顺序前图片和label的文件名不对应"

# 打乱图片和label的顺序
np.random.seed(42)
np.random.shuffle(image_files)
np.random.seed(42)
np.random.shuffle(label_files)

for image_file, label_file in zip(image_files, label_files):
    # 去掉文件名的后缀，比较是否相同
    assert image_file[:5] == label_file[:5], "打乱顺序后图片和label的文件名不对应{} {}".format(image_file, label_file)
# 计算图片和label的总数
total_count = len(image_files)

# 计算划分的分界点
train_point = int(total_count * train_ratio)  # train的分界点
val_point = int(total_count * (train_ratio + val_ratio))  # val的分界点

# 划分图片和label
for i in range(total_count):
    # 获取当前的图片和label的文件名
    image_file = image_files[i]
    label_file = label_files[i]

    # 获取当前的图片和label的完整路径
    image_path = os.path.join(image_dir, str(image_file))
    label_path = os.path.join(label_dir, str(label_file))

    # 根据划分的比例，复制图片和label到对应的输出文件夹
    if i < train_point:
        # 复制到train文件夹
        shutil.copy(image_path, train_image_dir)
        shutil.copy(label_path, train_label_dir)
    elif i < val_point:
        # 复制到val文件夹
        shutil.copy(image_path, val_image_dir)
        shutil.copy(label_path, val_label_dir)
    else:
        # 复制到test文件夹
        shutil.copy(image_path, test_image_dir)
        shutil.copy(label_path, test_label_dir)

# 对没有label的图片进行严格按比例的分配
# 计算没有label的图片的总数
no_label_count = len(no_label_images)

# 计算每个文件夹应该分配的图片的数量
train_count = int(no_label_count * train_ratio)  # train文件夹的图片数量
val_count = int(no_label_count * val_ratio)  # val文件夹的图片数量
test_count = no_label_count - train_count - val_count  # test文件夹的图片数量

np.random.shuffle(no_label_images)

for i in range(no_label_count):
    no_label_image = no_label_images[i]
    image_path = os.path.join(image_dir, str(no_label_image))

    if i < train_count:
        shutil.copy(image_path, train_image_dir)

    elif i < val_count+train_count:
        shutil.copy(image_path, val_image_dir)

    else:
        shutil.copy(image_path, test_image_dir)
