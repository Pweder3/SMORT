import storage
print("boot.py")
storage.remount("/",disable_concurrent_write_protection=True)