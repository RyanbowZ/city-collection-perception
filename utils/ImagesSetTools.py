import os
import random
import numpy as np
from utils.SaveDataBase import SaveImgSet

# 图片总共的个数
DICT_NUM = 2000



class GenerateRandom:
    num = 0
    unused = np.zeros(int(np.ceil(DICT_NUM / 40)))

    def __init__(self):
        # 打开数据库连接
        db = SaveImgSet()

        self.index = 0  # 被选中的文件夹的名称
        self.num = np.sum(self.unused)
        if self.num == 0:
            # print("num is zero")
            self.unused[self.index] += 1
            self.res = self.index
            # 将当前被选中的文件夹记录进数据库
            db.update_data(data=int(self.unused[self.index]), id=int(self.res))
        else:
            if self.unused[self.unused.argmin()] == 0:
                # 还有没有被选的
                self.index = self.num
                # print("cur_id = ", self.index)
                self.unused[int(self.index)] += 1
                self.res = int(self.index)
                db.update_data(data=int(self.unused[int(self.index)]), id=int(self.res))
            else:
                # 全部至少被选过一次
                # print("全部至少被选过一次")
                self.cur_id = self.unused.argmin()
                # print("cur_id = ", self.cur_id)
                self.unused[self.cur_id] += 1
                self.res = self.cur_id
                db.update_data(data=int(self.unused[self.cur_id]), id=int(self.res))

    def process(self):
        return self.res


def dataset_generator(path):
    """
    获取目录下所有文件的路径,存入set中
    :param path:路径
    :return: 随机化的列表
    """
    ls = []
    set_1 = []
    set_2 = []
    name_set_1 = []
    name_set_2 = []

    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            dataset_generator(file_path)
        else:
            # 路径转换
            file_path = file_path.replace('\\', '/').lstrip(".").lstrip("/stati").lstrip("c/")
            ls.append(file_path)
    random.shuffle(ls)
    count = len(ls) // 2
    for i in range(count):
        file = ls.pop()
        set_1.append(file)
        name_set_1.append(file.lstrip("images/data_set_test/"))
    for i in range(count):
        file = ls.pop()
        set_2.append(file)
        name_set_2.append(file.lstrip("images/data_set_test/"))
    # 每次取两个
    return set_1, set_2, name_set_1, name_set_2
