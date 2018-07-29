# coding=utf-8
import math
import random
import time
import pyautogui

from img_compare import compare
from img_screen_grab import get_area_img, delete_img

''' 
工具库，提供各种集成方法
'''


class Utils:

    def __init__(self):
        pass

    def pause_random_time(self):
        '''
        随机暂停1-3s
        '''
        time.sleep(random.randint(1, 3))

    def move_to_random_place(self):
        '''
        结束回合后移动到一个随机位置
        :return:
        '''
        pos_x = random.randint(318, 1025)
        pos_y = random.randint(271, 480)
        self.mouse_move_by_humen_speed(pos_x, pos_y)

    def locate_mouse_position(self):
        '''
        定位鼠标的当前位置
        :return:
        '''
        mouse_x, mouse_y = pyautogui.position()
        print('mouse_x, {}'.format(mouse_x))
        print('mouse_y, {}'.format(mouse_y))
        return mouse_x, mouse_y

    def get_length(self, p1, p2):
        '''
        获取两点间的直线距离
        '''
        p1_x, p1_y = p1
        p2_x, p2_y = p2
        return math.sqrt((p1_x - p2_x) ** 2 + (p1_y - p2_y) ** 2)

    def get_humen_time(self, pix_x, pix_y):
        '''
        获取模拟人的速度去移动需要的时间
        '''
        # 鼠标目前的位置
        mouse_now = pyautogui.position()
        # 鼠标到目标的距离
        mouse_locate_length = self.get_length(mouse_now, (pix_x, pix_y))
        # 人的鼠标移动速度
        humen_speed = random.randint(480, 530)
        # 移动花费的总时间
        whole_time = mouse_locate_length / humen_speed
        return whole_time

    def mouse_move_by_humen_speed(self, pix_x, pix_y):
        '''
        模拟人的速度去移动
        '''
        whole_time = self.get_humen_time(pix_x, pix_y)
        pyautogui.moveTo(pix_x, pix_y, whole_time)

    def mouse_drog_by_humen_speed(self, pix_x, pix_y):
        whole_time = self.get_humen_time(pix_x, pix_y)
        pyautogui.dragTo(pix_x, pix_y, whole_time)

    def end_my_turn(self):
        '''
        结束我的回合
        '''
        mouse_x = random.randint(1080, 1148)
        mouse_y = random.randint(340, 358)
        self.mouse_move_by_humen_speed(mouse_x, mouse_y)
        pyautogui.click()
        print('已结束我的回合')
        self.move_to_random_place()

    def has_hero_skill(self):
        position = (758, 534, 866, 610)
        store_path = "D:\\Python27\\workspace\\lushi_cheater\\screen_shut_file\\skill_btn.jpg"
        now_btn_img = get_area_img(store_path, position)
        compare_img_path = "D:\\Python27\\workspace\\lushi_cheater\\imgs\\skill_ok.jpg"
        compare_result = compare(store_path, compare_img_path)
        # 删除临时截图
        delete_img(store_path)
        if compare_result is True:
            print('可以使用英雄技能')
            return True
        else:
            print('不能使用英雄技能')
            return False

    def use_hero_skill(self):
        '''
        使用英雄技能
        '''
        mouse_x = random.randint(789, 835)
        mouse_y = random.randint(565, 604)
        self.mouse_move_by_humen_speed(mouse_x, mouse_y)
        pyautogui.click()
        print('已使用英雄技能')

    def is_my_turn(self):
        '''
        判断是否是我的回合，如果有结束按钮，代表是我的回合
        '''
        position = (1065, 335, 1155, 363)
        store_path = "D:\\Python27\\workspace\\lushi_cheater\\screen_shut_file\\screen_end_btn.jpg"
        now_btn_img = get_area_img(store_path, position)
        compare_img_path_1 = "D:\\Python27\\workspace\\lushi_cheater\\imgs\\first_turn_end_yellow.jpg"
        compare_img_path_2 = "D:\\Python27\\workspace\\lushi_cheater\\imgs\\first_turn_end_green.jpg"
        compare1 = compare(store_path, compare_img_path_1)
        compare2 = compare(store_path, compare_img_path_2)
        # 删除临时截图
        delete_img(store_path)
        if compare1 or compare2:
            print('是我的回合')
            return True
        else:
            print('不是我的回合')
            return False

    def game_over(self):
        '''
        判断游戏是否结束了
        :return:
        '''
        pass

    def play_game_card(self):
        # 移动到底部最左边
        # index = 0
        # for i in range(10):
        #     print('开始移动第{}次'.format(i+1))
        #     time.sleep(random.randint(1, 3))
        #     start_x = 861 + random.randint(-10, 10) + index
        #     start_y = 730 + random.randint(-29, 29)
        #     self.mouse_move_by_humen_speed(start_x, start_y)
        #     index -= 47
        # self.end_my_turn()
        while True:
            # 检查是否结束了游戏
            if self.game_over():
                break
            # 检查是否是本回合
            if self.is_my_turn():
                # 检查是否有英雄技能，有就使用
                if self.has_hero_skill() is True:
                    self.use_hero_skill()
                # 结束本回合，之后检查是否到了自己行动的回合
                self.end_my_turn()
            else:
                print('每5s检查一次是否到了我的回合')
                time.sleep(random.randint(4, 8))

    def run(self):
        # 定位鼠标位置
        # self.locate_mouse_position()
        # time.sleep(3000)
        # 点击图标进入游戏主界面
        self.mouse_move_by_humen_speed(210, 741)
        pyautogui.click()
        time.sleep(random.randint(1, 3))
        # 点击设置按钮
        # img_path = 'D:/Python27/workspace/lushi_cheater/imgs/setting_btn.PNG'
        # left, top, wigth, height = pyautogui.locateOnScreen(img_path)
        # self.mouse_move_by_humen_speed(left + wigth / 2, top + height / 2)
        # pyautogui.click()
        # 点击开始
        # self.mouse_move_by_humen_speed(690, 606)
        # pyautogui.click()
        # time.sleep(random.randint(1, 3))
        # 点击最下方的牌库循环出牌
        self.play_game_card()
        # self.mouse_move_by_humen_speed(672, 711)
        # self.mouse_move_by_humen_speed(1317, 20)
        # time.sleep(1)
        # pyautogui.mouseDown(button='left')
        # pyautogui.mouseUp(button='left')
        # self.mouse_drog_by_humen_speed(300, 400)


if __name__ == '__main__':
    u = Utils()
    u.run()
