class LogicGate:
	def __init__(self, label) -> None:
		self.label = label
		self.output = None

	def get_label(self):
		return self.label

	def get_output(self):
		self.output = self.perform_output()
		return self.output



class BinaryGate(LogicGate):
	def __init__(self, label, pinA=None, pinB=None) -> None:
		super().__init__(label)
		self.pinA = pinA
		self.pinB = pinB

	def get_pin_A(self):
		return self.get_pin_input(self.pinA, 'A')

	def get_pin_B(self):
		return self.get_pin_input(self.pinB, 'B')

	def set_next_pin(self, source):
		if self.pinA == None:
			self.pinA = source
		elif self.pinB == None:
			self.pinB = source
		else:
			raise Exception(f'Both pins of gate {self.get_label} are in use')


	def get_pin_input(self, PIN, label):
		if PIN or PIN == 0:
			if isinstance(PIN, Connector):
				return PIN.get_source_gate().get_output()
			elif PIN in [0,1]:
				if label.upper() == 'A':
					return self.pinA
				elif label.upper() == 'B':
					return self.pinB
			raise Exception(f'PIN {label} can be a valid integer [0,1] or a connector object')
		user_input = input(f"Enter value of PIN {label} for gate {self.get_label()}: ")
		if user_input == '1' or user_input == '0':
			return int(user_input)
		raise Exception(f"PIN {label} Value for gate {self.get_label()} can be either 0 or 1")



class UnaryGate(LogicGate):
	def __init__(self, label) -> None:
		super().__init__(label)
		self.pin = None

	def get_pin(self):
		return int(input(f"Enter value of PIN for gate {self.get_label()}: "))


class AndGate(BinaryGate):
	def __init__(self, label, pinA=None, pinB=None) -> None:
		super().__init__(label, pinA, pinB)

	def perform_output(self):
		self.pinA = self.get_pin_A()
		self.pinB = self.get_pin_B()
		if self.pinA == 1 and self.pinB == 1:
			return 1
		return 0


class ORGate(BinaryGate):
	def __init__(self, label, pinA=None, pinB=None) -> None:
		super().__init__(label, pinA, pinB)

	def perform_output(self):
		self.pinA = self.get_pin_A()
		self.pinB = self.get_pin_B()
		if self.pinA == 1 or self.pinB == 1:
			return 1
		return 0


class NOTGate(UnaryGate):
	def __init__(self, label) -> None:
		super().__init__(label)

	def perform_output(self):
		self.pin = self.get_pin()
		if self.pin == 1:
			return 0
		return 1


class NANDGate(AndGate):
	def perform_output(self):
		if super().perform_output() == 1:
			return 0
		return 1


class NORGate(ORGate):
	def perform_output(self):
		if super().perform_output() == 1:
			return 0
		return 1

class XORGate(ORGate):
	def perform_output(self):
		if self.pinA == 1 and self.pinB == 1:
			return 0
		return super().perform_output()


class Connector:
	def __init__(self, source_gate, dest_gate) -> None:
		self.source_gate = source_gate
		self.dest_gate = dest_gate
		dest_gate.set_next_pin(self)

	def get_source_gate(self):
		return self.source_gate

	def get_dest_gate(self):
		return self.dest_gate

class HalfAdder(BinaryGate):
	sum = 




# A1 = AndGate('A1')
# A2 = AndGate('A2')
# O1 = ORGate('O1')
# A3 = AndGate('A3')
# C1 = Connector(A1, O1)
# C2 = Connector(A2, O1)
# C3 = Connector(O1, A3)
# print(A3.get_output())
# nandgate = NANDGate('N1')
# norgate = NORGate('NOR1')
# print(norgate.get_output())

# A = int(input('A: '))
# B = int(input('B: '))
# C = int(input('C: '))
# D = int(input('D: '))

# A1 = AndGate('A1', A, B)
# B1 = AndGate('B1', C, D)
# NOR1 = NORGate('OR1')
# C1 = Connector(A1, NOR1)
# C2 = Connector(B1, NOR1)

# print(f"LHS: {NOR1.get_output()}")

# A2 = NANDGate('A2', A, B)
# B2 = NANDGate('B2', C, D)
# AND1 = AndGate('AND1')

# C3 = Connector(A2, AND1)
# C4 = Connector(B2, AND1)

# print(f"RHS: {AND1.get_output()}")

N1 = NANDGate('N1', 1, 0)
NOR1 = NORGate('NOR1', 1,0)
XOR1 = XORGate('XOR1', 1,0)
print(N1.get_output())
print(NOR1.get_output())
print(XOR1.get_output())