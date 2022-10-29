import superfox as fox

req = fox.get("pakkan.com.tr")

print(req.url)
print(req.domain)
print(req.ip)