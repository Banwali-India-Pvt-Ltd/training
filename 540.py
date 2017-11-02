from   __future__ import  print_function
import os
def mount_details():
    if os.path.exists('/proc/mounts'):
        fd = open('/proc/mounts')
        for line in fd:
            line = line.strip()
            words = line.split()
            if len(words) > 5:
                print('(%s)' % ' '.join(words[3:-2]))
            else:
                 print('')
if __name__ == '__main__':
    mount_details()