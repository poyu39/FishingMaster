import time

import pyautogui
from pynput import mouse
from pynput.keyboard import Listener

from bar import Bar

class FishingMaster:
    def __init__(self) -> None:
        self.mouse = mouse.Controller()
        self.click = False
        self.press = 0
        self.start_fishing = False
        self.bar = Bar()
    
    def on_press(self, key):
        self.press = str(key)
        # print(f"Key: {key}")
    
    def on_release(self, key):
        self.press = None
    
    def start_listener(self):
        keyboard_listener = Listener(on_press=self.on_press, on_release=self.on_release)
        keyboard_listener.start()
    
    def set_bar(self):
        if self.press == "'s'" and self.bar.set_step is None:
            print('開始設定')
            self.bar.set_step = 0
            time.sleep(0.5)
        elif self.press == "'s'" and self.bar.set_step == 0:
            print('已讀取起始點')
            self.bar.start = self.mouse.position
            self.bar.set_step = 1
            time.sleep(0.5)
        elif self.press == "'s'" and self.bar.set_step == 1:
            print('已讀取終點')
            print('已讀取背景色')
            self.bar.end = self.mouse.position
            self.bar.set_step = 2
            self.bar.bg_color = pyautogui.pixel(self.mouse.position[0], self.mouse.position[1])
            time.sleep(0.5)
        elif self.press == "'s'" and self.bar.set_step == 2:
            print('已讀取目標色')
            self.bar.target_color = pyautogui.pixel(self.mouse.position[0], self.mouse.position[1])
            self.bar.set_step = 3
            time.sleep(0.5)
            print('設定完成')
            print(f'起始點: {self.bar.start}')
            print(f'終點: {self.bar.end}')
            print(f'背景色: {self.bar.bg_color}')
            print(f'目標色: {self.bar.target_color}')
            print(f'開始釣魚')
    
    def fishing(self):
        if self.press == "'f'":
            self.start_fishing = not self.start_fishing
        if self.bar.set_step == 3 and self.start_fishing:
            # 起始點到終點之間沒有目標色 & 不能沒有背景色
            have_bg_color = False
            for x in range(self.bar.start[0], self.bar.end[0], 20):
                r, g, b = pyautogui.pixel(x, self.bar.start[1])
                if (r, g, b) == self.bar.target_color:
                    return
                if (r, g, b) == self.bar.bg_color:
                    have_bg_color = True
            if have_bg_color:
                self.mouse.click(mouse.Button.right)
                print('釣到魚')