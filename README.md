# Automação de Chat Bot no Instagram

---

# Execução da coleta de dados automatica

## Serviço
Automação e agendamento de execução pelo systemctl

*Criar o arquivo de serviço*

`sudo nano /etc/systemd/system/chatinstagram.service`

*Modelo do systemctl*
```bash
[Unit]
Description=Chat Instagram Bot
After=network.target

[Service]
Type=oneshot
User=prod
WorkingDirectory=/home/prod/env/prod/chat_instagram/app
ExecStart=/home/prod/env/prod/chat_instagram/.venv/bin/python /home/prod/env/prod/chat_instagram/app/app.py
Restart=no
Environment=PYTHONPATH=/home/prod/env/prod/chat_instagram/app
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
```
   
- Aponta para um ambiente virtual   
ExecStart=/caminho/da/pasta/projeto/chat_instagram/.venv/bin/python //caminho/da/pasta/projeto/chat_instagram/app/app.py

- Indica o ambiente de execuçao
Environment=PYTHONPATH=/home/prod/env/prod/chat_instagram/app/

## Timer
*Criar o arquivo de serviço*

`sudo nano /etc/systemd/system/chatinstagram.timer`

```bash
[Unit]
Description=Executar Chat Bot a cada minuto (6h-18h seg-sex)
Requires=chatinstagram.service

[Timer]
OnCalendar=Mon..Fri 6..18:00:00
AccuracySec=1s
Persistent=true

[Install]
WantedBy=timers.target
```

## Comandos
```bash
# Recarregar configurações
sudo systemctl daemon-reload

# Habilitar e iniciar o service/timer
sudo systemctl enable chatinstagram.service
sudo systemctl enable chatinstagram.timer

sudo systemctl restart chatinstagram.timer

# Ver status do service/timer
sudo systemctl status chatinstagram.service #  DEVE CONSTAR COMO <Loaded: loaded (/etc/systemd/system/chatinstagram.service; enabled) \ Active: inactive (dead)>
sudo systemctl status chatinstagram.timer

# Ver logs do service
sudo journalctl -u chatinstagram.service -f

# Ver logs do timer
sudo journalctl -u chatinstagram.timer -f
systemctl list-timers chatinstagram.timer
```