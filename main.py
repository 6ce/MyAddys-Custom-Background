import requests as Requests

print("Input your session cookie below:")
Session = str(input("\n"))
print("\nInput your image url below:")
Image = str(input("\n"))

Cookies = {
	"__Secure-next-auth.session-token": Session
}

Payload = {
	"backgroundData": Image
}

Headers = {
	"Content-Type": "text/plain;charset=UTF-8",
	"Referer": "https://myaddys.net/dashboard/background",
}

Response = Requests.post("https://myaddys.net/api/updateBackground", headers = Headers, json = Payload, cookies = Cookies).json()

print(Response["message"])
