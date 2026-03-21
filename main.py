import numpy as np
import sys

# ---- BUILDER FUNCTIONS ----
def build_state():
    zero = [1,0]
    one = [0,1]
    # - only two state real num qubits for now
    amp0 = complex(input("- [ Enter the amplitude for |0>: ] "))
    amp1 = complex(input("- [ Enter the amplitude for |1>: ] "))
    gen_state = [amp0, amp1]
    return gen_state


# ---- ACTION FUNCTIONS ----
def check_state_validity(gen_state):
    norm_zero = np.abs(gen_state[0]) ** 2
    norm_one = np.abs(gen_state[1]) ** 2
    norm = norm_zero + norm_one
    validity = np.abs(norm - 1)

    if validity < 10**(-4):
        print(f"[ VALID ] | Normalizes to {norm}")
    else:
        print(f"[ INVALID ] | Normalizes to {norm}")


# ---- WRAPPER FUNCTIONS ----
def action_one():
    state = build_state()
    validity = check_state_validity(state)
    return validity


# ---- IO ----
def ui():
    user_options = {
        1: action_one
    }

    print("----- QUANTUM COMPUTING SIMULATOR -----")
    print("[ OPTIONS ] | 1: Check state validity | More to be added soon:)")
    inp = int(input("- [ Input number to select action: ] "))

    if inp not in user_options.keys():
        raise ValueError("Please select a number from the given list.")

    user_options[inp]()
    reboot()
    

def reboot():
    print('')
    resp = input("- [ ! ] Run another test? Y/N: ")
    if resp.lower() == 'y':
        ui()
    elif resp.lower() == 'n':
        sys.exit()
    else:
        print("--- [ X ] Please respond with Y or N.")
        reboot()

if __name__ == "__main__":
    ui()