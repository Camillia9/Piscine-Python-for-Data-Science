from PIL import Image, UnidentifiedImageError
import numpy as np


def ft_load(path: str) -> np.ndarray:
    try:
        if not isinstance(path, str):
            raise AssertionError("path must be a string")
        if not path.lower().endswith((".jpg", ".jpeg")):
            raise AssertionError("only JPG and JPEG formats are supported")
        with Image.open(path)as img:
            arr = np.array(img.convert("RGB"))
    except AssertionError as e:
        print(f"Error: {e}")
        return None

    except FileNotFoundError:
        print(f"Error: file not found: {path}")
        return None
    except PermissionError:
        print(f"Error: Permission denied: {path}")
        return None
    except UnidentifiedImageError:
        print(f"Error: not a valid image: {path}")
    except OSError as e:
        print(f"Error: cannot read {path}: {e}")
        return None

    print(f"The shape of image is: {arr.shape}")
    return arr


def main():
    print(ft_load("landscape.jpg"))


if __name__ == '__main__':
    main()
