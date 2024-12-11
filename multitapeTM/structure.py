class State:
    def __init__(self, name):
        # Initializes a state with a name and an empty dictionary for transitions.
        pass

    def set_next(self, symbols, next_state, write_symbols, direction):
        # Defines a transition for the state based on input symbols, specifying the next state, symbols to write, and head movement directions.
        pass

    def delta(self, symbols):
        # Retrieves the transition for the given input symbols, if it exists.
        pass

class MultiTapeTM:
    def __init__(self, states, final_states, blank_symbol='B', initial_tapes=None, initial_heads=None):
        # Initializes the Turing machine with a set of states, final states, a blank symbol, initial tape configurations, and head positions.
        pass

    def transition(self):
        # Reads symbols from all tapes, determines the transition based on the current state, updates tapes and head positions, and transitions to the next state.
        pass

    def run(self):
        # Executes the Turing machine until it reaches a final state or halts due to a lack of valid transitions.
        pass
