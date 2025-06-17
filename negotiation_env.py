# import gym
# import numpy as np

# class NegotiationEnv(gym.Env):
#     def __init__(self, predicted_price=700000):
#         super(NegotiationEnv, self).__init__()
#         self.p = predicted_price
#         self.action_space = gym.spaces.Discrete(5)
#         self.observation_space = gym.spaces.Box(
#             low=np.array([0.0, 0]), high=np.array([2.0, 5]), dtype=np.float32
#         )
#         self.reset()

#     def reset(self):
#         self.round = 0
#         self.offer = np.random.uniform(0.7, 1.0) * self.p
#         return self._get_state()

#     def _get_state(self):
#         return np.array([self.offer / self.p, self.round], dtype=np.float32)

#     def step(self, action):
#         done = False
#         reward = 0

#         if action == 0:
#             reward = self.offer - 0.75 * self.p
#             done = True
#         elif action == 1:
#             reward = -10
#             done = True
#         else:
#             self.offer = self.p * {2: 0.95, 3: 0.9, 4: 0.85}[action]
#             reward = -0.5

#         self.round += 1
#         if self.round > 4:
#             done = True
#             reward -= 5

#         return self._get_state(), reward, done, {}
import gym
import numpy as np

class NegotiationEnv(gym.Env):
    def __init__(self, predicted_price=700000):
        super(NegotiationEnv, self).__init__()
        self.p = predicted_price
        self.action_space = gym.spaces.Discrete(5)
        self.observation_space = gym.spaces.Box(
            low=np.array([0.0, 0]), high=np.array([2.0, 5]), dtype=np.float32
        )
        self.reset()

    def reset(self):
        self.round = 0
        self.offer = np.random.uniform(0.7, 1.0) * self.p
        return self._get_state()

    def _get_state(self):
        return np.array([self.offer / self.p, self.round], dtype=np.float32)

    def step(self, action):
        done = False
        reward = 0

        if action == 0:  # Accept
            if self.offer >= 0.95 * self.p:
                reward = 5
            elif self.offer >= 0.85 * self.p:
                reward = 1
            else:
                reward = -5
            done = True

        elif action == 1:  # Reject
            reward = -10
            done = True

        else:  # Counteroffer
            self.offer = self.p * {2: 0.95, 3: 0.9, 4: 0.85}[action]
            reward = -0.5

        self.round += 1
        if self.round > 4:
            done = True
            reward -= 5

        return self._get_state(), reward, done, {}
