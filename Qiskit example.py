from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, plot_histogram
get_ipython().run_line_magic('matplotlib', 'inline')

def print_bloch_sphere(qc):
    state = Statevector.from_instruction(qc)
    return plot_bloch_multivector(state, title="New Bloch Multivector", reverse_bits=False)

def print_plot_histogram(qc):
    qc.measure_all()
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend)
    return plot_histogram(job.result().get_counts(), color='midnightblue', title="New Histogram")

qc = QuantumCircuit(2)
qc.x(0)
qc.cx(0,1)
qc.h(0)
qc.draw()

print_bloch_sphere(qc)
print_plot_histogram(qc)
qc.draw()

 



