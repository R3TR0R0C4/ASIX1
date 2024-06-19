import subprocess


def ipRoute(interficie):
    print(f"ip route | grep {interficie}" " | awk 'FNR==1{print $3}'")
    ruta=subprocess.run([f"ip route | grep {interficie}" " | awk 'FNR==1{print $3}'"], shell=True, capture_output=True, text=True)
    print(ruta.stdout)


ipRoute("eth0")