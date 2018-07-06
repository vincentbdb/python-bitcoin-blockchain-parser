#!-*- coding: utf-8 -*-
"""
练手小程序
"""
import json
import paramiko
import os
import time

sync_file_count = 0
HOST_IP = "180.76.243.167"
HOST_PORT = 22
USERNAME = "root"
PASSWORD = "GmM9*Q4YHsfouQevU"
file_path = "C:\\Users\\guolo\\AppData\\Roaming\\Bitcoin\\blocks\\"
server_path = "/data/block/"
try:
    transport = paramiko.Transport((HOST_IP, HOST_PORT))
    transport.connect(username=USERNAME, password=PASSWORD)
    sftp = paramiko.SFTPClient.from_transport(transport)
    print("连接远程服务器成功！")
    print("*******************************同步文件--开始")
    now = time.time()
    for file_name in os.listdir(file_path):
        if "blk013" in file_name:
            sftp.put(file_path + file_name, server_path + file_name)
            print("已同步本地文件： \"" + file_path + file_name + "\"  到服务器路径：\"" + server_path + file_name + "\"")
            sync_file_count += 1

    print("*******************************同步文件--结束")
finally:
    sftp.close()
    transport.close()

print("已经全部同步完成！一共同步了 " + str(sync_file_count) + " 个文件！")