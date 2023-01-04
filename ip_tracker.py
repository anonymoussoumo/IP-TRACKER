import requests
import pyfiglet
import colorama

colorama.init()

ascii_banner = pyfiglet.figlet_format("IP Tracker", font="slant")
print(ascii_banner)

# Write your API token on acess_key.For e.g acess_key=abcdefg")
ip_address = input(colorama.Fore.GREEN + "Enter the IP address you want to track: ")

url = f"http://api.ipstack.com/{ip_address}?access_key=YOUR_ACESS_KEY"
response = requests.get(url)

if response.status_code == 200:
        data = response.json()

        print(f"Country: {data['country_name']}")
        print(f"Region: {data['region_name']}")
        print(f"City: {data['city']}")
        print(f"Zip Code: {data['zip']}")
        print(f"Latitude: {data['latitude']}")
        print(f"Longitude: {data['longitude']}")
        print("Process Finished!")
else:
        print("Sorry we are unable to track the IP address")