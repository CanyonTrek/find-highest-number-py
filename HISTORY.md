# Walkthrough History – Git Tags

This file explains what each tag in the repository represents.

| Tag | Description |
|-----|-------------|
| `v2.0-earliest_version` | Initial implementation using `Topic`, with hardcoded logic and no abstraction. |
| `v2.1-coupled_manager` | Added `TopicManager` using a real `HighestNumberFinder`, but no injection yet. |
| `v2.2-working_with_stubs` | Introduced dependency injection and stubs for testability. |
| `v2.3-limitations_of_stubs` | Exposed limitations of stubs — e.g., handling multiple inputs. |
| `v2.4-replaced_stub_with_mock` | Swapped stubs with mocks for greater flexibility in tests. |
| `v2.5-initial_draft_of_TopicWriter` | First version of `TopicScoreWriter`, with hardcoded output. |
| `v2.6-TopicWriter_writes_one_score` | Writer now outputs one topic's real score from logic. |
| `v2.7-TopicWriter_final_test_and_solution` | Final implementation with complete logic, test coverage, and mock usage. |

