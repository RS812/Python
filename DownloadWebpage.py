from urllib.request import urlopen
url = 'https://www.mjkacc.com/p/staff.html'
with urlopen(url) as response:
    content = response.read().decode('utf-8')
with open('output.html', 'w') as file:
    file.write(content)
print("Webpage downloaded and saved as output.html")
