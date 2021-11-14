from qiskit import QuantumCircuit,QuantumRegister,ClassicalRegister, assemble, Aer, execute
from qiskit.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor

def print_plot_histogram(qc):  
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend)
    return plot_histogram(job.result().get_counts(), color='midnightblue', title="New Histogram")

qc = QuantumCircuit(4,2)
qc.x(0) 
qc.x(1) 
qc.cx(0,2)
qc.cx(1,2)
qc.ccx(0,1,3)
qc.measure(2,0)
qc.measure(3,1) 
qc.draw()

print_plot_histogram(qc)




