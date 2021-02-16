import wfdb

# 1 - WFDB
record = wfdb.rdrecord('mitdb/203', sampto=3000)
annotation = wfdb.rdann('mitdb/203', sampto=3000)

# 2 - Pré-processamento
# 2.1 - Mediana

# 2.2 - Butterworth


# 3 - Detecção e Segmentação
# 3.1 - Segmentação fixa

# 4 - Extração de Características
# 4.1 - Intervalos, amplitude e parâmetros de Hjorth

# 5 - Separação
# treino e testes

# 6 - Classificação e separação
# SVN