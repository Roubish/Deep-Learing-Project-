import os

# This function will change the class of each line passed as an argument
def single_line_change(original_line):
    if len(original_line)==0:
        pass
    dictt = {'0':'1'}
    arr = original_line.split()
    arr[0] = dictt[arr[0]]
    return " ".join(arr)

# This funtion will change all the lines in the txt file by calling single_line_change function on each line
def all_line_change(filename):
    with open(filename, "r+") as f:
        changed = []
        old = f.read() # read everything in the file
        old_split = old.split('\n')
        for i in old_split:
            try:
                changed.append(single_line_change(i))
            except:
                pass
    f.close()    
    return "\n".join(changed)

# This function will overwrite the given file with updated classes
def modify_file(filename):
    updated_content = all_line_change(filename)
    f = open(filename, "w")
    f.write(updated_content)
    f.close()

# This function will iterate over all the txt files in the directory and update each content
def iterate_directory(directory_name):
    for filename in os.listdir(directory_name):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            if f.split('.')[-1] == 'txt' and f.split("\\")[-1] != 'classes.txt':
                print(f.split("\\")[-1], "Updated")
                modify_file(f)

if __name__ == '__main__':
    # Mention the directory in which you want to change the classes to the new format
    directory = '/home/ghost/Downloads/pothole.v1i.yolov5pytorch/new_dataset/obj/'
    iterate_directory(directory)
