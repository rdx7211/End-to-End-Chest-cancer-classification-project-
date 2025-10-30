from CNN_Classifier.constants import *
from CNN_Classifier.utils.common import read_yaml, create_directories
from CNN_Classifier.entity.config_entity import (DataIngestionConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath: Path = CONFIG_FILE_PATH,
        params_filepath: Path = PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([Path(self.config["artifacts_root"])])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config["data_ingestion"]

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config["root_dir"]),
            source_URL=config["source_URL"],
            local_data_file=Path(config["local_data_file"]),
            unzip_dir=Path(config["unzip_dir"])
        )

        return data_ingestion_config