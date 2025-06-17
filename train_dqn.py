# from stable_baselines3 import DQN
# from negotiation_env import NegotiationEnv

# env = NegotiationEnv(predicted_price=700000)

# model = DQN(
#     "MlpPolicy", env,
#     learning_rate=1e-3,
#     buffer_size=10000,
#     exploration_fraction=0.2,
#     verbose=1,
#     tensorboard_log="./logs"
# )

# model.learn(total_timesteps=25000)
# model.save("negotiation_dqn")
# import pickle

# # Assuming model is your trained classifier
# with open("intent_model.pkl", "wb") as f:
#     pickle.dump(model, f)

from stable_baselines3 import DQN
from negotiation_env import NegotiationEnv

env = NegotiationEnv(predicted_price=700000)

model = DQN(
    "MlpPolicy", env,
    learning_rate=1e-3,
    buffer_size=50000,
    exploration_fraction=0.3,
    exploration_final_eps=0.05,
    verbose=1,
    tensorboard_log="./logs"
)

model.learn(total_timesteps=100000)
model.save("negotiation_dqn")

