# Importa a biblioteca 'requests', utilizada para realizar requisições HTTP em Python
import requests

def obter_dados_meteorologicos():
    """
    Estabelece comunicação HTTP GET com a API Meteorológica Offline local,
    valida e interpreta o retorno JSON e devolve um dicionário estruturado
    com os indicadores climáticos de Jaraguá do Sul - SC.
    """
    # Define local da API disponibilizada via FastAPI/Uvicorn na porta 8000
    url = "http://127.0.0.1:8000/v1/forecast"
    
    # Dicionário contendo os parâmetros obrigatórios exigidos pela documentação (Jaraguá do Sul - SC)
    parametros = {
        "latitude": -26.4851,
        "longitude": -49.0713
    }
    
    try:
        # Envia a requisição HTTP GET anexando os parâmetros na URL e define timeout de 10 segundos
        resposta = requests.get(url, params=parametros, timeout=10)
        
        # Verifica o código de status HTTP;
        resposta.raise_for_status()
        
        # Converte o corpo da resposta texto em formato JSON para um dicionário Python
        dados = resposta.json()
        
        # Valida se a chave principal 'current' existe na estrutura do JSON recebido
        if "current" not in dados:
            raise ValueError("Estrutura inválida: chave 'current' ausente na resposta da API.")
            
        # Acessa o sub-dicionário que contém os valores meteorológicos atuais
        atual = dados["current"]
        
        # Extrai cada variável meteorológica exigida e organiza em um dicionário padronizado para a interface
        return {
            "temperatura": atual["temperature_2m"],          # Temperatura do ar (°C)
            "umidade_relativa": atual["relative_humidity_2m"], # Umidade relativa do ar (%)
            "sensacao_termica": atual["apparent_temperature"], # Sensação térmica (°C)
            "precipitacao": atual["precipitation"],            # Precipitação acumulada (mm)
            "velocidade_vento": atual["wind_speed_10m"],       # Velocidade do vento (km/h)
            "horario": atual["time"]                           # Data e hora da medição (ISO 8601)
        }

    # Tratamento específico caso o servidor da API esteja desligado ou nao conseguindo acessar
    except requests.exceptions.ConnectionError:
        raise ConnectionError("API offline. Verifique se o servidor Uvicorn está rodando na porta 8000.")
    # Tratamento específico caso o servidor demore mais de 10 segundos para responder
    except requests.exceptions.Timeout:
        raise TimeoutError("Tempo limite excedido ao aguardar resposta da API.")
    # Tratamento para erros de protocolo HTTP (ex: 400 Bad Request, 404 Not Found, 500 Internal Server Error)
    except requests.exceptions.HTTPError as err:
        raise RuntimeError(f"Erro HTTP retornado pela API: {err}")
    # Tratamento caso alguma chave esperada não esteja presente no JSON retornado
    except KeyError as err:
        raise KeyError(f"Campo obrigatório ausente no JSON da API: {err}")
    # Captura qualquer outro erro inesperado durante a execução
    except Exception as erro:
        raise Exception(f"Erro inesperado ao processar os dados: {erro}")

