from topicmanager.topic_score_writer import TopicScoreWriter
from topicmanager.topic_top_score import TopicTopScore

# Example list of scores
top_scores = [
    TopicTopScore("Math", 95),
    TopicTopScore("Science", 88)
]

# This uses the default file "output.txt" defined in file_writer
writer = TopicScoreWriter()
writer.write_scores(top_scores)
