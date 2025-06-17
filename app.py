# from flask import Flask, request, jsonify, session, send_from_directory
# from flask_cors import CORS
# import numpy as np
# import re
# import pickle
# from negotiation_env import NegotiationEnv
# from stable_baselines3 import DQN

# app = Flask(__name__)
# CORS(app)
# app.secret_key = 'chatbot123'

# agent = DQN.load("negotiation_dqn")
# with open("intent_model.pkl", "rb") as f:
#     intent_model = pickle.load(f)
# with open("vectorizer.pkl", "rb") as f:
#     vectorizer = pickle.load(f)

# def classify_intent(msg):
#     X = vectorizer.transform([msg])
#     return intent_model.predict(X)[0]

# def extract_price(msg):
#     match = re.findall(r"\d{2,3}[kK]|\d{5,7}", msg)
#     if match:
#         return int(match[0].lower().replace('k', '000'))
#     return None

# def generate_negotiation_reply(offer, round_no, base_price):
#     state = np.array([offer / base_price, round_no], dtype=np.float32)
#     action = int(agent.predict(state, deterministic=True)[0])
#     responses = {
#         0: f"Sounds good! Deal at ₹{int(offer)}.",
#         1: "Sorry, that won't work for me.",
#         2: f"I can do ₹{int(0.95 * base_price)}—does that work?",
#         3: f"What about ₹{int(0.90 * base_price)}?",
#         4: f"My lowest is ₹{int(0.85 * base_price)}."
#     }
#     return responses[action], action

# @app.route("/chat", methods=["POST"])
# def chat():
#     data = request.get_json()
#     msg = data.get("message")
#     base_price = data.get("predicted_price", 700000)
#     offer = extract_price(msg) or 0.7 * base_price
#     round_no = session.get("round_no", 0)

#     intent = classify_intent(msg)
#     response, action = generate_negotiation_reply(offer, round_no, base_price)

#     session["round_no"] = round_no + 1
#     return jsonify({"intent": intent, "response": response})

# @app.route("/")
# def index():
#     return send_from_directory('.', 'chat.html')

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, request, jsonify, session, send_from_directory
# from flask_cors import CORS
# import numpy as np
# import re
# import pickle
# from negotiation_env import NegotiationEnv
# from stable_baselines3 import DQN

# app = Flask(__name__)
# CORS(app)
# app.secret_key = 'chatbot123'

# agent = DQN.load("negotiation_dqn")
# with open("intent_model.pkl", "rb") as f:
#     intent_model = pickle.load(f)
# with open("vectorizer.pkl", "rb") as f:
#     vectorizer = pickle.load(f)

# def classify_intent(msg):
#     X = vectorizer.transform([msg])
#     return intent_model.predict(X)[0]

# def extract_price(msg):
#     match = re.findall(r"\d{2,3}[kK]|\d{5,7}", msg)
#     if match:
#         return int(match[0].lower().replace('k', '000'))
#     return None

# def generate_negotiation_reply(offer, round_no, base_price):
#     state = np.array([offer / base_price, round_no], dtype=np.float32)
#     action = int(agent.predict(state, deterministic=True)[0])
#     responses = {
#         0: f"Sounds good! Deal at ₹{int(offer)}.",
#         1: "Sorry, that won't work for me.",
#         2: f"I can do ₹{int(0.95 * base_price)}—does that work?",
#         3: f"What about ₹{int(0.90 * base_price)}?",
#         4: f"My lowest is ₹{int(0.85 * base_price)}."
#     }
#     return responses[action], action

# @app.route("/chat", methods=["POST"])
# def chat():
#     data = request.get_json()
#     msg = data.get("message")
#     base_price = data.get("predicted_price", 700000)
#     offer = extract_price(msg) or 0.7 * base_price
#     round_no = session.get("round_no", 0)

#     intent = classify_intent(msg)
#     response, action = generate_negotiation_reply(offer, round_no, base_price)

#     session["round_no"] = round_no + 1
#     return jsonify({"intent": intent, "response": response})

# @app.route("/")
# def index():
#     return send_from_directory('.', 'chat.html')

# if __name__ == "__main__":
#     app.run(debug=True)

## ai-engine/app.py






# from flask import Flask, request, jsonify, session, send_from_directory
# from flask_cors import CORS
# import numpy as np
# import re
# import pickle
# import random
# from negotiation_env import NegotiationEnv
# from stable_baselines3 import DQN

# app = Flask(__name__)
# CORS(app)
# app.secret_key = 'chatbot123'

# agent = DQN.load("negotiation_dqn")
# with open("intent_model.pkl", "rb") as f:
#     intent_model = pickle.load(f)
# with open("vectorizer.pkl", "rb") as f:
#     vectorizer = pickle.load(f)

# def classify_intent(msg):
#     X = vectorizer.transform([msg])
#     return intent_model.predict(X)[0]

# def extract_price(msg):
#     match = re.findall(r"\d{2,3}[kK]|\d{5,7}", msg)
#     if match:
#         return int(match[0].lower().replace('k', '000'))
#     return None

# def generate_negotiation_reply(offer, round_no, base_price, tone):
#     state = np.array([offer / base_price, round_no], dtype=np.float32)
#     action = int(agent.predict(state, deterministic=True)[0])

#     counter_templates = {
#         "friendly": [
#             "Okay, I understand! 😊 Let's try ₹{price}.",
#             "Sounds fair! Can we agree on ₹{price}?"
#         ],
#         "strict": [
#             "₹{price} is the minimum I can do.",
#             "I can't go lower than ₹{price}."
#         ],
#         "playful": [
#             "Let’s split the difference: ₹{price} 😎",
#             "What if I say ₹{price}? Deal? 😜"
#         ]
#     }

#     response_variants = {
#         0: f"Deal at ₹{int(offer)}! 🎉",
#         1: "Sorry, I can’t go that low.",
#         2: random.choice(counter_templates[tone]).format(price=int(0.95 * base_price)),
#         3: random.choice(counter_templates[tone]).format(price=int(0.90 * base_price)),
#         4: random.choice(counter_templates[tone]).format(price=int(0.85 * base_price)),
#     }
#     return response_variants[action], action

# @app.route("/chat", methods=["POST"])
# def chat():
#     data = request.get_json()
#     msg = data.get("message")
#     base_price = data.get("predicted_price", 700000)
#     offer = extract_price(msg) or 0.7 * base_price
#     round_no = session.get("round_no", 0)

#     # Setup conversation memory
#     if "round_no" not in session:
#         session["round_no"] = 0
#         session["last_offer"] = 0
#         session["concession_count"] = 0
#         session["tone"] = "friendly"  # could also be 'strict', 'playful'

#     tone = session.get("tone", "friendly")

#     intent = classify_intent(msg)

#     if intent == "greet":
#         response = "Hi! I'm your virtual assistant. Let’s talk about the car price."
#     elif intent == "accept":
#         response = "Great! Deal confirmed."
#     elif intent == "reject":
#         response = "No worries. Let me know if you change your mind."
#     elif intent == "counter":
#         response = "Okay, I’m open to negotiate. What’s your next offer?"
#     elif intent == "offer":
#         response, action = generate_negotiation_reply(offer, round_no, base_price, tone)
#         session["last_offer"] = offer
#         if action in [2, 3, 4]:
#             session["concession_count"] += 1
#     else:
#         response = "Sorry, I didn't understand that. Can you rephrase your offer?"

#     session["round_no"] = round_no + 1
#     return jsonify({"intent": intent, "response": response})

# @app.route("/")
# def index():
#     return send_from_directory('.', 'chat.html')

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, request, jsonify, session, send_from_directory
# from flask_cors import CORS
# import numpy as np
# import re
# import pickle
# import random
# from negotiation_env import NegotiationEnv
# from stable_baselines3 import DQN
# from state_manager import ConversationState


# app = Flask(__name__)
# CORS(app)
# app.secret_key = 'chatbot123'

# # Load DQN negotiation model
# agent = DQN.load("negotiation_dqn")
# with open("intent_model.pkl", "rb") as f:
#     intent_model = pickle.load(f)
# with open("vectorizer.pkl", "rb") as f:
#     vectorizer = pickle.load(f)

# # Load supervised response model
# with open("response_model.pkl", "rb") as f:
#     response_model = pickle.load(f)
# with open("response_vectorizer.pkl", "rb") as f:
#     response_vectorizer = pickle.load(f)

# def classify_intent(msg):
#     X = vectorizer.transform([msg])
#     return intent_model.predict(X)[0]

# def extract_price(msg):
#     match = re.findall(r"\d{2,3}[kK]|\d{5,7}", msg)
#     if match:
#         return int(match[0].lower().replace('k', '000'))
#     return None

# def generate_negotiation_reply(offer, round_no, base_price, tone):
#     state = np.array([offer / base_price, round_no], dtype=np.float32)
#     action = int(agent.predict(state, deterministic=True)[0])

#     counter_templates = {
#         "friendly": [
#             "Okay, I understand! 😊 Let's try ₹{price}.",
#             "Sounds fair! Can we agree on ₹{price}?"
#         ],
#         "strict": [
#             "₹{price} is the minimum I can do.",
#             "I can't go lower than ₹{price}."
#         ],
#         "playful": [
#             "Let’s split the difference: ₹{price} 😎",
#             "What if I say ₹{price}? Deal? 😜"
#         ]
#     }

#     response_variants = {
#         0: f"Deal at ₹{int(offer)}! 🎉",
#         1: "Sorry, I can’t go that low.",
#         2: random.choice(counter_templates[tone]).format(price=int(0.95 * base_price)),
#         3: random.choice(counter_templates[tone]).format(price=int(0.90 * base_price)),
#         4: random.choice(counter_templates[tone]).format(price=int(0.85 * base_price)),
#     }
#     return response_variants[action], action

# def generate_humanlike_response(msg):
#     X = response_vectorizer.transform([msg])
#     return response_model.predict(X)[0]

# @app.route("/chat", methods=["POST"])
# def chat():
#     data = request.get_json()
#     msg = data.get("message")
#     base_price = data.get("predicted_price", 700000)

#     sentiment = detect_sentiment(msg)
#     if sentiment == "negative":
#         state.tone = "friendly"
#     elif sentiment == "positive":
#         state.tone = "playful"

#     # Load or initialize conversation state
#     if "state" not in session:
#         state = ConversationState()
#     else:
#         state = ConversationState.from_dict(session["state"])

#     offer = extract_price(msg) or 0.7 * base_price
#     round_no = state.round
#     tone = state.tone
#     intent = classify_intent(msg)

#     if intent == "greet":
#         response = "Hi! I'm your virtual assistant. Let’s talk about the car price."
#     elif intent == "accept":
#         response = "Great! Deal confirmed."
#     elif intent == "reject":
#         response = "No worries. Let me know if you change your mind."
#     elif intent == "counter":
#         response = "Okay, I’m open to negotiate. What’s your next offer?"
#     elif intent == "offer":
#         response, action = generate_negotiation_reply(offer, round_no, base_price, tone)
#         state.last_offer = offer
#         if action in [2, 3, 4]:
#             state.concession_count += 1
#     else:
#         response = generate_humanlike_response(msg)

#     state.round += 1
#     state.update(msg, response, offer)
#     session["state"] = state.to_dict()

#     return jsonify({"intent": intent, "response": response})


# @app.route("/")
# def index():
#     return send_from_directory('.', 'chat.html')

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, request, jsonify, session, send_from_directory
# from flask_cors import CORS
# import numpy as np
# import re
# import pickle
# import random
# from textblob import TextBlob
# from negotiation_env import NegotiationEnv
# from stable_baselines3 import DQN
# from state_manager import ConversationState

# app = Flask(__name__)
# CORS(app)
# app.secret_key = 'chatbot123'

# # Load DQN negotiation model
# agent = DQN.load("negotiation_dqn")
# with open("intent_model.pkl", "rb") as f:
#     intent_model = pickle.load(f)
# with open("vectorizer.pkl", "rb") as f:
#     vectorizer = pickle.load(f)

# # Load supervised response model
# with open("response_model.pkl", "rb") as f:
#     response_model = pickle.load(f)
# with open("response_vectorizer.pkl", "rb") as f:
#     response_vectorizer = pickle.load(f)

# def classify_intent(msg):
#     X = vectorizer.transform([msg])
#     return intent_model.predict(X)[0]

# def extract_price(msg):
#     match = re.findall(r"\d{2,3}[kK]|\d{5,7}", msg)
#     if match:
#         return int(match[0].lower().replace('k', '000'))
#     return None

# def detect_sentiment(msg):
#     polarity = TextBlob(msg).sentiment.polarity
#     if polarity > 0.3:
#         return "positive"
#     elif polarity < -0.3:
#         return "negative"
#     else:
#         return "neutral"

# def update_buyer_profile(state, offer, base_price):
#     if offer / base_price < 0.75:
#         state.buyer_type = "lowballer"
#     elif state.round > 3 and state.concession_count < 2:
#         state.buyer_type = "stubborn"
#     elif state.concession_count >= 3:
#         state.buyer_type = "negotiator"
#     return state

# def generate_negotiation_reply(offer, round_no, base_price, tone):
#     state = np.array([offer / base_price, round_no], dtype=np.float32)
#     action = int(agent.predict(state, deterministic=True)[0])

#     counter_templates = {
#         "friendly": [
#             "Okay, I understand! 😊 Let's try ₹{price}.",
#             "Sounds fair! Can we agree on ₹{price}?"
#         ],
#         "strict": [
#             "₹{price} is the minimum I can do.",
#             "I can't go lower than ₹{price}."
#         ],
#         "playful": [
#             "Let’s split the difference: ₹{price} 😎",
#             "What if I say ₹{price}? Deal? 😜"
#         ]
#     }

#     response_variants = {
#         0: f"Deal at ₹{int(offer)}! 🎉",
#         1: "Sorry, I can’t go that low.",
#         2: random.choice(counter_templates[tone]).format(price=int(0.95 * base_price)),
#         3: random.choice(counter_templates[tone]).format(price=int(0.90 * base_price)),
#         4: random.choice(counter_templates[tone]).format(price=int(0.85 * base_price)),
#     }
#     return response_variants[action], action

# def generate_humanlike_response(msg):
#     X = response_vectorizer.transform([msg])
#     return response_model.predict(X)[0]

# @app.route("/chat", methods=["POST"])
# def chat():
#     data = request.get_json()
#     msg = data.get("message")
#     base_price = data.get("predicted_price", 700000)

#     # Load or initialize conversation state
#     if "state" not in session:
#         state = ConversationState()
#     else:
#         state = ConversationState.from_dict(session["state"])

#     offer = extract_price(msg) or 0.7 * base_price
#     round_no = state.round
#     sentiment = detect_sentiment(msg)

#     # Update tone based on sentiment
#     if sentiment == "negative":
#         state.tone = "friendly"
#     elif sentiment == "positive":
#         state.tone = "playful"

#     tone = state.tone
#     intent = classify_intent(msg)

#     if intent == "greet":
#         response = "Hi! I'm your virtual assistant. Let’s talk about the car price."
#     elif intent == "accept":
#         response = "Great! Deal confirmed."
#     elif intent == "reject":
#         response = "No worries. Let me know if you change your mind."
#     elif intent == "counter":
#         response = "Okay, I’m open to negotiate. What’s your next offer?"
#     elif intent == "offer":
#         response, action = generate_negotiation_reply(offer, round_no, base_price, tone)
#         state.last_offer = offer
#         if action in [2, 3, 4]:
#             state.concession_count += 1
#         state = update_buyer_profile(state, offer, base_price)
#     else:
#         response = generate_humanlike_response(msg)

#     state.round += 1
#     state.update(msg, response, offer)
#     session["state"] = state.to_dict()

#     return jsonify({"intent": intent, "response": response, "buyer_type": state.buyer_type, "tone": tone})

# @app.route("/")
# def index():
#     return send_from_directory('.', 'chat.html')

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify, session, send_from_directory
from flask_cors import CORS
import numpy as np
import re
import pickle
import random
from textblob import TextBlob
from negotiation_env import NegotiationEnv
from stable_baselines3 import DQN
from state_manager import ConversationState

app = Flask(__name__)
CORS(app)
app.secret_key = 'chatbot123'

# Load DQN negotiation model
agent = DQN.load("negotiation_dqn")
with open("intent_model.pkl", "rb") as f:
    intent_model = pickle.load(f)
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Load Craigslist-trained response model
with open("response_model.pkl", "rb") as f:
    response_model = pickle.load(f)
with open("response_vectorizer.pkl", "rb") as f:
    response_vectorizer = pickle.load(f)


def classify_intent(msg):
    X = vectorizer.transform([msg])
    return intent_model.predict(X)[0]

def extract_price(msg):
    match = re.findall(r"\d{2,3}[kK]|\d{5,7}", msg)
    if match:
        return int(match[0].lower().replace('k', '000'))
    return None

def detect_sentiment(msg):
    polarity = TextBlob(msg).sentiment.polarity
    if polarity > 0.3:
        return "positive"
    elif polarity < -0.3:
        return "negative"
    else:
        return "neutral"

def update_buyer_profile(state, offer, base_price):
    if offer / base_price < 0.75:
        state.buyer_type = "lowballer"
    elif state.round > 3 and state.concession_count < 2:
        state.buyer_type = "stubborn"
    elif state.concession_count >= 3:
        state.buyer_type = "negotiator"
    return state

def generate_negotiation_reply(offer, round_no, base_price, tone):
    state = np.array([offer / base_price, round_no], dtype=np.float32)
    action = int(agent.predict(state, deterministic=True)[0])

    counter_templates = {
        "friendly": [
            "Okay, I understand! 😊 Let's try ₹{price}.",
            "Sounds fair! Can we agree on ₹{price}?"
        ],
        "strict": [
            "₹{price} is the minimum I can do.",
            "I can't go lower than ₹{price}."
        ],
        "playful": [
            "Let’s split the difference: ₹{price} 😎",
            "What if I say ₹{price}? Deal? 😜"
        ]
    }

    response_variants = {
        0: f"Deal at ₹{int(offer)}! 🎉",
        1: "Sorry, I can’t go that low.",
        2: random.choice(counter_templates[tone]).format(price=int(0.95 * base_price)),
        3: random.choice(counter_templates[tone]).format(price=int(0.90 * base_price)),
        4: random.choice(counter_templates[tone]).format(price=int(0.85 * base_price)),
    }
    return response_variants[action], action

def generate_humanlike_response(msg):
    X = response_vectorizer.transform([msg])
    return response_model.predict(X)[0]

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("message")
    base_price = data.get("predicted_price", 700000)

    # Load or initialize conversation state
    if "state" not in session:
        state = ConversationState()
    else:
        state = ConversationState.from_dict(session["state"])

    offer = extract_price(msg) or 0.7 * base_price
    round_no = state.round
    sentiment = detect_sentiment(msg)

    # Update tone based on sentiment
    if sentiment == "negative":
        state.tone = "friendly"
    elif sentiment == "positive":
        state.tone = "playful"

    tone = state.tone
    intent = classify_intent(msg)

    if intent == "greet":
        response = "Hi! I'm your virtual assistant. Let’s talk about the car price."
    elif intent == "accept":
        response = "Great! Deal confirmed."
    elif intent == "reject":
        response = "No worries. Let me know if you change your mind."
    elif intent == "counter":
        response = "Okay, I’m open to negotiate. What’s your next offer?"
    elif intent == "offer":
        response, action = generate_negotiation_reply(offer, round_no, base_price, tone)
        state.last_offer = offer
        if action in [2, 3, 4]:
            state.concession_count += 1
        state = update_buyer_profile(state, offer, base_price)
    else:
        response = generate_humanlike_response(msg)

    state.round += 1
    state.update(msg, response, offer)
    session["state"] = state.to_dict()

    return jsonify({"intent": intent, "response": response, "buyer_type": state.buyer_type, "tone": tone})

@app.route("/")
def index():
    return send_from_directory('.', 'chat.html')

if __name__ == "__main__":
    app.run(debug=True)

