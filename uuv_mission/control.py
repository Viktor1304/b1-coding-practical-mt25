class PDController:
    def __init__(self, KP: float = 0.15, KD: float = 0.6):
        self.KP: float = KP
        self.KD: float = KD
        self.prev_error: float = 0.0

    def __call__(self, error: float) -> float:
        """
        Compute the control action using a PD controller.
        Args:
            error (float): The current error value.
        Returns:
            float: The control action.
        """

        derivative = error - self.prev_error
        control_action = self.KP * error + self.KD * derivative
        self.prev_error = error
        return control_action

