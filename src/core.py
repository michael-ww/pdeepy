import base64
import datetime

groupAuthToken = "group-c1f78a308c4eb0553ed5a470:edeb32c6a889227089923be4"
print(base64.b64encode(groupAuthToken.encode(encoding="utf-8")))

appAuthToken = "92ae6ff970a1552605340a53:e285f94c7ae2bedd3f14ff9e"
print(base64.b64encode(appAuthToken.encode(encoding="utf-8")))

print(datetime.datetime.utcnow())
