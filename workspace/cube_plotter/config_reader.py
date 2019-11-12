import yaml 

def read_config(config_name):
    result = dict()
    with open(config_name) as config:
        result = yaml.safe_load(config)
    print(result)

read_config("config_test.yaml")
