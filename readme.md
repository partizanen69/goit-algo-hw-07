Setup virtual environment and install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install networkx matplotlib
pip freeze > requirements.txt
pip install -r requirements.txt
```

Run tasks

```bash
python3 task1.py
python3 task2.py
python3 task3.py
```
