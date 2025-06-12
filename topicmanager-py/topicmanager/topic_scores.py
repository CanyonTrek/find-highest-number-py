class TopicScores:
    def __init__(self, topic_name, scores):
        self.topic_name = topic_name
        self.scores = scores

    def get_topic_name(self):
        return self.topic_name

    def get_scores(self):
        return self.scores
