# TP 1 - Servidor Web
### Esse trabalho foi feito segundo as seguintes especificaçoes
Faça um servidor de páginas (HTTP) que rode em uma determinada porta e diretório. Ao ser acessado, o servidor irá listas os arquivos deste diretório com links e ao receber a requisição de um arquivo, o servidor deverá fazer a transferência do mesmo (download).

O servidor deverá ainda ter um caminho especial /HEADER que, ao ser requisitado retornará o cabeçalho HTTP da requisição.

Exemplo: meu_server 8000 /home/flavio

Ao acessar o servidor pelo seu navegador, por exemplo no endereço http://localhost:8000, o mesmo deverá listar o conteúdo da pasta /home/flavio.

### Como executar o servidor
```
python3 main.py
```
### Apos escutar o comando o servidor ficará ouvindo a porta 8080, para acessar-lo digite o comando abaixo no navegador 
```
0.0.0.0/8080
```
### O servidor premite que se execute codigos python para isso adicione -run a um aquivo python como no exemplo:
```
0.0.0.0/8080/test.py-run
```
### Para buscar por caminhos absolutos adicione mais uma barra apos a porta como o exemplo:
```
0.0.0.0/8080//etc
```
