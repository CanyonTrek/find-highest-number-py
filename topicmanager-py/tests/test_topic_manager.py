
import unittest
from topicmanager.topic_manager import TopicManager
from topicmanager.topic_scores import TopicScores
from topicmanager.topic_top_score import TopicTopScore
# from topicmanager.highest_number_finder import HighestNumberFinder

class TestTopicManager(unittest.TestCase):
    def test_empty_list_returns_empty_result(self):
        scores = []
        manager = TopicManager()
        result = manager.find_topic_high_scores(scores)
        self.assertEqual(result, [])

    def test_single_topic_returns_correct_top_score(self):
        scores = [56, 67, 45, 89]
        topics = [TopicScores("Physics", scores)]
        manager = TopicManager(HighestNumberFinder())
        result = manager.find_topic_high_scores(topics)
        self.assertEqual(result[0].topic_name, "Physics")
        self.assertEqual(result[0].top_score, 89)

    def test_stub_finder_returns_correct_top_score(self):
        scores = [56, 67, 45, 89]
        topics = [TopicScores("Physics", scores)]
        manager = TopicManager(HighestNumberFinder())
        result = manager.find_topic_high_scores(topics)
        self.assertEqual(result[0].topic_name, "Physics")
        self.assertEqual(result[0].top_score, 89)


if __name__ == '__main__':
    unittest.main()
