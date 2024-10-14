import json

def setContext(pathToConfigFile):
    # Load config
    with open(pathToConfigFile) as config_file:
        config = json.load(config_file)
    return config