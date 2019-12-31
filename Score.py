# This function adding score to text file, if the file update is fail the function will create file name Scoresbeackup.txt
def add_score(points):
    try:
        import Utils
        fr = open(Utils.SCORES_FILE_NAME , "r")
        fr = fr.read()
        if fr.isdecimal() :
            frw= int(fr) + int(points)
            frw = str(frw)
            fw = open(Utils.SCORES_FILE_NAME , "w")
            fw.write(frw)
            fw.close()
            print(frw)
        else:
            fw = open(Utils.SCORES_FILE_NAME, "w")
            fw.write(str(points))
            fw.close()
    except:
        f = open("Scoresbeackup.txt", "w")
        f.write(str(points))
        f.close()
