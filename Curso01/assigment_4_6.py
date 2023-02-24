def computepay(h, r):
    if h <= 40 :
        return h * r
    else :
        return (h - 40) * (r * 1.5) + (40 * r)

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
p = computepay(h, r)
print("Pay", p)