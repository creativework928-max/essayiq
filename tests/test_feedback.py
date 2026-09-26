from src.services.feedback_service import feedback,indicators

def test_feedback_is_deterministic():
    text="This is a clear essay. It uses several transitions. Therefore, ideas connect."
    assert feedback(text)==feedback(text)
    assert set(indicators(text))=={"content","grammar","organization","vocabulary","readability"}
