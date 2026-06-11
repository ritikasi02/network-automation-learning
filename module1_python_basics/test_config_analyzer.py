from config_analyzer import get_hostname, get_interfaces, read_confg
import pytest

@pytest.mark.parametrize("lines, expected", [
    (["hostname R1\n", "!\n", "interface GigabitEthernet0/0\n"], "R1"),
    (["R1\n", "!\n", "interface GigabitEthernet0/0\n"], "unknown"),
    (["hostname CORE-SW1\n", "!\n", "interface GigabitEthernet0/0\n"], "CORE-SW1"),
])
def test_hostname(lines, expected):
    result = get_hostname(lines)
    assert result == expected

#def test_get_hostname():
#    lines = ["hostname R1\n", "!\n", "interface GigabitEthernet0/0\n"] # Arrange: build the input
#    result = get_hostname(lines) # Act: run the function
#    assert result == "R1"  # Assert: check the output


#def test_get_hostname_missing():
#    lines = ["R1\n", "!\n", "interface GigabitEthernet0/0\n"] # Arrange: build the input
#    result = get_hostname(lines)
#    assert result == "unknown"

def test_get_interfaces():
    lines = ["interface GigabitEthernet0/0", 
             "description WAN Link to R2", 
             "ip address 10.1.1.1 255.255.255.0", 
             "duplex auto",
             "speed auto",
             "media-type rj45",
             "!",
            ]
    result = get_interfaces(lines)
    assert result == [{"name": "interface GigabitEthernet0/0", "ip": "10.1.1.1", "mask":"255.255.255.0"}]

def test_get_interfaces_no_ip():
    lines = ["interface GigabitEthernet0/0", 
             "description WAN Link to R2", 
             "no ip address", 
             "duplex auto",
             "speed auto",
             "media-type rj45",
             "!",
            ]
    result = get_interfaces(lines)
    assert result == []

    
def test_read_confg(tmp_path):
    config_file = tmp_path / "R1.txt"
    config_file.write_text("hostname R1\ninterface Gig0/0\n")
    result = read_confg(config_file)
    assert result == ["hostname R1\n", "interface Gig0/0\n"]