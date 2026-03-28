import pandas as pd

class CleanEnv:
    def __init__(self):
        self.data = None
        self.steps = 0

    def reset(self):
        self.data = pd.read_csv("data.csv")
        self.steps = 0
        return self.state()

    def state(self):
        return {
            "missing_values": self.data.isnull().sum().to_dict(),
            "duplicates": int(self.data.duplicated().sum())
        }

    def step(self, action):
        reward = 0

        if action == "fill_missing":
            before = self.data.isnull().sum().sum()
            self.data = self.data.fillna(self.data.mean(numeric_only=True))
            after = self.data.isnull().sum().sum()
            reward += (before - after) * 0.1

        elif action == "remove_duplicates":
            before = self.data.duplicated().sum()
            self.data = self.data.drop_duplicates()
            after = self.data.duplicated().sum()
            reward += (before - after) * 0.2

        elif action == "drop_missing":
            before = len(self.data)
            self.data = self.data.dropna()
            after = len(self.data)
            reward += (before - after) * 0.1

        else:
            reward -= 0.2  # wrong action

        self.steps += 1
        done = self.steps >= 5

        return self.state(), reward, done, {}
        