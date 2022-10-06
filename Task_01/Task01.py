import random
import time

# @author Zozulia Vyacheslav
# @Version 1.1

# Brut-force key

def brute(key):

    force_key = 0
    start = time.perf_counter_ns()
    while True:
        if (force_key != key):
            force_key = force_key + 1
        else:
            print("Brute-force key: ", force_key)
            duration = time.perf_counter_ns() - start
            print(f"Key was found in {duration // 1000000}ms.\n")
            break


# Key generation in a range

def generate(range):
    key = random.randint(0, range)
    print("Key: ", key)
    brute(key - 1)

# Output

def prints(bits):
    for i in range(len(bits)):
        options = 2 ** bits[i]
        print(bits[i], "- bit | Options - ", options)
        generate(options)

# Enter function
def main():
    bits = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
    prints(bits)

if __name__ == "__main__":
    main()
