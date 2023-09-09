from structure.tire.tire_behavior import TireBehavior
from structure.elevation.elevation_behavior import ElevationBehavior
from structure.transmission.transmission_behavior import TransmissionBehavior


class Car:
    def __init__(self, tire_behavior: TireBehavior, elevation_behavior: ElevationBehavior, transmission_behavior: TransmissionBehavior) -> None:
        self.tire_behavior = tire_behavior
        self.elevation_behavior = elevation_behavior
        self.transmission_behavior = transmission_behavior
