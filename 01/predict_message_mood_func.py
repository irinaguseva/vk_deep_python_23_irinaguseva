import random


class SomeModel:
    def predict(self, message: str) -> float:
        return random.uniform(0, 1)


def predict_message_mood(
    message: str,
    model: SomeModel,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:

    if not isinstance(model, SomeModel):
        raise TypeError('Ошибка. Функции на вход подана не модель SomeModel')
    pred = model.predict(message)
    if not isinstance(pred, (int, float)):
        raise TypeError("Ошибка. Pred должен быть числом")
    if not isinstance(bad_thresholds, (int, float)):
        raise TypeError("Ошибка. bad_thresholds должен быть числом")
    if not isinstance(good_thresholds, (int, float)):
        raise TypeError("Ошибка. good_thresholds должен быть числом")
    assert bad_thresholds < good_thresholds, 'Некорректные значения bad_thresholds, good_thresholds'
    if pred < bad_thresholds:
        return "неуд"
    if pred > good_thresholds:
        return "отл"
    return "норм"
