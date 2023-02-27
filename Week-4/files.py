
f = open('C:\Users\ADMIN\Documents\Inspire-Youth-In-STEM\Week-4\tes.txt')
print(f.readline())
filename = 'C:\Users\ADMIN\Documents\Inspire-Youth-In-STEM\Week-4\tes.txt'
try;

    for file in filename:
       with open(filename,'r+w',encoding=None ) as f_object:
        contents = f_object.read()




file_name = 'C:\\Users\\ADMIN\\Documents\\Inspire-Youth-In-STEM\Week-4\tes.txt'
f = open(file_name,'r+w',encoding=None)
print(file_name.readlines())