candidatos = [
    ["candidato 1", "e5_t10_p8_s8"],
    ["candidato 2", "e10_t7_p7_s8"],
    ["candidato 3", "e8_t5_p4_s9"],
    ["candidato 4", "e2_t2_p2_s1"],
    ["candidato 5", "e10_t10_p8_s9"]  
]


def buscarCandidato(candidatos, entrevista, teorico, pratico, soft):
      candidatosAprovados = []
      for candidato, resultado in candidatos:
            notas = resultado.split('_')
            e =int(notas[0][1:])
            t =int(notas[1][1:])
            p =int(notas[2][1:])
            s =int(notas[3][1:])
            if e >= entrevista and t >= teorico and p >= pratico and s >= soft:
                 candidatosAprovados.append(candidato)
                 return candidatosAprovados
            
entrevista = int(input("Qual a nota minima para a entrevista [e]? "))
teorico = int(input("Qual a nota minima para o teste teórico [t]? "))
pratico = int(input("Qual a nota minima para o teste prático [p]? "))
soft = int(input("Qual a nota minima para a avaliação de soft skills [s]? "))

candidatosAprovados = buscarCandidato(candidatos, entrevista, teorico, pratico, soft) #lista

if candidatosAprovados:
    print("Candidatos aprovados:")
    for candidato in candidatosAprovados:
        print(candidato)
else:
    print("Não existem candidatos com os critérios compativeis.")

