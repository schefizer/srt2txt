import sys
import os
# sys.path
# sys.path.append('/Users/xxx/Documents/Financial Engineering and Artificial Intelligence in Python/')

path = "/Users/xxx/Documents/lessons/Financial Engineering and Artificial Intelligence in Python/"

dirs = os.listdir(path)
dirs = sorted(dirs)

for dire in dirs:
    path_sub = path+dire+'/'
    if not os.path.isdir(path_sub):
        continue
    files = os.listdir(path_sub)
    files = sorted(files)
    s = []

    file_name_save = path+dire+'.txt'
    with open(file_name_save, 'w') as f:
        f.write('#'*100)
        f.write('\n')
        f.write(dire)
        f.write('\n')
        f.write('#'*100)
        f.write('\n\n\n')
    for file in files:
        if file[-4:] != '.srt':
            continue
        with open(path_sub+file, 'r') as f:
            myset = []
            for line in f:
                if '-->' in line or line[:-1].isdigit() or line == '\n':
                    continue
                line = line.strip()
                myset.append(line)

        length = len(myset)

        line = []
        for line_num in range(length):
            if myset[line_num][-1] not in ['.', '?', '!', ] and line_num < length-2:
                if myset[line_num]==temp_1:
                    line[-1]+=' '+myset[line_num+1]
                    temp_1=myset[line_num+1]
                    continue

                temp = ' '.join([myset[line_num], myset[line_num+1]])
                line.append(temp)
                temp_1=myset[line_num+1]
            elif myset[line_num]==temp_1:
                continue
            else:
                line.append(myset[line_num])

            result = '\n'.join(line)

        with open(file_name_save, 'a+') as f:
            f.write(file)
            f.write('\n\n\n')
            f.write(result)
            f.write('\n\n\n\n\n')
            f.write('*'*100)
            f.write('\n')
            f.write('*'*100)
            f.write('\n\n\n\n\n')
