# herramientas automatizadas

# ennumerar puertos, determinar las versionas, buscara si hay una vulnerabilidad

import os 
import sys 
import subprocess

def parser(nmap_query, ip):
    """  print("-"*50)
    print(ip)
    results = os.system(nmap_query)
    print("-"*50)
    print(results)
    print("-"*50)
    with open('readme.txt', 'w') as f:
        f.write(nmap_query) """
   
    print("-" * 50)
    print(ip)
    
    # Ejecuta el comando y captura la salida
    result = subprocess.run(nmap_query, shell=True, stdout=subprocess.PIPE, text=True)
    output = result.stdout
    
    print("-" * 50)
    print(output)
    print("-" * 50)

    with open('readme2.txt', 'w') as f:
        f.write(output)


def main():
    target="199.250.215.182"
    mode = " --top-ports 100 --script vuln -sV"
    consulta = "nmap " + target + mode
    parser(consulta, target)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt: 
        sys.exit()

        