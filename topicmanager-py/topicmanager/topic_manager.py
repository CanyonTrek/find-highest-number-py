from topicmanager.topic_top_score import TopicTopScore

class TopicManager:
    def __init__(self, highest_number_finder=None):
        self.highest_number_finder = highest_number_finder

    def find_topic_high_scores(self, topic_scores_list):
        if not self.highest_number_finder:
            raise ValueError("Highest number finder not provided")

        top_scores = []
        for ts in topic_scores_list:
            top_score = self.highest_number_finder.find_highest_number(ts.scores)
            top_scores.append(TopicTopScore(ts.topic_name, top_score))
        return top_scores
