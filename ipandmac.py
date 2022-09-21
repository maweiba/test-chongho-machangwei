# -*- coding: utf-8 -*-

import os
import socket


def outputCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text


def getPCName(ip):
    return socket.gethostbyaddr(ip)


def getIpMacList():
    ipList = []
    arp_cmd = "arp -a"  # 列出局域网所有 ip
    arp_result = outputCmd(arp_cmd)
    result = arp_result.split("\n")
    ipInfo = []
    total = len(result) - 3
    for idx in range(3, len(result)):
        item = {}
        line = result[idx]
        lineSplit = line.split(" ")
        ip = ''
        mac = ''
        notNullCount = 0
        for idx2 in lineSplit:
            if idx2 != "":
                notNullCount += 1
                if notNullCount == 1:
                    ip = idx2
                elif notNullCount == 2:
                    mac = idx2
        if ip == "":
            continue

        if mac == "":
            continue

        item['ip'] = ip
        item['mac'] = mac

        ipList.append(item)
    return ipList


if __name__ == '__main__':
    ipMacList = getIpMacList()
    total = len(ipMacList)
    ipInfo = []
    for idx in range(0, len(ipMacList)):
        item = {}
        ip = ipMacList[idx]['ip']
        mac = ipMacList[idx]['mac']
        name = ''

        if ip.startswith('172') == False:
            continue
        try:
            name = getPCName(ip)
        except Exception:
            pass
        else:
            pass

        if name == "" or name is None:
            continue

        item['ip'] = ip
        item['mac'] = mac
        item['name'] = name[0]
        ipInfo.append(item)
        print("Getting {}/{}".format(idx, total))

    print("ip\tmac\tname")
    for item in ipInfo:
        print("{}\t{}\t{}".format(item["ip"], item["mac"], item["name"]))
