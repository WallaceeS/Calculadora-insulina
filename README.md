Calculadora Personalizada de Insulina

Este projeto em Python calcula a quantidade de insulina necessária com base na alimentação e nos níveis de glicemia (destro), conforme recomendação médica personalizada.

⚠️ **Aviso importante:** Esta calculadora é de uso pessoal e baseada em orientação médica específica. Não deve ser utilizada por outras pessoas.

---

Como funciona?

O usuário escolhe o tipo de refeição (café da manhã, almoço, lanche ou janta)
Informa os alimentos consumidos e a quantidade
Digita o valor da glicemia (destro)
O sistema calcula a quantidade total de carboidratos ingeridos e aplica a fórmula de cálculo de insulina (carboidratos / fator individual + correção do destro)

---

 Fórmula utilizada

Exemplo de cálculo:
```
insulina_carboidrato = carboidrato_total / fator_individual
insulina_correção = (glicemia - 100) / 150

total_insulina = insulina_carboidrato + insulina_correção
```

O valor final passa por um ajuste de arredondamento baseado em orientações médicas específicas.

---

 Tecnologias utilizadas

- Python 3
- Módulo `decimal` para arredondamento preciso
- Lógica condicional e estruturas de repetição

---

 Alimentos utilizados

Os alimentos listados no código foram definidos com base nos hábitos alimentares da pessoa para quem o projeto foi desenvolvido.  
Os valores de carboidrato foram extraídos do:

> **Manual de Contagem de Carboidratos para Pessoas com Diabetes**  
> Sociedade Brasileira de Diabetes, 2016

---

Sobre

Projeto criado como prática pessoal.  
Este repositório faz parte da minha jornada de aprendizado em Python.
