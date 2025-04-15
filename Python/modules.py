import os



folder_name = os.path.join(os.getcwd(), 'dir1')


for artifact in os.listdir(folder_name):
    if ".txt" in artifact:
        file_name = os.path.join(folder_name, artifact)
        file_name2 = os.path.join(folder_name, "modified_"+artifact)

        f1 = open(file_name, 'r')
        out = f1.read()

        out = out.replace("Acting", "Somthing")
        f2= open(file_name2, 'w')
        f2.write(out)