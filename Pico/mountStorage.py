
import storage
import time
        
        
def mountStorage(func):
    
    def wrapper(*args,**kwargs):
        storage.disable_usb_drive()
        storage.umount("/")
        func(*args,**kwargs)
        storage.remount("/",disable_concurrent_write_protection=True)
        storage.enable_usb_drive()    
    return wrapper


if __name__ == "__main__":
    def main():
        while time.monotonic() < 2:
            with open("/data.csv", "a") as datalog: 
               datalog.write(time.time())
        
    main()


    