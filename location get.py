import requests
def get_location(ip=None):
    try :
       url = f"https://ipinfo.io/{ip}/json" if ip else "https://ipinfo.io/json"
       response = requests.get(url)
       response.raise_for_status()
       data = response.json()
 
       print(" Location Information:")
       print(f"IP Address : {data.get('ip')}")
       print(f"City       : {data.get('city')}")
       print(f"Region     : {data.get('region')}")
       print(f"Country    : {data.get('country')}")
       print(f"Location   : {data.get('loc')}")  # Latitude, Longitude
       print(f"Timezone   : {data.get('timezone')}")
       print(f"ISP/Org    : {data.get('org')}")
       print(f"ISP/Org    : {data.get('org')}")

    except requests.RequestException as e:
           print("Error fetching location:", e)


if __name__ == "__main__":
    user_ip = input("🔎 Enter an IP address (or press Enter to use your own): ").strip()
    get_location(user_ip if user_ip else None)
    
    
