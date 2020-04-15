# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import json
import pickle
import numpy as np
import pandas as pd
import azureml.train.automl
from sklearn.externals import joblib
from azureml.core.model import Model

from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType
from inference_schema.parameter_types.pandas_parameter_type import PandasParameterType


input_sample = pd.DataFrame({'id': pd.Series(['6471903'], dtype='int64'), 'document': pd.Series(['진짜 별로다 헐 ㅡ'], dtype='object')})
output_sample = np.array([0])


def init():
    global model
    # This name is model.id of model that we want to deploy deserialize the model file back
    # into a sklearn model
    model_path = Model.get_model_path(model_name = 'AutoML949b4194920')
    model = joblib.load(model_path)


@input_schema('data', PandasParameterType(input_sample))
@output_schema(NumpyParameterType(output_sample))
def run(data):
    try:
        # result = model.predict(data)
        # return json.dumps({"result": result.tolist()})

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
