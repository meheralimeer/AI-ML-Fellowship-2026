# Task 4 — Libraries, Packaging, Documentation & Production Readiness

This task covers converting scripts into modules, creating a custom Python package, and managing dependencies.

## 1. Modular Programming

The scripts from previous tasks (`factorial.py` and `string_reverse.py`) have been converted into reusable modules. They are located in the `modules/` directory.

A `main.py` script is included to demonstrate how to import and use these modules.

### To Run the Demonstration:

```bash
python3 main.py
```

## 2. Virtual Environment & Packages

It is a best practice to use a virtual environment for Python projects to manage dependencies.

### Creating a Virtual Environment:

To create and activate a virtual environment, run the following commands from the `Week1-python-and-git-foundation` directory:

```bash
# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

A `requirements.txt` file has been added to the project. Although it is empty for now, you can add dependencies to it and install them using:

```bash
pip install -r requirements.txt
```

## 3. Custom Python Package

A simple Python package named `simple_calculator` has been created in the `mypackage/` directory.

### Package Structure:

```
mypackage/
├── README.md
├── setup.py
└── simple_calculator/
    ├── __init__.py
    └── arithmetic.py
```

### To Install the Package:

Navigate to the `mypackage/` directory and run:

```bash
pip install .
```

This will install the `simple_calculator` package in your environment, and you can then import its functions in other Python scripts.
