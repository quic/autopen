'''
Command-line interface for AutoPen
'''

import os
import install
import open_
import uninstall
import update

class SplashScreen:
    def __init__(self):
        self.options = ('Tools', 'How-To', 'About AutoPen',
                'Terms and Conditions')

class ToolsPage:
    def __init__(self):
        self.options = ('CAN', 'SDR', 'Miscellaneous',
                'Bluetooth/Wifi', 'See All Tools')

class HowToPage:
    def __init__(self):
        self.text = '''
        How to do things in AutoPen will be updated here
        '''

class AboutAutoPenPage:
    def __init__(self):
        self.text = '''
        Autopen is an open-source toolkit designed to assist security
        analysts, manufacturers, and various professionals to detect
        potential in vehicles using the tools that will be provided. The
        product is meant simplify installation, help the user in getting
        to know what tools are their disposal, and teach them how to use
        them.
        '''

class TermsAndConditionsPage:
    def __init__(self):
        self.text = '''
        Do not do anything that is illegal and will get you in trouble.
        '''

class CanPage:
    def __init__(self):
        self.options = ('can-utils', 'canbus-utils', 'can-utils-x',
                    'j1939', 'canbadger-hw', 'canbadger-sw',
                    'caringcaribou', 'kayak', 'c0f', 'udsim', 'pyobd',
                    'o2oo')

class SdrPage:
    def __init__(self):
        self.options = ('gnuradio', 'gqrx')

class MiscPage:
    def __init__(self):
        self.options = ['katoolin']

class BluetoothWifiPage:
    def __init__(self):
        self.options = ('aircrack-ng', 'bluelog', 'bluemaho', 'btscanner',
                    'tshark', 'wireshark')
class AllToolsPage:
    def __init__(self):
        self.options = CanPage().options + SdrPage().options + \
                tuple(MiscPage().options) + BluetoothWifiPage().options

class BaseToolPage:
    def __init__(self):
        self.options = ('install', 'update', 'uninstall')

class AutoPenCli:
    def __init__(self):
        self.PROMPT = 'autopen> '
        self.exit_labels = ('exit', 'quit')
        self.back_labels = ('back', 'b')
        self.underline = '========================='

    def print_options(self, options):
        for serial, option in enumerate(options):
            print serial, option

    def install_update_remove(self, tool_name):
        while(True):
            os.system('clear')
            print tool_name
            print self.underline
            base_tool_page = BaseToolPage()
            self.print_options(base_tool_page.options)
            tool_input = raw_input(self.PROMPT)
            if tool_input in self.back_labels:
                break
            elif tool_input in self.exit_labels:
                exit()
            elif  tool_input == str(base_tool_page.options.index(
                base_tool_page.options[0])):
                # install tool
                install.install(tool_name)
            elif tool_input == str(base_tool_page.options.index(
                base_tool_page.options[1])):
                # update tool
                update.update(tool_name)
            elif tool_input == str(base_tool_page.options.index(
                base_tool_page.options[2])):
                # uninstall tool
                uninstall.uninstall(tool_name)

    def run(self):
        while(True):
            # splash screen options
            os.system('clear')
            print 'AutoPen'
            print self.underline
            splash_screen = SplashScreen()
            self.print_options(splash_screen.options)
            splash_option = raw_input(self.PROMPT)
            if splash_option in self.exit_labels:
                exit()
            elif splash_option == str(splash_screen.options.index(
                    splash_screen.options[0])):
                # tools page options
                tools_page = ToolsPage()
                while(True):
                    os.system('clear')
                    print splash_screen.options[0]
                    print self.underline
                    self.print_options(tools_page.options)
                    tools_page_input = raw_input(self.PROMPT)
                    if tools_page_input in self.back_labels:
                        break
                    elif tools_page_input in self.exit_labels:
                        exit()
                    elif tools_page_input in str(tools_page.options.index(
                        tools_page.options[0])):
                        # CAN page options
                        can_page = CanPage()
                        while(True):
                            os.system('clear')
                            print tools_page.options[0]
                            print self.underline
                            self.print_options(can_page.options)
                            can_page_input = raw_input(self.PROMPT)
                            if can_page_input in self.back_labels:
                                break
                            elif can_page_input in self.exit_labels:
                                exit()
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[0])):
                                # CAN utils options
                                tool_name = can_page.options[0]
                                self.install_update_remove(tool_name)
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[1])):
                                tool_name = can_page.options[1]
                                # CAN bus utils options
                                self.install_update_remove(tool_name)
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[2])):
                                # CAN utils X options
                                while(True):
                                    os.system('clear')
                                    print can_page.options[2]
                                    print self.underline
                                    base_tool_page = BaseToolPage()
                                    self.print_options(base_tool_page.options)
                                    tool_input = raw_input(self.PROMPT)
                                    if tool_input in self.back_labels:
                                        break
                                    elif tool_input in self.exit_labels:
                                        exit()
                                    elif  tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[0])):
                                        # install tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[1])):
                                        # update tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[2])):
                                        # uninstall tool
                                        pass
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[3])):
                                # CAN utils j1939 options
                                while(True):
                                    os.system('clear')
                                    print can_page.options[3]
                                    print self.underline
                                    base_tool_page = BaseToolPage()
                                    self.print_options(base_tool_page.options)
                                    tool_input = raw_input(self.PROMPT)
                                    if tool_input in self.back_labels:
                                        break
                                    elif tool_input in self.exit_labels:
                                        exit()
                                    elif  tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[0])):
                                        # install tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[1])):
                                        # update tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[2])):
                                        # uninstall tool
                                        pass
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[4])):
                                # CAN Badger HW options
                                while(True):
                                    os.system('clear')
                                    print can_page.options[4]
                                    print self.underline
                                    base_tool_page = BaseToolPage()
                                    self.print_options(base_tool_page.options)
                                    tool_input = raw_input(self.PROMPT)
                                    if tool_input in self.back_labels:
                                        break
                                    elif tool_input in self.exit_labels:
                                        exit()
                                    elif  tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[0])):
                                        # install tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[1])):
                                        # update tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[2])):
                                        # uninstall tool
                                        pass
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[5])):
                                # CAN Badger SW options
                                while(True):
                                    os.system('clear')
                                    print can_page.options[5]
                                    print self.underline
                                    base_tool_page = BaseToolPage()
                                    self.print_options(base_tool_page.options)
                                    tool_input = raw_input(self.PROMPT)
                                    if tool_input in self.back_labels:
                                        break
                                    elif tool_input in self.exit_labels:
                                        exit()
                                    elif  tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[0])):
                                        # install tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[1])):
                                        # update tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[2])):
                                        # uninstall tool
                                        pass
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[6])):
                                # Caring Caribou options
                                while(True):
                                    os.system('clear')
                                    print can_page.options[6]
                                    print self.underline
                                    base_tool_page = BaseToolPage()
                                    self.print_options(base_tool_page.options)
                                    tool_input = raw_input(self.PROMPT)
                                    if tool_input in self.back_labels:
                                        break
                                    elif tool_input in self.exit_labels:
                                        exit()
                                    elif  tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[0])):
                                        # install tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[1])):
                                        # update tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[2])):
                                        # uninstall tool
                                        pass
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[7])):
                                # Kayak options
                                while(True):
                                    os.system('clear')
                                    print can_page.options[7]
                                    print self.underline
                                    base_tool_page = BaseToolPage()
                                    self.print_options(base_tool_page.options)
                                    tool_input = raw_input(self.PROMPT)
                                    if tool_input in self.back_labels:
                                        break
                                    elif tool_input in self.exit_labels:
                                        exit()
                                    elif  tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[0])):
                                        # install tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[1])):
                                        # update tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[2])):
                                        # uninstall tool
                                        pass
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[8])):
                                # c0f options
                                while(True):
                                    os.system('clear')
                                    print can_page.options[8]
                                    print self.underline
                                    base_tool_page = BaseToolPage()
                                    self.print_options(base_tool_page.options)
                                    tool_input = raw_input(self.PROMPT)
                                    if tool_input in self.back_labels:
                                        break
                                    elif tool_input in self.exit_labels:
                                        exit()
                                    elif  tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[0])):
                                        # install tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[1])):
                                        # update tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[2])):
                                        # uninstall tool
                                        pass
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[9])):
                                # UDSim options
                                while(True):
                                    os.system('clear')
                                    print can_page.options[9]
                                    print self.underline
                                    base_tool_page = BaseToolPage()
                                    self.print_options(base_tool_page.options)
                                    tool_input = raw_input(self.PROMPT)
                                    if tool_input in self.back_labels:
                                        break
                                    elif tool_input in self.exit_labels:
                                        exit()
                                    elif  tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[0])):
                                        # install tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[1])):
                                        # update tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[2])):
                                        # uninstall tool
                                        pass
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[10])):
                                # PyOBD options
                                while(True):
                                    os.system('clear')
                                    print can_page.options[10]
                                    print self.underline
                                    base_tool_page = BaseToolPage()
                                    self.print_options(base_tool_page.options)
                                    tool_input = raw_input(self.PROMPT)
                                    if tool_input in self.back_labels:
                                        break
                                    elif tool_input in self.exit_labels:
                                        exit()
                                    elif  tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[0])):
                                        # install tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[1])):
                                        # update tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[2])):
                                        # uninstall tool
                                        pass
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[11])):
                                # O2OO options
                                while(True):
                                    os.system('clear')
                                    print can_page.options[11]
                                    print self.underline
                                    base_tool_page = BaseToolPage()
                                    self.print_options(base_tool_page.options)
                                    tool_input = raw_input(self.PROMPT)
                                    if tool_input in self.back_labels:
                                        break
                                    elif tool_input in self.exit_labels:
                                        exit()
                                    elif  tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[0])):
                                        # install tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[1])):
                                        # update tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[2])):
                                        # uninstall tool
                                        pass
                    elif tools_page_input in str(tools_page.options.index(
                        tools_page.options[1])):
                        # SDR page options
                        sdr_page = SdrPage()
                        while(True):
                            os.system('clear')
                            print tools_page.options[1]
                            print self.underline
                            self.print_options(sdr_page.options)
                            sdr_page_input = raw_input(self.PROMPT)
                            if sdr_page_input in self.back_labels:
                                break
                            elif sdr_page_input in self.exit_labels:
                                exit()
                            elif sdr_page_input == str(sdr_page.options.index(
                                    sdr_page.options[0])):
                                # GNU Radio options
                                while(True):
                                    os.system('clear')
                                    print sdr_page.options[0]
                                    print self.underline
                                    base_tool_page = BaseToolPage()
                                    self.print_options(base_tool_page.options)
                                    tool_input = raw_input(self.PROMPT)
                                    if tool_input in self.back_labels:
                                        break
                                    elif tool_input in self.exit_labels:
                                        exit()
                                    elif  tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[0])):
                                        # install tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[1])):
                                        # update tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[2])):
                                        # uninstall tool
                                        pass
                            elif sdr_page_input == str(sdr_page.options.index(
                                    sdr_page.options[1])):
                                # gqrx options
                                while(True):
                                    os.system('clear')
                                    print sdr_page.options[1]
                                    print self.underline
                                    base_tool_page = BaseToolPage()
                                    self.print_options(base_tool_page.options)
                                    tool_input = raw_input(self.PROMPT)
                                    if tool_input in self.back_labels:
                                        break
                                    elif tool_input in self.exit_labels:
                                        exit()
                                    elif  tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[0])):
                                        # install tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[1])):
                                        # update tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[2])):
                                        # uninstall tool
                                        pass
                    elif tools_page_input in str(tools_page.options.index(
                        tools_page.options[2])):
                        # Miscellaneous tools page options
                        misc_page = MiscPage()
                        while(True):
                            os.system('clear')
                            print tools_page.options[2]
                            print self.underline
                            self.print_options(misc_page.options)
                            misc_page_input = raw_input(self.PROMPT)
                            if misc_page_input in self.back_labels:
                                break
                            elif misc_page_input in self.exit_labels:
                                exit()
                            elif misc_page_input == str(misc_page.options.index(
                                    misc_page.options[0])):
                                # katoolin options
                                while(True):
                                    os.system('clear')
                                    print misc_page.options[0]
                                    print self.underline
                                    base_tool_page = BaseToolPage()
                                    self.print_options(base_tool_page.options)
                                    tool_input = raw_input(self.PROMPT)
                                    if tool_input in self.back_labels:
                                        break
                                    elif tool_input in self.exit_labels:
                                        exit()
                                    elif  tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[0])):
                                        # install tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[1])):
                                        # update tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[2])):
                                        # uninstall tool
                                        pass
                    elif tools_page_input in str(tools_page.options.index(
                        tools_page.options[3])):
                        # bluetooth/wifi page options
                        bluetooth_wifi_page = BluetoothWifiPage()
                        while(True):
                            os.system('clear')
                            print tools_page.options[3]
                            print self.underline
                            self.print_options(bluetooth_wifi_page.options)
                            bluetooth_wifi_page_input = raw_input(self.PROMPT)
                            if bluetooth_wifi_page_input in self.back_labels:
                                break
                            elif bluetooth_wifi_page_input in self.exit_labels:
                                exit()
                            elif bluetooth_wifi_page_input == str(bluetooth_wifi_page.options.index(
                                    bluetooth_wifi_page.options[0])):
                                # aircrack-ng options
                                while(True):
                                    os.system('clear')
                                    print bluetooth_wifi_page.options[0]
                                    print self.underline
                                    base_tool_page = BaseToolPage()
                                    self.print_options(base_tool_page.options)
                                    tool_input = raw_input(self.PROMPT)
                                    if tool_input in self.back_labels:
                                        break
                                    elif tool_input in self.exit_labels:
                                        exit()
                                    elif  tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[0])):
                                        # install tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[1])):
                                        # update tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[2])):
                                        # uninstall tool
                                        pass
                            elif bluetooth_wifi_page_input == str(bluetooth_wifi_page.options.index(
                                    bluetooth_wifi_page.options[1])):
                                # bluelog options
                                while(True):
                                    os.system('clear')
                                    print bluetooth_wifi_page.options[1]
                                    print self.underline
                                    base_tool_page = BaseToolPage()
                                    self.print_options(base_tool_page.options)
                                    tool_input = raw_input(self.PROMPT)
                                    if tool_input in self.back_labels:
                                        break
                                    elif tool_input in self.exit_labels:
                                        exit()
                                    elif  tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[0])):
                                        # install tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[1])):
                                        # update tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[2])):
                                        # uninstall tool
                                        pass
                            elif bluetooth_wifi_page_input == str(bluetooth_wifi_page.options.index(
                                    bluetooth_wifi_page.options[2])):
                                # bluemaho options
                                while(True):
                                    os.system('clear')
                                    print bluetooth_wifi_page.options[2]
                                    print self.underline
                                    base_tool_page = BaseToolPage()
                                    self.print_options(base_tool_page.options)
                                    tool_input = raw_input(self.PROMPT)
                                    if tool_input in self.back_labels:
                                        break
                                    elif tool_input in self.exit_labels:
                                        exit()
                                    elif  tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[0])):
                                        # install tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[1])):
                                        # update tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[2])):
                                        # uninstall tool
                                        pass
                            elif bluetooth_wifi_page_input == str(bluetooth_wifi_page.options.index(
                                    bluetooth_wifi_page.options[3])):
                                # btscanner options
                                while(True):
                                    os.system('clear')
                                    print bluetooth_wifi_page.options[3]
                                    print self.underline
                                    base_tool_page = BaseToolPage()
                                    self.print_options(base_tool_page.options)
                                    tool_input = raw_input(self.PROMPT)
                                    if tool_input in self.back_labels:
                                        break
                                    elif tool_input in self.exit_labels:
                                        exit()
                                    elif  tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[0])):
                                        # install tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[1])):
                                        # update tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[2])):
                                        # uninstall tool
                                        pass
                            elif bluetooth_wifi_page_input == str(bluetooth_wifi_page.options.index(
                                    bluetooth_wifi_page.options[4])):
                                # tshark options
                                while(True):
                                    os.system('clear')
                                    print bluetooth_wifi_page.options[4]
                                    print self.underline
                                    base_tool_page = BaseToolPage()
                                    self.print_options(base_tool_page.options)
                                    tool_input = raw_input(self.PROMPT)
                                    if tool_input in self.back_labels:
                                        break
                                    elif tool_input in self.exit_labels:
                                        exit()
                                    elif  tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[0])):
                                        # install tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[1])):
                                        # update tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[2])):
                                        # uninstall tool
                                        pass
                            elif bluetooth_wifi_page_input == str(bluetooth_wifi_page.options.index(
                                    bluetooth_wifi_page.options[5])):
                                # wireshark options
                                while(True):
                                    os.system('clear')
                                    print bluetooth_wifi_page.options[5]
                                    print self.underline
                                    base_tool_page = BaseToolPage()
                                    self.print_options(base_tool_page.options)
                                    tool_input = raw_input(self.PROMPT)
                                    if tool_input in self.back_labels:
                                        break
                                    elif tool_input in self.exit_labels:
                                        exit()
                                    elif  tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[0])):
                                        # install tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[1])):
                                        # update tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[2])):
                                        # uninstall tool
                                        pass
                    elif tools_page_input in str(tools_page.options.index(
                        tools_page.options[4])):
                        # All tools page options
                        all_tools_page = AllToolsPage()
                        while(True):
                            os.system('clear')
                            print tools_page.options[4]
                            print self.underline
                            self.print_options(all_tools_page.options)
                            all_tools_page_input = raw_input(self.PROMPT)
                            if all_tools_page_input in self.back_labels:
                                break
                            elif all_tools_page_input in self.exit_labels:
                                exit()
                            elif all_tools_input == str(all_tools_page.options.index(
                                    all_tools_page.options[5])):
                                # options
                                while(True):
                                    os.system('clear')
                                    print all_tools_page.options[5]
                                    print self.underline
                                    base_tool_page = BaseToolPage()
                                    self.print_options(base_tool_page.options)
                                    tool_input = raw_input(self.PROMPT)
                                    if tool_input in self.back_labels:
                                        break
                                    elif tool_input in self.exit_labels:
                                        exit()
                                    elif  tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[0])):
                                        # install tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[1])):
                                        # update tool
                                        pass
                                    elif tool_input == str(base_tool_page.options.index(
                                        base_tool_page.options[2])):
                                        # uninstall tool
                                        pass
            elif splash_option == str(splash_screen.options.index(
                    splash_screen.options[1])):
                # how to page text
                how_to_page = howtopage()
                while(true):
                    os.system('clear')
                    print splash_screen.options[1]
                    print self.underline
                    print how_to_page.text
                    how_to_input = raw_input(self.prompt)
                    if how_to_input in self.back_labels:
                        break
                    elif how_to_input in self.exit_labels:
                        exit()
            elif splash_option == str(splash_screen.options.index(
                    splash_screen.options[2])):
                # about autopen page text
                about_autopen = aboutautopenpage()
                while(true):
                    os.system('clear')
                    print splash_screen.options[2]
                    print self.underline
                    print about_autopen.text
                    about_autopen_input = raw_input(self.prompt)
                    if about_autopen_input in self.back_labels:
                        break
                    elif about_autopen_input in self.exit_labels:
                        exit()
            elif splash_option == str(splash_screen.options.index(
                    splash_screen.options[3])):
                # terms and conditions text
                terms_and_conditions = termsandconditionspage()
                while(true):
                    os.system('clear')
                    print splash_screen.options[3]
                    print self.underline
                    print terms_and_conditions.text
                    tnc_input = raw_input(self.prompt)
                    if tnc_input in self.back_labels:
                        break
                    elif tnc_input in self.exit_labels:
                        exit()

