# Automação de Chat Bot no Instagram

---

# Execução da coleta de dados automatica
Modelo do systemctl
```
[Unit]
Description=Chat Instagram Bot
After=network.target

[Service]
Type=simple
User=prod
WorkingDirectory=/caminho/da/pasta/projeto/chat_instagram/app/
ExecStart=/caminho/da/pasta/projeto/chat_instagram/.venv/bin/python //caminho/da/pasta/projeto/chat_instagram/app/app.py
Restart=on-failure
RestartSec=5s
Environment=PYTHONPATH=/home/prod/env/prod/chat_instagram/app/

[Install]
WantedBy=multi-user.target
```
   
- Aponta para um ambiente virtual   
ExecStart=/caminho/da/pasta/projeto/chat_instagram/.venv/bin/python //caminho/da/pasta/projeto/chat_instagram/app/app.py

- Indica o ambiente de execuçao
Environment=PYTHONPATH=/home/prod/env/prod/chat_instagram/app/


```bash
sudo systemctl daemon-reload
sudo systemctl restart chatinstagram.service
sudo systemctl status chatinstagram.service
```

