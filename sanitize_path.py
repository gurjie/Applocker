import array

def main(): 
    path = "D:/R2R/R2R ENCRYPTED.txt" 
    exploded = path.split("\\")
    if(len(exploded)==1):
        exploded = path.split("/")
    reconstructed = ""
    i = 0
    for i in range(0,len(exploded)):
        reconstructed = reconstructed + exploded[i]+"'/'"
    index = reconstructed.find("'")
    rindex = reconstructed.rfind("'")
    reconstructed = reconstructed[0:index]+reconstructed[index+1:rindex]+reconstructed[rindex+1:]
    r2index = reconstructed.rfind("/")
    reconstructed = reconstructed[0:r2index]


if __name__ == "__main__": 
    main()