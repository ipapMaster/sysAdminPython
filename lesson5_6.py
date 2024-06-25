# Сериализация
import pickle as p  # с большой осторожностью

d = {'apple': 'яблоко',
     'plum': 'слива',
     'pineapple': 'ананас',
     }

# with open('dictfile.dat', 'wb') as pcl:
#     p.dump(d, pcl)  # сериализация

with open('dictfile.dat', 'rb') as pcl:
    r_dict = p.load(pcl)  # десериализация

print(r_dict)
