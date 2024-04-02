import keyboard
import mouse
import time

start_key = "Alt + Z"
end_key = "ALt + X"
break_key = "Alt + C"
def keys():
    print("Для запуска кликера нажмите Alt + Z.\n"
          "Для остановки кликера нажмите Alt + X\n"
          "Для выхода из программы нажмите Alt + С\n")
    keyboard.add_hotkey(start_key, click)
    keyboard.wait(break_key)
def click():
    # try:
    #     print("Кликер запущен")
    #     while True:
    #         while not keyboard.is_pressed(end_key):
    #             mouse.click()
    #             time.sleep(0.0002)
    #         else:
    #             print("Кликер остановлен")
    #             break
    # except:
    #     KeyboardInterrupt
    pass
if __name__ == "__main__":
    keys()
