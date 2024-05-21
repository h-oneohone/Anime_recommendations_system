# Package
## Python module
* `scipy`
* `numpy`
* `kaggle`
* `pandas`
* `os`
* `zipfile`
* `bigtree`
* `tqdm`
* `itertools`
* `collections`
* `functools`

# Usage
## Collaborative Filtering
```python
from agent import Agent
agent = Agent(dataset_path='dataset', weight_path='weight', download_dataset=True, download_weight=True)

# Get k recommended animes by id
print(agent.find_similar_animes(id=813, k=10))

# Get k recommended animes by name
print(agent.find_similar_animes(name='Dragon Ball Z', k=10))

# Get DataFrame result
print(agent.find_similar_animes(name='Dragon Ball Z', k=10, return_df=True))

# Get top_k * num_animes recommend_animes using watched_episodes attribute by user_id, return id result
print(agent.find_anime_for_user_using_episode(id=0, top_k=5, num_animes=4))

# Get top_k * num_animes recommend_animes using watched_episodes attribute by user_id, return name result
print(agent.find_anime_for_user_using_episode(id=0, top_k=5, num_animes=4, return_name=True))

# Get top_k * num_animes recommend_animes using watched_episodes attribute by user_id, return DataFrame result
print(agent.find_anime_for_user_using_episode(id=0, top_k=5, num_animes=4, return_df=True))

# Get top_k * num_animes recommend_animes using rating attribute by user_id, return id result
print(agent.find_anime_for_user_using_rating(id=0, top_k=5, num_animes=4))

# Get top_k * num_animes recommend_animes using rating attribute by user_id, return name result
print(agent.find_anime_for_user_using_rating(id=0, top_k=5, num_animes=4, return_name=True))

# Get top_k * num_animes recommend_animes using rating attribute by user_id, return DataFrame result
print(agent.find_anime_for_user_using_rating(id=0, top_k=5, num_animes=4))
```

## Apriori
```python
from agent import Agent
agent = Agent(dataset_path='dataset', weight_path='weight', download_dataset=True, download_weight=True)
agent.build_itemSetList(num_users=20000, num_animes=1000) # max num_users=313670, num_animes=17172
agent.build_apriori(minSup=0.12, minConf=0.5)
# Get all rules of FP-growth algorithm by name
for rule in agent.rules_apriori:
    print(agent.anime_df.loc[agent.anime_df['MAL_ID'].isin(list(rule[0]))]['Name'].tolist(), end=' ')
    print('--->', end=' ')
    print(agent.anime_df.loc[agent.anime_df['MAL_ID'].isin(list(rule[1]))]['Name'].tolist(), end=' ')
    print(rule[2])
```
Custom dataset
```python
from agent import Agent
agent = Agent(custom_dataset=True)
agent.itemSetList = [
        ['M', 'O', 'N', 'K', 'E', 'Y'],
        ['D', 'O', 'N', 'K', 'E', 'Y'],
        ['M', 'A', 'K', 'E'],
        ['M', 'U', 'C', 'K', 'Y'],
        ['C', 'O', 'O', 'K', 'I', 'E']
    ]
agent.build_apriori(minSup=0.6, minConf=0.8)
for i in agent.freqItemSet_apriori:
    print(i)
for i in agent.rules_apriori:
    print(i)
```


## Apriori Hash Tree
```python
from agent import Agent
agent = Agent(dataset_path='dataset', weight_path='weight', download_dataset=True, download_weight=True)
agent.build_itemSetList(num_users=20000, num_animes=1000) # max num_users=313670, num_animes=17172
agent.build_apriori_hash_tree(minSup=0.12, minConf=0.5)
# Get all rules of FP-growth algorithm by name
for rule in agent.rules_apriori_hash_tree:
    print(agent.anime_df.loc[agent.anime_df['MAL_ID'].isin(list(rule[0]))]['Name'].tolist(), end=' ')
    print('--->', end=' ')
    print(agent.anime_df.loc[agent.anime_df['MAL_ID'].isin(list(rule[1]))]['Name'].tolist(), end=' ')
    print(rule[2])
```
Custom dataset
```python
from agent import Agent
agent = Agent(custom_dataset=True)
agent.itemSetList = [
        ['M', 'O', 'N', 'K', 'E', 'Y'],
        ['D', 'O', 'N', 'K', 'E', 'Y'],
        ['M', 'A', 'K', 'E'],
        ['M', 'U', 'C', 'K', 'Y'],
        ['C', 'O', 'O', 'K', 'I', 'E']
    ]
agent.build_apriori_hash_tree(minSup=0.6, minConf=0.8)
for i in agent.freqItemSet_apriori_hash_tree:
    print(i)
for i in agent.rules_apriori_hash_tree:
    print(i)
```

## FP-growth

<p align=center>
    <img src="assets/fpgrowth.png" width="702" height="455">
</p>

```python
from agent import Agent
agent = Agent(dataset_path='dataset', weight_path='weight', download_dataset=True, download_weight=True)
agent.build_itemSetList(num_users=20000, num_animes=1000) # max num_users=313670, num_animes=17172
agent.build_fpgrowth(minSup=0.12, minConf=0.5)

# Get all rules of FP-growth algorithm by id
print(agent.rules_fpgrowth)

# Get all rules of FP-growth algorithm by name
for rule in agent.rules_fpgrowth:
    print(agent.anime_df.loc[agent.anime_df['MAL_ID'].isin(list(rule[0]))]['Name'].tolist(), end=' ')
    print('--->', end=' ')
    print(agent.anime_df.loc[agent.anime_df['MAL_ID'].isin(list(rule[1]))]['Name'].tolist(), end=' ')
    print(rule[2])

# Get recommended animes using fp-growth algorithm by user_id, return id result
print(agent.find_anime_for_user_using_fpgrowth(id=12))

# Get recommended animes using fp-growth algorithm by user_id, return name result
print(agent.find_anime_for_user_using_fpgrowth(id=12, return_name=True))

# Get recommended animes using fp-growth algorithm by user_id, return DataFrame result
print(agent.find_anime_for_user_using_fpgrowth(id=12, return_df=True))
```

# Demo
## Time implement
```python
import time
import matplotlib.pyplot as plt
from agent import Agent

# Khởi tạo agent
agent.build_itemSetList(num_users=2000, num_animes=100) # max num_users=313670, num_animes=17172

# Danh sách các giá trị minSup
minSup_values = [i/100 for i in range(5, 81, 5)]
memory_usage = []
execution_time_apriori = []
execution_time_apriori_hash_tree = []
execution_time_fpgrowth = []

for minSup in minSup_values:
    start_time = time.time()
    
    agent.build_apriori_hash_tree(minSup=minSup, minConf=0.8)
    
    end_time = time.time()
    
    execution_time_apriori_hash_tree.append(end_time - start_time)

for minSup in minSup_values:
    start_time = time.time()
    
    agent.build_apriori(minSup=minSup, minConf=0.8)
    
    end_time = time.time()
    
    execution_time_apriori.append(end_time - start_time)

for minSup in minSup_values:
    start_time = time.time()
    
    agent.build_fpgrowth(minSup=minSup, minConf=0.8)
    
    end_time = time.time()
    
    execution_time_fpgrowth.append(end_time - start_time)

# Vẽ biểu đồ bộ nhớ sử dụng
plt.figure(figsize=(12, 6))

plt.plot(minSup_values, execution_time_apriori, marker='o', linestyle='-', label='apriori')
plt.plot(minSup_values, execution_time_apriori_hash_tree, marker='o', linestyle='-', label='apriori_hash_tree')
plt.plot(minSup_values, execution_time_fpgrowth, marker='o', linestyle='-', label='fpgrowth')
plt.legend()
plt.xlabel('minSup')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs minSup')

plt.tight_layout()
plt.show()
```
## Time library
```python
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import time
import matplotlib.pyplot as plt
from agent import Agent

# Khởi tạo agent
agent.build_itemSetList(num_users=2000, num_animes=100) # max num_users=313670, num_animes=17172

# Dữ liệu mẫu: danh sách các giỏ hàng
dataset = agent.itemSetList


# Chuyển đổi dữ liệu thành dạng one-hot encoding
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)


minSup_values = [i/100 for i in range(5, 81, 5)]
execution_time_apriori = []
execution_time_apriori_hash_tree = []
execution_time_fpgrowth = []

for minSup in minSup_values:
    start_time = time.time()
    
    apriori(df, min_support=minSup, use_colnames=True)
    
    end_time = time.time()
    
    execution_time_apriori.append(end_time - start_time)

for minSup in minSup_values:
    start_time = time.time()
    
    fpgrowth(df, min_support=minSup, use_colnames=True)
    
    end_time = time.time()
    
    execution_time_fpgrowth.append(end_time - start_time)

plt.plot(minSup_values, execution_time_apriori, marker='o', linestyle='-', label='apriori')
plt.plot(minSup_values, execution_time_fpgrowth, marker='o', linestyle='-', label='fpgrowth')
plt.legend()
plt.xlabel('minSup')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs minSup')

plt.tight_layout()
plt.show()
```

# Algorithm Tutorial
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/14RzLFOnpWyvpsUsygTfF5HB29xyopL-x?usp=sharing)

# Hashtree
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-LTgmARJj-gpRQFYD-k0-ofFnE0e0uL5?usp=sharing#scrollTo=Yn0ZSK7sgbUf)

# Dataset
[![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/hernan4444/anime-recommendation-database-2020)

## Cropped dataset
[![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=googledrive&logoColor=white)](https://drive.google.com/drive/folders/1CYjnad4Qmc5wx9BpXKcbHMbHE18iQNOa?usp=sharing)

[![Data+name_anime](https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=googledrive&logoColor=white)](https://drive.google.com/drive/folders/1KfSMMcVeuBAycFdKLDF-XTvP7s96YP8t?usp=sharing)
