import toml
# Open the TOML configuration file and load its contents
with open('config.toml') as f:
    config = toml.load(f)