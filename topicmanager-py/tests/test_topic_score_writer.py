
import unittest
from unittest.mock import Mock, call
from topicmanager.topic_top_score import TopicTopScore
from topicmanager.topic_score_writer import TopicScoreWriter

class TestTopicScoreWriter(unittest.TestCase):

    def test_writes_single_topic_score_once(self):
        scores = [TopicTopScore("Physics", 89)]
        file_writer = Mock()
        writer = TopicScoreWriter(file_writer)

        writer.write_scores(scores)

        file_writer.write_line.assert_called_once_with("Physics, 89")

    def test_does_not_write_when_list_is_empty(self):
        scores = []
        file_writer = Mock()
        writer = TopicScoreWriter(file_writer)

        writer.write_scores(scores)

        file_writer.write_line.assert_not_called()

    def test_writes_multiple_topic_scores(self):
        scores = [
            TopicTopScore("Physics", 89),
            TopicTopScore("Art", 87),
            TopicTopScore("Comp Sci", 97)
        ]
        file_writer = Mock()
        writer = TopicScoreWriter(file_writer)

        writer.write_scores(scores)

        expected_calls = [
            call("Physics, 89"),
            call("Art, 87"),
            call("Comp Sci, 97")
        ]
        file_writer.write_line.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()
