from utils.transform_data_utils import TransformData
from services.request_service import RequestService
from services.frame_service import FrameService

URL = "https://datos.gob.mx/"
json_urls = ["https://datos.gob.mx/cms-api/apis?order=DESC&page=1&per_page=5&sort=creation_date&type=RECOMMENDED", \
        "https://datos.gob.mx/cms-api/datasets?order=DESC&page=1&per_page=5&sort=creation_date&type=RECOMMENDED", \
        "https://datos.gob.mx/ckan-admin/api/3/action/package_search?q=&rows=5&sort=metadata_modified+desc"]

def main():
    """
        This program first makes an HTTP GET request to URL, in case of failure the program is exited.
        In case of success, a list of JSONs is created with the content of every response of the three different APIs.
        Then the data of each of those responses is transformed so that all datasets have the same structure.
        Then that transformed data can be concatenated into one single list in order to create the DataFrame.
        
        The output is the number of rows of the dataset and the number of records by file type.
    """
    try:
        request_service = RequestService(URL)
    except Exception as err:
        print(f"There was a problem with the request service: {err}")
        exit(1)

    jsons = [request_service.get_json_request(url) for url in json_urls]

    jsons[2] = TransformData.standardize_data(jsons[2])
    jsons[0] = TransformData.standardize_ids(jsons[0])
    jsons[1] = TransformData.standardize_ids(jsons[1])

    final_list = jsons[0] + jsons[1] + jsons[2]
    
    df = FrameService(final_list)

    print(f"<<>> Number of datasets: {df.get_row_num()}")

    print(f"<<>> Datasets by file type: \n {df.group_by_file_format()}")


if __name__ == '__main__':
    main()