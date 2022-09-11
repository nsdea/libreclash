import yaml
import json
import flask

from datetime import datetime

def add_ext(filename: str, extension: str='json') -> str:
    """Appends the file extension the given file name if needed.

    Args:
        filename (str): File name. With or without extension.
        extension (str): File extension. With or without dot. Defaults to JSON

    Returns:
        str: Full file name.
    """

    if not extension.startswith('.'):
        extension = f'.{extension}' 

    if not filename.endswith(extension):
        filename += extension

    return 'libreclash/' + filename    

def read_json(filename: str):
    """Reads a JSON file and returns the loaded data.

    Args:
        name (str): The file to read (with or without .json)
    """

    with open(add_ext(filename), 'r') as f:
        return json.load(f)

def write_json(filename: str, data) -> None:
    """Writes data to a JSON file.

    Args:
        filename (str): The file to write to (with or without .json)
        data (_type_): The data to write to the file.
    """

    with open(add_ext(filename), 'w') as f:
        json.dump(data, f, indent=4, sort_keys=False)

def b_to_gb(size: float) -> int:
    """Converts bytes to gigabystes.

    Args:
        size (float): bytes

    Returns:
        int: gigabytes
    """
    return size//1000000000

def ip(request: flask.Request) -> str: # PRIVACY NOTICE
    if not request.environ.get('HTTP_X_FORWARDED_FOR'):
        return request.environ['REMOTE_ADDR']
    return request.environ['HTTP_X_FORWARDED_FOR']

def yml(path: str, edit_to=None):
    path = f'{path}.yml'

    if not edit_to:
        try:
            with open(path) as f:
                return yaml.load(f.read(), Loader=yaml.SafeLoader)
        except:
            open(path, 'w').write('{}')
            return {}

    with open(path, 'w') as f:
        yaml.dump(edit_to, f, sort_keys=False, default_flow_style=False, indent=4)

def unix_to_readable(unix):
    return datetime.utcfromtimestamp(float(unix)).strftime('%Y/%m/%d %H:%M')
