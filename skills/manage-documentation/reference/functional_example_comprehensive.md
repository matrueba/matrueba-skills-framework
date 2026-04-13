## Service Functionalities (mandatory)


- **[GW-1]** - Route incoming HTTP requests to appropriate backend microservices based on configured routing rules and URL patterns
- **[GW-2]** - Authenticate users using JWT tokens and manage user sessions with token refresh capabilities
- **[GW-3]** - Enforce role-based access control (RBAC) and validate user permissions for each endpoint
- **[GW-4]** - Implement rate limiting using token bucket algorithm with per-user and per-endpoint limits
- **[GW-5]** - Validate incoming JSON request payloads against defined JSON schemas using Joi validation
- **[GW-6]** - Transform and normalize responses from multiple backend services into consistent API format
- **[GW-7]** - Centralized logging of all requests, responses, and errors with correlation ID tracking
- **[GW-8]** - Graceful error handling with appropriate HTTP status codes and standardized error responses


