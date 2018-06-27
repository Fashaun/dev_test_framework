import os

def mrc_robot_uexit():
    print("Unexpected Exit ...")
    os._exit(1)

def mrc_robot_nexit():
    print("Normally Exit ...")
    os._exit(0)
