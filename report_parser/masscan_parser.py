import json.decoder
from json import load as json_load
from os import remove, rename
from random import randrange


class MasScanReportParser:
    def __init__(self, report_path: str):
        self.__report_file_path: str = report_path
        self.__tmp_dir: str = "..\\test\\"

    def check_format_report_file(self):
        pass

    def __json_parser(self) -> list:
        try:
            with open(file=self.__report_file_path, mode="r", encoding="UTF-8", errors="ignore") as json_file:
                return json_load(json_file)
        except json.decoder.JSONDecodeError:
            return self.fix_masscan_json(bad_json_file=self.__report_file_path)

    def fix_masscan_json(self, bad_json_file: str):
        """
        old bug masscan json format
        https://github.com/robertdavidgraham/masscan/issues/493
        """

        tmp_json_file: str = f"{self.__tmp_dir}tmp{randrange(10000, 99999)}"

        with open(file=bad_json_file, mode="r", encoding="UTF-8", errors="ignore") as json_file, \
                open(tmp_json_file, "w") as tmp_file:
            counter: int = 0
            number_lines: int = len(json_file.readlines())
            json_file.seek(0)

            for line in json_file.readlines():
                counter += 1
                if counter == number_lines - 1:
                    tmp_file.write(line.rstrip("\n").rstrip(","))
                    continue
                tmp_file.write(line)

        remove(bad_json_file)
        rename(tmp_json_file, bad_json_file)

        fix_json_file: str = bad_json_file

        self.__report_file_path = fix_json_file
        return self.__json_parser()

    def __json_get_value(self, user_value: str) -> list:
        all_ip: list = []
        for ip in self.__json_parser():
            ip: dict
            if ip.get(user_value) is not None:
                all_ip.append(ip.get(user_value))
        return all_ip

    def json_get_all_ip(self) -> list:
        return self.__json_get_value(user_value="ip")

    def json_get_all_port(self) -> list:
        all_port_info: list = self.__json_get_value(user_value="ports")
        all_port: list = []
        for port in all_port_info:
            all_port.append(port[0].get("port"))
        return all_port

    def get_json_clear_report(self) -> dict:
        is_result: dict = {}
        masscan_result = self.__json_parser()

        for item in masscan_result:
            item: dict
            if not is_result.get(item.get('ip')):
                is_result[item.get('ip')]: list = [ports_item['port'] for ports_item in item.get('ports')]
            is_result[item.get('ip')] += [ports_item['port'] for ports_item in item.get('ports')]

        return is_result


test_class = MasScanReportParser(report_path="..\\test\\test.json")
test_class.get_json_clear_report()
