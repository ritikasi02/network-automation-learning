show_run = "sample_configs/R1_config.txt"
with open(show_run, "r") as f:
    for line in f:
        if line.strip().startswith("hostname"):
            x = line.strip().split()[1]
            print(x)
