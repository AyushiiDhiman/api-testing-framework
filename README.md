✅ API Testing Framework (Python + Pytest)

A modular, scalable, and beginner-friendly API automation testing framework built using Python, Pytest, Requests, and JSON Schema Validation.
Designed to demonstrate strong testing fundamentals, clean architecture, and professional automation practices.

🚀 Features

✅ Modular API client for GET/POST/PUT/DELETE
✅ Centralized endpoint management
✅ Reusable assertion layer (status code, response time, key validation)
✅ JSON Schema Validation for contract testing
✅ Easy test structuring using Pytest
✅ Environment-based configuration
✅ Fully Git-versioned and CI/CD friendly
✅ Clean folder structure for real-world automation projects

API_testing_framework/
│
├── core/
│   ├── api_client.py        # Handles HTTP requests
│   ├── endpoints.py         # Stores all API endpoints
│   ├── assertions.py        # Custom assertion helpers
│   └── config.py            # Base URL and environment configs
│
├── tests/
│   ├── test_auth_api.py     # Authentication API tests
│   ├── test_users_api.py    # User API tests + schema validation
│
├── README.md                # Project documentation
├── requirements.txt         # Dependencies
└── .gitignore


🔧 Tech Stack

Python 3.14

Pytest

Requests

JSONSchema (for contract testing)

Git & GitHub

VS Code / PyCharm


📈 What This Project Demonstrates

✅ Understanding of API automation
✅ Writing reusable & maintainable test frameworks
✅ Contract Testing using JSON Schema
✅ Clean Git workflow
✅ Practical Pytest usage
✅ Strong fundamentals for real QA + SDET roles


⭐ Future Enhancements

Add CI/CD pipeline (GitHub Actions)

Add HTML reporting (Allure / Pytest-HTML)

Add logging

Add POST/PUT/DELETE validations

Integrate with Mock APIs for full coverage
