import numpy as np

class ActiveSession:
    def __init__(self, amp0, amp1):
        self.amp0 = complex(amp0)
        self.amp1 = complex(amp1)

    def build_gen_state(amp0, amp1):
        gen_state = np.array([amp0, amp1])
        return gen_state

state = ActiveSession(0.5, 1.0)
gen_state = state.build_gen_state()
print(gen_state)
