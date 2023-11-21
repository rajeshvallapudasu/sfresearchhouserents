import time
import requests
from bs4 import BeautifulSoup
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
"Accept-Language":"en-US,en;q=0.9"
}
response = requests.get(
    "https://ess.tstransco.in/irj/portal",
    headers=headers)
rents_data=response.text