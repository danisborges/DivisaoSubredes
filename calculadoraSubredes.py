def calcular_subrede(quantidade_maquinas):
    if quantidade_maquinas == 0:
        return "0.0.0.0/32", 1
    
    bits_necessarios = 1
    while (2 ** bits_necessarios) - 2 < quantidade_maquinas:
        bits_necessarios += 1
    
    prefixo = 32 - bits_necessarios
    total_enderecos = 2 ** bits_necessarios
    
    return prefixo, total_enderecos

def calcular_enderecos(base_ip, prefixo, total_enderecos):
    ip_base = [int(part) for part in base_ip.split('.')]
    ip_int = ip_base[0] << 24 | ip_base[1] << 16 | ip_base[2] << 8 | ip_base[3]
    
    enderecos = []
    for i in range(total_enderecos):
        ip = []
        for j in range(4):
            ip.append(str((ip_int >> (24 - (8 * j))) & 0xFF))
        enderecos.append('.'.join(ip))
        ip_int += 1
    
    return enderecos

def incrementar_ip(ip, incremento):
    ip_parts = ip.split('.')
    ip_int = (int(ip_parts[0]) << 24) | (int(ip_parts[1]) << 16) | (int(ip_parts[2]) << 8) | int(ip_parts[3])
    ip_int += incremento
    return '.'.join([str((ip_int >> (24 - (8 * i))) & 0xFF) for i in range(4)])

def main():
    print("Bem-vindo ao sistema de cálculo de sub-redes!")
    setores_info = []
    base_ip = input("Digite o endereço IP base (ex: 192.168.0.0): ").strip()
    ip_atual = base_ip

    while True:
        setor = input("Digite o nome do setor (ou 'sair' para terminar): ").strip().lower()
        if setor == 'sair':
            break
        
        maquinas = int(input(f"Quantas máquinas há no setor {setor}? ").strip())
        prefixo, total_enderecos = calcular_subrede(maquinas)
        enderecos = calcular_enderecos(ip_atual, prefixo, total_enderecos)
        
        setores_info.append((setor, maquinas, f"{ip_atual}/{prefixo}", enderecos[1], enderecos[2:2+maquinas]))
        ip_atual = incrementar_ip(enderecos[-1], 1)

    print("\nTabela de Sub-redes:")
    print(f"{'Setor':<15}{'Máquinas':<10}{'Sub-rede':<18}{'Gateway':<15}{'Máquina':<8}{'Endereço'}")
    for setor, maquinas, subrede, gateway, enderecos in setores_info:
        contagem_maquinas = 1
        for endereco in enderecos:
            print(f"{setor:<15}{maquinas:<10}{subrede:<18}{gateway:<15}{contagem_maquinas:<8}{endereco}")
            contagem_maquinas += 1

main()
