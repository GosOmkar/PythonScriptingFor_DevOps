
import os

# Blueprint or a Template

class Utilities:
    def show_disk(self):
        print(os.system("df -h"))

    def show_ram(self):
        print(os.system("free -h"))

    def show_sys_details(self):
        print(os.uname().sysname)

machine_A = Utilities()    # object 1
machine_B = Utilities()    # object 2

machine_A.show_disk()
machine_A.show_ram()