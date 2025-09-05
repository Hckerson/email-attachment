import os
import yaml
from pathlib import Path
from dataclasses import dataclass


DEFAULT_CONFIG = {"download_folder": "downloads", "date_format": "%Y-%m-%d"}


@dataclass
class Appconfig:
    file_dir = os.path.abspath(os.path.dirname(__file__))
    root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    logs_dir = os.path.join(root_dir, "logs")
    downloads_dir = os.path.join(root_dir, "downloads")

    pdfs_dir = os.path.join(downloads_dir, "pdfs")
    images_dir = os.path.join(downloads_dir, "images")
    others_dir = os.path.join(downloads_dir, "others")

    p = Path("config.yml")
    if p.exists() and p.is_file():
        _data = yaml.safe_load(p.read_text())
    else:
        p.write_text(yaml.dump(DEFAULT_CONFIG))
        _data = DEFAULT_CONFIG

    def configs(self):
        return self._data


def prep_dir(cfg: Appconfig):
    for dir in [cfg.file_dir, cfg.root_dir]:
        os.makedirs(dir, exist_ok=True)


def get_config():
    cfg = Appconfig()
    prep_dir(cfg)
    return cfg
