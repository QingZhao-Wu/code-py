#Q2.py
sum = 0.005
up = pow(1 + sum, 365)
down = pow(1 - sum, 365)
print("ε: {:.2f}εδΈ: {:.2f}".format(up, down))