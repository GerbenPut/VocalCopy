def TestFunction():
    f = open("static/testfiles/demofile.txt", "a")
    f.write("Now the file has more content!\n")
    f.close()
