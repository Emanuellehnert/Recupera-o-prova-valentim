# RECUPERAÇÃO VALETIM-17-11
Importante!
Esse codigo se refere ao consumidor logo acima, usando a API disponibilizada pelo professor, junto a consulta de api offline e o frontend junto.
API Meteorológica Offline
API REST desenvolvida com Python e FastAPI para disponibilização de dados meteorológicos simulados, armazenados localmente em JSON.

O projeto foi desenvolvido para permitir o consumo de informações meteorológicas por aplicações Python, sem necessidade de conexão com serviços externos.

1. Tecnologias utilizadas
Python
FastAPI
Uvicorn
JSON
Requests (para aplicações consumidoras)
2. Estrutura do projeto
api-meteorologica-offline/
├── app/
│   ├── data/
│   │   └── dados_meteorologicos.json
│   ├── routes/
│   │   ├── __init__.py
│   │   └── meteorologia.py
│   ├── __init__.py
│   ├── main.py
│   └── services.py
├── .gitignore
├── requirements.txt
└── README.md
3. Instalação
Pré-requisitos
Python 3.10 ou superior.
pip.
Clonar o repositório
git clone https://github.com/jpsvalentim/api-meteorologica-offline.git
Acessar a pasta:

cd api-meteorologica-offline
Criar ambiente virtual
Windows PowerShell:

python -m venv .venv
Ativar o ambiente:

.\.venv\Scripts\Activate.ps1
Instalar dependências
pip install -r requirements.txt
4. Executar a API
Com o ambiente virtual ativado, execute:

uvicorn app.main:app --reload
A API estará disponível em:

http://127.0.0.1:8000
Documentação interativa Swagger:

http://127.0.0.1:8000/docs
5. Endpoints disponíveis
Método	Endpoint	Descrição
GET	/	Informações gerais da API
GET	/health	Verificação de disponibilidade
GET	/v1/forecast	Consulta de dados meteorológicos
6. Consulta meteorológica
O endpoint /v1/forecast disponibiliza informações meteorológicas atuais e horárias.

Parâmetros
Parâmetro	Tipo	Descrição
latitude	float	Latitude da localidade
longitude	float	Longitude da localidade
current	string	Variáveis meteorológicas atuais desejadas
hourly	string	Variáveis meteorológicas horárias desejadas
forecast_days	integer	Limite de dias utilizado no cálculo dos registros horários
timezone	string	Fuso horário informado na consulta
Localidade disponível:

Latitude: -26.4851
Longitude: -49.0713
Fuso horário: America/Sao_Paulo
Variáveis atuais disponíveis
temperature_2m
relative_humidity_2m
apparent_temperature
precipitation
wind_speed_10m
Variáveis horárias disponíveis
temperature_2m
relative_humidity_2m
precipitation
wind_speed_10m