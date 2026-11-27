from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    try:
        arr = ft_load("animal.jpeg")
        if arr is None:
            return
        print(arr)

        if arr.shape[0] < 500 or arr.shape[1] < 800:
            raise AssertionError(
                f"image too small for the zoom area: {arr.shape}"
            )

        zoom = arr[100:500, 400:800]
        # zoom[lignes, colonnes, canaux] (':': On garde tout, '0:1': 3D)
        zoom_gris = zoom[:, :, 0:1]
        print(f"New shape after slicing: {zoom_gris.shape}")
        print(zoom_gris)

        plt.imshow(zoom_gris, cmap="gray")
        plt.show()
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except KeyboardInterrupt:
        print("\nInterrupted by user")
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")


if __name__ == '__main__':
    main()


# L'image fait 768 sur 1024 px, on recup (zoom):
# 100:500 : les lignes 100 a 499.
# 400:800 : les colonnes 400 a 799.
# imshow dessine le tableau en image
# imshow accept qu'une shape a 2 dimmensions (400, 400) pas (400, 400, 2)
# Ici '1', matplotlib retirre lui-meme la 3d
# Les dimensions:
# arr[0, 0]       # le pixel en haut à gauche → [120 111 132]
# arr[0, 0, 0]    # sa valeur de rouge        → 120
# arr[0, 0, 1]    # sa valeur de vert         → 111
# arr[0, 0, 2]    # sa valeur de bleu         → 132
