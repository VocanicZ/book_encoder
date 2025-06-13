import argostranslate.package
import argostranslate.translate

class Translate:
    def __init__(self):
        argostranslate.package.update_package_index()
        available_packages = argostranslate.package.get_available_packages()
        # Get currently installed packages
        installed_packages = argostranslate.package.get_installed_packages()

        languages = [("en", "fr"), ("fr", "en")]
         # Download and install missing packages
        for from_code, to_code in languages:
            if any(p.from_code == from_code and p.to_code == to_code for p in installed_packages):
                continue
            try:
                package_to_install = next(
                    filter(
                        lambda x: x.from_code == from_code and x.to_code == to_code,
                        available_packages
                    )
                )
                argostranslate.package.install_from_path(package_to_install.download())
            except StopIteration:
                print(f"No package available for {from_code} -> {to_code}")

    def translate_to_english(self, sentence_fr: str) -> str:
        return argostranslate.translate.translate(sentence_fr, "fr", "en")

    def translate_to_french(self, sentence_en: str) -> str:
        return argostranslate.translate.translate(sentence_en, "en", "fr")