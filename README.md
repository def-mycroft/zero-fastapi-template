# API Template

This project provides a starting point for developing an API using FastAPI.
Intended to be simultaneously scalable and quick to implement, this code allows
for rapidly developing an API with minimal boilerplate, built-in validation, and
easy deployment. It provides a structured yet flexible foundation for building
robust, production-ready services with FastAPI's powerful asynchronous
capabilities.

The intention is to allow data scientists / analysts to quickly make available
API endpoints for more effective code modularization. 

## Server Initialization and Test Request 

Functionalities are provided to easily launch the server and then make a request
to verify that the boilerplate code is working . 

To launch the server, simply run `python main.py`:

```bash
(zero) [main] m $  python main.py 
INFO:     Started server process [2765591]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

...and file `run.py` includes a test case: 

```python
import requests

url = 'http://localhost:8000/main'
payload = {
    'param1': 'param1',
    'param2': 'param2',
}

response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())

```

...after running `run.py`, the server log should look like: 

```bash
(zero) [main] m $  python main.py 
INFO:     Started server process [2765591]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
param1=param1 param2=param2
INFO:     127.0.0.1:36828 - "POST /main HTTP/1.1" 200 OK
```

## Integrating Custom Functionality 

In the given example, params `param1` and `param2` are sent to the server in
`run.py`, and the printed to the terminal in `endpoints.py`. 

Custom functionality can be implemented by modifying `endpoints.py`, where
imports can be added and functionality implemented in endpoint functions like
`main_endpoint`. 

In the current state, the API functionality is intended to be provided locally
(i.e. only programs on the same computer will be able to make requests).
Exposing endpoints via a remote server will require relatively simple
development steps, however the details of these steps are dependent on many
factors, therefore more development work is required to launch the API on a
remote server. 

