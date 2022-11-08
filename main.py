import argparse
from report_parser import masscan_parser
from configurator import config
from recon import port_finder


class ArgumentParser:
    def __int__(self):
        pass


"""

class CommandHandler:
    pass

class UserValueChecker:
    pass
    
"""
user_set_rate = "500"
user_set_target = "192.168.0.1"

new_config = config.MasScanConfig(masscan_rate=user_set_rate, masscan_target=user_set_rate)

new_scan = port_finder.MasScanStarter(user_config=new_config)

if __name__ == '__main__':
    pass
