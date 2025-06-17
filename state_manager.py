# state_manager.py

class ConversationState:
    def __init__(self):
        self.round = 0
        self.last_offer = 0
        self.concession_count = 0
        self.tone = "friendly"
        self.buyer_type = "neutral"   # or 'lowballer', 'stubborn', etc.
        self.history = []             # [(user_msg, bot_reply)]
    
    def update(self, user_msg, bot_reply, offer=None):
        self.round += 1
        if offer:
            self.last_offer = offer
        self.history.append((user_msg, bot_reply))
    
    def to_dict(self):
        return self.__dict__
    
    @staticmethod
    def from_dict(d):
        obj = ConversationState()
        obj.__dict__.update(d)
        return obj
