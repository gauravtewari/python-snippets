
import os, re

"""
for /path/to/file/filename.csv.gz
the function below returns 3 things
('/path/to/file', 'filename.csv', '.gz')

"""
def get_dir_file_ext(filename):
    _dir = os.path.dirname(filename)
    _file_with_ext = os.path.basename(filename)
    _file, _ext = os.path.splitext(_file_with_ext)
    return _dir, _file, _ext


"""
input: filename with full path
output: (dirname, tuple containing matching groups)
for example :
split_path('/path/to/file/london_bridge_is_falling_down.csv.gz', '(.*)(london.*falling)(.*)')
will return
('/path/to/file', ('', 'london_bridge_is_falling', '_down.csv.gz'))

the matching groups can be indexed as list for e.g. dirname, match = split_path(...)
match[0], match[1] and so on will contain the matching groups as specified in the pattern

split_path('/path/to/file/london_bridge_is_falling_down.csv.gz', '(jungle.*book)')
will return
('/path/to/file', None)
"""
def split_path(filename, pattern):
    _dirname = os.path.dirname(filename)
    _match = re.search(pattern, os.path.basename(filename))
    if(_match):
        return _dirname, _match.groups()
    else:
        return _dirname, None

if __name__ == '__main__':
    file_name = '/path/to/file/filename.csv.gz'
    print("File Exists:", os.path.exists(file_name))
    print("IS File:", os.path.isfile(file_name))
    print("basename:", os.path.basename(file_name)) # gives the filename with extension
    print("dirname:", os.path.dirname(file_name)) # returns the path to the dir in which file is located
    print("joined dirname + basename:", os.path.join(os.path.dirname(file_name), os.path.basename(file_name))) # returns same as file_name

