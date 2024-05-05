from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def initialize_circuit(num_nodes):
    num_qubits = num_nodes * 2 + 1
    qc = QuantumCircuit(num_qubits, num_qubits)

    qc.h(0)

    return qc

def quantum_walk(qc, num_steps):
    num_nodes = (qc.num_qubits - 1) // 2

    for step in range(num_steps):
        qc.append(coin_operator(qc.num_qubits), range(qc.num_qubits))

        qc.append(shift_operator(num_nodes), range(qc.num_qubits))

    return qc

def coin_operator(num_qubits):
    qc_coin = QuantumCircuit(num_qubits)
    qc_coin.h(0)
    qc_coin.x(0)
    qc_coin.cz(0, 1)
    qc_coin.x(0)
    qc_coin.h(0)

    return qc_coin.to_gate()

def shift_operator(num_nodes):
    qc_shift = QuantumCircuit(num_nodes * 2 + 1)
    for i in range(num_nodes):
        qc_shift.cx(i * 2 + 1, i*  2 + 2)
        qc_shift.x(i * 2 + 1)
        qc_shift.x(i * 2 + 2)
        qc_shift.cz(i * 2 + 1, i*  2 + 2)
        qc_shift.x(i * 2 + 1)
        qc_shift.x(i * 2 + 2)
        qc_shift.cx(i*  2 + 1, i * 2 + 2)

    return qc_shift.to_gate()

def run_quantum_walk(num_nodes, num_steps):
    qc = initialize_circuit(num_nodes)
    qc = quantum_walk(qc, num_steps)

    qc.measure(range(qc.num_qubits), range(qc.num_qubits))

    backend = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend, shots=1024).result()
    counts = result.get_counts(qc)

    return counts

def plot_quantum_walk(counts):
    plt.bar(counts.keys(), counts.values())
    plt.xlabel('Node')
    plt.ylabel('Frequency')
    plt.title('Quantum Walk')
    plt.show()

num_nodes = 4  
num_steps = 3 

counts = run_quantum_walk(num_nodes, num_steps)
plot_quantum_walk(counts)