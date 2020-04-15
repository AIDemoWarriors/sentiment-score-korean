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
service = AciWebservice(ws, "sentiment-scorer-korean")

# input_sample = pd.DataFrame({'id': pd.Series(['6471903'], dtype='int64'), 'document': pd.Series(['진짜 별로다 헐 ㅡ'], dtype='object')})
from load_dataset import testdata as input_sample

import json
test = json.dumps({"data": input_sample.values.tolist()})
result = service.run(input_data=bytes(test, encoding="utf8"))

print(input_sample)
print(result)
