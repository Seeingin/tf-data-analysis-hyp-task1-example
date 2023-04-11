import pandas as pd
import numpy as np


chat_id = 752592494 

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    x = x_success / x_cnt
    y = y_success / y_cnt
    if y - x > 0:
      res = False
    if y - x < 0:
      res = True
    return res # Ваш ответ, True или False
