class SuffixAutomatonNode:
    def __init__(self):
        self.next = {}  # Transition to next states based on character
        self.length = 0  # Length of the node's substring
        self.link = 0  # Suffix link to another state


suffixAutomaton = []
last = 0  # Index of the last state in the automaton


# Initialize the suffix automaton
def initialize():
    global last
    initial_node = SuffixAutomatonNode()
    initial_node.length = 0
    initial_node.link = -1
    suffixAutomaton.append(initial_node)
    last = 0


# Extend the automaton with a new character
def extend_automaton(c):
    global last
    new_node = SuffixAutomatonNode()
    new_node.length = suffixAutomaton[last].length + 1

    current = last
    while current != -1 and c not in suffixAutomaton[current].next:
        suffixAutomaton[current].next[c] = len(suffixAutomaton)  # Create a new state
        current = suffixAutomaton[current].link

    if current == -1:
        new_node.link = 0  # The root state
    else:
        next_state = suffixAutomaton[current].next[c]
        if suffixAutomaton[current].length + 1 == suffixAutomaton[next_state].length:
            new_node.link = next_state
        else:
            clone_node = SuffixAutomatonNode()
            clone_node.__dict__.update(suffixAutomaton[next_state].__dict__)
            clone_node.length = suffixAutomaton[current].length + 1

            suffixAutomaton.append(clone_node)  # Clone the state

            while current != -1 and suffixAutomaton[current].next[c] == next_state:
                suffixAutomaton[current].next[c] = len(suffixAutomaton) - 1
                current = suffixAutomaton[current].link

            new_node.link = len(suffixAutomaton) - 1
            suffixAutomaton[next_state].link = new_node.link

    suffixAutomaton.append(new_node)
    last = len(suffixAutomaton) - 1


# Traverse the suffix automaton
def traverse_automaton():
    print("Traversing Suffix Automaton:")
    for i, state in enumerate(suffixAutomaton):
        print(f"State {i}, Length: {state.length}, Suffix Link: {state.link}")
        for char, next_state in state.next.items():
            print(f" Transition on '{char}' to State {next_state}")


def main():
    input_str = "abab"
    initialize()

    for c in input_str:
        extend_automaton(c)

    # Traverse the constructed suffix automaton
    traverse_automaton()


if __name__ == "__main__":
    main()
