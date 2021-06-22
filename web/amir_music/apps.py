from django.apps import AppConfig


class amirMusicConfig(AppConfig):
    name = 'amir_music'

    def ready(self) -> None:
        import amir_music.signals