import pandas as pd
import numpy as np
from random import randint

def set_snt(snt: str):
    df = pd.DataFrame({
        "sentence": [snt]
    })
    df.to_csv("data/snt_unset.csv", mode='a', header=False, index=False)

def set_snts(snts: list):
    df = pd.DataFrame({
        "sentence": snts
    })
    df.to_csv("data/snt_unset.csv", mode='a', header=False, index=False)

def get_snt():
    snts = pd.read_csv("data/snt_unset.csv")
    return snts["sentence"][randint(0, len(snts["sentence"]) - 1)]
