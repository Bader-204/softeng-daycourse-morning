import sys
from pathlib import Path
from smoothie import smoothie
sys.path.append(str(Path(__file__).parent.parent / "src"))


def test_smoothie():
    assert smoothie(["banana", "strawberry", "yogurt"]) == "Icy Water smoothie with banana, strawberry, yogurt"
    ...  # Continue adding tests here
def test_smoothie():
 assert smoothie(["banana", "strawberry", "kiwi"]) == "Icy Water smoothie with banana, kiwi, strawberry"
 assert smoothie(["banana", "strawberry", "kiwi"], base="almond milk", ice=False) == "Almond Milk smoothie with banana, kiwi, strawberry"
 assert smoothie([], ice=False) == "Just Water!"
 assert smoothie(["  Mango  ", "banana", "Mango"]) == "Icy Water smoothie with banana, mango"
 assert smoothie(["spinach", "kale", 42]) == "I don't know how to make that smoothie!"
 assert smoothie(["blueberry", "raspberry"], base="") == "Icy Water smoothie with blueberry, raspberry" 
 