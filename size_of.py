from dataclasses import dataclass
from typing import NamedTuple
from pympler import asizeof


@dataclass(slots=True, frozen=True)
class CoordinatesDT:
    longitude: float
    latitude: float


class CoordinatesNT(NamedTuple):
    longitude: float
    latitude: float


coordinates_dt = CoordinatesDT(longitude=10.0, latitude=20.0)
coordinates_nt = CoordinatesNT(longitude=10.0, latitude=20.0)
print("dataclass", asizeof.asized(coordinates_dt).size)  # 328 bytes
print("namedtuple:", asizeof.asized(coordinates_nt).size)  # 104 bytes
