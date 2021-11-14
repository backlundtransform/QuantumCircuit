namespace Quantum.QSharpTestProject1 {
  open Microsoft.Quantum.Canon;
  open Microsoft.Quantum.Diagnostics;
  open Microsoft.Quantum.Intrinsic;
  open Microsoft.Quantum.Arithmetic;
  open Microsoft.Quantum.Arrays;
  open Microsoft.Quantum.Convert;
  open Microsoft.Quantum.Math;

  @Test("QuantumSimulator")
  operation AllocateQubit(): Unit {

    use q1 = Qubit();
    use q2 = Qubit();
    within {
      X(q1);
      CNOT(q1, q2);
      H(q1);

    }
    apply {
      AssertMeasurementProbability([PauliZ], [q1], One, 0.5, "qubit must be in |-> state.", 1e-1);
      AssertMeasurementProbability([PauliX], [q2], One, 0.5, "qubit must be in |1> state.", 1e-1);
    }

    Message("Test passed.");
  }

  @Test("QuantumSimulator")
  operation GroverTest(): Unit {

    let numberOfQubits = 10;
    let iterations = Round(Sqrt(IntAsDouble(PowI(2, numberOfQubits))));
    let searchItem = 10;

    let result = Grover(searchItem, numberOfQubits, iterations);
    Fact(result == searchItem, "");
  }

  operation Grover(markIndex: Int, numberOfQubits: Int, iterations: Int): Int {
    use qubits = Qubit[numberOfQubits];

    ApplyToEachA(H, qubits);

    for x in 1..iterations {

      let markerBits = IntAsBoolArray(markIndex, numberOfQubits);
   
      Oracle(qubits,markerBits,numberOfQubits);

      AmplifyAmplitude(qubits);
    }
    let register = LittleEndian(qubits);
    let number = MeasureInteger(register);
    ResetAll(qubits);

    return number;
  }

  operation AmplifyAmplitude(qubits: Qubit[]): Unit is Adj {
    within {
      ApplyToEachA(H, qubits);
      ApplyToEachA(X, qubits);
    }
    apply {
      Controlled Z(Most(qubits), Tail(qubits));
    }
  }
   operation Oracle(qubits: Qubit[], markerBits:Bool[],numberOfQubits:Int): Unit is Adj {
    within {
        for i in 0..numberOfQubits - 1 {
        if not markerBits[i] {
          X(qubits[i]);
        }
      }
    }
    apply {
     Controlled Z(Most(qubits), Tail(qubits));
    }
  }
}