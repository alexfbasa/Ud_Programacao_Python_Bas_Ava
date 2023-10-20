import requests
import urllib3
from bs4 import BeautifulSoup

# URL da página que contém os links de áudio
url = "https://www.dkefe.com/en/audio/vocabulary-builder/1-1"

# Fazer uma solicitação GET à página
response = requests.get(url, verify=False)
urllib3.disable_warnings()

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Parse o HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontre todos os elementos <a> que contêm links de áudio
    audio_links = soup.find_all('a', href=True)

    # Filtrar apenas os links que terminam com extensões de áudio, como .mp3
    audio_links = [link['href'] for link in audio_links if link['href'].endswith(('.mp3', '.wav', '.ogg'))]

    # Imprimir os links encontrados
    for link in audio_links:
        print(link)
else:
    print("Falha ao acessar a página:", response.status_code)
