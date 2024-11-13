s = 'X-DSPAM-Confidence: 0.8475'
space_index = s.find(':')
number = float(s[space_index+1:])
print(f'The number iss {number:.4f}')