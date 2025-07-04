Simple script to feed jira descriptions into Ollama and get suggestions posted back to the issue

## How to run
1. Install dependencies, including Ollama
2. Create a `config.json` file in the `config` folder with all fields present in the example
3. Run `main.py` 

## Setup Ollama
https://github.com/ollama/ollama/blob/main/docs/linux.md 
1. Get ollama and install it: `curl -fsSL https://ollama.com/install.sh | sh`
2. Start ollama:`ollama serve`
3. Add a user to run ollama: 
```
sudo useradd -r -s /bin/false -U -m -d /usr/share/ollama ollama
sudo usermod -a -G ollama $(whoami)
```
4. Create a service file in `/etc/systemd/system/ollama.service`:
```
[Unit]
Description=Ollama Service
After=network-online.target

[Service]
ExecStart=/usr/bin/ollama serve
User=ollama
Group=ollama
Restart=always
RestartSec=3
Environment="PATH=$PATH"

[Install]
WantedBy=default.target
```
5. Start the service:
```
sudo systemctl daemon-reload
sudo systemctl enable ollama
```
6. Update ollama if needed: `curl -fsSL https://ollama.com/install.sh | sh`
7. Install a model: `ollama pull <model-name>` Ex: `ollama pull llama3.1`

## Olamma logs
`sudo journalctl -u ollama.service > ollama_logs.txt`
