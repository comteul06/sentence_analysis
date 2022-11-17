import pandas as pd
import numpy as np
from random import randint

UNSETPATH = "data/snt_unset.csv"
SETPATH = "data/snt_set.csv"

class SntData:
    __cnt = 3
    __snt = ""
    __sbj = ""
    __vrb = ""
    __obj = ""
    __cmpl = ""
    __index = -1

    def __init__(self, snt, index, sbj, vrb, obj, cmpl):
        self.__snt, self.__index, self.__sbj, self.__vrb, self.__obj, self.__cmpl = snt, index, sbj, vrb, obj, cmpl

    @property
    def sentence(self):
        return self.__snt
        
    @property
    def subject(self):
        return self.__sbj
        
    @property
    def verb(self):
        return self.__vrb
        
    @property
    def object(self):
        return self.__obj
        
    @property
    def complement(self):
        return self.__cmpl
    
    def __str__(self):
        return f"{self.__snt}\n{self.__sbj}, {self.__vrb}, {self.__obj}, {self.__cmpl}"

    def save(self, save_data):
        _save_data = save_data if save_data != "-1" else ""
        if self.__cnt == 3:
            self.__sbj = save_data
        elif self.__cnt == 2:
            self.__vrb = save_data
        elif self.__cnt == 1:
            self.__obj = save_data
        else:
            self.__cmpl = save_data
        self.__cnt -= 1
        return self.__cnt + 1

#region Sets

def add_snt(snt: str):
    df = pd.DataFrame({
        "sentence": [snt]
    })
    df.to_csv(UNSETPATH, mode='a', header=False, index=False)

def add_snts(snts: list):
    df = pd.DataFrame({
        "sentence": snts
    })
    df.to_csv(UNSETPATH, mode='a', header=False, index=False)

def add_snt_data(data: SntData):
    df = pd.DataFrame({
        "sentence": [data.sentence],
        "subject": [data.subject],
        "verb": [data.verb],
        "object": [data.object],
        "complement": [data.complement]
    })
    df.to_csv(SETPATH, mode='a', header=False, index=False)

#endregion

#region Gets

def get_snt_empty():
    data = pd.read_csv(UNSETPATH)
    index = randint(0, len(data["sentence"]) - 1)
    return SntData(data["sentence"][index], index, "", "", "", "")

def get_snt_data():
    data = pd.read_csv(UNSETPATH)
    index = randint(0, len(data["sentence"] - 1))
    return SntData(data["sentence"], data["subject"], data["verb"], data["object"], data["complement"])

#endregion

#region Removes

def remove_unset_at(index: int):
    data = pd.read_csv(UNSETPATH)
    data.drop(index)

def remove_set_at(index: int):
    data = pd.read_csv(SETPATH)
    data.drop(index)

#endregion
