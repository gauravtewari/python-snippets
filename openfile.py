

import os

def openfile_for_reading(filename):
    try:
        if filename.endswith('.gz'):
            f = os.popen('gzip -d -c %s' % (filename),'r')
        elif filename.endswith('.xz'):
            f = os.popen('xz -d -c %s' % (filename),'r')
        elif filename.endswith('.zst'):
            f = os.popen('zstd -d -c %s' % (filename),'r')
        else:
            f = open(filename,'r')
        return f
    except IOError:
        print(f'Could not read file {filename}')
        return None

# Read a config file and return the next record
# useful for reading config/trace files

class read_file:
    def __init__(self, filename):
        self.config_file = filename
        self.f = openfile_for_reading(self.config_file)
        assert(self.f)
        print("Opened for reading:", self.config_file)

    def __del__(self):
        if(self.f):
            print("Closing file:", self.config_file)
            self.f.close()

    def get_next_record(self):
        for line in self.f:
            line = line.strip()
            if(line):
                return line
