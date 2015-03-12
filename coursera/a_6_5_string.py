"""
Programming for Everybody (Python)
Assignment 5.2

Write code using find() and string slicing 
to extract the number at the end of the line below. 
"""

text = "X-DSPAM-Confidence:    0.8475";
indx = text.find("0");
s = text[indx:]
n = float(s)
print n