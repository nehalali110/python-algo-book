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
	def __init__(self, label) -> None:
		super().__init__(label)
		self.pinA = None
		self.pinB = None

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
		if PIN:
			return PIN.get_source_gate().get_output()
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
	def __init__(self, label) -> None:
		super().__init__(label)

	def perform_output(self):
		self.pinA = self.get_pin_A()
		self.pinB = self.get_pin_B()
		if self.pinA == 1 and self.pinB == 1:
			return 1
		return 0


class ORGate(BinaryGate):
	def __init__(self, label) -> None:
		super().__init__(label)

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


class NANDGate(BinaryGate):
	def __init__(self, label) -> None:
		super().__init__(label)

	def perform_output(self):
		self.pinA = self.get_pin_A()
		self.pinB = self.get_pin_B()
		if self.pinA == 1 and self.pinB == 1:
			return 0
		return 1


class NORGate(BinaryGate):
	def __init__(self, label) -> None:
		super().__init__(label)

	def perform_output(self):
		self.pinA = self.get_pin_A()
		self.pinB = self.get_pin_B()
		if self.pinA == 0 and self.pinB == 0:
			return 1
		return 0


class Connector:
	def __init__(self, source_gate, dest_gate) -> None:
		self.source_gate = source_gate
		self.dest_gate = dest_gate
		dest_gate.set_next_pin(self)

	def get_source_gate(self):
		return self.source_gate

	def get_dest_gate(self):
		return self.dest_gate




# A1 = AndGate('A1')
# A2 = AndGate('A2')
# O1 = ORGate('O1')
# A3 = AndGate('A3')
# C1 = Connector(A1, O1)
# C2 = Connector(A2, O1)
# C3 = Connector(O1, A3)
# print(A3.get_output())
nandgate = NANDGate('N1')
norgate = NORGate('NOR1')
print(norgate.get_output())
