import requests

def FetchPage(url):
    """Check page HTML contents."""
    # make HTTP request
    response = requests.get(url)

    # if success: return html text
    if response.status_code == 200:
        return response.text
    # else: return None or raise error 
    else:
        return None

url = "https://manjaro.org/"
html = FetchPage(url)
print(html)
print(f"\nCurrent lenght of characters contained on {url}: {len(html)} characters.")
