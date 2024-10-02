import requests
import json

url = "https://discord.com/api/download/stable?platform=linux&format=tar.gz"
response = requests.get(url)

if response.status_code == 200:
    final_url = response.url
    start = final_url.find("linux/") + len("linux/")
    end = final_url.find("/discord")
    version = final_url[start:end]
    
    print(f"Extracted Version: {version}")
    
    build_info_path = "/opt/discord/resources/build_info.json"
    
    try:
        with open(build_info_path, "r") as file:
            data = json.load(file)
            
        data['version'] = version
        
        with open(build_info_path, "w") as file:
            json.dump(data, file, indent=2)
        
        print(f"Updated version in {build_info_path} to {version}")
        
    except FileNotFoundError:
        print(f"Error: {build_info_path} not found.")
else:
    print(f"Failed to retrieve the URL, status code: {response.status_code}")

