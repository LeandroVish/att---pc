# 11. Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, 
# contendo um relatório dos endereços IP válidos e inválidos. O arquivo de entrada possui o seguinte formato:
"""
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256
"""

# O arquivo de saída possui o seguinte formato:
# [Endereços válidos:]
"""
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4
"""
# [Endereços inválidos:]
"""
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
"""

def validar_ip(ip):
    partes = ip.split(".")
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte.isdigit() or not 0 <= int(parte) <= 255:
            return False
    return True

arquivo_entrada = open("ips.txt", "r")
arquivo_saida = open("relatorio_ips.txt", "w")
ips_validos = []
ips_invalidos = []
for linha in arquivo_entrada.readlines():
    ip = linha.strip()
    if validar_ip(ip):
        ips_validos.append(ip)
    else:
        ips_invalidos.append(ip)
arquivo_saida.write("[Endereços válidos:]\n")
for ip in ips_validos:
    arquivo_saida.write(ip + "\n")
arquivo_saida.write("\n[Endereços inválidos:]\n")
for ip in ips_invalidos:
    arquivo_saida.write(ip + "\n")
arquivo_entrada.close()
arquivo_saida.close()
print("Relatório de IPs gerado em 'relatorio_ips.txt' com sucesso.")