# Leitura do arquivo de alinhamento gerado pelo clustalw2
from Bio import AlignIO

pos_1 = 0
pos_2 = 0
pos_3 = 0
# Ler o alinhamento
align = AlignIO.read("atp6_felinae.aln", "clustal")

# Loop através do comprimento do alinhamento
for i in range(align.get_alignment_length()):
    coluna = align[:, i]
    caracteres_unicos = set(coluna)
    if len(caracteres_unicos) != 1:
        pos = (i + 1) / 3
        pos_str = f'{pos:.2f}'
        if pos_str.endswith('.33'):
            pos_1 += 1
        elif pos_str.endswith('.00'):
            pos_3 += 1
        else:
            if pos_str.endswith('.67'):
                pos_2 += 1


print(f'1a posição: {pos_1}')
print(f'2a posição: {pos_2}')
print(f'3a posição: {pos_3}')


for i in range(align.get_alignment_length()):
    coluna = align[:, i]
    caracteres_unicos = set(coluna)
    if len(caracteres_unicos) != 1:
        pos = (i + 1) / 3
        pos_str = f'{pos:.2f}'
        if pos_str.endswith('.33'):
            posicao = 1
            codon_1 = round(float(pos_str)) + 0.5
            print(f'No alinhamento {i+1}, o codon {codon_1 + 0.5} está na {posicao} posição')
        elif pos_str.endswith('.67'):
            posicao = 2
            codon_2 = round(float(pos_str))
            print(f'No alinhamento {i+1}, o codon {codon_2} está na {posicao} posição')
        else:
            if pos_str.endswith('.00'):
                posicao = 3
                codon_3 = pos_str
                print(f'No alinhamento {i+1}, o codon {codon_3} está na {posicao} posição')