text = "X-DSPAM-Confidence:    0.8475"
firstSpace = text.find(" ")
numberString = text[firstSpace + 4: ]
print(float(numberString))
