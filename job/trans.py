#!-*- coding: utf-8 -*-
"""
练手小程序
"""
import json
import paramiko
import os

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
    for filename in os.listdir(file_path):
        if "blk011" in filename or "blk012" in filename:
            sftp.put(file_path + filename, server_path + filename)
            print("已同步本地文件： \"" + file_path + filename + "\"  到服务器路径：\"" + server_path + filename + "\"")
            sync_file_count += 1

    print("*******************************同步文件--结束")
finally:
    sftp.close()
    transport.close()

print("已经全部同步完成！一共同步了 " + str(sync_file_count) + " 个文件！")