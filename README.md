API Meteorológica Offline
API REST desenvolvida com Python e FastAPI para disponibilização de dados meteorológicos simulados, armazenados localmente em JSON.

O projeto foi desenvolvido para permitir o consumo de informações meteorológicas por aplicações Python, sem necessidade de conexão com serviços externos.

1. Tecnologias utilizadas
Python
FastAPI
Uvicorn
JSON
Requests (para aplicações consumidoras)
2.
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

latitude
longitude
current
hourly
forecast_days
timezone

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