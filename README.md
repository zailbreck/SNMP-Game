# SNMP Snake Game

This repository is useful for changing the status of the ethernet or port on the router switch into a snake game. This program displays a grid with colors that show the status changes of each port in the form of an interactive game.

---

## 1. **Python Environment Setup**

### **a. Check Python Installation**
Before starting, make sure Python is installed by running the following command:

```sh
python --version
```
or if using `python3`:

```sh
python3 --version
```

If not already installed, download and install Python from [python.org](https://www.python.org/downloads/).

### **b. Create a Virtual Environment (Optional, but Recommended)**
To keep dependencies clean, create a virtual environment with the following command:

```sh
python -m venv env
```
or if using `python3`:

```sh
python3 -m venv env
```

Enable the virtual environment:
- **Windows**:
  ```sh
  env\Scripts\activate
  ```
- **Linux/Mac**:
  ```sh
  source env/bin/activate
  ```

---

## 2. **Installation of Required Libraries**
Run the following command in the terminal: 

```sh
pip install -r requirements.txt
```

If using `python3`, use:
```sh
pip3 install -r requirements.txt
```

## 3. **Running the Program**
After the installation is complete, run the following command: 

```sh
python main.py
```

If using `python3`, use:
```sh
python3 main.py
```