from datetime import datetime

from hyp3_metadata import __main__


def test_create_rtc_gamma_readme(tmp_path, test_data_folder):
    product_dir = test_data_folder / 'S1A_IW_20150621T120220_SVP_RTC10_G_saufem_F8E2'
    payload = __main__.marshal_metadata(
        product_dir=product_dir,
        granule_name='S1A_IW_SLC__1SSV_20150621T120220_20150621T120232_006471_008934_72D8',
        dem_name='SRTMGL1',
        processing_date=datetime.strptime('2020-01-01T00:00:00+0000', '%Y-%m-%dT%H:%M:%S%z'),
        resolution=30.0,
        radiometry='gamma-0',
        scale='power',
        filter_applied=False,
        looks=3,
        plugin_name='hyp3_rtc_gamma',
        plugin_version='2.3.0',
        processor_name='GAMMA',
        processor_version='20191203',
    )

    output_file = __main__.create_readme(payload)

    assert output_file.exists()


def test_create_dem_xml(tmp_path, test_data_folder):
    product_dir = test_data_folder / 'S1A_IW_20150621T120220_SVP_RTC10_G_saufem_F8E2'
    payload = __main__.marshal_metadata(
        product_dir=product_dir,
        granule_name='S1A_IW_SLC__1SSV_20150621T120220_20150621T120232_006471_008934_72D8',
        dem_name='SRTMGL1',
        processing_date=datetime.strptime('2020-01-01T00:00:00+0000', '%Y-%m-%dT%H:%M:%S%z'),
        resolution=30.0,
        radiometry='gamma-0',
        scale='power',
        filter_applied=False,
        looks=3,
        plugin_name='hyp3_rtc_gamma',
        plugin_version='2.3.0',
        processor_name='GAMMA',
        processor_version='20191203',
    )

    output_file = __main__.create_dem_xml(payload)

    assert output_file.exists()


def test_create_greyscale_browse_xml(tmp_path, test_data_folder):
    product_dir = test_data_folder / 'S1A_IW_20150621T120220_SVP_RTC10_G_saufem_F8E2'
    payload = __main__.marshal_metadata(
        product_dir=product_dir,
        granule_name='S1A_IW_SLC__1SSV_20150621T120220_20150621T120232_006471_008934_72D8',
        dem_name='SRTMGL1',
        processing_date=datetime.strptime('2020-01-01T00:00:00+0000', '%Y-%m-%dT%H:%M:%S%z'),
        resolution=30.0,
        radiometry='gamma-0',
        scale='power',
        filter_applied=False,
        looks=3,
        plugin_name='hyp3_rtc_gamma',
        plugin_version='2.3.0',
        processor_name='GAMMA',
        processor_version='20191203',
    )

    output_file = __main__.create_browse_xml(payload)

    assert output_file.exists()
