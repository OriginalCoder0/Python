"""
 Name: 连连看游戏
 Athor: 卢华东
 Email: luhuadong@163.com
 Date: 2018-07-07
 Description: 哎呀，反正就是连连看啦

"""

import sys, time
import math, random
import pygame
from pygame.locals import *

# 全局的设置类
class Settings:

    def __init__(self):
        # 定义游戏窗口大小，为背景图片的一半
        self.screen_size = (self.screen_width, self.screen_height) = (800, 480)
        self.game_size = (self.game_row, self.game_col) = (6, 10)
        self.map_total = self.game_row * self.game_col
        self.element_num = 12
        self.bg_color = (220, 220, 220)
        self.title = 'Pig Pig 连连看'
        self.win_image = './images/you_win.png'

        self.grid_size = 80
        self.scale_size = (76, 76)

        self.points = []



# 实例化设置对象
settings = Settings()

# 图像列表映射
map_list = []
#global map_list
image_list = []


# 图片按钮
class ImageBtn:

    __checkable = True
    __checked = False

    def __init__(self, screen, image_path, x, y, number, element):
        self.x = x
        self.y = y
        self.element = element
        self.number = number
        self.screen = screen
        self.image = pygame.image.load(image_path)

        # 因为图片原始大小为 200x200，所以要进行缩放
        self.image = pygame.transform.scale(self.image, settings.scale_size)

    def __del__(self):
        pass

    def display(self):
        # 描边
        """
        if self.__checked:
            #self.image = pygame.transform.laplacian(self.image)
            pygame.draw.rect(self.image, (0,205,205), (0,0,self.image.get_width()-1,self.image.get_height()-1), 2)
        """

        """
        if not self.__checkable:
            self.image.fill((255, 255,240))
        """
        if self.__checked:
            pygame.draw.rect(self.image, (0,205,205,255), (0,0,self.image.get_width()-1,self.image.get_height()-1), 2)
        else:
            pygame.draw.rect(self.image, (0,205,205,0), (0,0,self.image.get_width()-1,self.image.get_height()-1), 2)

        self.screen.blit(self.image, (self.x, self.y))

    def hide(self):
        self.__checked = False
        self.__checkable = False
        # 图片不可视
        #self.image.set_alpha(255)
        self.image.fill((255, 255,240))

    def is_checkable(self):
        return self.__checkable

    def click(self):
        self.__checked = not self.__checked
        return self.__checked

    def reset(self):
        self.__checked = False

    def get_geometry(self):
        return (int(self.x), int(self.y), settings.scale_size[0], settings.scale_size[1])



# 水平扫描
def horizontal_scan(points):
    """
    水平标定

    以 p1 和 p2 所在的两个行作为基准线，然后用垂直线在有效范围内扫描，
    一旦发现可行路径，直接返回。

      hLine1  和   hLine2   分别是扫描的上边线和下边线
    leftLimit 和 rightLimit 分别是扫描的左边线和右边线
    """
    column = settings.game_col
    p1_x = int(points[0].number % column)
    p1_y = int(points[0].number / column)
    p2_x = int(points[1].number % column)
    p2_y = int(points[1].number / column)

    # 如果 p1 和 p2 在同一行，则不符合要求
    if p1_y == p2_y:
        return False

    print("Horizontal Scanning ...")

    # 确保 p1 在 p2 的左边，或在同一条垂直线上（非必要条件）
    """
    if p1_x > p2_x:
        pt_x = p1_x; pt_y = p1_y
        p1_x = p2_x; p1_y = p2_y
        p2_x = pt_x; p2_y = pt_y
    }
    """

    # 记录两条水平基准线

    # hLine1 为上水平线，hLine2 为下水平线
    if p1_y < p2_y:
        hLine1 = p1_y
        hLine2 = p2_y
    else:
        hLine1 = p2_y
        hLine2 = p1_y

    # 初始化左、右边界线为 0
    leftLimit = 0;
    rightLimit = column-1

    print("top:%d, bottom:%d, left:%d, right:%d" %(hLine1, hLine2, leftLimit, rightLimit))


    # 寻找左边界线

    i = p1_x
    # 第一次扫描
    # 当 i 大于 0 时，才进入循环
    while i > 0:
        # 判断左边点是否为空
        if map_list[p1_y * column+ i - 1] != 0:
            break
        # 当左边点为空时会继续扫面下一个左边点
        i -= 1
    leftLimit = i;
    print("第一次扫描(left)")
    print("top:%d, bottom:%d, left:%d, right:%d" %(hLine1, hLine2, leftLimit, rightLimit))

    # 第二次扫描
    i = p2_x
    while i > 0:
        if map_list[p2_y * column + i - 1] != 0:
            break
        i -= 1

    # leftLimit 记录左边界线，该界线所在的点为空或p1、p2本身
    if i > leftLimit:
        leftLimit = i

    print("第二次扫描(left)")
    print("top:%d, bottom:%d, left:%d, right:%d" %(hLine1, hLine2, leftLimit, rightLimit))

    # 如果 leftLimit 为 0，说明p1、p2已经在外界接通了，直接返回
    if leftLimit == 0:
        return True

    # 寻找右边界线
    i = p1_x
    while i < column-1:
        if map_list[p1_y * column + i + 1] != 0:
            break;
        i += 1
    rightLimit = i

    print("第一次扫描(right)")
    print("top:%d, bottom:%d, left:%d, right:%d" %(hLine1, hLine2, leftLimit, rightLimit))

    i = p2_x
    while i < column-1:
        if map_list[p2_y * column + i + 1] != 0:
            break
        i += 1

    if i < rightLimit:
        rightLimit = i

    print("第二次扫描(right)")
    print("top:%d, bottom:%d, left:%d, right:%d" %(hLine1, hLine2, leftLimit, rightLimit))

    if rightLimit == column-1:
        return True    # Bug

    # 判断 leftLimit 和 rightLimit
    if leftLimit > rightLimit:
        # 如果左边界线超出右边界线，则无法连接
        print("不能相连：leftLimit > rightLimit")
        return False
    else:
        # 从左往右扫描
        for i in range(leftLimit, rightLimit+1):
            print("从左往右扫描：%d -> %d"%(i, rightLimit))
            j = hLine1 + 1
            for j in range(hLine1+1, hLine2):
                print(" j=%d"%j)
                # 只要当前列有阻碍，马上跳出
                if map_list[j * column + i] != 0:
                    # 回退一行
                    #j -= 1
                    break
                j += 1
            if j == hLine2:
                print("最复杂的水平扫描成功！")
                return True

        return False;



# 垂直扫描
def vertical_scan(points):

    """
    垂直标定

    以 p1 和 p2 所在的两个列作为基准线，然后用水平线在有效范围内扫描，
    一旦发现可行路径，直接返回。

    """

    row = settings.game_row
    column = settings.game_col
    p1_x = int(points[0].number % column)
    p1_y = int(points[0].number / column)
    p2_x = int(points[1].number % column)
    p2_y = int(points[1].number / column)

    # 如果 p1 和 p2 在同一列，则不符合要求
    if p1_x == p2_x:
        return False

    print("Vertical Scanning ...")

    # 确保 p1 在 p2 的上边，或在同一条水平线上（非必要条件）
    """
    if(p1_y > p2_y) {
        pt_y = p1_y; pt_x = p1_x
        p1_y = p2_y; p1_x = p2_x
        p2_y = pt_y; p2_x = pt_x
    }
    """

    # 记录两条垂直基准线
    if p1_x < p2_x:
        vLine1 = p1_x # 左垂直线
        vLine2 = p2_x # 右垂直线
    else:
        vLine1 = p2_x
        vLine2 = p1_x

    # 初始化上、下边界线
    topLimit = 0
    bottomLimit = row-1

    # 寻找上边界线
    i = p1_y
    # 第一次扫描
    # 当 i 大于 0 时，才进入循环
    while i > 0:
        if map_list[p1_x + (i-1) * column] != 0:
            break # 判断上边点是否为空
        i -= 1 # 当上边点为空时会继续扫面下一个上边点
    topLimit = i

    print("第一次扫描(top)")
    print("top:%d, bottom:%d, left:%d, right:%d" %(topLimit, bottomLimit, vLine1, vLine2))

    # 第二次扫描
    i = p2_y
    while i > 0:
        if map_list[p2_x + (i-1) * column] != 0:
            break
        i -= 1

    # topLimit 记录上边界线，该界线所在的点为空或p1、p2本身
    if i > topLimit:
        topLimit = i

    print("第二次扫描(top)")
    print("top:%d, bottom:%d, left:%d, right:%d" %(topLimit, bottomLimit, vLine1, vLine2))

    # 如果 topLimit 为 0，说明p1、p2已经在外界接通了，直接返回
    if topLimit == 0:
        return True

    # 寻找下边界线
    i = p1_y
    while i < row-1:
        if map_list[p1_x + (i+1) * column] != 0:
            break
        i += 1
    bottomLimit = i

    print("第一次扫描(bottom)")
    print("top:%d, bottom:%d, left:%d, right:%d" %(topLimit, bottomLimit, vLine1, vLine2))

    i = p2_y
    while i < row-1:
        if map_list[p2_x + (i+1) * column] != 0:
            break
        i += 1

    if i < bottomLimit:
        bottomLimit = i

    print("第二次扫描(bottom)")
    print("top:%d, bottom:%d, left:%d, right:%d" %(topLimit, bottomLimit, vLine1, vLine2))

    if bottomLimit == row-1:
        return True

    # 判断 topLimit 和 bottomLimit
    if topLimit > bottomLimit:
        # 如果上边界线超出下边界线，则无法连接
        print("不能相连：topLimit > bottomLimit")
        return False
    else:
        # 从上往下扫描
        for i in range(topLimit, bottomLimit+1):
            print("从上往下扫描：%d -> %d"%(i, bottomLimit))
            j = vLine1 + 1
            for j in range(vLine1+1, vLine2):
                print(" j=%d"%j)
                # 只要当前行有阻碍，马上跳出
                if map_list[i * column + j] != 0:
                    # 回退一列
                    #j -= 1
                    break
                j += 1
            if j == vLine2:
                print("最复杂的垂直扫描成功！")
                return True

        return False


# 判断能否消除
def can_clear(points):
    # 如果两个元素不相同，还连个屁
    if points[0].element != points[1].element:
        return False
    else:
        if vertical_scan(points) or horizontal_scan(points):
            return True
        else:
            return False


def check_event(btn_list):
    """
        Key event capture and key_control
    """
    for event in pygame.event.get():
        if event.type == QUIT:
            print("exit...")
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print("Mouse button down, position:", pos)

            for btn in btn_list:
                geo = btn.get_geometry()
                x = geo[0]; y = geo[1]; w = geo[2]; h = geo[3]
                # 判断是否在图片块范围内
                if pos[0] > x and pos[0] < x+w and pos[1] > y and pos[1] < y+h:
                    print("inside:", id(btn))
                    # 如果图片还没被消除
                    if btn.is_checkable():
                        print("Block:", geo)
                        print("number: %d, element: %d" %(btn.number, btn.element))
                        print("> checked")

                        if not btn.click():
                            # 点自己是没有用的
                            settings.points.clear()
                            break

                        # 前面已经记录一个点了
                        if settings.points != []:
                            settings.points.append(btn)
                            # 检查是否相同、能否相连
                            if can_clear(settings.points):
                                # 消灭它们
                                for point in settings.points:
                                    print("+++++++++++", point.number)
                                    print("-----------", map_list)
                                    map_list[point.number] = 0
                                    point.number = 0
                                    point.hide()
                            else:
                                # 不匹配，恢复图片状态
                                for point in settings.points:
                                    point.reset()
                            # 这次判断完毕，清除记录的点
                            settings.points.clear()

                        # 这次是干净的操作
                        else:
                            # 记录第一个点
                            settings.points.append(btn)

                    else:
                        print("Here is no picture")

                    # 可以退出了，不用再找坐标了
                    break




# 构建游戏布局地图
def build_map():

    t_list = []
    m_list = []

    # 构建成对数据
    for i in range(0, settings.map_total, 2):
        # 随机生成成对的图片元素标号（1-12），存放于 tmp_list
        e = math.ceil(random.random()*settings.element_num)
        # double append
        t_list.append(e)
        t_list.append(e)

    # 打乱数据
    for i in range(0, settings.map_total, 1):
        # 将 tmp_list 中的图片元素随机排列在 m_list
        index = int(random.random()*(settings.map_total-i))
        m_list.append(t_list[index])
        # 删除已保存到 m_list 中的元素
        t_list.pop(index)

    return m_list


# 检查是否全部消除
def is_over():

    for each in map_list:
        if each > 0:
            return False

    return True


def main():

    # 初始化 Pygame
    pygame.init()

    # 创建一个游戏窗口
    screen = pygame.display.set_mode(settings.screen_size, 0, 0)

    # 设置窗口标题
    pygame.display.set_caption(settings.title)

    # 在窗口中加载游戏背景
    #background = pygame.image.load(settings.bg_image)

    # 准备图片元素

    global map_list
    map_list = build_map()
    nc = 0
    for m in map_list:
        nc += 1
        print("{0:>2}".format(m), end=' ')
        if nc % 10 == 0:
            print("")

    # 创建图片列表
    for i in range(0, settings.map_total):
        x = int(i%settings.game_col) * settings.grid_size + (settings.grid_size -settings.scale_size[0])/2
        y = int(i/settings.game_col) * settings.grid_size + (settings.grid_size -settings.scale_size[0])/2
        element = './images/element_'+str(map_list[i])+'.png'
        image_list.append(ImageBtn(screen, element, x, y, i, map_list[i]))


    play = True
    i = 0

    while True:
        screen.fill(settings.bg_color)
        if play:

            if is_over():
                play = False

            for im in image_list:
                im.display()

            pygame.display.update()

        else:
            youwin = pygame.image.load(settings.win_image)
            screen.blit(youwin, ((settings.screen_width-youwin.get_width())/2,(settings.screen_height-youwin.get_height())/2))
            pygame.display.update()
            #print("Game Over")

        # 检查按键事件
        check_event(image_list)
        #print("while --> ", map_list)

        time.sleep(0.04)



# 判断是否为主运行程序，是则调用 main()
if __name__ == '__main__':
    main()

