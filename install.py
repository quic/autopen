import general_use
import dependencies
import tools
import subprocess

class Tool:
    def __init__(self):
        self.tool_name = ''
        self.tool_repo_link = ''
        self.tool_repo_type = ''

    def init(self, tool_name, tool_repo_link, tool_repo_type):
        self.tool_name = tool_name
        self.tool_repo_link = tool_repo_link
        self.tool_repo_type = tool_repo_type

def install(toolname):
    '''
    This function calls the appropriate installation function (github,
    download or command line) to install the tool provided (toolname)
    '''
    try:
        fh = open('tool_and_repo.txt', 'r')
    except IOError:
        print 'Could not open file tool_repo_link.txt'

    lines = fh.readlines()
    tool = Tool()
    for line in lines:
        tool_name, tool_repo_link, tool_repo_type = line.split(',')
        if tool_name is toolname:
            tool.init(tool_name, tool_repo_link, tool_repo_type)
            break

    distro = general_use.check_distribution()
    pack_man = general_use.package_tool(distro)

    if tool.tool_repo_type is 'git':
        return tools.github_tools(pack_man, tool.tool_name, tool.tool_repo_link)
    elif tool.tool_repo_type is 'downloaded':
        return tools.downloaded_tools(pack_man, tool.tool_name, tool.tool_repo_link)
    elif tool.tool_repo_type is 'installed':
        return tools.installed_tools(pack_man, tool.tool_name)
    elif tool_name is 'can-utils-x': #special case
        return dependencies.can_utils_x(pack_man)


    # if toolname == 'canbus-utils':
        # return tools.github_tools(pack_man, 'canbus-utils', repo_canbus_utils)
    # elif toolname == 'Kayak':
        # return tools.github_tools(pack_man, 'Kayak', repo_kayak)
    # elif toolname == 'caringcaribou':
        # return tools.github_tools(pack_man, 'caringcaribou', repo_caringcaribou)    #CANT TEST THIS UNLESS A DEVICE IS ATTACHED AND SET UP
    # elif toolname == 'c0f':
        # return tools.github_tools(pack_man, 'c0f', repo_c0f)
    # elif toolname == 'udsim':
        # return tools.github_tools(pack_man, 'udsim', repo_udsim)    #CANT TEST THIS UNLESS A DEVICE IS ATTACHED AND SET UP
    # elif toolname == 'katoolin':
        # return tools.github_tools(pack_man, 'katoolin', repo_katoolin)
    # elif toolname == 'bluelog':
        # return tools.github_tools(pack_man, 'Bluelog', repo_bluelog)
    # elif toolname == 'bluemaho':
        # return tools.github_tools(pack_man, 'bluemaho', repo_bluemaho)
    # elif toolname == 'j1939':
        # return tools.github_tools(pack_man, 'j1939', repo_j1939)
    # elif toolname == 'canbadger-hw':
        # return tools.github_tools(pack_man, 'canbadger-hw', repo_canbadger)        #CANT TEST THIS UNLESS A DEVICE IS ATTACHED AND SET UP
    # elif toolname == 'canbadger-sw':
        # return tools.github_tools(pack_man, 'canbadger-sw', repo_canbadger_server)
    # elif toolname == 'can-utils-x':
        # return dependencies.can_utils_x(pack_man)

    # elif toolname == 'pyobd':
        # return tools.downloaded_tools(pack_man, 'pyobd', link_pyobd)    #MAY NOT INSTALL, IT NEEDS OLDER LIBRARIES
    # elif toolname == 'o2oo':
        # return tools.downloaded_tools(pack_man, 'o2oo', link_o2oo)

    # elif toolname == 'btscanner':
        # return tools.installed_tools(pack_man, 'btscanner')
    # elif toolname == 'gnuradio':
        # return tools.installed_tools(pack_man, 'gnuradio')
    # elif toolname == 'aircrack-ng':
        # return tools.installed_tools(pack_man, 'aircrack-ng')
    # elif toolname == 'gqrx':
        # return tools.installed_tools(pack_man, 'gqrx')
    # elif toolname == 'can-utils':
        # return tools.installed_tools(pack_man, 'can-utils')
    # elif toolname == 'wireshark':
        # return tools.installed_tools(pack_man, 'wireshark')
    # elif toolname == 'tshark':
        # return tools.installed_tools(pack_man, 'tshark')

def test(name):
    it = open('installed.txt', 'a')
    it.write(name)
    it.write('\n')
    return 0

