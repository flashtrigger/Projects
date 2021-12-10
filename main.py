from Functions import build
import pickle
# TODO: Initialize PC attributes, load, Tkinter

testPC = pickle.load(open("FighterBarb.pickle", "rb"))

# transient function making the changes I want at this moment
build(testPC)

print(str(testPC.HP))


pickle.dump(testPC, open("FighterBarb.pickle", "wb"))
