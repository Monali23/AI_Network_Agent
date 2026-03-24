from agents.root_cause_agent import detect_root_cause

def test_root_cause():
    result = detect_root_cause()
    assert result is not None