#!/bin/bash

VERSION="0.1"
PROGRAM="monitor"
AUTHOR="k2pme"

#############################################################
#   XXX: Coloured variables
#############################################################
green="\033[32m"
blue="\033[34m"
normal="\033[m"
red="\033[31m"
purple="033[m"

#############################################################
#   XXX: Configuration
#############################################################

EXIT_CODE["Error"]=200
EXIT_CODE["Success"]=0
EXIT_CODE["missing"]=1

#############################################################
#   XXX: Help functions
#############################################################

function show_usage() {
    echo -e "monitor [network card name] option"
    echo -e "Options "
    echo -e "\tstop :\t\tStop a network card"
    echo -e "\tstart :\t\tStart a network card"
    echo -e "\tnetcard :\tRead and write available network card list in $file_data"
    echo -e "\toff :\t\tPower off a network card"
    echo -e "\ton : \t\tPower on a network card"
    echo -e "\tv : \t\tShow version of this tool"
    echo -e "\tairodump : \tExecute airodump-ng from aircrack-ng suite"
    echo -e "\th or help :\tShow this section"

}

function show_version(){
    echo "$VERSION"
}


##############################################################
#   XXX: Useful Data
##############################################################

netLayer=""
layer=()
trash="/dev/null"
readonly file_data="Lucy/bash/netcard.json"
debug=""


##############################################################
#   XXX: Useful functions
##############################################################

monitor(){

    #set network card in monitor mode
    

    netLayer=$1     # getting name of the network card
    

    ifconfig $netLayer down         # stoping the network card in question
    iwconfig $netLayer mode monitor # Setting in monitor mode
    ifconfig $netLayer up           # finally start the card

    return ${EXIT_CODE["success"]}
}

down(){

    #Stop a network card 

    netLayer=$1     # getting name of the network card

    ifconfig $netLayer down
}

up(){
    
    # Start a network card
    

    netLayer=$1     # getting name of the network card

    ifconfig $netLayer up
}

monitorOff(){

    # disable monitor mode
    ifconfig $netLayer down 
    iwconfig $netLayer mode managed
    ifconfig $netLayer up
}

layerlist(){

    # read and write network support in a file

    a=1
    echo -n "{" > $file_data
    for i in $(ls /proc/net/dev_snmp6)
    do
        layer[$a]=$i
        echo -n "\"$a\" : \"$i\", " >> $file_data 

        ((a=a+1))
    done

    echo -n "\"status\" : \"ok\"}" >> $file_data 
    #chown "$SUDO_USER $file_data"
    echo -e "$green Sucesss ! $normal"
    return_check $?
}


airodump_api(){

    # execute a gnome-terminal with airodump-ng on

    gnome-terminal -- sudo airodump-ng $1
    return_check $?
}


privileges(){

    # Check privileges

    if [[ "$LOGNAME" = "root" ]]
    then

        echo "Starting"
    
    else 
        echo -e "$red Run this script with root privileges"
        exit ${EXIT_CODE["Error"]}
    fi
}


check_arg(){

    # check program args

    if [ -z "$1" ] && [ -z "$2" ]
    then
        echo -e "$red check your arg, please$normal"
        show_usage
        exit ${EXIT_CODE["Error"]}
    else
        echo -e "$green[*]arg ok[*]$normal"
    fi
}

return_check(){

    # exit code system

    if [ "$1" == 0 ]
    then 
        return ${EXIT_CODE["Success"]}
    else 
        echo -n "$red Fatal Error code 200 $normal"
        exit ${EXIT_CODE["Error"]}
    fi
}



####################################################################################
#   XXX: main 
#   This is the main code of this program
####################################################################################




privileges              # check privilges
check_arg $1 $2         # check the necessay arg 

#
#   stop argument
#
if [[ $2 == "stop" ]] && [[ -n "$1" ]]
then
    monitorOff $1
    exit ${EXIT_CODE["Success"]}

#
#   start argument
#
elif [[ $2 = "start" ]] && [[ -n "$1" ]]
then

    monitor $1
    exit ${EXIT_CODE["Success"]}

#
#   netcard argument
#
elif [[ $1 = "netcard" ]] && [[ -z "$2" ]]
then
    layerlist
    exit ${EXIT_CODE["Success"]}

#
#   off argument
#
elif [[ $2 = "off" ]] && [[ -n "$1" ]]
then
    down $1
    exit ${EXIT_CODE["Success"]}

#
#   on argument
#
elif [[ $2 = "on" ]] && [[ -n "$1" ]]
then
    up $1
    exit ${EXIT_CODE["Success"]}

#
#   v argument
#
elif [[ $1 = "v" ]] && [[ -z "$2" ]]
then
    show_version
    exit ${EXIT_CODE["Success"]}

#
#   airodump argument
#
elif [[ $2 = "airodump" ]] && [[ -n "$1" ]]
then
    airodump_api $1
    exit ${EXIT_CODE["Success"]}

#
#   help argument
#
elif [[ $1 = "help" ]] || [[ $1 = "h" ]] && [[ -z "$2" ]]
then 
    show_usage
    exit ${EXIT_CODE["Success"]}

else
    echo -e "$red arg error$normal"
    show_usage
    exit ${EXIT_CODE["Error"]}
fi


###         |
#####       |   
#           |   look on show_usage function for more information  
####        |
#######     |


