import cowsay
import numpy as np

if __name__ == "__main__":
    a = np.arange(15).reshape(3, 5)
    cowsay.cow(str(a))
