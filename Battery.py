def get_battery(devices):
    cmd = "adb -s " + devices + " shell dumpsys battery"
    print(cmd)
    output = subprocess.check_output(cmd).split()
               stderr=subprocess.PIPE).stdout.readlines()
    st = ".".join([x.decode() for x in output]) # 转换为string
    print(st)
    battery2 = int(re.findall("level:.(\d+)*", st, re.S)[0])
    writeInfo(battery2, PATH("../info/" + devices + "_battery.pickle"))
    return battery2