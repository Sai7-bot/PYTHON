score = input("Enter Score: ")
s = float(score)
try:
   s > 1.0 or s < 0.0
except:
   print("Please enter score in range of 0.0 and 1.0")
   quit()
if s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
else:
    print("F")
