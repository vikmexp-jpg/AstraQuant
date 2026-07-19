from pathlib import Path
import logging
import winsound

logger = logging.getLogger("AstraQuant")


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
            try:
                logger.debug(f"Playing sound: {filename}")
                winsound.PlaySound(
                    str(sound),
                    winsound.SND_FILENAME | winsound.SND_ASYNC,
                )
                logger.debug(f"Sound played successfully: {filename}")
            except Exception as e:
                logger.error(f"Failed to play sound {filename}: {e}", exc_info=True)
        else:
            logger.warning(f"Sound file not found: {sound}")

    @staticmethod
    def buy():
        logger.debug("Playing buy alert sound")
        SoundAlert.play("buy.wav")

    @staticmethod
    def sell():
        logger.info("Playing sell alert sound")
        SoundAlert.play("sell.wav")

    @staticmethod
    def error():
        logger.warning("Playing error alert sound")
        SoundAlert.play("error.wav")