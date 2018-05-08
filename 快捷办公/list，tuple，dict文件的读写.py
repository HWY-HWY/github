import pickle


path = r"C:\Users\Administrator\Desktop\3.txt"
data = [1, 2, 3, 4, "abc"]
f = open(path, "wb")
pickle.dump(data, f)
f.close()

f1 = open(path, "rb")
getdata = pickle.load(f1)
print(getdata)
print(type(getdata))
f1.close()
