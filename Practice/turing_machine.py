class TuringMachine:
    def __init__(self, initial_state="qs", initial_tape="⊲"):
        self.state = initial_state
        self.tape = list(initial_tape)  # Use a list for mutability
        self.head_position = 0
        self.instructions = {
            "qs,⊲": ("q1", "⊲", 1),
            "q1,b": ("q2", "0", 1),
            "q2,b": ("q1", "1", -1),
            "q1,0": ("q2", "1", 1),
            "q1,1": ("q2", "0", 1),
            "q2,0": ("q1", "1", -1),
            "q2,1": ("q1", "0", -1),
            "q1,⊲": ("qh", "⊲", 0),  # Halt state
        }

    def run(self, max_steps=1000):  # Added a max_steps to prevent infinite loops
        steps = 0
        while self.state != "qh" and steps < max_steps:
            steps += 1
            current_symbol = self.tape[self.head_position]
            instruction_key = f"{self.state},{current_symbol}"

            if instruction_key in self.instructions:
                print(f"Step {steps}: {self.state} {self.tape[:self.head_position]}[{current_symbol}]{self.tape[self.head_position + 1:]}")
                next_state, write_symbol, move_direction = self.instructions[instruction_key]

                self.tape[self.head_position] = write_symbol
                self.state = next_state
                self.head_position += move_direction


                # Handle tape expansion if moving beyond the current bounds
                if self.head_position < 0:
                    self.tape.insert(0, "⊲")  # Add blank at the beginning
                    self.head_position = 0  # Head is at the beginning
                elif self.head_position >= len(self.tape):
                    self.tape.append("b")  # Add blank at the end

            else:
                print(f"Error: No instruction found for state '{self.state}' and symbol '{current_symbol}'")
                return  # Stop if no instruction is found

        print(f"Turing Machine halted after {steps} steps.")
        print("Final tape:", "".join(self.tape))
        print("Final state:", self.state)

# Example usage:
'''
tm = TuringMachine()
tm.run()
'''

tm2 = TuringMachine(initial_tape="⊲bbbbbbbbbbbbbbbbbb") # Example with input
tm2.run()

'''
tm3 = TuringMachine(initial_tape="⊲111b") # Another example with input
tm3.run()
'''