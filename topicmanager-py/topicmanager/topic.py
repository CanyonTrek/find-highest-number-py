class Topic:
    def __init__(self, topic_name, score):
        self.topic_name = topic_name
        self.score = score

    def get_topic_name(self):
        return self.topic_name

    def get_score(self):
        return self.score
