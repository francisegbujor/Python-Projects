import os

def main():
    i = 0
    path = "C:/Users/Francis/Desktop/RenameFolder/"
    for filename in os.listdir(path):
        print("old file name: ", filename)
        new_filename = "img" + str(i) + ".txt"
        print("new file name: ", new_filename)
        source_path = os.path.join(path, filename)
        new_path = os.path.join(path, new_filename)
        
        os.rename(source_path, new_path)
        i += 1

if __name__ == '__main__':
    main()