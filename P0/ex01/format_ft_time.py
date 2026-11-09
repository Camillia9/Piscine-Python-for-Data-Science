import time
from datetime import datetime

def main():
    # recupere le timestamp en temps reel (nb de sc ecoule depuis janier 1970)
    timestamp = time.time()

    print(f"Seconds since January 1, 1970: {timestamp} or {timestamp:.2e} in scientific notation")
    print(datetime.fromtimestamp(timestamp).strftime("%b %d %Y"))

    # datetime.fromtimestamp convertit le timestamp en date et heure
    # strftime permet de personnaliser le format. Ici on veut juste la date: (b: mois, d: jour: Y: annee)

if __name__ == '__main__':
    main()