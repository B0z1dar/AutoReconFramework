from configurator import config


class MasScanStarter:
    def __init__(self, user_config: config.MasScanConfig):
        self.config = user_config
        self.target = self.config.get_targets()
        self.rate = self.config.get_rate()

    def start_scan(self):
        f"""sudo masscan -p1-65535 --{self.rate} --open-only {self.target} -oJ ..\\reports\\scan_result.json"""

