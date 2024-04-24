# Falta:
- [X] Cliente deve estar rodando em background?
- [ ] Sincronizar um unico arquivo? Escolher?
- [X] Pasta vazia?
- [ ] Multi-threading?
- [X] Se a pasta ja existir, ignorar
- [X] Automatizar o processo inteiro: complicado rodar em background
- [X] Robustez: Incorpore recursos para aumentar a robustez do seu serviço, como tratamento de
erros, lógica de reconexão em caso de falha na rede e verificações de integridade dos dados
(por exemplo, checksums ou hashes).
   - [X] Tratamento de erros
   - [ ] Logica de reconexao em falha na rede
   - [X] Verificacao de integridade dos dados
- [ ] Sincronização Bidirecional (Avançado): Implemente a sincronização bidirecional, onde
alterações em qualquer uma das pastas, cliente ou servidor, são espelhadas na outra. Esse
recurso requer lógica de resolução de conflitos
- [X] Criar apresentacao slide  incluindo configuração, uso e detalhes de design (8 slides?)

# Rodar

`python3 -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`python3 main.py`

- Arquivos em ./source-folder serão sincronizado sem ./mirror-folder
