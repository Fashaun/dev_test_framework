import yaml
import json

# Example Codes
with open("../config/config.yaml", "r") as stream:
    data = yaml.load(stream)
    print(data)
    print("\n")
    # Error
    #print(data.skip_files)
    # Go deeper
    print(data['mgmt_group']['member']['mrc_gw'])
    print(data['mgmt_mrc_server'] + "- yaya")

