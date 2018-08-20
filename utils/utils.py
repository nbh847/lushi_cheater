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
        pyautogui.FAILSAFE = True

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
        pos_x = random.randint(318, 559)
        pos_y = random.randint(271, 436)
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
        humen_speed = random.randint(650, 780)
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
        if compare_result <= 15:
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
        if compare1 <= 25 or compare2 <= 19:
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

    def drag_cards_to_ground(self):
        '''
        把随从从手里拖到场上
        '''
        pix_x = random.randint(316, 1029)
        pix_y = random.randint(390, 467)
        whole_time = self.get_humen_time(pix_x, pix_y)
        pyautogui.dragTo(pix_x, pix_y, whole_time)

    def drag_cards_to_fight_hero(self):
        '''
        让随从打敌方英雄的脸
        '''
        pix_x = random.randint(652, 725)
        pix_y = random.randint(127, 172)
        whole_time = self.get_humen_time(pix_x, pix_y)
        pyautogui.dragTo(pix_x, pix_y, whole_time)
        pyautogui.rightClick()

    def follower_action(self):
        '''
        让能行动的随从攻击敌方英雄
        '''
        index = 0
        for i in range(10):
            print('开始打敌方英雄的脸第{}次'.format(i + 1))
            start_x = 1013 + random.randint(-10, 10) + index
            start_y = 429 + random.randint(-29, 29)
            self.mouse_move_by_humen_speed(start_x, start_y)
            self.drag_cards_to_fight_hero()
            index -= 68

    def move_cards(self):
        # 移动到底部最左边打出所有能打出的随从
        index = 0
        for i in range(10):
            print('开始移动第{}次'.format(i + 1))
            start_x = 453 + random.randint(-10, 10) + index
            start_y = 734 + random.randint(-29, 29)
            self.mouse_move_by_humen_speed(start_x, start_y)
            self.drag_cards_to_ground()
            index += 47
        # 把场上所有能行动的随从全部行动
        self.follower_action()

    def confirm_game_start(self):
        '''
        确认是否要点击游戏确认开始按钮
        '''
        position = (660, 597, 716, 619)
        store_path = "D:\\Python27\\workspace\\lushi_cheater\\screen_shut_file\\game_confirm_start.jpg"
        get_area_img(store_path, position)
        compare_img_path = "D:\\Python27\\workspace\\lushi_cheater\\imgs\\game_confirm_start.jpg"
        compare_result = compare(store_path, compare_img_path)
        # 删除临时截图
        delete_img(store_path)
        if compare_result <= 7:
            print('需要点击游戏确认按钮')
            mouse_x = random.randint(660, 716)
            mouse_y = random.randint(597, 619)
            self.mouse_move_by_humen_speed(mouse_x, mouse_y)
            pyautogui.click()
            print('已点击')
        else:
            print('不需要点击游戏确认按钮')

    def confirm_standard_game_begin(self):
        '''
        确认是否需要点击标准对战按钮
        '''
        position = (963, 591, 1036, 662)
        store_path = "D:\\Python27\\workspace\\lushi_cheater\\screen_shut_file\\game_standard_begin.jpg"
        get_area_img(store_path, position)
        compare_img_path = "D:\\Python27\\workspace\\lushi_cheater\\imgs\\game_standard_begin.jpg"
        compare_result = compare(store_path, compare_img_path)
        # 删除临时截图
        delete_img(store_path)
        if compare_result <= 12:
            print('需要点击标准对战按钮')
            mouse_x = random.randint(963, 1036)
            mouse_y = random.randint(591, 662)
            self.mouse_move_by_humen_speed(mouse_x, mouse_y)
            pyautogui.click()
            print('已点击')
        else:
            print('不需要点击标准对战按钮')

    def play_game_card(self):
        '''
        游戏行动模块
        '''
        while True:
            # 点击一下，确认可以退出每局结束的比赛
            pyautogui.click(683, 458)
            # 检查是否需要点击标准对战
            self.confirm_standard_game_begin()
            # 检查是否需要点击确认游戏
            self.confirm_game_start()
            # time.sleep(2000)
            # 检查是否结束了游戏
            if self.game_over():
                break
            # 检查是否是本回合
            if self.is_my_turn():
                # 暂停6s等待所有的卡牌加载完
                time.sleep(random.randint(3, 6))
                # 开始出牌
                self.move_cards()
                # 检查是否有英雄技能，有就使用
                # if self.has_hero_skill() is True:
                self.use_hero_skill()
                # 结束本回合，之后检查是否到了自己行动的回合
                self.end_my_turn()
            else:
                print('每5s检查一次是否到了我的回合')
                time.sleep(random.randint(2, 4))

    def run(self):
        # 定位鼠标位置
        # self.locate_mouse_position()
        # time.sleep(3000)
        # 点击图标进入游戏主界面
        self.mouse_move_by_humen_speed(210, 741)
        pyautogui.click()
        time.sleep(random.randint(1, 3))
        # 点击最下方的牌库循环出牌
        self.play_game_card()


if __name__ == '__main__':
    u = Utils()
    u.run()
