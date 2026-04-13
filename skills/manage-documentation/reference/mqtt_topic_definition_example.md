#### Topic: NETWORK/PRIVATE/RESULT/COMMISSIONING

**Message Example:**
```json
{
    "timestamp": 55521145214,
    "app_source_command": "tbox_api",
    "token": 403,
    "command": "commissioning",
    "params": {}
}
```

**Comments:** -

---

#### Topic: NETWORK/PRIVATE/RESULT/COMMISSIONING

**Message Example:**
```json
{
    "timestamp": 55521145215,
    "app_source_command": "tbox_api",
    "app_source_result": "chirpstack_nwk_adapter",
    "token": 403,
    "command": "commissioning",
    "params": {},
    "result": {
        "return": 0,
        "data": {}
    },
    "message": "OK. Commissioning process completed succesfully"
}
```

**Comments:** -

---

#### Topic: NETWORK/PRIVATE/COMMAND/TX/MULTICAST/<multicast_code>

**Message Example:**
```json
{
     "timestamp": 55521145214,
    "app_source_command": "tracker_control",
    "token": 403,
    "command": "P16",
    "params": {
        "payload": {
            "type": "base64",
            "value": "ACMeIT7a/w==",
            "units": "na",      
            "scale": 1
        }
    }
}
```

**Comments:** -

---

#### Topic: NETWORK/PRIVATE/COMMAND/TX/UNICAST/DBOX/<blockid>/<trackerid>
#### Topic: NETWORK/PRIVATE/COMMAND/TX/UNICAST/MBOX/<blockid>/<mboxid>

**Message Example:**
```json
{
    "timestamp": 55521145214,
    "app_source_command": "tracker_control",
    "token": 403,
    "command": "P24",
    "params": {	
		"payload": {
            "type": "base64",
            "value": "ACMeIT7a/w==",
            "units": "na",      
            "scale": 1
        },
        "encapsulated": {
            "type": "bool",
            "value": true,
            "units": "na",      
            "scale": 1
        },
        "m_index": {
            "type": "uint16",
            "value": 0,
            "units": "na",      
            "scale": 1
        }
    }
}
```

**Comments:** The type of message to be sent shall be located in the “command” section of the MQTT message.

---


#### Topic: NETWORK/PRIVATE/COMMAND/TX/UNICAST/DBOX/<blockid>/<trackerid>
#### Topic: NETWORK/PRIVATE/COMMAND/TX/UNICAST/MBOX/<blockid>/<mboxid>

**Message Example:**
```json
{
    "timestamp": 55521145214,
    "app_source_command": "tracker_control",
    "token": 403,
    "command": "P24",
    "params": {	
		"payload": {
            "type": "base64",
            "value": "ACMeIT7a/w==",
            "units": "na",      
            "scale": 1
        },
        "encapsulated": {
            "type": "bool",
            "value": true,
            "units": "na",      
            "scale": 1
        },
        "m_index": {
            "type": "uint16",
            "value": 0,
            "units": "na",      
            "scale": 1
        }
    }
}
```

**Comments:** The type of message to be sent shall be located in the “command” section of the MQTT message.

---
#### Topic: NETWORK/PRIVATE/RESULT/TX/UNICAST/DBOX/<blockid>/<trackerid>
#### Topic: NETWORK/PRIVATE/RESULT/TX/UNICAST/MBOX/<blockid>/<mboxid>
#### Topic: NETWORK/PRIVATE/RESULT/TX/UNICAST/CLEANING_ROBOT/<pathid>/<robotid>
#### Topic: NETWORK/PRIVATE/RESULT/TX/MULTICAST/<multicast_code>

**Direction:** Response

**Message Example:**
```json
{
  "timestamp": 1654782294096,
  "result": {
    "return": 0,
    "message": "OK",
    "data": {}
  },
  "token": 23950,
  "app_source_command": "tracker_control",
  "app_source_result": "chirpstack_nwk_adapter",
  "command": "P10",
  "params": {
    "payload": {
      "type": "base64",
      "value": "AAAAAA==",
      "units": "na",
      "scale": 1
    },
    "encapsulated": {
      "type": "bool",
      "value": true,
      "units": "na",      
      "scale": 1
    },
    "m_index": {
      "type": "uint16",
      "value": 0,
      "units": "na",      
      "scale": 1
    }
  }
}
```

**Comments:** Answer to command messages

---

#### Topic: NETWORK/PRIVATE/EVENT/LORA/RX/DBOX/<blockid>/<trackerid>
#### Topic: NETWORK/PRIVATE/EVENT/LORA/RX/MBOX/<blockid>/<mboxid>
#### Topic: NETWORK/PRIVATE/EVENT/LORA/RX/CLEANING_ROBOT/<pathid>/<robotid>

**Direction:** Event

**Message Example:**
```json
{
    "timestamp": 55521145214,
    "app_source": "chirpstack_nwk_adapter",
    "id": "<deveui>",
    "link": "LORA",
    "data": {
        "payload": {
            "type": "base64",
            "value": "ACMeIT7a/w==",
            "units": "na",      
            "scale": 1
        },
        "msg_type": {
            "type": "string",
            "value": "P1",
            "units": "na",
            "scale": 1
        }
    }
}
```

**Comments:** EVENT type messages are described in MQTT - Message Specification

---

#### Topic: NETWORK/PRIVATE/EVENT/LORA/JOIN/DBOX/<blockid>/<trackerid>
#### Topic: NETWORK/PRIVATE/EVENT/LORA/JOIN/MBOX/<blockid>/<mboxid>
#### Topic: NETWORK/PRIVATE/EVENT/LORA/JOIN/CLEANING_ROBOT/<pathid>/<robotid>

**Direction:** Event

**Message Example:**
```json
{
    "timestamp": 55521145214,
    "app_source": "chirpstack_nwk_adapter",
    "id": "<deveui>",
    "link": "LORA",
    "data": {}
}
```

**Comments:** Empty data, only a notification

---

#### Topic: NETWORK/PRIVATE/DATA/LORA/STATS/DBOX/<blockid>/<trackerid>
#### Topic: NETWORK/PRIVATE/DATA/LORA/STATS/MBOX/<blockid>/<mboxid>
#### Topic: NETWORK/PRIVATE/DATA/LORA/STATS/CLEANING_ROBOT/<pathid>/<robotid>

**Direction:** Data

**Message Example:**
```json
{
    "timestamp": 55521145214,
    "app_source": "chirpstack_nwk_adapter",
    "id": "c48fc1000000105f",
    "link": "LORA",
    "data": {
        "SNRrx": {
            "type": "float32",
            "value": 12.5,
            "units": "decibel",
            "scale": 1
        },
        "RSSIrx": {
            "type": "float32",
            "value": -91,
            "units": "decibelmilliwats",
            "scale": 1
        },
        "spreadingFactor": {
            "type": "int8",
            "value": 9,
            "units": "na",
            "scale": 1
        },
        "frequency": {
            "type": "int64",
            "value": 867900000,
            "units": "hertz",
            "scale": 1
        }
    }
}
```

**Comments:** -

---

#### Topic: NETWORK/PRIVATE/COMMAND/MANAGER

**Direction:** Command

**Message Example:**
```json
{
    "timestamp": 55521145214,
    "app_source_command": "webserver",
    "token": 403,
    "command": "fail_safe_sf_configuration",
    "params": {
        "enable":{
            "type": "bool",
            "value": true,
            "units": "na",
            "scale": 1
        },
        "sf_alternate_1": {
            "type": "uint8",
            "value": 9,
            "units": "na",
            "scale": 1
        },
        "sf_alternate_2":{
            "type": "uint8",
            "value": 12,
            "units": "na",
            "scale": 1
        }
    }
}
```

**Comments:** This command is sent to configure Spreading Factor Fail Safe functionality.

---

#### Topic: NETWORK/PRIVATE/RESULT/MANAGER

**Direction:** Response

**Message Example:**
```json
{
  "timestamp": 1654782294096,
  "result": {
    "return": 0,
    "message": "OK",
    "data": {}
  },
  "token": 23950,
  "app_source_command": "webserver",
  "app_source_result": "chirpstack_nwk_adapter",
  "command": "sf_config",
  "params": {
    "enable":{
            "type": "bool",
            "value": true,
            "units": "na",
            "scale": 1
    },
    "sf_alternate_1": {
            "type": "uint8",
            "value": 9,
            "units": "na",
            "scale": 1
        },
        "sf_alternate_2":{
            "type": "uint8",
            "value": 12,
            "units": "na",
            "scale": 1
        }
  }
}
```

**Comments:** -

---

#### Topic: NETWORK/PRIVATE/DATA/MANAGER/FAIL_SAFE/SF/CONFIGURATION

**Direction:** Data

**Message Example:**
```json
{
    "app_source": "chirpstack_nwk_adapter",
    "timestamp": 1693394082923,
    "data": {
        "enable":{
            "type": "bool",
            "value": true,
            "units": "na",
            "scale": 1
        },
        "sf_alternate_1": {
            "type": "uint8",
            "value": 9,
            "units": "na",
            "scale": 1
        },
        "sf_alternate_2": {
            "type": "uint8",
            "value": 12,
            "units": "na",
            "scale": 1
        }
    },
    "link": "LORA"
}
```

**Comments:** Retained Spreading Factor Fail Safe configuration

---

#### Topic: NETWORK/PRIVATE/COMMAND/MANAGER/LORAWAN/<MULTICAST_CODE>

**Direction:** Command

**Message Example:**
```json
{
    "timestamp": 55521145214,
    "app_source_command": "tbox_api",
    "token": 404,
    "command": "get_configuration",
    "params": {
        "multicast_code": {
            "type": "uint8",
            "value": 0,
            "units": "na",
            "scale": 1
        }
    }
}
```

**Comments:** -

---

#### Topic: NETWORK/PRIVATE/RESULT/MANAGER/LORAWAN/<MULTICAST_CODE>

**Direction:** Response

**Message Example:**
```json
{
    "timestamp": 55521145215,
    "app_source_command": "tbox_api",
    "app_source_result": "network-manager",
    "token": 404,
    "command": "get_configuration",
    "params": {
        "multicast_code": {
            "type": "uint8",
            "value": 0,
            "units": "na",
            "scale": 1
        }
    },
    "result": {
        "return": 0,
        "message": "OK",
        "data": {
            "loraRegion": {
                "type": "string",
                "value": "lora_region",
                "units": "na",
                "scale": 1
            },
            "multicastDelay": {
                "type": "uint16",
                "value": 100,
                "units": "milliseconds",
                "scale": 1
            },
            "totalGateways": {
                "type": "uint8",
                "value": 0,
                "units": "na",
                "scale": 1
            },
            "rx2DataRate": {
                "type": "uint8",
                "value": 0,
                "units": "na",
                "scale": 1
            }
        }
    }
}
```

**Comments:** -
