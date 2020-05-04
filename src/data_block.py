from geojson import FeatureCollection, Feature
from shapely.geometry import shape

from blockutils.blocks import DataBlock
from blockutils.datapath import set_data_path
from blockutils.logging import get_logger
from blockutils.stac import STACQuery

logger = get_logger(__name__)


class ADataBlock(DataBlock):
    """
    A data block template
    """

    def fetch(self, query: STACQuery, dry_run: bool = False) -> FeatureCollection:
        return_geojson = {
            "type": "Polygon",
            "coordinates": [
                [
                    [126.934801, 37.580773],
                    [126.938385, 37.580773],
                    [126.938385, 37.583766],
                    [126.934801, 37.583766],
                    [126.934801, 37.580773],
                ]
            ],
        }
        return_poly = shape(return_geojson)
        feature = Feature(bbox=return_poly.bounds, geometry=return_poly)
        set_data_path(feature, "a_file_name.tiff")
        out_fc = FeatureCollection([feature])
        return out_fc
