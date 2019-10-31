stall_dict = {}
ep_dict = {}
pb_dict = {}

with open('database.txt', 'r') as f:
    everything = f.read()

# string management
blocks = everything.split('//')
for block in blocks:
    # block = block.rstrip('\\n')  # \\n
    items = block.splitlines()
    if items[0] == '':
        del items[0]
    name = items[0]
    stall_dict[name] = []
    for i in range(1, len(items)):
        if items[i][:2] == 'PH':
            pb_dict[name] = items[i][3:]
        elif items[i][:2] == 'EP':
            ep_dict[name] = items[i][3:]
        else:
            if items[i] != 'Closed':
                stall_dict[name].append(items[i])
            else:
                stall_dict[name].append(-1)

if __name__ == '__main__':
    print(stall_dict)
    print(ep_dict)
    print(pb_dict)