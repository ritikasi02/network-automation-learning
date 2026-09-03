parsed = [
    {"hostname": "R1", 
    
    "interfaces": 
        [{"name": "interface gig0/0", 
         "ip": "10.1.1.1",
         "mask": "255.255.255.0",
        }],
    "ospf": 
        [
        {"network": "10.1.1.0",
        "wildcard": "0.0.0.255",
        "area": "1",
        }
        ],
    },

    {"hostname": "R2",
     "interfaces": [],
     "ospf": [],
    }
]

