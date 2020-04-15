# sentiment-score-korean

Use Naver Sentiment Movie Corpus (https://github.com/e9t/nsmc) and Azure ML to create a sentiment classifier for Korean.

---

## Overview

### What's inside

### How it works

---

## Technologies Used

### Azure Machine Learning studio

### Python SDK for Azure Machine Learning

---

## Installation and Usage

```bash
git clone https://github.com/AIDemoWarriors/sentiment-score-korean
cp config.json.dist config.json
vi config.json
```

If you want to download already trained ML model, download [this file](https://aidemowarriors.blob.core.windows.net/sentiment-scorer-korean/azureml-models/AutoML949b4194920/1/model.pkl) and save it under `.\\azureml-models\\AutoML949b4194920\\1\\`. Check out [how model management works in Azure ML](https://docs.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment#register-and-track-ml-models)

Else if you want to use your own ML model (trained with Automated ML from Azure ML), modify the `config.json` to connect to the Azure Machine Learning Workspace, where your model can be created and registered.

```bash
cp config.json.dist config.json
vi config.json
```

Enjoy!

---

## Notes and Features

---

## Ideas for Future Development

---

## License

[LICENSE](LICENSE)

---

## References
