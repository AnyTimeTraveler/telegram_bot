def load_config(path):
    import json
    config_file = open(path, 'r')
    config = json.loads(config_file.read())
    config_file.close()
    return config


def save_config(path, config):
    import json
    config_file = open(path, 'w')
    config_file.write(json.dumps(config))
    config_file.close()


def import_file(path, file_name):
    import importlib.util
    import os

    spec = importlib.util.spec_from_file_location(path, (os.path.abspath(path) + '/' + file_name))
    imported = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(imported)
    return imported


def check_module(module):
    try:
        if not module.get_name:
            return False
        if not module.load:
            return False
    except AttributeError:
        return False
    return True
