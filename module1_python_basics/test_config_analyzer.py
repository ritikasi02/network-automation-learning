from config_analyzer import get_hostname

def test_get_hostname():
    lines = ["hostname R1\n", "!\n", "interface GigabitEthernet0/0\n"] # Arrange: build the input
    result = get_hostname(lines) # Act: run the function
    assert result == "R1"  # Assert: check the output


def test_get_hostname_missing():
    lines = ["R1\n", "!\n", "interface GigabitEthernet0/0\n"] # Arrange: build the input
    result = get_hostname(lines)
    assert result == "unknown"
