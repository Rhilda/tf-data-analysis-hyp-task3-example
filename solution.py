import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest

chat_id = 773978697 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.09
    pvalue = ztest(x, value=300, alternative='smaller')[1]
    return pvalue < alpha 
