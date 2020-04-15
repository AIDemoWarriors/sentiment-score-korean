import json
import pickle
import numpy as np
import pandas as pd
from azureml.core.workspace import Workspace
import azureml.train.automl
from sklearn.externals import joblib
from azureml.core.model import Model

ws = Workspace.from_config('./config.json')

from azureml.core.webservice import Webservice, AciWebservice, AksWebservice
# service = AciWebservice(ws, "sentiment-scorer-korean")
# service = AksWebservice(ws, "sentiment-scorer-korean-aks")
service = AksWebservice(ws, "sentiment-scorer-korean-aks-prob")

service.get_logs()