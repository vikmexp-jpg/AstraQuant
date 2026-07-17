from pathlib import Path
import winsound


class SoundAlert:

    SOUND_DIR = (
        Path(__file__).resolve().parents[2]
        / "assets"
        / "sounds"
    )

    @staticmethod
    def play(filename: str):

        sound = SoundAlert.SOUND_DIR / filename

        if sound.exists():

            winsound.PlaySound(
                str(sound),
                winsound.SND_FILENAME | winsound.SND_ASYNC,
            )

    @staticmethod
    def buy():
        SoundAlert.play("buy.wav")

    @staticmethod
    def sell():
        SoundAlert.play("sell.wav")

    @staticmethod
    def error():
        SoundAlert.play("error.wav")