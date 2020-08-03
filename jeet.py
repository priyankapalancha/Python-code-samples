import jwt

result = {"version" : "hi"
	"example":"Here provides any sample json"

  }
 

 
 // secret that will be provided to us by anyone so that we can decode the message  using secret and algorithm

encoded = jwt.encode(result,'secret',algorithm='HS512')

print(encoded)

x = jwt.decode(encoded,'secret',algorithm='HS512')
print(x)