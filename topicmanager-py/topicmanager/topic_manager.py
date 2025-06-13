from highestnumber finder import HighestNumberFinder
from topicmanager.topic_top_score import TopicTopScore

class TopicManager:
    def __init__(self):
        self.highest_number_finder = HighesNumberFinder()

    def find_topic_high_scores(self, topic):
        return TopiceTopScore(topic.topic_name, topic.get_score())
