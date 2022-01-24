import pickle
#converts object to file supporting form- serialization

# cars = ['Audi', 'BMW', 'Baleno'] #pickling pthon object
# file = "mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()

#deserialization

file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))
