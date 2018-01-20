
import hashlib



m=hashlib.md5()

m.update("alex".encode("utf8"))  #534b44a19bf18d20b71ecc4eb77c572f

print(m.hexdigest())


m.update("alex".encode("utf8"))  #alexalex

print(m.hexdigest())

n=hashlib.md5("salt".encode("utf8"))
n.update(b"alexalex")
print(n.hexdigest())


# m=hashlib.sha1()

