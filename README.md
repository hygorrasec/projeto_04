# Projeto 04 - Universidade de Vassouras

[![N|Solid](https://universidadedevassouras.edu.br/wp-content/uploads/2022/03/campus_marica.png)](https://universidadedevassouras.edu.br/campus-marica/)

## Estrutura de dados

Este projeto envolve o uso de estruturas de dados para criar um algoritmo eficiente que possa manipular conjuntos de dados grandes e complexos.

## O projeto

Este é o Projeto 04 do curso de Engenharia de Software da Universidade de Vassouras. O objetivo deste projeto é criar um algoritmo capaz de determinar a posição de cada elemento de um conjunto e imprimir esses valores de forma ascendente, bem como imprimir separadamente as posições atuais. Por fim, a notação Big'O do resultado deve ser impressa de forma gráfica.

// Entrada

elementos = [[a,b,c,d],[q,i,n,m],[f,e,h,j],[p,o,l,g]]

// Saída

[a,b,c,d,e,f,g,h,i,j,l,m,n,o,p,q]
[0:0,0:1,0:2,0:3,2:1,2:0,3:3,2:2,1:1,2:3,3:2,1:3,1:2,3:1,3:0,1:0]

## Tecnologia Utilizada

- O projeto é desenvolvido em Python.

## Como Utilizar

1. Faça o download ou clone do repositório para sua máquina.
2. Crie um ambiente virtual: python3.x -m venv venv
3. Ative o ambiente virtual: Linux: ```. venv/bin/activate``` ou: ```source venv/bin/activate``` | Windows (PowerShell): ```.\venv\Scripts\Activate.ps1``` | Windows (CMD): ```.\venv\Scripts\activate.bat```
4. (WINDOWS) Se apresentar algum erro de permissão, siga: 1: Abrir o PowerShell como Administrador; 2: Digitar o comando: Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned; 3: Fechar o terminal e abrir novamente. Provalmente vai funcionar.
5. Instale as bibliotecas: ```pip install -r requirements.txt```

## Como Contribuir

Contribuições são bem-vindas! Se você deseja contribuir para o projeto, siga os seguintes passos:

1. Faça um fork deste repositório.
2. Se instalar alguma nova biblioteca, rode o comando: ```pip freeze > requirements.txt``` para atualizando o requirements.txt;
3. Crie uma nova branch com suas alterações: `git checkout -b minha-alteracao`
4. Faça as alterações necessárias e commit: `git commit -m "Descrição da minha alteração"`
5. Push para a branch: `git push origin minha-alteracao`
6. Abra um pull request para este repositório.

## Autores

Este projeto foi desenvolvido pelos seguintes autores:

- Fábio Lima
- Hygor Rasec
- Victor Bernardo

Disciplina (Estrutura de Dados) ministrada pelo professor:

- Marcio Garrido

## Licença

The MIT License (MIT)

Direitos autorais (c) 2023 - Fábio Lima, Hygor Rasec e Victor Bernardo

Por meio desta, é concedida permissão, gratuitamente, a qualquer pessoa que obtenha uma cópia deste software e arquivos de documentação associados (o "Software"), para lidar com o Software sem restrições, incluindo, sem limitação, os direitos de usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender cópias do Software, e permitir que as pessoas para quem o Software é fornecido façam o mesmo, sujeitas às seguintes condições:

O aviso de direitos autorais acima e este aviso de permissão devem ser incluídos em todas as cópias ou partes substanciais do Software.

O SOFTWARE É FORNECIDO "COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO, EXPRESSA OU IMPLÍCITA, INCLUINDO, MAS NÃO SE LIMITANDO ÀS GARANTIAS DE COMERCIALIZAÇÃO, ADEQUAÇÃO A UM FIM ESPECÍFICO E NÃO VIOLAÇÃO. EM NENHUMA CIRCUNSTÂNCIA, OS AUTORES OU DETENTORES DE DIREITOS AUTORAIS SERÃO RESPONSÁVEIS POR QUALQUER RECLAMAÇÃO, DANOS OU OUTRA RESPONSABILIDADE, SEJA EM UMA AÇÃO DE CONTRATO, DELITO OU DE OUTRA FORMA, DECORRENTE DE, OU EM CONEXÃO COM O SOFTWARE OU O USO OU OUTRAS NEGOCIAÇÕES NO SOFTWARE.
