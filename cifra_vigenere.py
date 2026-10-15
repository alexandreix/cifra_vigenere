def decodificar_vigenere(texto_cifrado, chave):
    texto_decodificado = []
    chave = chave.lower()
    indice_chave = 0
    
    for caractere in texto_cifrado:
        # Verifica se o caractere é uma letra minúscula
        if 'a' <= caractere <= 'z':
            # Transforma as letras em números (0 a 25)
            posicao_cifrada = ord(caractere) - ord('a')
            posicao_chave = ord(chave[indice_chave % len(chave)]) - ord('a')
            
            # Aplica a fórmula matemática de decodificação: (C - K) % 26
            posicao_real = (posicao_cifrada - posicao_chave) % 26
            
            # Transforma o número de volta em letra e adiciona ao resultado
            texto_decodificado.append(chr(posicao_real + ord('a')))
            
            # Avança para a próxima letra da chave
            indice_chave += 1
            
        # Mantém letras maiúsculas funcionando sob a mesma lógica
        elif 'A' <= caractere <= 'Z':
            posicao_cifrada = ord(caractere) - ord('A')
            posicao_chave = ord(chave[indice_chave % len(chave)]) - ord('a')
            posicao_real = (posicao_cifrada - posicao_chave) % 26
            texto_decodificado.append(chr(posicao_real + ord('A')))
            indice_chave += 1
            
        else:
            # Se for símbolo (/, :, .), mantém igual sem avançar a chave
            texto_decodificado.append(caractere)
            
    return "".join(texto_decodificado)

# Dados do desafio do outdoor
link_criptografado = "zhvhg://esfgwfu.umdwf/chdnq"
chave_secreta = "soc"

# Executa a função
link_final = decodificar_vigenere(link_criptografado, chave_secreta)

print(f"Texto original: {link_criptografado}")
print(f"Chave utilizada: {chave_secreta}")
print(f"Link descoberto: {link_final}")
