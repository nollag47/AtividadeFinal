Descrição:

Quando é usado:

Quando queremos evitar ter que implementar subclasses de uma classe principal para cada tipo de objeto;
Diminuir o uso de if e else;
Quando o código precisa criar cópias de algum objeto em tempo de execução; 
Esse padrão pode ser usado em sistemas que precisam ser independentes de como os componentes são criados, configurados e apresentados.

Estrutura:

Relações com outros padrões:

Em um sistema que usa o padrão fábrica abstrata para criar objetos, a hierarquia de classes pode ser muito complexa, e o Prototype é uma alternativa mais simples porque faz a mesma coisa com menos classes.

Exemplo:

Vantagens:

Diminuar a repetição de linhas em seu código;
A prototipagem é muito útil quando o processo de criação de  produtos é muito caro ou mais caro  que a clonagem.

Desvantagens:

Conclusão:

Prototype pode ajudar a limpar o código, caso seus objetos tiverem dezenas de campos e centenas de configurações possíveis, cloná-los pode funcionar como uma alternativa à criação de subclasses. Você pode criar um ou mais objetos definidos de maneiras diferentes. Se você precisar de um objeto semelhante ao definido, basta clonar o protótipo em vez de criar um novo objeto do zero.
