## To load model locally, install automl. Follow https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-environment#local
## Alternatively, you can run this on preconfigured compute. Follow https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-environment#compute-instance

# pip install sklearn inference-schema azureml-automl-runtime

import json
import pickle
import numpy as np
import pandas as pd
from azureml.core.workspace import Workspace
import azureml.train.automl, azureml.automl.runtime
from sklearn.externals import joblib
from azureml.core.model import Model

from inference_schema.schema_decorators import input_schema
from inference_schema.parameter_types.pandas_parameter_type import PandasParameterType

# input_sample = pd.DataFrame({'id': pd.Series(['6471903'], dtype='int64'), 'document': pd.Series(['진짜 별로다 헐 ㅡ'], dtype='object')})
from load_dataset import testdata as input_sample

def init():
    global model
    ## Uncomment below to retrieve the new model
    # global ws
    # ws = Workspace.from_config('./config.json')
    # model_path = Model.get_model_path(model_name = 'AutoML949b4194920', _workspace=ws)

    model_path = ".\\azureml-models\\AutoML949b4194920\\1\\model.pkl"
    model = joblib.load(model_path)

@input_schema('data', PandasParameterType(input_sample))
def run(data):
    try:
        ## get probability and class for positive sentiment
        THRESHOLD = 0.5
        result = model.predict_proba(data)
        result_df = pd.DataFrame(result)
        result_df.columns = ['neg', 'pos']
        result_df['predicted'] = result_df['pos'] > THRESHOLD
        result_df = result_df.astype({'predicted': int})
        result_df = result_df.astype({'predicted': str})
        result_df = pd.concat([data, result_df[['pos','predicted']]], axis=1)

        return json.dumps({"result": result_df.values.tolist()})
    except Exception as e:
        result = str(e)
        return json.dumps({"error": result})

if __name__=='__main__':
    init()
    result = run(input_sample)
    # print(input_sample)
    # print(result)

    # input_sample['predicted'] = list(json.loads(result).values())[0]
    # input_sample['prob'] = list(json.loads(result).values())[0]
    # print(input_sample)

    print(json.loads(result).values())
    with open('./output.json','w') as f:
        f.write(result)
    ## Remember to open the output with proper encoding (for example UTF-8)
