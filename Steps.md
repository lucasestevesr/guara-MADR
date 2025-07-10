-- Criação do Repositório no github
-- Git Clone do repositório
-- Inicialização do gerenciador de dependências Poetry (Criação do pyproject.toml)- poetry init
-- Instalação da versão Python Poetry - poetry python install 3.13
-- Instalar dependências com Poetry. -poetry add 'x'
    {
        FastAPI...
    }
-- Instalar dependências de desenvolvimento. -poetry add --group dev 'x'
-- Configuração das ferramentas de desenvolvimento:
    - Ruff: Analisar código de forma estática(Linter) baseado nas boas práticas de Python e também formatar o código. Essa configuração é feita no pyproject.toml.
    - Sobre o Linter: 
        Durante a análise estática do código, queremos buscar por coisas específicas.
        No Ruff, precisamos dizer exatamente o que ele deve analisar. 

        I (Isort): Checagem de ordenação de imports em ordem alfabética
        F (Pyflakes): Procura por alguns erros em relação a boas práticas de código
        E (Erros pycodestyle): Erros de estilo de código
        W (Avisos pycodestyle): Avisos de coisas não recomendadas no estilo de código
        PL (Pylint): Como o F, também procura por erros em relação a boas práticas de código
        PT (flake8-pytest): Checagem de boas práticas do Pytest

    -pytest
        addopts = '-p no:warnings'  //usado para ter uma visualização mais limpa dos testes.
    
    -Taskipy: é um task runner, agiliza o desenvolvimento criando alias de comandos.

-- Arquivos de configuração: .env e settings.py
-- Criação de .gitignore antes dos commits;
-- Estruturação das pastas. 