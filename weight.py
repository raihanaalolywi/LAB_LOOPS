wieght = float (input("Enter your weight in :"))
height = float (input ("Enter your height in "))

bmi = wieght / (height **2)
print("your bmi is:", round (bmi ,3 ))

if bmi > 25:
    print ("You are overwieght you need to work out more and watch your diet.")
elif bmi >= 18.5 and bmi <= 25:
    print("You are fit & healthy.")
else:
    print("You are underweight. Watch your health")