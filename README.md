# Package
## Python module
* `scipy`
* `numpy`
* `gdown==4.7.3`
* `pandas`
* `os`
* `zipfile`

# Usage
```python
from agent import Agent
agent = Agent(dataset_path='dataset', weight_path='weight', download_dataset=True, download_weight=True)

# Get k recommended animes by id
print(agent.act(id=813, k=10))

# Get k recommended animes by name
print(agent.act(name='Dragon Ball Z', k=10))

# Get DataFrame result
print(agent.act(name='Dragon Ball Z', k=10, return_df=True))
```

# Algorithm Tutorial
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/14RzLFOnpWyvpsUsygTfF5HB29xyopL-x?usp=sharing)
