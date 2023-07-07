statuses = {
            "Alice": "online",
            "Bob": "offline",
            "Eve": "online",
        }

def online_status(statuses):    
    l = []
    current_status = list(statuses.keys())
    print(current_status)
    for i,j in statuses.items():
        if j == "online":
            x = current_status.index(i)
            l.append(x)
            count = len(l)
    print(l)
    print(count)



online_status(statuses)




