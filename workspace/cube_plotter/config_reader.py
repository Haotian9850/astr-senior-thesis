import yaml 

def read_config(config_name):
    result = dict()
    with open(config_name) as config:
        result = yaml.safe_load(config)
    return result
