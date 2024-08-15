from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Any
from agent import Agent

app = FastAPI()


agent_colab = Agent(dataset_path='dataset', weight_path='weight', download_dataset=True, download_weight=True)


class DataModel(BaseModel):
    data: List[List[str]]
    minSup: float
    minConf: float

@app.post("/Apriori")
def run_apriori(data: DataModel):
    try:
        print(data.data)
        agent = Agent(custom_dataset=True)
        agent.itemSetList = data.data
        agent.build_apriori(minSup=data.minSup, minConf=data.minConf)

        # Convert tuple keys to strings with elements separated by a comma
        freq_itemsets = [",".join(k) for k, v in agent.freqItemSet_apriori]
        rules = [{
            "lhs": list(rule[0]),
            "rhs": list(rule[1]),
            "confidence": rule[2],
        } for rule in agent.rules_apriori]

        print("freq_itemsets:", freq_itemsets)
        print("rules:", rules)
        print("type(freq_itemsets):", type(freq_itemsets))
        print("type(rules):", type(rules))

        return {"freq_itemsets": freq_itemsets, "rules": rules}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/AprioriHashTree")
def run_apriori_hash_tree(data: DataModel):
    try:
        print(data.data)
        agent = Agent(custom_dataset=True)
        agent.itemSetList = data.data
        agent.build_apriori_hash_tree(minSup=data.minSup, minConf=data.minConf)

        # Convert tuple keys to strings with elements separated by a comma
        freq_itemsets = [",".join(k) for k in agent.freqItemSet_apriori_hash_tree]
        rules = [{
            "lhs": list(rule[0]),
            "rhs": list(rule[1]),
            "confidence": rule[2],
        } for rule in agent.rules_apriori_hash_tree]

        print("freq_itemsets:", freq_itemsets)
        print("rules:", rules)
        print("type(freq_itemsets):", type(freq_itemsets))
        print("type(rules):", type(rules))

        return {"freq_itemsets": freq_itemsets, "rules": rules}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/FPGrowth")
def run_fpgrowth(data: DataModel):
    try:
        print(data.data)
        agent = Agent(custom_dataset=True)
        agent.itemSetList = data.data
        agent.build_fpgrowth(visualize=True, minSup=data.minSup, minConf=data.minConf)

        # Convert tuple keys to strings with elements separated by a comma
        freq_itemsets = [",".join(k) for k in agent.freqItemSet_fpgrowth]
        rules = [{
            "lhs": list(rule[0]),
            "rhs": list(rule[1]),
            "confidence": rule[2],
        } for rule in agent.rules_fpgrowth]

        print("freq_itemsets:", freq_itemsets)
        print("rules:", rules)
        print("type(freq_itemsets):", type(freq_itemsets))
        print("type(rules):", type(rules))

        return {"freq_itemsets": freq_itemsets, "rules": rules}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
class DataModelColab(BaseModel):
    id: int
    top_k: int
    num_animes: int


@app.post("/colab_filtering")
def run_colab_filtering(data: DataModelColab):
    try:
        print(data.id, data.top_k, data.num_animes)
        result = agent_colab.find_anime_for_user_using_episode(id=data.id,top_k=data.top_k, num_animes=data.num_animes, return_name=True)
        print("result:", result)
        # Convert tuple keys to strings with elements separated by a comma
        animes = [k for k in result]
        print("animes:", animes)
        return {"animes": animes}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))