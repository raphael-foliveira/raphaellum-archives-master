from src.models.band import Band, BandGenre, BandMember


def search_band_by_name(name: str, bands_list) -> list[str]:
    result_list = []
    for band in bands_list:
        if name.lower() in band.name.lower():
            result_list.append(band)
    return result_list
