from configurator import config
from os import system


class MasScanStarter:
    def __init__(self, user_config: config.MasScanConfig):
        self.config = user_config
        self.target = self.config.get_targets()
        self.rate = self.config.get_rate()

    def start_scan(self):
        f"""sudo masscan -p1-65535 --{self.rate} --open-only {self.target} -oJ ..\\reports\\scan_result.json"""


class NmapStartScan:
    def __init__(self):
        self.vuln_date_base: list = []
        self.report_path: str = ""

    @staticmethod
    def test_vuln_scan_func(target: str, ports: str):
        system(f"nmap -sV -p {ports} --script vulscan,vuln,vulners --script-args vulscandb=exploitdb.csv {target} -Pn")
