import numpy as np

class Qubit:
    def __init__(self, state):
        self.state = np.array(state)

class QuantumGate:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def apply(self, qubit):
        new_state = np.dot(self.matrix, qubit.state)
        return Qubit(new_state)

class QuantumCircuit:
    def __init__(self, qubits):
        self.qubits = qubits

    def apply_gate(self, gate, index):
        self.qubits[index] = gate.apply(self.qubits[index])

    def measure(self):
        probabilities = [abs(qubit.state[0])**2 for qubit in self.qubits]
        normalized_probabilities = probabilities / np.sum(probabilities)
        return np.random.choice([i for i in range(len(normalized_probabilities))], p=normalized_probabilities)

qubit1 = Qubit([1/np.sqrt(2), 1/np.sqrt(2)])
qubit2 = Qubit([1j/np.sqrt(2), -1j/np.sqrt(2)])
hadamard_matrix = 1/np.sqrt(2) * np.array([[1, 1], [1, -1]])
hadamard_gate = QuantumGate(hadamard_matrix)
quantum_circuit = QuantumCircuit([qubit1, qubit2])
quantum_circuit.apply_gate(hadamard_gate, 0)
measurement = quantum_circuit.measure()
print("Measurement Result:", measurement)