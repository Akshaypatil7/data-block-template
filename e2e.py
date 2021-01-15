"""
End-to-end test: Fetches data, creates output, stores it in /tmp and checks if output
is valid.
"""

from pathlib import Path

import geojson

from blockutils.e2e import E2ETest

# Disable unused params for assert
# pylint: disable=unused-argument
def asserts(input_dir: Path, output_dir: Path, quicklook_dir: Path, logger):
    # Print out bbox of one tile
    geojson_path = output_dir / "data.json"

    with open(str(geojson_path)) as f:
        feature_collection = geojson.load(f)

    out_path = feature_collection.features[0]["properties"]["up42.data_path"]
    logger.info(out_path)

    logger.info("e2e test successful")


if __name__ == "__main__":
    e2e = E2ETest("a-data-block")
    e2e.asserts = asserts
    e2e.run()
