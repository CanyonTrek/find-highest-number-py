# Find Highest Number - TDD Walkthrough (Python)

This project is a step-by-step **Test-Driven Development (TDD)** walkthrough showing how to evolve a Python application using real-world practices like stubs, mocks, refactoring, and separation of concerns.

The walkthrough starts with a minimal hard-coded solution and incrementally evolves toward a fully testable, clean, and modular application.

---

## 🚀 Final App Overview (v2.7)

This app processes a list of topics, calculates the highest score per topic, and writes the results to a file using clean, testable classes. It includes:

- `Topic`, `TopicManager`, `TopicTopScore` models
- `HighestNumberFinder` logic
- `TopicScoreWriter` for writing results
- Unit tests using `unittest` and `unittest.mock`

---

## 📂 Project Structure

```
topicmanager-py/
├── main.py
├── topicmanager/
│   ├── topic.py
│   ├── topic_manager.py
│   ├── topic_top_score.py
│   ├── topic_score_writer.py
│   ├── highest_number_finder.py
│   └── file_writer.py
├── tests/
│   ├── test_topic_manager.py
│   └── test_topic_score_writer.py
```

---

## 🏷️ Tags and Evolution

Each Git tag represents an important step in the TDD journey. See [`HISTORY.md`](HISTORY.md) for full detail.

---

## 🧪 Running Tests

```bash
python -m unittest discover topicmanager-py/tests
```

---

## 🧠 Educational Use

This project is designed for learners and instructors working through Python testing patterns. Use the tags to checkout each state:

```bash
git checkout v2.3-limitations_of_stubs
```


