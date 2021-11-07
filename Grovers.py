from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, plot_histogram
get_ipython().run_line_magic('matplotlib', 'inline')

def print_bloch_sphere(qc):
    state = Statevector.from_instruction(qc)
    return plot_bloch_multivector(state, title="New Bloch Multivector", reverse_bits=False)

def print_plot_histogram(qc):  
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend)
    return plot_histogram(job.result().get_counts(), color='midnightblue', title="New Histogram")

def diffuser(nqubits):
    qc = QuantumCircuit(nqubits)
    for qubit in range(nqubits):
        qc.h(qubit)
    for qubit in range(nqubits):
        qc.x(qubit)
  
    qc.h(nqubits-1)
    qc.mct(list(range(nqubits-1)), nqubits-1) 
    qc.h(nqubits-1)

    for qubit in range(nqubits):
        qc.x(qubit)

    for qubit in range(nqubits):
        qc.h(qubit)
    U_s = qc.to_gate()
    U_s.name = "diffuser"
    return U_s

def initialize_s(qc, qubits):
    for q in qubits:
        qc.h(q)
    return qc

def oracle():
    qc = QuantumCircuit(3)
    qc.cz(1, 2)
    qc.cz(0, 2)
    qc.name ="Oracle"
    return qc.to_gate()

n = 3
grover_circuit = QuantumCircuit(n)
grover_circuit = initialize_s(grover_circuit, [0,1,2])
grover_circuit.append(oracle(), [0,1,2])
grover_circuit.append(diffuser(n), [0,1,2])
grover_circuit.measure_all()
grover_circuit.draw()


print_plot_histogram(grover_circuit)




