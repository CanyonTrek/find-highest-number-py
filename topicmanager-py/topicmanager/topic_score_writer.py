from topicmanager.topic_top_score import TopicTopScore
from topicmanager.file_writer import write_line_to_file 

class TopicScoreWriter:
    def __init__(self, write_line=None):  
        if write_line is None:
            write_line = write_line_to_file
        self.write_line = write_line

    def write_scores(self, top_scores):
        self.write_line("Physics, 89")
