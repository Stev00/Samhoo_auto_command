#python3 win7
#utf-8

'this is a test program about SPH2000,Version = 0.5'

__author__ = 'ZhangTong'


import pyautogui

while True:
    print('\n"tx"   for TX Test'
          '\n"rx"   for RX Test'
          '\n"q"    for Quit')

    mode = input('Please Input Test Mode:')

    if mode.upper() == 'TX':

        print('\n\n\n\n\n'
              '\n"ah350"       for Analog HighPower 350MHz TX'
              '\n"dm400"       for Digital MiddlePower 400MHz TX'
              '\n"0"or" "      for Stop TX'
              '\n"q"           for Quit')

        while True:
            x = list(input('\n\n\nPlease Input Mode & Frequency:'))
            screen_width_last, screen_height_last = pyautogui.position()
            screen_width, screen_height = pyautogui.size()
            screen_width, screen_height = screen_width * 0.75, screen_height * 0.75

            y = x+['zhangdansan']

            if y[0].upper() == 'D':

                pyautogui.moveTo(screen_width, screen_height)
                pyautogui.click()

#                pyautogui.press(['a', 't', '+', 't', 'u', 'n', 'e', 'enter'], interval=0.3)
                pyautogui.press(['d', 's', 'p', ' ', '1', 'enter'], interval=0.3)
                pyautogui.press(['m', 'o', 'd', ' ', 't', ' ', '0', 'enter'], interval=0.3)
                pyautogui.press(['r', 'm', 's', ' ', '1', 'enter'], interval=0.3)
                pyautogui.press(['l', 'c', 'k', ' ', 'x', ' ', ] + x[2:] + ['enter'], interval=0.3)
                pyautogui.press(['p', 'w', 'r', ' ', ] + [x[1]] + ['enter'], interval=0.3)
                pyautogui.press(['m', 'o', 'd', ' ', 'm', ' ', '1', 'enter'], interval=0.3)
                pyautogui.press(['t', 'p', 's', ' ', '2', 'enter'], interval=0.3)
                pyautogui.press(['m', 'o', 'd', ' ', 't', ' ', '1', 'enter'], interval=0.3)

                pyautogui.moveTo(screen_width_last, screen_height_last)
                pyautogui.click()
                print('\n\nTesting Digital TX...')

            elif y[0].upper() == 'A':
                pyautogui.moveTo(screen_width, screen_height)
                pyautogui.click()

#                pyautogui.press(['a', 't', '+', 't', 'u', 'n', 'e', 'enter'], interval=0.3)
                pyautogui.press(['d', 's', 'p', ' ', '1', 'enter'], interval=0.3)
                pyautogui.press(['m', 'o', 'd', ' ', 't', ' ', '0', 'enter'], interval=0.3)
                pyautogui.press(['r', 'm', 's', ' ', '0', 'enter'], interval=0.3)
                pyautogui.press(['l', 'c', 'k', ' ', 'x', ' ', ] + x[2:] + ['enter'], interval=0.3)
                pyautogui.press(['p', 'w', 'r', ' '] + [x[1]] + ['enter'], interval=0.3)
                pyautogui.press(['p', 't', 't', ' ', '1', 'enter'], interval=0.3)

                pyautogui.moveTo(screen_width_last, screen_height_last)
                pyautogui.click()
                print('\n\nTesting Analog TX...')

            elif y[0].upper() == 'Q':
                print('\n\nFinish')
                break

            elif y[0] == ' ':
                pyautogui.moveTo(screen_width, screen_height)
                pyautogui.click()

                pyautogui.press(['m', 'o', 'd', ' ', 't', ' ', '0', 'enter'], interval=0.1)

                pyautogui.moveTo(screen_width_last, screen_height_last)
                pyautogui.click()
                print('\n\nStop TX')

            elif y[0] == '0':
                pyautogui.moveTo(screen_width, screen_height)
                pyautogui.click()

                pyautogui.press(['m', 'o', 'd', ' ', 't', ' ', '0', 'enter'], interval=0.1)

                pyautogui.moveTo(screen_width_last, screen_height_last)
                pyautogui.click()
                print('\n\nStop TX')

            else:
                print('\n\nInput Wrong')


    elif mode.upper() == 'RX':
        print('\n\n\n\n\n'
              '\n"a0333.5"      for Analog WideBand 333.5MHz RX'
              '\n"d2470"        for Digital NarrowBand 470MHz RX'
              '\n"0"or" "       for Stop RX'
              '\n"q"            for Quit')

        while True:
            x = list(input('\n\n\nPlease Input Mode & Frequency:'))
            screen_width_last, screen_height_last = pyautogui.position()
            screen_width, screen_height = pyautogui.size()
            screen_width, screen_height = screen_width * 0.75, screen_height * 0.75

            y = x + ['zhangdansan']

            if y[0].upper() == 'D':

                pyautogui.moveTo(screen_width, screen_height)
                pyautogui.click()
    
                pyautogui.press(['d', 's', 'p', ' ', '1', 'enter'], interval=0.3)
                pyautogui.press(['m', 'o', 'd', ' ', 't', ' ', '0', 'enter'], interval=0.3)
                pyautogui.press(['r', 'm', 's', ' ', '1', 'enter'], interval=0.3)
                pyautogui.press(['c', 's', 's', ' ', ] + [x[1]] + ['enter'], interval=0.3) #宽窄带
                pyautogui.press(['l', 'c', 'k', ' ', 'r', ' ', ] + x[2:] + ['enter'], interval=0.3)
                pyautogui.press(['m', 'o', 'd', ' ', 't', ' ', '5', 'enter'], interval=0.3) #接收模式
                pyautogui.press(['b', 'e', 'r', ' ', '0', 'enter'], interval=0.3) #开启误码率侦测
                pyautogui.press(['b', 'e', 'r', ' ', '1', 'enter'], interval=0.3) #关闭误码率侦测
                pyautogui.moveTo(screen_width_last, screen_height_last)
                pyautogui.click()
                print('\n\nTesting Digital RX...')



            elif y[0].upper() == 'A':
                pyautogui.moveTo(screen_width, screen_height)
                pyautogui.click()

#                pyautogui.press(['a', 't', '+', 't', 'u', 'n', 'e', 'enter'], interval=0.3)
                pyautogui.press(['d', 's', 'p', ' ', '1', 'enter'], interval=0.3)
                pyautogui.press(['m', 'o', 'd', ' ', 't', ' ', '0', 'enter'], interval=0.3)
                pyautogui.press(['r', 'm', 's', ' ', '0', 'enter'], interval=0.3)
                pyautogui.press(['c', 's', 's', ' ', ] + [x[1]] + ['enter'], interval=0.3) 
                pyautogui.press(['l', 'c', 'k', ' ', 'r', ' ', ] + x[2:] + ['enter'], interval=0.3)
                pyautogui.press(['m', 'o', 'd', ' ', 't', ' ', '5', 'enter'], interval=0.3)
#                pyautogui.press(['s', 'p', 'k', ' ', '3', 'enter'], interval=0.3)
                pyautogui.press(['s', 'p', 'k', ' ', '2', 'enter'], interval=0.3) #切换外部SPK
                pyautogui.press(['a', 's', 'l', ' ', '0', 'enter'], interval=0.3) #关闭静噪
                pyautogui.moveTo(screen_width_last, screen_height_last)
                pyautogui.click()
                print('\n\nTesting Analog RX...')


            elif y[0] == ' ':

                pyautogui.moveTo(screen_width, screen_height)
                pyautogui.click()

                pyautogui.press(['m', 'o', 'd', ' ', 't', ' ', '0', 'enter'], interval=0.1)

                pyautogui.moveTo(screen_width_last, screen_height_last)
                pyautogui.click()

                print('\n\nStop TX')


            elif y[0] == '0':

                pyautogui.moveTo(screen_width, screen_height)
                pyautogui.click()

                pyautogui.press(['m', 'o', 'd', ' ', 't', ' ', '0', 'enter'], interval=0.1)

                pyautogui.moveTo(screen_width_last, screen_height_last)
                pyautogui.click()

                print('\n\nStop TX')


            elif y[0].upper() == 'Q':
                print('\n\nFinish')
                break

            else:
                print('\n\nInput Wrong')

    elif mode.upper() == 'Q':
        break

    else:
        print('\nInput Wrong')