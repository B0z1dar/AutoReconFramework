from ipaddress import *


class MasScanConfig:
    def __init__(self, masscan_rate: str, masscan_target: str):
        self.__rate = masscan_rate
        self.__target = masscan_target

    def set_rate(self):
        pass

    def set_targets(self):
        pass

    def get_rate(self):
        pass

    def get_targets(self):
        pass


class NmapConfig:
    def __init__(self):
        pass

    def set_cve_db(self):
        pass
