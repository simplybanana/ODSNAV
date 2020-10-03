from python_imagesearch.imagesearch import imagesearch_loop
from python_imagesearch.imagesearch import imagesearch
from python_imagesearch.imagesearch import imagesearcharea
import pyautogui
import msvcrt as m
import pygetwindow as gw
import time
from time import sleep
import keyboard

timeInterval = 0.5
innerLoop = False
counter = 0

winEditSalesOrder = gw.getWindowsWithTitle('Edit - Sales')[0]
winEditSalesOrder.activate()


def waitForWindow(windowName):
    toc = 0
    i = 0
    while i == 0 and toc < 10:
        try:
            win = gw.getWindowsWithTitle(windowName)[0]
            print('Opened after: '+str(toc)+'s')
            i += 1
            return True
        except:
            print('Not open, waiting for '+windowName+'...')
        toc = time.perf_counter()
        sleep(1)
    sleep(1)


def lookAndPress(imageName):
    pos = imagesearch(imageName)
    if pos[0] != -1:
        pyautogui.click(pos[0],pos[1])
    else:
        print("Could not find: " + imageName)


def lookImageCheck(imageName):
    pos = imagesearch(imageName)
    if pos[0] != -1:
        return True
    else:
        return False


def waitAndPress(imageName):
    pos = imagesearch_loop(imageName, 0.2)
    if pos[0] != -1:
        pyautogui.click(pos[0],pos[1])
    else:
        print("Could not find: " + imageName)


def waitImageCheck(imageName):
    pos = imagesearch_loop(imageName, 0.2)
    if pos[0] != -1:
        return True
    else:
        print("Could not find: " + imageName)
        return False


def homeTab():
    sleep(timeInterval)
    pyautogui.press('alt')
    sleep(timeInterval)
    pyautogui.press('h')
    sleep(timeInterval)


def navigateTab():
    pyautogui.press('alt')
    sleep(timeInterval)
    pyautogui.press('n')
    sleep(timeInterval)


def releaseButton():
    pyautogui.hotkey('ctrl', 'f9')


def createWareShipButton():
    homeTab()
    pyautogui.press('w')


def wareShipLineButton():
    homeTab()
    pyautogui.press('8')


def showWareDocButton():
    pyautogui.hotkey('shift', 'f7')


def nextButton():
    pyautogui.hotkey('ctrl', 'pagedown')


def nextButtonCheck():
    pos = imagesearch("./nextBlank.png", 1)
    if pos[0] != -1:
        return True
    else:
        return False


def createPickButton():
    homeTab()
    pyautogui.press('k')


def pickLinesButton():
    homeTab()
    pyautogui.press('s')


def cardButton():
    homeTab()
    pyautogui.press('c')


def quantityButton():
    homeTab()
    pyautogui.press('a')


def registerButton():
    homeTab()
    pyautogui.press('r')


if __name__ == "__main__":
    while True:
        sleep(0.3)
        releaseButton()
        createWareShipButton()
        sleep(1)
        if lookImageCheck("./releaseError.png"):
            pyautogui.press('enter')
        else:
            pyautogui.press('enter')
            innerLoop = True

        if not innerLoop:
            counter += 1
            if counter > 10:
                exit()
            wareShipLineButton()
            waitForWindow('Whse. Shipment')
            showWareDocButton()
            waitForWindow('Warehouse Shipment')
            if lookImageCheck("./completelyPicked.png"):
                pyautogui.press('esc')
                sleep(0.5)
                pyautogui.press('esc')
            sleep(1)
            if nextButtonCheck:
                exit()
            else:
                nextButton()
        else:
            counter = 0
            innerLoop = False
            waitForWindow('Warehouse Shipment')
            print('about to create pick')
            createPickButton()
            sleep(1)
            pyautogui.hotkey('ctrl', 'enter')
            sleep(1)
            pyautogui.press('enter')
            pickLinesButton()
            waitForWindow('Warehouse Activity')
            cardButton()
            waitForWindow('Warehouse Pick')
            quantityButton()
            registerButton()
            sleep(1)
            if lookImageCheck("./yesButton.png"):
                pyautogui.press('left')
                sleep(timeInterval)
                pyautogui.press('enter')
                sleep(timeInterval)
            elif lookImageCheck("./noBin.png"):
                a = keyboard.read_key('d')
                if a == 'a':
                    sleep(sleepTime)
                    pyautogui.press('esc')
                    sleep(sleepTime)
                    pyautogui.press('esc')
                elif a != 'd' and a != 'a':
                    exit()
            sleep(1)
            pyautogui.press('esc')
            sleep(0.5)
            pyautogui.press('esc')
            sleep(1)
            if nextButtonCheck:
                exit()
            else:
                nextButton()
