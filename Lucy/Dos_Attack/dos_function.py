# -*- coding: utf-8 -*-
from .data_dos.var_dos import *
import json
"""Set up useful fonction for dos attack"""

def dos_help() :
    print("this is some variables which have to be fill :\n\tap : access poin Mac address\n\tclient : target client Mac address\n\tgateway : gateway Mac address\n\ncommand : \n\tstart : to perform you attack \n\tback to get back to the main \n\targ : display attack args\n\tairodump : execute airodump-ng interface\n\thelp : display this")
    

def dos_args(data) :
    
    for i in data :
        print(f"{i} : {data[i]}")
        
        
def read_arg() :
    
    try : 
        with open(ARG_FILE, "r") as file :
            data = json.load(file)
    
    except FileNotFoundError :
        write_arg()
        
    else : 
        return data

def write_arg(data = {"ap" : None, "dest" : None}) :
    
    with open(ARG_FILE, "w") as file :
        json.dump(data, file)
        
    return 0
        
        

        