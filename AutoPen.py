#! /usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='''Autopen is an open-source
                                 toolkit designed to assist security analysts,
                                 manufacturers, and various professionals to
                                 detect potential vulnerabilities in vehicles
                                 using the tools that will be provided. The
                                 product is meant to simplify installation,
                                 help the user in getting to know what tools
                                 are at their disposal, and teach them how to
                                 use them.''')
parser.add_argument('-g', '--gui', action='store_true', help='launch as GUI')

args = parser.parse_args()

# graphical user interface
if args.gui:
    import autopengui
# command-line interface
else:
    import autopencli

if __name__ == "__main__":
    if args.gui:
        autopengui.AutoPenApp().run()
    else:
        autopencli.AutoPenCli().run()

