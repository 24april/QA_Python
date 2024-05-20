logs = [
    '192.168.0.1 /home',
    '192.168.0.1 /about',
    '192.168.0.2 /home',
    '192.168.0.7 /about',
    '192.168.0.7 /ab',
    '192.168.0.7 /about',
    '192.168.0.1 /home',
    '192.168.0.2 /contact',
    '192.168.0.1 /about'
]
def analyze_logs(logs):
    ipuniqurl={}
    logssplit=[]
    for log in logs:
        log=log.split()
        logssplit.append(log)
    uniqiplist=[]
    for log in logssplit:
        if log[0] in uniqiplist:
            continue
        uniqiplist.append(log[0])
    ipdicturl={}
    for ip in uniqiplist:
        ipdicturl[ip]=[]
        for log in logssplit:
            if ip==log[0]:
                ipdicturl[ip].append(log[1])
    print(ipdicturl)
    for ip in ipdicturl:
        ipuniqurl[ip]=len(set(ipdicturl[ip]))
    return ipuniqurl
print(analyze_logs(logs))
