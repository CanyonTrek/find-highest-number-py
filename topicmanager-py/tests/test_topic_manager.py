
import unittest
from topicmanager.topic_manager import TopicManager
from topicmanager.topic_scores import TopicScores
from topicmanager.topic_top_score import TopicTopScore
# from topicmanager.highest_number_finder import HighestNumberFinder

class TestTopicManager(unittest.TestCase):
    def test_single_topic_returns_correct_top_score(self):
        topic = Topic("Physics", 89)
        manager = TopicManager()
        result = manager.find_topic_high_scores(topic)
        self.assertEqual(result.topic_name, "Physics")
        self.assertEqual(result.top_score, 89)


if __name__ == '__main__':
    unittest.main()
