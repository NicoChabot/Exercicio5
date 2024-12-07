import numpy as np
from scipy.stats import ttest_ind

# Dados dos grupos
copilot = np.array([100, 59, 98, 103, 130, 70, 109, 88, 76, 123])
sem_copilot = np.array([205, 188, 130, 98, 100, 174, 207, 198, 172, 209])

# Cálculo das medidas de tendência central
medias = {
    "Copilot": {"Média": np.mean(copilot), "Mediana": np.median(copilot)},
    "Sem Copilot": {"Média": np.mean(sem_copilot), "Mediana": np.median(sem_copilot)}
}

medias

# Teste t para amostras independentes (one-tailed)
t_stat, p_value = ttest_ind(copilot, sem_copilot, alternative='less')

{"t_statistic": t_stat, "p_value": p_value}

