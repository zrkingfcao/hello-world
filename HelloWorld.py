try:
    i=0
    while i<5:
        print("Hello World {}".format(i+1))
        i+=1
except Exception as e:
    print(e)