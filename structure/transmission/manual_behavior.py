from structure.transmission.transmission_behavior import TransmissionBehavior


class ManualBehavior(TransmissionBehavior):
    def __init__(self) -> None:
        super().__init__()
        self.gears = ["N", "1", "2", "3", "4", "5", "R"]
