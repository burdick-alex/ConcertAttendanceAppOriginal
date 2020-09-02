import kivy
kivy.require('1.10.0')
from kivy.lang.builder import Builder
import sys
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from time import sleep
import threading
from threading import Thread
fileName = ''
appOrWrite = 0
numOfPeople = 0
finalList = []
typers = 0
swipers = 0
class ScreenManagement(ScreenManager):
    pass
class StartScreen(Screen):
    def selectNewFile(self):
        global fileName
        global appOrWrite
        fileName = self.ids["file"].text
        print()
        self.manager.current = "login"
    def selectExistingFile(self):
        global fileName
        global appOrWrite
        appOrWrite = 1
        fileName = self.ids["file"].text
        print()
        self.manager.current = "login"
class TypeOrSwipe(Screen):
    def keyboard(self):
        self.manager.current = "login"
class Swipe(Screen):
    def on_enter(self, *args):
        self.ids.uin.focus= True
    def swiperNoSwiping(self):
        global numOfPeople
        global finalList
        global fileName
        global appOrWrite
        global swipers
        if appOrWrite == 0:
            with open(fileName, "w+") as uinList:
                uinNum = self.ids["uin"].text
                if len(uinNum) < 54:
                    self.manager.current = "swipes"
                else:
                    uinList.write(uinNum+"\n")
                    print("I didn't add a line")
                    print(uinNum)
                    finalList.append(uinNum)
                    numOfPeople += 1
                    swipers += 1
                    self.manager.current = "ending"
                    self.ids["uin"].text = ''
                    appOrWrite += 1
        else:
            with open(fileName, "a") as uinList:
                uinNum = self.ids["uin"].text
                if len(uinNum) < 54:
                    self.manager.current = "swipes"
                else:
                    uinNum = uinNum[:55]
                    print(uinNum)
                    finalList.append(uinNum)
                    numOfPeople += 1
                    swipers += 1
                    uinList.write(uinNum+"\n")
                    uinList.flush()
                    self.manager.current = "ending"
                    self.ids["uin"].text = ''
                    appOrWrite += 1

class Login(Screen):
    Window.clearcolor = (0.0, 0.0, 255, 1.0)
    def timerForText(self):
        print("checking length")
        print(self.ids["uin"].text)
        if len(self.ids["uin"].text) > 8:
                self.cool()


    def on_enter(self, *args):
        self.ids["uin"].text = ""
        self.ids.uin.focus= True
        Clock.schedule_interval(lambda dt: self.timerForText(), 0.5)
    def cool(self):
        global fileName
        global appOrWrite
        global numOfPeople
        global typers
        global finalList
        if appOrWrite == 0:
            with open(fileName, "w+") as uinList:
                uinNum = self.ids["uin"].text
                if len(uinNum) < 7:
                    self.manager.current = "login"
                else:
                    uinList.write(str(uinNum)+"\n")
                    print(uinNum)
                    finalList.append(uinNum)
                    numOfPeople += 1
                    typers += 1
                    self.manager.current = "ending"
                    self.ids["uin"].text = ''
                    appOrWrite += 1
        else:
            with open(fileName, "a") as uinList:
                uinNum = self.ids["uin"].text
                if len(uinNum) < 7:
                    self.manager.current = "login"
                else:
                    uinList.write(str(uinNum)+"\n")
                    print(uinNum)
                    finalList.append(uinNum)
                    numOfPeople += 1
                    typers += 1
                    self.manager.current = "ending"
                    self.ids["uin"].text = ''
                    appOrWrite += 1

class Ending(Screen):
    def change(self):
        sleep(1.5)
        self.manager.current = "login"


kv_file = Builder.load_file("Kivy.kv")


class HelloKivyApp(App):
    def build(self):
        return kv_file

if __name__ in ('__android__', '__main__'):
    HelloKivyApp().run()


print(numOfPeople,"people showed up.")
print("People who typed:",typers)
print("People who swiped:",swipers)
print("Here are their uin's and swipes:")
print(finalList)

