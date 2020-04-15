import pandas as pd

testdata = pd.read_csv("./testdata.csv", names=["id","document"])
# print(testdata)
# print(testdata.shape)
# print(type(testdata))

# input_sample = pd.DataFrame({'id': pd.Series(['6471903'], dtype='int64'), 'document': pd.Series(['진짜 별로다 헐 ㅡ'], dtype='object')})
# print(input_sample)
# print(input_sample.shape)
# print(type(input_sample))
