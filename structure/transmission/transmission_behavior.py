class TransmissionBehavior:
    def shift(self, gear):
        if gear not in self.gears:
            raise Exception("Not a Correct Gear")
