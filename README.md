# Falta:
- [ ] Cliente deve estar rodando em background?
- [ ] Sincronizar um unico arquivo? Escolher?
- [ ] Pasta vazia?
- [ ] Multi-threading?
- [ ] Se a pasta ja existir, ignorar
- [ ] Automatizar o processo inteiro (Desenvolvimento de API): complicado rodar em background
- [ ] Robustez: Incorpore recursos para aumentar a robustez do seu serviço, como tratamento de
erros, lógica de reconexão em caso de falha na rede e verificações de integridade dos dados
(por exemplo, checksums ou hashes).
- [ ] Sincronização Bidirecional (Avançado): Implemente a sincronização bidirecional, onde
alterações em qualquer uma das pastas, cliente ou servidor, são espelhadas na outra. Esse
recurso requer lógica de resolução de conflitos
- [ ] Criar apresentacao slide  incluindo configuração, uso e detalhes de design (8 slides?)

# Setup and run nameserver (easy way - Debian/Ubuntu)

`chmod +x setup.sh`

`source setup.sh`

# Others

`python3 -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

- Make directories ./source-folder and 
./mirror-folder

- Open nameserver
`pyro5-ns`

# All

- Populate ./source-folder with desired files for mirroring.

- Run server in another shell instance with venv activated: `python3 server.py`

- Run client in another shell instance with venv activated: `python3 client.py`

- Mirrored files will be on ./mirror-folder
