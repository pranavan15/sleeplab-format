import json
import numpy as np

from pathlib import Path
from sleeplab_format.test_utils.fixtures import *


def create_datasets(basedir: Path) -> None:
    ds_name = 'dataset1'
    series_name = 'series1'
    subject_ids = ['10001', '10002', '10003']
    
    ds_dir = basedir / ds_name
    series_dir = ds_dir / series_name
    series_dir.mkdir(exist_ok=True, parents=True)

    for sid in subject_ids:
        subject_dir = series_dir / sid
        subject_dir.mkdir(exist_ok=True)

        subject_metadata_path = subject_dir / 'metadata.json'
        with open(subject_metadata_path, 'w') as f:
            json.dump(subject_metadata(sid), f, indent=2)

        for k, v in sample_arrays().items():
            sarr_path = subject_dir / k
            sarr_path.mkdir(exist_ok=True)

            attr_path = sarr_path / 'attributes.json'
            with open(attr_path, 'w') as f:
                json.dump(v['attributes'], f, indent=2)

            values_path = sarr_path / f'data.npy'
            np.save(values_path, v['values'], allow_pickle=False)

        events_path = subject_dir / 'events_annotated.json'
        with open(events_path, 'w') as f:
            json.dump(events(), f, indent=2)

        hg_path = subject_dir / 'hypnogram_annotated.json'
        with open(hg_path, 'w') as f:
            json.dump(hypnogram(), f, indent=2)

        study_logs_path = subject_dir / 'study_logs.json'
        with open(study_logs_path, 'w') as f:
            json.dump(study_logs(), f, indent=2)


if __name__ == '__main__':
    basedir = Path(__file__).parent / 'datasets'
    create_datasets(basedir)