import numpy as np
import sys

# ---- BUILDER FUNCTIONS ----
def build_state():
    zero = [1,0]
    one = [0,1]
    # - only two state real num qubits for now
    amp0 = complex(input("- [ Enter the amplitude for |0>: ] "))
    amp1 = complex(input("- [ Enter the amplitude for |1>: ] "))
    gen_state = np.array([amp0, amp1])
    return gen_state


# ---- ACTION FUNCTIONS ----
def check_state_validity(gen_state):
    norm_zero = np.abs(gen_state[0]) ** 2
    norm_one = np.abs(gen_state[1]) ** 2
    norm = norm_zero + norm_one
    dist_from_one = np.abs(norm - 1)

    if dist_from_one < 10**(-4):
        print(f"[ VALID ] | Measures at {norm}")
        return True, norm
    else:
        print(f"[ INVALID ] | Measures at {norm}")
        return False, norm
    
def normalize_state(gen_state, validity, norm):
    if norm == 0.0:
        print("-- [ X ] Zero vector cannot be normalized.")
    elif validity is True:
        print("-- [ ! ] State is already normalized.")
    else:
        normalized = (1/np.sqrt(norm)) * gen_state
        print(f"[ NORMALIZED STATE: ] {normalized}")
        return normalized


# ---- WRAPPER FUNCTIONS ----
def action_one():
    state = build_state()
    validity = check_state_validity(state)
    return validity

def action_two():
    state = build_state()
    validity, norm = check_state_validity(state)
    normalize = normalize_state(state, validity, norm)
    return normalize


# ---- IO ----
def ui():
    user_options = {
        1: action_one,
        2: action_two
    }

    print("----- QUANTUM COMPUTING SIMULATOR -----")
    print("[ OPTIONS ] | 1: Check state validity | 2: Normalize invalid state | Exit | " \
    "More to be added soon:)")
    inp = input("- [ Input number to select action: ] ")

    if inp.lower() == 'exit':
        sys.exit()
    elif not inp.isnumeric():
        print("-- [ X ] Please enter a number.")
        print("")
        ui()

    inp = int(inp)
    if inp not in user_options.keys():
        print("-- [ X ] Please select a number from the given list.")
        print("")
        ui()

    user_options[inp]()
    reboot()
    

def reboot():
    print('')
    resp = input("[ ! ] Run another test? Y/N: ")
    print('')
    if resp.lower() == 'y':
        ui()
    elif resp.lower() == 'n':
        sys.exit()
    else:
        print("--- [ X ] Please respond with Y or N.")
        reboot()

if __name__ == "__main__":
    ui()