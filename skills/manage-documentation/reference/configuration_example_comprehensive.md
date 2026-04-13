# Configuration Example Comprehensive

## System Requirements (mandatory)

| Requirement | Version | Description |
| :--- | :--- | :--- |
| Language | Node.js 18.x | JavaScript runtime environment |
| Database | MongoDB 5.0+ | Document storage for configurations and metadata |
| Message Broker | MQTT 3.1.1 | Event-driven messaging for service integration |
| Cache Store | Redis 7.0+ | In-memory cache for performance optimization |

---

## System Dependencies (mandatory)

| Library | Version |
| :--- | :--- |
| express | ^4.18.2 |
| mongoose | ^7.0.0 |
| mqtt | ^4.3.7 |
| redis | ^4.6.0 |

---

## MQTT Client Configuration

| Client ID | MQTT Version | Username | Clean Session |
| :--- | :--- | :--- | :--- |
| api-gateway-001 | 3.1.1 | mqtt_user | true |

---

### Environment Variables (mandatory)

Every variable described in this section is necessary to correctly initialize the microservice, unless explicitly described as optional.

* Variables with default values shall take that configuration if not defined. Thus, code will not be blocked.
* Variables without default values shall block the code execution.

| Variable | Values | Default Value | Description |
| :--- | :--- | :--- | :--- |
| NODE_ENV | development, production, test | development | Environment mode for the application |
| PORT | number (1-65535) | 3000 | HTTP server listening port |
| LOG_LEVEL | debug, info, warn, error | info | Application logging verbosity level |
| DB_HOST | hostname/IP | localhost | MongoDB connection hostname |
| DB_PORT | number (1-65535) | 27017 | MongoDB connection port |
| DB_NAME | string | api_gateway | MongoDB database name |
| DB_USER | string | [required] | MongoDB authentication username |
| DB_PASSWORD | string | [required] | MongoDB authentication password |
| REDIS_HOST | hostname/IP | localhost | Redis connection hostname |
| REDIS_PORT | number (1-65535) | 6379 | Redis connection port |
| MQTT_HOST | hostname/IP | localhost | MQTT broker hostname |
| MQTT_PORT | number (1-65535) | 1883 | MQTT broker port |
| MQTT_USERNAME | string | mqtt_user | MQTT authentication username |
| MQTT_PASSWORD | string | [required] | MQTT authentication password |
| JWT_SECRET | string (minimum 32 chars) | [required] | Secret key for JWT token signing |
| JWT_EXPIRY | string (e.g., 24h, 7d) | 24h | JWT token expiration time |
| RATE_LIMIT_WINDOW | milliseconds | 900000 | Rate limit time window (ms) |
| RATE_LIMIT_MAX_REQUESTS | number | 100 | Maximum requests per time window |
| CORS_ORIGIN | URL/*, comma-separated | * | Allowed CORS origins (OPTIONAL) |
| SERVICE_REGISTRY_URL | URL | `http://localhost:8080` | Service registry/discovery URL |
| ENABLE_HTTPS | true, false | false | Enable HTTPS for the server (OPTIONAL) |
| CERT_PATH | file path | /certs/server.crt | Path to SSL certificate (if HTTPS enabled) |
| KEY_PATH | file path | /certs/server.key | Path to SSL private key (if HTTPS enabled) |

---

### Data Bases

| Data Base | Table/Collection | Environment Variable |
| :--- | :--- | :--- |
| MongoDB | api_configurations | DB_NAME |
| Redis | route_cache | REDIS_HOST, REDIS_PORT |
