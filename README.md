## Receipt processor

A Python Flask based application that provides APIs to process receipts and retrieve points awarded for the processed receipts. 


## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Details](#details)

## Overview
The application provides two API endpoints:

1. POST /receipts/process - This endpoint takes in the receipt JSON data, processes the receipt and items and returns a unique ID for the receipt.

2. GET /receipts/{id}/points - This endpoint retrieves the points awarded for the given receipt ID.

## Installation

Clone the repository:

```
git clone https://github.com/aishwarya-suyamindra/receipt-processor.git
```

The application can be run with Docker:

1. **Build the docker image:**

    ```
   docker build -t receipt-processor-app .
    ```

2. **Run the container with the image**

    ```
    docker run --rm -p 4000:4000 receipt-processor-app
    ```

Alternatively, to run the application locally, ensure Python is installed.

1. **Set up a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the flask application**

    ```bash
    python app.py
    ```

The application should be running on http://localhost:4000.

## Details

The application is built with:
- Flask – A lightweight web framework

- Pydantic – Library used for data validation to ensure correct request formats

- Swagger - Tool used to document the API endpoints request and response format

The application validates JSON data sent in the POST request to ensure all required fields are properly populated. If any fields are missing or incorrectly formatted, the API returns an HTTP 400 status code with an appropriate error message. The points awarded are in line with the specified rules.

The application is documented with the help of Swagger. The config file used is in line with the api.yml specified in the challenge. When the values specified for the fields are incorrect, the response body includes an appropriate error message indicating the same. This is added in the schema.

Current Limitations & Future Improvements:

- Data Persistence and caching: Currently, receipt data is not stored permanently and will be lost on application restart. Future enhancements could include database integration for persistent storage, along with caching mechanisms to store points awarded for frequently accessed receipts.

- Security: User registration, Authentication and authorization can be added to secure access to the API and make it available for many users.