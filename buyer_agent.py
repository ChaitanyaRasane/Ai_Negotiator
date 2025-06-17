# buyer_agent.py
import random

class BuyerAgent:
    def __init__(self, budget_ratio=0.9, min_ratio=0.75, max_rounds=5):
        self.budget_ratio = budget_ratio
        self.min_ratio = min_ratio
        self.max_rounds = max_rounds
        self.reset()

    def reset(self, base_price=700000):
        self.base_price = base_price
        self.offer = int(self.base_price * self.min_ratio)
        self.round = 0
        self.accepted = False
        return self.offer

    def respond_to(self, seller_offer):
        self.round += 1
        max_price = int(self.base_price * self.budget_ratio)

        if seller_offer <= max_price:
            self.accepted = True
            return "accept", seller_offer

        elif self.round >= self.max_rounds:
            return "reject", None

        # Increase offer gradually
        increment = int((max_price - self.offer) / (self.max_rounds - self.round + 1))
        self.offer += increment
        return "counter", self.offer

    def message_for(self, intent, amount=None):
        if intent == "accept":
            return f"Okay! Deal at ₹{amount}."
        elif intent == "reject":
            return "That's too high for me. I'll pass."
        elif intent == "counter":
            return f"Can you do ₹{amount}?"
        return "I need to think about it."


# simulate_self_play.py
from buyer_agent import BuyerAgent
from negotiation_env import NegotiationEnv
from stable_baselines3 import DQN
import numpy as np

base_price = 700000
buyer = BuyerAgent()
seller = DQN.load("negotiation_dqn")

offer = buyer.reset(base_price)
print(f"Buyer: Can you sell at ₹{offer}?")

done = False
while not done:
    state = np.array([offer / base_price, buyer.round], dtype=np.float32)
    action = int(seller.predict(state, deterministic=True)[0])

    seller_responses = {
        0: ("accept", offer),
        1: ("reject", None),
        2: ("counter", int(0.95 * base_price)),
        3: ("counter", int(0.90 * base_price)),
        4: ("counter", int(0.85 * base_price))
    }

    intent, seller_offer = seller_responses[action]
    print(f"Seller: {intent.upper()} at ₹{seller_offer if seller_offer else 'N/A'}")

    if intent in ["accept", "reject"]:
        print("Buyer:", buyer.message_for(intent, seller_offer))
        break

    intent, offer = buyer.respond_to(seller_offer)
    print("Buyer:", buyer.message_for(intent, offer))
    if intent in ["accept", "reject"]:
        break
