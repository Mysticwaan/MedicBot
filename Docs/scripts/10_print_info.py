import uos

def print_info():
    print('\nboard info:\n')
    d = uos.uname()
    print('board name:', d[4])
    print('micropython version:', d[2])
     
    print('\nbuildin modules\n')
    help('modules')
     
    import machine
    print('\nsystem freq: {} MHz'.format(machine.freq()//1000000))
     
    import gc
    print('\nmemory:', gc.mem_free()+gc.mem_alloc())
     
     
    d = uos.statvfs('/')
    print('\nDisk size:')
    print('  total:', d[0]*d[2])
    print('   free:', d[0]*d[3])
    
if __name__ == '__main__':
    print_info()