import numpy as np

def trigonometric_identity(angle: float) -> float:
    """Calculates trig identity
    
        param:
        angle: angle in radians

        return: trignometric one

    """
    print("Running trigonometric_identity()")
    return np.cos(angle) ** 2+np.sin(angle) ** 2

# när vi kör denna så kommer __name__ == "__main__".
# ifall vi importerar den så kommer __name__ == "module2"
if __name__ == "__main__":
    print("Running directly from module2.py")
    print(trigonometric_identity(42))
else:
    print("You have imported me")