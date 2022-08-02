import httpx


resp = httpx.get('https://swapi.dev/api/people')
print(resp)


with httpx.Client() as client:
    resp = client.get('https://swapi.dev/api/people')
    print(resp)

