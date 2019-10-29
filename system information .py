import platform 
def sys_info():
    print('Computer name (in the network): ' + platform.node())
    print('Machine type: ' + platform.machine())
    print('Processor: ' + platform.processor())
    print('Operating system: ' + platform.system())
    print('Operating system version: ' + platform.version())
    print('Operating system release: ' + platform.release())
    return
