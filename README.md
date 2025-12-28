# Exchange Rates API Colombia

Una libreria Python per ottenere i tassi di cambio utilizzando l'API di exchange-rates.org, con particolare focus sul Peso Colombiano (COP).

## 📋 Descrizione

Questa libreria fornisce un'interfaccia semplice e intuitiva per convertire valute utilizzando l'API di exchange-rates.org. Include funzionalità per elaborare e formattare le risposte dell'API, rendendo più facile l'integrazione nei tuoi progetti.

## ✨ Caratteristiche

- Conversione di valute in tempo reale
- Formattazione automatica delle date
- Pulizia e normalizzazione delle risposte API
- Interfaccia semplice e intuitiva
- Supporto per tutte le valute supportate da exchange-rates.org

## 📦 Installazione

### Requisiti

- Python 3.6 o superiore
- Libreria `requests`

### Installazione delle dipendenze

```bash
pip install requests
```

## 🚀 Utilizzo

### Esempio base

```python
from exchange_rate import ExchangeRatesAPI

# Crea un'istanza dell'API
er = ExchangeRatesAPI()

# Ottieni il tasso di cambio
rate = er.get_rates(1, "EUR", "COP")

print(rate)
```

### Esempio con importo personalizzato

```python
from exchange_rate import ExchangeRatesAPI

er = ExchangeRatesAPI()

# Converti 100 EUR in COP
rate = er.get_rates(100, "EUR", "COP")

print(rate)
```

## 📚 Documentazione API

### Classe `ExchangeRatesAPI`

#### Metodi

##### `__init__()`
Inizializza l'istanza dell'API con le configurazioni predefinite.

##### `get_rates(amount: int, from_currency: str, to_currency: str)`
Ottiene il tasso di cambio tra due valute.

**Parametri:**
- `amount` (int): L'importo da convertire
- `from_currency` (str): Codice valuta di origine (es. "EUR", "USD")
- `to_currency` (str): Codice valuta di destinazione (es. "COP")

**Ritorna:**
- `dict`: Un dizionario contenente le informazioni sul tasso di cambio, con chiavi in minuscolo e dati formattati

**Esempio:**
```python
rate = er.get_rates(1, "EUR", "COP")
# Ritorna un dizionario con informazioni sul tasso di cambio
```

##### `convert_date(original_date: str) -> str`
Converte una data dal formato ISO al formato leggibile.

**Parametri:**
- `original_date` (str): Data nel formato "YYYY-MM-DDTHH:MM:SS"

**Ritorna:**
- `str`: Data formattata come "DD/MM/YY HH:MM"

##### `processing_res(res: dict) -> dict`
Elabora la risposta dell'API, rimuovendo chiavi indesiderate e convertendo tutte le chiavi in minuscolo.

**Parametri:**
- `res` (dict): Risposta grezza dall'API

**Ritorna:**
- `dict`: Risposta elaborata e pulita

## 🔧 Configurazione

La classe utilizza le seguenti configurazioni predefinite:

- **API URL**:** `https://www.exchange-rates.org`
- **API Version**: `v2`
- **Headers**: Configurati per simulare una richiesta browser

## 📝 Note

- L'API utilizza l'endpoint italiano (`/it/api/`) di exchange-rates.org
- Le risposte vengono automaticamente elaborate per rimuovere informazioni non necessarie
- Tutte le chiavi del dizionario di risposta sono convertite in minuscolo per maggiore consistenza


## 📄 Licenza

Questo progetto è fornito "così com'è" per uso personale e educativo.

## 🔗 Link utili

- [Exchange Rates API](https://www.exchange-rates.org)