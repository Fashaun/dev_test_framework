import sys
import yaml
import os

#print("["+ len(sys.argv) + "] - " + os.getcwd())
#print(len(sys.argv))

def update():
    pwd = os.getcwd()
    yaml_exfile = pwd + '/data/config.yaml.save' 

    if len(sys.argv) != 6:
        print("Please specify enough data")
        os._exit(1)

    if not ( os.path.isfile(yaml_file)):
        print("No such file or directory: " + yaml_file)
        os._exit(1)

    with open(yaml_file) as f:
        config = yaml.load(f)

    dut = 'dut'+sys.argv[1]
    config['dut_mrc_server'] = sys.argv[2]
    config['dut_group']['member'][dut]['name'] = sys.argv[3]
    config['dut_group']['member'][dut]['device_name'] = sys.argv[4]
    config['dut_group']['member'][dut]['device_type'] = sys.argv[5]

    with open(yaml_file, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)

if __name__ == "__main__":
    update()
