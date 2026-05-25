show_run = "sample_configs/R1_config.txt"
with open(show_run, "r") as f:
    for line in f:
        if line.strip().startswith("hostname"):
            x = line.strip().split()[1]
            print(x)

with open(show_run, "r") as f:
    y = f.readlines()
    for i, line in enumerate(y):
        if line.strip().startswith("interface"):
            for j in range(i+1, i+10):
                if "ip address" in y[j] and "no ip address" not in y[j]:
                    ip = y[j].strip().split()[2]
                    mask = y[j].strip().split()[3]
                    print(line.strip(), ip, mask)
                    break
                if y[j].strip() == "!":
                    break


