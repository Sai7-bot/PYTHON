text = "X-DSPAM-Confidence:    0.8475";
m = text.find("0")
val = text[m:]
d = float(val)
print(d)
