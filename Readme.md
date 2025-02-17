# Rules Engine Tests

This repository contains tests for the Rules Engine component of the Spot-On project.

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Rules Engine is a core component of the Spot-On project, responsible for evaluating and executing business rules. This repository includes various tests to ensure the correctness and reliability of the Rules Engine.

## Requirements
python3
postgresql

## Setup

To set up the testing environment, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/spot-on.git
    ```
2. Navigate to the tests directory:
    ```sh
    cd spot-on/rules_engine/tests
    ```
3. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```
5. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running Tests

To run the tests, use the following command:
```sh
pytest tests
```

This will execute all the test cases and display the results in the terminal.

## Contributing

We welcome contributions to improve the Rules Engine and its tests. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push the branch to your fork.
4. Create a pull request with a detailed description of your changes.

