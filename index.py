import os
import google.auth
from google.oauth2 import service_account
import urllib.request
import xml.etree.ElementTree as ET
import time

DOMAIN = "https://brendaglobo-pseo.geom-cmarco.workers.dev"
SITEMAP_URL = f"{DOMAIN}/sitemap.xml"
BATCH_SIZE = 180  # Numero di URL da inviare al giorno per rimanere sotto la quota
STATE_FILE = "index_state.txt"

print(f"Scaricamento della sitemap da: {SITEMAP_URL}...")
req = urllib.request.Request(SITEMAP_URL, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    xml_data = response.read()

root = ET.fromstring(xml_data)
namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
all_urls = [loc.text for loc in root.findall('.//ns:loc', namespace)]
total_urls = len(all_urls)
print(f"Trovate {total_urls} pagine nella sitemap.")

# Leggi lo stato precedente (indice di partenza)
start_index = 0
if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r") as f:
        try:
            start_index = int(f.read().strip())
        except ValueError:
            start_index = 0

if start_index >= total_urls:
    print("Tutte le pagine sono state già indicizzate! Reset dell'indice a 0.")
    start_index = 0

end_index = min(start_index + BATCH_SIZE, total_urls)
batch_urls = all_urls[start_index:end_index]

print(f"Invio del batch dal {start_index} al {end_index} (totale {len(batch_urls)} URL)...")

# Autenticazione con la chiave JSON
if os.path.exists("key.json"):
    credentials = service_account.Credentials.from_service_account_file(
        "key.json", scopes=["https://www.googleapis.com/auth/indexing"]
    )
else:
    credentials, project = google.auth.default(
        scopes=["https://www.googleapis.com/auth/indexing"]
    )

from google.auth.transport.requests import AuthorizedSession
session = AuthorizedSession(credentials)
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

success_count = 0
for i, url in enumerate(batch_urls, start=start_index + 1):
    body = {"url": url, "type": "URL_UPDATED"}
    response = session.post(ENDPOINT, json=body)
    
    if response.status_code == 200:
        print(f"[{i}/{total_urls}] [SUCCESSO] {url}")
        success_count += 1
    else:
        print(f"[{i}/{total_urls}] [ERRORE {response.status_code}] {url}: {response.text}")
        if response.status_code == 429:
            print("Raggiunto il limite di quota (429). Interrompo il batch per oggi.")
            break
    time.sleep(0.3)

# Salva il nuovo stato
new_state = start_index + success_count
with open(STATE_FILE, "w") as f:
    f.write(str(new_state))

print(f"Batch completato. Prossimo indice salvato: {new_state}/{total_urls}")