from utils import CargoData

n = 36 # boxes
mean = 72 # lb
std = 3 # lb
max_cargo = 2630 # lb

data = CargoData()
data.set_data(std=std, mean=mean)
print('Probability for safety trip: {:.2f}%'.format(data.get_safety_probability(cargo=max_cargo, n=n)))
