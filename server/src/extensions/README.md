# LocalSO Extensions
Extensions to enhance the functionality of the LocalSO server.

## Setup
Extensions may have extra dependencies and are not enabled by default. To install all required dependencies, run:
```
pip install -r src/extensions/requirements.txt
```

Extensions can be enabled by modifying `config.json`.

## Websocket Extensions
Allows clients to connect to server via websockets. Used by HTML5 client.
