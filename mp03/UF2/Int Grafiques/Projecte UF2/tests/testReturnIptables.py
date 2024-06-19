import subprocess
import sys

try:
    reglesIPtables = subprocess.run(["sudo","iptables", "-L", "-t", "nat"], capture_output=True, text=True, check=True)
except subprocess.CalledProcessError as error:
    if error.returncode == 4:
        print("Necessites iniciar el programa com administrador")
    else:
        print("An error occurred:", error)
        print("ass")