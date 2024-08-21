text = "Learning is a continuous journey that requires dedication, curiosity, and the willingness to adapt. Every step forward, no matter how small, brings us closer to mastering new skills and achieving our goals. Embrace challenges as opportunities for growth, and remember that persistence is key to success."
t=text.split()
print (t)
freq = {}
for i in t:
    if i in freq:
        freq[i] +=1
    else:
        freq[i]=1

print(freq)