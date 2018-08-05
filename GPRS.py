def get_flow(pid, type, devices):
    # pid = get_pid(pkg_name)
    _flow1 = [[], []]
    if pid is not None:
        cmd = "adb -s " + devices + " shell cat /proc/" + pid + "/net/dev"
        print(cmd)
        _flow = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE).stdout.readlines()
        for item in _flow:
            if type == "wifi" and item.split()[0].decode() == "wlan0:":  # wifi
                # 0 上传流量，1 下载流量
                _flow1[0].append(int(item.split()[1].decode()))
                _flow1[1].append(int(item.split()[9].decode()))
                print("------flow---------")
                print(_flow1)
                break
            if type == "gprs" and item.split()[0].decode() == "rmnet0:":  # gprs
                print("-----flow---------")
                _flow1[0].append(int(item.split()[1].decode()))
                _flow1[1].append(int(item.split()[9].decode()))
                print(_flow1)
                break
    else:
        _flow1[0].append(0)
        _flow1[1].append(0)