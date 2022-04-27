import yaml


class Helper:

    @staticmethod
    def load_yml_file(data_file=str):
        """
        Load a YML into a dict
        :param data_file: Complete path to the data file.
        :return: Dict with all the config values loaded.
        """
        with open(data_file) as f:
            config_dict = yaml.safe_load(f)
            return config_dict

