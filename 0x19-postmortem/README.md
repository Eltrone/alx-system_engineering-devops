# Project Postmortem

## Issue Summary
- **Duration**: May 7, 2024, from 2:00 PM UTC to 4:30 PM UTC.
- **Impact**: A database failure caused significant downtime for our main web application, impacting approximately 70% of our users. Affected users experienced extremely slow loading times and frequent disconnections.
- **Root Cause**: The outage was primarily caused by an overload of requests coupled with suboptimal database server configuration.

## Timeline
- **2:00 PM UTC**: Incident detected via performance monitoring alert.
- **2:05 PM UTC**: DevOps team begins initial assessment, checking server load and error logs.
- **2:20 PM UTC**: DDoS attack ruled out after reviewing network traffic.
- **2:45 PM UTC**: Incident escalated to the database management team due to observed lengthy transaction locks.
- **3:30 PM UTC**: Suboptimal configuration identified as probable cause.
- **4:30 PM UTC**: New server configuration implemented, database restarted, full service restoration achieved.

## Root Cause and Resolution
Incorrect database cache settings failed to accommodate an increase in data volume. Adjusting the cache size and transaction cleanup parameters resolved the issue.

## Corrective and Preventive Measures
To prevent future incidents, the following steps are recommended:
- **Periodic Review of Database Configurations**: Ensure configurations are adapted to current loads.
- **Proactive Database Performance Monitoring**: Early detection and resolution of performance issues.
- **Technical Team Training**: Ongoing education on best practices for database management under high load.
- **Nginx Server Patch**: Upgrade to the latest stable version for improved traffic management.
- **Memory Monitoring**: Implement monitoring to detect and mitigate performance issues due to insufficient memory.

## Conclusion
This postmortem aims to document the incident comprehensively to prevent recurrence and improve our system resilience. For further details or inquiries, please contact the project team.
