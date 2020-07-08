import yaml
import os
from Common import all_path


class Yaml:
    def get_yaml_data(self, yaml_file):
        yaml_path = os.path.join(all_path.yaml_path, yaml_file)
        file = open(yaml_path, 'r', encoding="utf-8")
        file_data = file.read()
        file.close()
        data = yaml.load(file_data, Loader=yaml.FullLoader)
        # data_list = list(data)
        return data

    def write_yaml_data(self, yaml_file, yaml_data):
        from ruamel import yaml
        yaml_path = os.path.join(all_path.yaml_path, yaml_file)
        file = open(yaml_path, 'w', encoding='utf-8')
        yaml.dump(yaml_data, file, Dumper=yaml.RoundTripDumper, allow_unicode=True)
        file.close()


