import requests as Requests

print("Input your session cookie below:")
Session = str(input("\n"))

Cookies = {
	"__Secure-next-auth.session-token": Session
}

Payload = {
	"backgroundData": "https://i.imgur.com/qQTROq9.jpg"
}

Headers = {
	"Content-Type": "text/plain;charset=UTF-8",
	"Referer": "https://myaddys.net/dashboard/background",
}

Response = Requests.post("https://myaddys.net/api/updateBackground", headers = Headers, json = Payload, cookies = Cookies).json()

print(Response["message"])
