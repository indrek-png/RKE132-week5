#Kirjuta programm, mis käib läbi iga tähe sõnes ja prindib selle välja.
text = "hello"

""" for i in text:
    print(i) """

#Prindi sõna taguripidi (viimasest tähemärgist esimese juurde, iga täht sõnest kuvatakse eraldi reale tagurüidi järjekorras)

length = len(text)
print(length)

for letter in range(len(text) -1, -1, -1):
    print(text[letter])
