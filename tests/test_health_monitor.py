from health_monitor import generate_report


def test_generate_report():
    assert generate_report() is None
