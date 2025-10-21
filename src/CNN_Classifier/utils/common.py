import os
from box.exceptions import BoxValueError
import yaml
from CNN_Classifier import logger
import  json    
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object

    Args:
        path_to_yaml (Path): Path to the yaml file

    Raises:
        e: BoxValueError if yaml file is empty

    Returns:
        ConfigBox: ConfigBox object
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise BoxValueError("YAML file is empty")
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"BoxValueError: {e}")
        raise e
    except Exception as e:
        logger.error(f"Error reading the yaml file: {e}")
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list[Path]) -> None:
    """Creates a list of directories if they don't exist

    Args:
        path_to_directories (list[Path]): List of directory paths
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logger.info(f"Directory created at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict[str, Any]) -> None:
    """Saves a dictionary as a json file

    Args:
        path (Path): Path to the json file
        data (dict[str, Any]): Data to be saved
    """
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)    
    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads a json file and returns a ConfigBox object

    Args:
        path (Path): Path to the json file

    Returns:
        ConfigBox: ConfigBox object
    """
    with open(path, 'r') as json_file:
        content = json.load(json_file)
        logger.info(f"JSON file loaded from: {path}")
        return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """Saves data as a binary file using joblib

    Args:
        data (Any): Data to be saved
        path (Path): Path to the binary file
    """
    joblib.dump(data, path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads a binary file using joblib

    Args:
        path (Path): Path to the binary file

    Returns:
        Any: Loaded data
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """Get size in KB

    Args:
        path (Path): Path to the file

    Returns:
        str: Size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"                        


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())