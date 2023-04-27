import glob
import os.path

from fluent_compiler.bundle import FluentBundle
from fluentogram import TranslatorHub, FluentTranslator


def create_translator_hub_from_directory(path: str, root_locale: str) -> TranslatorHub:
    locales = [
        os.path.basename(language_path)  # resources/locales/en -> en
        for language_path in glob.glob(f"{path}/*")
    ]
    if root_locale not in locales:
        raise ValueError("Root localization code is not included in localizations")

    return TranslatorHub(
        locales_map={
            locale: (locale,)
            for locale in locales
        },
        translators=[
            FluentTranslator(
                locale=locale,
                translator=FluentBundle.from_files(
                    locale=locale,
                    filenames=glob.glob(f"{path}/{locale}/**/*.ftl", recursive=True)
                )
            )
            for locale in locales
        ],
        root_locale=root_locale
    )
