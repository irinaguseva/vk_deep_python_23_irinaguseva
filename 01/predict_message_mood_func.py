import random

class SomeModel:
    def predict(self, message: str) -> float:
        # реализация не важна
        return random.uniform(0, 1)

def predict_message_mood(
    message: str,
    model: SomeModel,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    pred = model.predict(message)
    if pred < bad_thresholds:
        return 'неуд'
    elif pred > good_thresholds:
        return 'отл'
    else:
        return 'норм'
