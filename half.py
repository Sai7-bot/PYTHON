hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)

def computepay(h,r):
    if h == 40:
        return h * r
    elif h > 40:
        return (40 * r + (h-40) * 1.5 * r)

p = computepay(h,r)
print("Pay",p)
