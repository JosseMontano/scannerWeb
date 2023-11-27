import sys
import subprocess

import openai

openai.api_key = "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"


def parser(nmap_query, ip):
    print("-" * 50)
    print(ip)

    # Ejecuta el comando y captura la salida
    result = subprocess.run(nmap_query, shell=True, stdout=subprocess.PIPE, text=True)
    output = result.stdout

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "user",
                "content": "Hola!, estoy utilizando nmap para escanear servidores, dime una explicacion simplificada de los resultados "
                + output,
            }
        ],
    )

    print(response.choices[0].message.content)

    with open("readme3.txt", "w") as f:
        f.write(output)


def main():
    # nmap -sV --script nmap-vulners <IP> -p22,80,3306
    target = "200.80.43.108"
    mode = " --top-ports 100 --script vuln -sV"  #
    consulta = "nmap " + target + mode
    parser(consulta, target)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
