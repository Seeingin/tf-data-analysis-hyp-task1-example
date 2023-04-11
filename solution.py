import pandas as pd
import numpy as np


chat_id = 752592494

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:

    import scipy.stats as stats

    p_hat = (x_success + y_success) / (x_cnt + y_cnt)
    z = (y_success/y_cnt - x_success/x_cnt) / (p_hat * (1 - p_hat) * (1/x_cnt + 1/y_cnt)) ** 0.5
    p_value = 1 - stats.norm.cdf(z)

    if p_value > 0.05:
      res = False
    else:
      res = True
    return res
