import json
s ="[{\"xyz_owner\":\"T\",\"xyz_x2_sages\":135000,\"xyz_x2_statutory_flag\":\"N\",\"xyz_bb\":\"654321987\",\"xyz_code\":[\"D\",\"DD\"],\"xyz_x2_12s\":[20000,4000]}]"


#ss=s[1:len(s)-1]
#print(ss)

b = s.replace("\\", "")
#print(b)

c=json.loads(b)


for k in c:
    print(k)
