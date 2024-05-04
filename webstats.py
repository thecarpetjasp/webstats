import re


def logmanager(function, day):
        if day == 'today':
                logfilename = 'access.log'
        elif day == 'yesterday':
                logfilename = 'access.log.1'
        logs = open(f"/var/log/nginx/{logfilename}", "r").readlines()
        if function == 'viewers':
                ips = [re.search(r'\d+[.]\d+[.]\d+[.]\d+', log).group(0) for log in logs]
                unique_viewers = len(set(ips))
                print(f"\nUnique viewers for {day}: {unique_viewers}\n")
        elif function == 'successful':
                successful_logs = [log for log in logs if re.search(r'\s200\s', log)]
                print('\n')
                for s in successful_logs:
                        print(s)
                print('\n')
        elif function == 'failed':
                failed_logs = [log for log in logs if not re.search(r'\s200\s', log)]
                print('\n')
                for s in failed_logs:
                        print(s)
                print('\n')

print("\nWEB STAT CONSOLE\n")
print("[1] Check unique viewers for the day")
print("[2] Check unique viewers for yesterday")
print("[3] Display successful logs for today")
print("[4] Display successful logs for yesterday")
print("[5] Display unsuccessful logs for today")
print("[6] Display unsuccessful logs for yesterday")
choice = int(input("\nChoose by number: "))

valid_choices = [1,2,3,4,5,6]

if choice not in valid_choices:
        print("Your choice wasn't recognised. Please try again.")
        exit()

if choice == 1:
        logmanager('viewers', 'today')
elif choice == 2:
        logmanager('viewers', 'yesterday')
elif choice == 3:
        logmanager('successful', 'today')
elif choice == 4:
        logmanager('successful', 'yesterday')
elif choice == 5:
        logmanager('failed', 'today')
elif choice == 6:
        logmanager('failed', 'yesterday')
