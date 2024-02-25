# ISDM hackathon

This repository contains code for the [ISDM hackathon]([url](https://www.isdm.org.in/isdm-code-for-change)https://www.isdm.org.in/isdm-code-for-change)


## Setup environment


1. **Install Python**: If you don't have Python installed on your machine, download and install it from the [official website](https://www.python.org/downloads/). This project uses Python 3.x.

2. **Check Python Version**: Verify your Python installation by opening a terminal/command prompt and typing:
    ```bash
    python --version
    ```
    You should see Python 3.x as the output.

3. **Create a Virtual Environment**: Navigate to your project directory and create a new virtual environment at the root
    ```bash
    cd /path/to/your/project
    python -m venv venv
    ```
4. **Activate the Virtual Environment**: Before you can start installing or using packages in your virtual environment you’ll need to activate it. Activation depends on your operating system:
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
5. **Install Required Packages**: Install the required packages using pip. If you have a `requirements.txt` file, you can install all packages from it:
    ```bash
    pip install -r requirements.txt
    ```

Remember to deactivate the virtual environment when you're done:
```bash
deactivate
```


## Start the interactive jupyter notebook

Make sure the python virtual environment is activated and dependencies are installed. From the root directory launch the jupyter server

```bash
jupyter notebook
```

## Running scripts

Activate the env and go to the project root and run the script as

```bash
python scripts/<file_name>.py
```