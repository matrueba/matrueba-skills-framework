

## System Requirements (mandatory)

| Requirement | Version | Description |
| :--- | :--- | :--- |
| Language | [version] | Runtime environment |
| Database | [type/version] | Data persistence |
| Message Broker | [type/version] | MQTT or similar |

---


## System Dependencies (mandatory)

| Libray | Version |
| :--- | :--- | :--- |
| Library name | [version] |

---

## MQTT Client Configuration 

| Client ID | MQTT Version | User name | Clean session |
| :--- | :--- | :--- | :--- |

---

### Environment Variables (mandatory)

Every variable described in this section is necessary to correctly initialise the microservice, unless explicity described as optional.

Env variables file and its default values can be found at *src/common_utils/parameters.ts*

* Variables with default values shall take that configuration if not defined. Thus, code will not be blocked.
* Variables without default values shall block the code execution.

| Variable | Values | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |

---

### Data Bases

| Data Base | Table | Variable |
| :--- | :--- | :--- | :--- | :--- |
