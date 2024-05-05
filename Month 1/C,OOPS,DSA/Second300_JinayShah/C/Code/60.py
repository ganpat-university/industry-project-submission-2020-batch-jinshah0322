from qiskit import QuantumCircuit, execute, Aer

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0,1], [0,1])

job = execute(qc, Aer.get_backend('qasm_simulator'))
result = job.result()

counts = result.get_counts(qc)
print("\nTotal count for 00 and 11 are:",counts)