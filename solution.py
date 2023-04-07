import pandas as pd
import numpy as np

from scipy.stats import gamma


chat_id = 460109099 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean() - 1/2
    scale = 2 / (83**2)
    left_q = gamma.ppf(alpha/2, len(x)) / n
    right_q = gamma.ppf(1 - alpha/2, len(x)) / n
    
    return scale * (loc + left_q), \
           scale * (loc + right_q)
