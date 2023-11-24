import toml
# Open the TOML configuration file and load its contents
from scripts.substitute_variables import process
print("everywhere")
with open('config.toml') as f:
    config = toml.load(f)

role_file_type = config["role"].split(".")[-1] # gets what comes after the dot on the file path
with open(config["role"],"r") as file:
    if role_file_type == 'json':
        """this minifies the file if it's a json"""
        # print("json file")
        import json
        role = json.load(file)
        role = str(role) # the api doesn't take a json, it takes a string
        role = process(text=role, variables=config["context"])
        print(f"using role file {config['role']}")
    elif role_file_type == 'txt':
        role = file.read()
        role = process(text=role, variables=config["context"])
    else:
        raise Exception("unrecognized file extension")