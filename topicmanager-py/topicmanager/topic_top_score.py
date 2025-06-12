class TopicTopScore:
    def __init__(self, topic_name, top_score):
        self.topic_name = topic_name
        self.top_score = top_score

    def get_topic_name(self):
        return self.topic_name

    def get_top_score(self):
        return self.top_score

    def __eq__(self, other):
        return (
            isinstance(other, TopicTopScore) and
            self.topic_name.lower() == other.topic_name.lower() and
            self.top_score == other.top_score
        )
