# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 08:35:48 2020

@author: win 8.1
"""
import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
