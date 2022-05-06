import threading
import datetime
import os
import re

def execCmd(cmd):
    try:
        print("%s开始执行%s" % (cmd,datetime.datetime.now()))
        res = os.popen(cmd)
        f.write(cmd)
        if(cmd[0:7]=="python"):
            for i in res.readlines():
                m = re.search(r'200 -    ',i)
                if m!=None:
                    index = i.index("200 -    ")
                    print(i[index:])
                    f.write("  "+i[index:])
            print("%s结束执行%s" % (cmd,datetime.datetime.now()))
        elif(cmd[0:4]=="nmap"):
            print("%s开始执行%s" % (cmd, datetime.datetime.now()))
            for i in res.readlines():
                print(i)
                f.write(i)
            print("%s结束执行%s" % (cmd, datetime.datetime.now()))
    except:
        print("dirsearch 部分目录报错")
if __name__ == '__main__':
    addressfile = open(r"C:\Users\leavrow\Desktop\address.txt","r",encoding="utf-8")
    f = open(r"C:\Users\leavrow\Desktop\address_dir.txt","w",encoding="utf-8")
    cmds=["python D:\ctf-tools\dirsearch-master\dirsearch.py -i 200 -u "+i.replace("\n","") for i in addressfile.readlines()]
    #cmds =["nmap -sV "+i.replace("\n","") for i in addressfile.readlines()]
    print(cmds[0])
    threads = []
    for cmd in cmds:
        th = threading.Thread(target=execCmd, args=(cmd,))
        th.start()
        threads.append(th)
    for th in threads:
        th.join()
    addressfile.close()
    f.close()
