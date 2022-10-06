import random
import time

# @author Zozulia Vyacheslav
# @Version 1.0

# Brut-force key
# @param key generation in a range
# @return brut_force_key with the previous value of the found key
# @return duration time finding the key
def brute(key):
    force_key = 0
    start = time.perf_counter_ns()
    while True:
        if (force_key != key):
            force_key = force_key + 1
        else:
            print("Brute-force key: ", force_key)
            duration = time.perf_counter_ns() - start
            print(f"The key was found in {duration // 1000000}ms.\n")
            break


# Key generation in a range
# @param bits_range bit range
# @return key generated in a specific range
def generate(range):
    key = random.randint(0, range)
    print("Key: ", key)
    brute(key - 1)

# Output

def prints(bits):
    for i in range(len(bits)):
        options = 2 ** bits[i]
        print(bits[i], "- bit, Key options:", options)
        generate(options)

# Enter function
def main():
    bits = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
    prints(bits)

if __name__ == "__main__":
    main()