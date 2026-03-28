
from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class DataCleaningEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.state_data = {
            "missing_values": random.randint(5, 10),
            "duplicates": random.randint(3, 8),
            "steps": 0
        }
        return self.state()

    def step(self, action):
        reward = 0
        done = False

        if action.action_type == "remove_missing":
            if self.state_data["missing_values"] > 0:
                self.state_data["missing_values"] -= 1
                reward = 1
            else:
                reward = -1

        elif action.action_type == "remove_duplicates":
            if self.state_data["duplicates"] > 0:
                self.state_data["duplicates"] -= 1
                reward = 1
            else:
                reward = -1

        elif action.action_type == "finish":
            if self.state_data["missing_values"] == 0 and self.state_data["duplicates"] == 0:
                reward = 10
                done = True
            else:
                reward = -5

        else:
            reward = -2

        self.state_data["steps"] += 1

        return self.state(), reward, done

    def state(self):
        return self.state_data


class Action(BaseModel):
    action_type: str


env = DataCleaningEnv()


@app.get("/")
def home():
    return {"message": "Server working 🚀"}


@app.get("/reset")
def reset():
    return env.reset()


@app.post("/step")
def step(action: Action):
    state, reward, done = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }


@app.get("/state")
def state():
    return env.state()

