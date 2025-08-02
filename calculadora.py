# Valores da nossa Matriz de Confusão (escolhidos arbitrariamente)

VP = 85 # Verdadeiros Positivos
VN = 90 # Verdadeiros Negativos
FP = 10 # Falsos Positivos
FN = 15 # Falsos Negativos

print ("Valores da Matriz de Confusão:")
print (f"VP: {VP}, VN: {VN}, FP: {FP}, FN: {FN}\n")

def calcular_sensibilidade(vp, fn):
    """
  Calcula a Sensibilidade (também conhecida como Recall ou Taxa de Verdadeiros Positivos).
  Mede a proporção de positivos reais que foram corretamente identificados.
  """
    try:
        sensibilidade = vp / (vp + fn)
        return sensibilidade
    except ZeroDivisionError:
        return 0.0
    
def calcular_especificidade(vn, fp):
  """
  Calcula a Especificidade (ou Taxa de Verdadeiros Negativos).
  Mede a proporção de negativos reais que foram corretamente identificados.
  """
  try:
    especificidade = vn / (fp + vn)
    return especificidade
  except ZeroDivisionError:
    return 0.0



def calcular_acuracia(vp, vn, fp, fn):
    """
  Calcula a Acurácia geral do modelo.
  Mede a proporção de previsões corretas (tanto positivas quanto negativas).
    """
    total_amostras = vp + vn + fp + fn
    try:
        acuracia = (vp + vn) / total_amostras
        return acuracia
    except ZeroDivisionError:
        return 0.0
    
def calcular_precisao(vp, fp):
    """
        Calcula a Precisão (ou Valor Preditivo Positivo).
        Mede a proporção de predições positivas que estavam corretas.
    """
    try:
        precisao = vp / (vp + fp)
        return precisao
    except ZeroDivisionError:
        return 0.0
    
def calcular_f_score(precisao, sensibilidade):
    """
  Calcula o F-Score, que é a média harmônica da precisão e da sensibilidade.
  Busca um equilíbrio entre as duas métricas.
  """
    try:
        f_score = 2 * (precisao * sensibilidade) / (precisao + sensibilidade)
        return f_score
    except ZeroDivisionError:
        return 0.0
    


# --- Bloco Principal de Execução ---

if __name__ == "__main__":
    # Calcular cada métrica usando as funções
    sensibilidade = calcular_sensibilidade(VP, FN)
    especificidade = calcular_especificidade(VN, FP)
    acuracia = calcular_acuracia(VP, VN, FP, FN)
    precisao = calcular_precisao(VP, FP)
    
    # O F-Score depende da precisão e da sensibilidade
    f_score = calcular_f_score(precisao, sensibilidade)

    # Exibir os resultados
    print("--- Métricas de Avaliação ---")
    print(f"Acurácia: {acuracia:.2%}")
    print(f"Sensibilidade (Recall): {sensibilidade:.2%}")
    print(f"Especificidade: {especificidade:.2%}")
    print(f"Precisão: {precisao:.2%}")
    print(f"F-Score: {f_score:.2%}")