import subprocess
import openai
from config import tokenOpenAi


#random name
import random
import string

def get_random_string(length):
    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    # print random string
    return result_str



openai.api_key = tokenOpenAi


def parser(nmap_query, ip):
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

    nameFile = get_random_string(8);
    nameFile = nameFile + ".txt"
    with open(nameFile, "w") as f:
        f.write(output)

    return response.choices[0].message.content, nameFile


def nmap(ip):
    mode = " --top-ports 100 --script vuln -sV"  
    consulta = "nmap " + ip + mode
    msg, nameFile = parser(consulta, ip)
    return msg, nameFile