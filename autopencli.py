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
                    'caringcaribou', 'Kayak', 'c0f', 'udsim', 'pyobd',
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

    def page_options(self, title, page):
        os.system('clear')
        print title
        print self.underline
        self.print_options(page.options)
        user_input = raw_input(self.PROMPT)
        return user_input

    def page_text(self, title, page):
        os.system('clear')
        print title
        print self.underline
        print page.text
        user_input = raw_input(self.PROMPT)
        return user_input

    def page_exec(self, title, page):
        while(True):
            user_input = self.page_text(title, page)
            if user_input in self.back_labels:
                break
            elif user_input in self.exit_labels:
                exit()

    def install_update_remove(self, tool_name):
        while(True):
            base_tool_page = BaseToolPage()
            tool_input = self.page_options(tool_name, base_tool_page)
            if tool_input in self.back_labels:
                break
            elif tool_input in self.exit_labels:
                exit()
            elif  tool_input == str(base_tool_page.options.index(
                base_tool_page.options[0])):
                # install tool
                return_code = install.install(tool_name)
                print return_code
                if return_code != 0:
                    print 'Error installing', tool_name
                else:
                    print 'Installed', tool_name
            elif tool_input == str(base_tool_page.options.index(
                base_tool_page.options[1])):
                # update tool
                return_code = update.update(tool_name)
                if return_code != 0:
                    print 'Error updating', tool_name
                else:
                    print 'Updated', tool_name
            elif tool_input == str(base_tool_page.options.index(
                base_tool_page.options[2])):
                # uninstall tool
                return_code = uninstall.uninstall(tool_name)
                if return_code != 0:
                    print 'Error Uninstalling', tool_name
                else:
                    print 'Uninstalled', tool_name
            raw_input('Press enter to continue...')

    def run(self):
        while(True):
            # splash screen options
            splash_screen = SplashScreen()
            splash_option = self.page_options('AutoPen', splash_screen)
            if splash_option in self.exit_labels:
                exit()
            elif splash_option == str(splash_screen.options.index(
                    splash_screen.options[0])):
                # tools page options
                tools_page = ToolsPage()
                while(True):
                    tools_page_input = self.page_options(
                            splash_screen.options[0], tools_page)
                    if tools_page_input in self.back_labels:
                        break
                    elif tools_page_input in self.exit_labels:
                        exit()
                    elif tools_page_input in str(tools_page.options.index(
                        tools_page.options[0])):
                        # CAN page options
                        can_page = CanPage()
                        while(True):
                            can_page_input = self.page_options(
                                    tools_page.options[0], can_page)
                            if can_page_input in self.back_labels:
                                break
                            elif can_page_input in self.exit_labels:
                                exit()
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[0])):
                                # CAN utils options
                                self.install_update_remove(can_page.options[0])
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[1])):
                                # CAN bus utils options
                                self.install_update_remove(can_page.options[1])
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[2])):
                                # CAN utils X options
                                self.install_update_remove(can_page.options[2])
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[3])):
                                # CAN utils j1939 options
                                self.install_update_remove(can_page.options[3])
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[4])):
                                # CAN Badger HW options
                                self.install_update_remove(can_page.options[4])
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[5])):
                                # CAN Badger SW options
                                self.install_update_remove(can_page.options[5])
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[6])):
                                # Caring Caribou options
                                self.install_update_remove(can_page.options[6])
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[7])):
                                # Kayak options
                                self.install_update_remove(can_page.options[7])
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[8])):
                                # c0f options
                                self.install_update_remove(can_page.options[8])
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[9])):
                                # UDSim options
                                self.install_update_remove(can_page.options[9])
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[10])):
                                # PyOBD options
                                self.install_update_remove(can_page.options[10])
                            elif can_page_input == str(can_page.options.index(
                                    can_page.options[11])):
                                # O2OO options
                                self.install_update_remove(can_page.options[11])
                    elif tools_page_input in str(tools_page.options.index(
                        tools_page.options[1])):
                        # SDR page options
                        sdr_page = SdrPage()
                        while(True):
                            sdr_page_input = self.page_options(
                                    tools_page.options[1], sdr_page)
                            if sdr_page_input in self.back_labels:
                                break
                            elif sdr_page_input in self.exit_labels:
                                exit()
                            elif sdr_page_input == str(sdr_page.options.index(
                                    sdr_page.options[0])):
                                # GNU Radio options
                                self.install_update_remove(sdr_page.options[0])
                            elif sdr_page_input == str(sdr_page.options.index(
                                    sdr_page.options[1])):
                                # gqrx options
                                self.install_update_remove(sdr_page.options[1])
                    elif tools_page_input in str(tools_page.options.index(
                        tools_page.options[2])):
                        # Miscellaneous tools page options
                        misc_page = MiscPage()
                        while(True):
                            misc_page_input = self.page_options(
                                    tools_page.options[2], misc_page)
                            if misc_page_input in self.back_labels:
                                break
                            elif misc_page_input in self.exit_labels:
                                exit()
                            elif misc_page_input == str(misc_page.options.index(
                                    misc_page.options[0])):
                                # katoolin options
                                self.install_update_remove(misc_page.options[0])
                    elif tools_page_input in str(tools_page.options.index(
                        tools_page.options[3])):
                        # bluetooth/wifi page options
                        bluetooth_wifi_page = BluetoothWifiPage()
                        while(True):
                            bluetooth_wifi_page_input = self.page_options(
                                    tools_page.options[3],
                                    bluetooth_wifi_page)
                            if bluetooth_wifi_page_input in self.back_labels:
                                break
                            elif bluetooth_wifi_page_input in self.exit_labels:
                                exit()
                            elif bluetooth_wifi_page_input == str(bluetooth_wifi_page.options.index(
                                    bluetooth_wifi_page.options[0])):
                                # aircrack-ng options
                                self.install_update_remove(bluetooth_wifi_page.options[0])
                            elif bluetooth_wifi_page_input == str(bluetooth_wifi_page.options.index(
                                    bluetooth_wifi_page.options[1])):
                                # bluelog options
                                self.install_update_remove(bluetooth_wifi_page.options[1])
                            elif bluetooth_wifi_page_input == str(bluetooth_wifi_page.options.index(
                                    bluetooth_wifi_page.options[2])):
                                # bluemaho options
                                self.install_update_remove(bluetooth_wifi_page.options[2])
                            elif bluetooth_wifi_page_input == str(bluetooth_wifi_page.options.index(
                                    bluetooth_wifi_page.options[3])):
                                # btscanner options
                                self.install_update_remove(bluetooth_wifi_page.options[3])
                            elif bluetooth_wifi_page_input == str(bluetooth_wifi_page.options.index(
                                    bluetooth_wifi_page.options[4])):
                                # tshark options
                                self.install_update_remove(bluetooth_wifi_page.options[4])
                            elif bluetooth_wifi_page_input == str(bluetooth_wifi_page.options.index(
                                    bluetooth_wifi_page.options[5])):
                                # wireshark options
                                self.install_update_remove(bluetooth_wifi_page.options[5])
                    elif tools_page_input in str(tools_page.options.index(
                        tools_page.options[4])):
                        # All tools page options
                        all_tools_page = AllToolsPage()
                        while(True):
                            all_tools_page_input = self.page_options(
                                    tools_page.options[4],
                                    all_tools_page)
                            if all_tools_page_input in self.back_labels:
                                break
                            elif all_tools_page_input in self.exit_labels:
                                exit()
                            elif all_tools_input == str(all_tools_page.options.index(
                                    all_tools_page.options[0])):
                                # options
                                self.install_update_remove(all_tools_page.options[0])
            elif splash_option == str(splash_screen.options.index(
                    splash_screen.options[1])):
                # how to page text
                self.page_exec(splash_screen.options[1], HowToPage())
            elif splash_option == str(splash_screen.options.index(
                    splash_screen.options[2])):
                # about autopen page text
                self.page_exec(splash_screen.options[2], AboutAutoPenPage())
            elif splash_option == str(splash_screen.options.index(
                    splash_screen.options[3])):
                # terms and conditions text
                self.page_exec(splash_screen.options[2], TermsAndConditionsPage())

