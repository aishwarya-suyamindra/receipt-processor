## Receipt processor

A Python Flask based application that provides APIs to process receipts and retrieve points calculated for the processed receipts. 


## Table of Contents

- [Overview](#overview)
- [Installation](#installation)

## Overview
The application provides two API endpoints:

-   ```
    POST /receipts/process
    ```

-   ```
    GET /receipts/{id}/points
    ```


## Installation

The application can run with Docker:

1. **Build the docker image:**

    ```bash
   docker build -t receipt-processor-app .
    ```

2. **Run the container with the image**

    ```bash
    docker run --rm -p 4000:4000 receipt-processor-app
    ```

The application should be running on [http://localhost:4000](http://localhost:4000).


