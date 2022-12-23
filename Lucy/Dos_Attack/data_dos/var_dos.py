from platform import uname

ARG_FILE = "Lucy/Dos_Attack/data_dos/arg_data.json"
USER_CHECK = "Lucy/bash/user.json"
PRIVILEGES = "Lucy/bash/check.sh"


if uname()[0] == "Linux" :
    CARD_FILE = "Lucy/bash/netcard.json"
    SHELL_FILE = "./Lucy/bash/monitor.sh"
    
elif uname()[0] == "Windows" :
    
    CARD_FILE = ""
    SHELL_FILE = "..\..\batch\monitor.bat"
else :
    print("Your system is not supported")
