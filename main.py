import argparse
from report_parser import masscan_parser
from configurator import config
from recon import scaner


class ArgumentParser:
    def __int__(self):
        self.user_arguments = argparse.ArgumentParser(description="Auto target vuln recon")
        self.masscan_rate = self.user_arguments.add_argument("--rate", help="Masscan scan speed rate")
        self.scan_target = self.user_arguments.add_argument("--target", help="Set target in formate "
                                                                             "x.x.x.x or x.x.x.x-x.x.x.x or"
                                                                             "x.x.x.x/x")
        # self.formate_test = self.user_arguments.add_argument("--web", help="It's set it flag") add in future
        self.arguments = self.user_arguments.parse_args()


"""

class CommandHandler:
    pass

class UserValueChecker:
    pass
    
"""
user_set_rate = "500"
user_set_target = "192.168.0.1"

new_config_masscan = config.MasScanConfig(masscan_rate=user_set_rate, masscan_target=user_set_rate)
new_scan_masscan = scaner.MasScanStarter(user_config=new_config_masscan)

new_scan_nmap = scaner.NmapStartScan()

masscan_result_parser = masscan_parser.MasScanReportParser(report_path="test\\plesk.json")
find_target = masscan_result_parser.json_get_clear_report()
print(find_target)
for i in find_target:
    i: dict
    target: str = i.get('ip')
    ports: str = ','.join([str(i) for i in i.get('ports')])
    print(f"sc")
    new_scan_nmap.test_vuln_scan_func(target=target, ports=ports)


if __name__ == '__main__':
    pass
