
car={"maruti":10000,"toyata":20000,"suzuki":300000}
# print(car)
# # print(car.keys())

# # for i in car:
# #     print(i,car.get(i))

# car.update({"maruti":100})
# print(car)

# car.pop("toyata")
# print(car)

# car.update({"Mistubishi":300})
# print(car)

# car.popitem()
# print(car)

# car.clear()
# print(car)

for keys in car:
    print(keys)

for v in car.values():
    print(v)

for kv in car.items():
    print(kv[0],kv[1])

for k,v in car.items():
    print(k,v)
