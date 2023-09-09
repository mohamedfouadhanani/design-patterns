from structure.transmission.transmission_behavior import TransmissionBehavior


class AutomaticBehavior(TransmissionBehavior):
    def __init__(self) -> None:
        super().__init__()
        self.gears = ["N", "D", "P", "S", "R"]
