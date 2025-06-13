
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

    def test_multiple_topics_stub_finder(self):
        topics = [
            TopicScores("Physics", [56, 67, 45, 89]),
            TopicScores("Art", [87, 66, 78]),
            TopicScores("Comp Sci", [45, 88, 97, 56])
        ]
        manager = TopicManager(HighestNumberFinder())
        result = manager.find_topic_high_scores(topics)
        self.assertEqual(result[0].topic_name, "Physics")
        self.assertEqual(result[0].top_score, 89)
        self.assertEqual(result[1].topic_name, "Art")
        self.assertEqual(result[1].top_score, 87)
        self.assertEqual(result[2].topic_name, "Comp Sci")
        self.assertEqual(result[2].top_score, 97)


if __name__ == '__main__':
    unittest.main()
