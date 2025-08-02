# 📊 Calculadora de Métricas de Classificação

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Um script Python para calcular as principais métricas de avaliação para modelos de classificação em Machine Learning. Este projeto foi desenvolvido como um exercício prático para entender os conceitos fundamentais por trás da avaliação de performance de modelos.

---

## 📖 Conceitos

O script utiliza os quatro resultados fundamentais de uma **Matriz de Confusão** para realizar os cálculos:
* **Verdadeiro Positivo (VP):** Previsão positiva que foi um acerto.
* **Verdadeiro Negativo (VN):** Previsão negativa que foi um acerto.
* **Falso Positivo (FP):** Previsão positiva que foi um erro (Erro Tipo I).
* **Falso Negativo (FN):** Previsão negativa que foi um erro (Erro Tipo II).

---

## ✨ Features

O script calcula e exibe as seguintes métricas:

* ✅ **Acurácia:** A porcentagem geral de acertos do modelo.
    * Fórmula: `(VP + VN) / (VP + VN + FP + FN)`
* 🎯 **Precisão (Precision):** Das previsões positivas, quantas estavam corretas.
    * Fórmula: `VP / (VP + FP)`
* 🔍 **Sensibilidade (Recall/Revocação):** Dos valores realmente positivos, quantos o modelo conseguiu identificar.
    * Fórmula: `VP / (VP + FN)`
* 🛡️ **Especificidade:** Dos valores realmente negativos, quantos o modelo conseguiu identificar.
    * Fórmula: `VN / (FP + VN)`
* ⚖️ **F-Score:** A média harmônica entre Precisão e Sensibilidade, buscando um equilíbrio entre as duas.
    * Fórmula: `2 * (Precisão * Sensibilidade) / (Precisão + Sensibilidade)`

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para executar o projeto em sua máquina local.

### Pré-requisitos

* [Python 3.x](https://www.python.org/downloads/) instalado.

### Passos

1.  **Clone o repositório:**
    ```sh
    git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
    ```
    *Substitua `SEU-USUARIO` e `SEU-REPOSITORIO` pelos seus dados.*

2.  **Navegue até a pasta do projeto:**
    ```sh
    cd SEU-REPOSITORIO
    ```

3.  **(Opcional, mas recomendado) Crie e ative um ambiente virtual:**
    ```sh
    # Criar o ambiente
    python -m venv .venv

    # Ativar no Windows
    .\.venv\Scripts\activate

    # Ativar no Linux/Mac
    source .venv/bin/activate
    ```

4.  **Execute o script:**
    ```sh
    python calculadora.py
    ```

5.  Os resultados serão exibidos diretamente no seu terminal. Para testar outros valores, basta editar as variáveis `VP`, `VN`, `FP` e `FN` no topo do arquivo `calculadora.py`.

---

## ✍️ Autor

* **[Bárbara Lampert]** - [LinkedIn](www.linkedin.com/in/barbara-lampert/) 

---


