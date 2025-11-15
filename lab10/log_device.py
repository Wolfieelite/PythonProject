import shelve
from time import strftime


def log_nearby_devices(d):
    with shelve.open("device_log.db") as db:
        for name, address in d.items():
            key = name + "_" + address
            formatted_time = strftime("%Y-%m-%d %H:%M:%S")

            if key in db:
                time_list = db[key]
                time_list.append(formatted_time)
                db[key] = time_list
            else:
                db[key] = [formatted_time]
    print("logged devices to database")