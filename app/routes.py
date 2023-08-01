from app import app

@app.route('/')
#@app.route('/index')

def index():
    #rerun 'Olá mundo'
    return '''

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Currículo de Cylene</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f0f0f0;
            color: #333;
        }
        h1 {
            text-align: center;
            font-size: 36px;
            color: #555;
            margin-bottom: 20px;
        }
        h2 {
            font-size: 24px;
            color: #007BFF;
            margin-top: 40px;
            margin-bottom: 10px;
        }
        ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        li {
            margin-bottom: 10px;
        }
        strong {
            color: #007BFF;
        }
        .section {
            border-bottom: 2px solid #007BFF;
            padding-bottom: 10px;
        }
        .section:last-child {
            border-bottom: none;
            padding-bottom: 0;
        }
    </style>
</head>
<body>
    <h1>Currículo de Cylene</h1>
    <div class="section">
        <h2>Informações Pessoais</h2>
        <ul>
            <li><strong>Nome:</strong> Cylene Silva</li>
            <li><strong>Data de Nascimento:</strong> 10 de janeiro de 1990</li>
            <li><strong>Email:</strong> cylene.silva@email.com</li>
            <li><strong>Telefone:</strong> (99) 99999-9999</li>
            <li><strong>Endereço:</strong> Rua Fictícia, 123 - Bairro Imaginário, Cidade dos Sonhos</li>
        </ul>
    </div>

    <div class="section">
        <h2>Experiência Profissional</h2>
        <ul>
            <li>
                <strong>Desenvolvedora Web</strong><br>
                Empresa XYZ - São Paulo, Brasil<br>
                Março de 2018 - Presente<br>
                - Responsável pelo desenvolvimento de websites usando HTML, CSS e JavaScript.<br>
                - Colaboração em projetos de equipe e resolução de problemas técnicos.
            </li>
            <li>
                <strong>Estagiária de Marketing Digital</strong><br>
                Agência ABC - Rio de Janeiro, Brasil<br>
                Julho de 2017 - Fevereiro de 2018<br>
                - Auxílio na criação de campanhas de marketing online.<br>
                - Monitoramento de métricas de desempenho e análise de resultados.
            </li>
        </ul>
    </div>

    <div class="section">
        <h2>Educação</h2>
        <ul>
            <li>
                <strong>Bacharelado em Ciência da Computação</strong><br>
                Universidade Imaginária - Cidade dos Sonhos, Brasil<br>
                Agosto de 2012 - Dezembro de 2016
            </li>
            <li>
                <strong>Técnico em Design Gráfico</strong><br>
                Escola de Design Fantástico - Cidade dos Sonhos, Brasil<br>
                Março de 2011 - Julho de 2012
            </li>
        </ul>
    </div>
</body>
</html>





'''

@app.route('/contato')
def contato():
    return 'Meu contato: (61)981214705'

@app.route('/sobre')
def sobre():
    return '44 anos, casada e mãe de uma menina linda. Temente a Deus e feliz sewmpe!!!'

