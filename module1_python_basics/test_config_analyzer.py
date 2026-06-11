from config_analyzer import get_hostname, get_interfaces

def test_get_hostname():
    lines = ["hostname R1\n", "!\n", "interface GigabitEthernet0/0\n"] # Arrange: build the input
    result = get_hostname(lines) # Act: run the function
    assert result == "R1"  # Assert: check the output


def test_get_hostname_missing():
    lines = ["R1\n", "!\n", "interface GigabitEthernet0/0\n"] # Arrange: build the input
    result = get_hostname(lines)
    assert result == "unknown"

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

    