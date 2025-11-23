# script-amigo-secreto 🎁

### Motivação
Criei esse código para facilitar o sorteio do jogo Amigo Secreto, evitando a necessidade de download de aplicativos por parte dos participantes ou cadastro por meio de e-mail ou outras redes sociais, tornando prático o sorteio e focando somente no resultado: cada participante deve ter um amigo secreto, que não pode ser ele mesmo, e este resultado ser enviado por e-mail para todos os participantes.

### Como rodar?
1. É necessário que você tenha Python e Pip instalados, além de importar a biblioteca *email* por meio de ```pip install email```.
2. Você tem duas opções de código:
   - Você insere manualmente o nome e e-mail dos participantes -> Arquivo ```script-amigo-secreto.py```
   - Você insere o nome e e-mail dos participantes em um arquivo à parte chamado ```participantes.txt``` -> Arquivo ```script-adaptado.py```
3. Em seguida, você deve criar um arquivo ```<nome-arquivo>.py```, copiar o código do arquivo correspondente para a sua IDE e alterar os campos evidenciados: a mensagem que você deseja que os participantes recebam e as suas credenciais gmail, como e-mail e senha (que pode ser encontrada em "senhas do app" nas configurações do Gmail). Prático, não é mesmo?
5. Após ter realizado as devidas alterações e rodar no terminal ```python <nome-arquivo>.py```.
6. Receba o nome de seu amigo secreto por e-mail e aproveite a brincadeira! =)

### Observações
Obs: Você consegue verificar no terminal se o script está funcionando corretamente conforme os e-mails forem sendo enviados.

Obs 2: O campo de nome do participante não aceita nomes compostos, deve ser apenas um único nome.
