import fiona
import fiona.crs
import pprint

def geospatial_data_reader(filepath):
    data = fiona.open(filepath)
    file_info = {'driver': data.driver, 'crs': data.crs, 'schema': data.schema, 'data': data}
    return file_info

def geospatial_data_writer(counties_dict, new_data_list):
    new_driver = None
    new_crs = None
    new_schema = None
    file_info = {}
    #copy reference information from old file to ouput file
    file_info = counties_dict
    new_driver = file_info['driver']
    new_crs = file_info['crs']
    new_schema = file_info['schema']
    print new_schema
    
    #write the temp variables to a new shapefile
    with fiona.open('./output.shp','w', new_driver, new_schema, new_crs) as output:
        for data in new_data_list:
            output.write(data)

def geospatial_data_manipulator(filepath):
    # get all the necessary data from the data reader
    counties_dict = {}
    counties_dict = geospatial_data_reader(filepath)
    counties = counties_dict['data']
    # add a new attribute of type float
    counties_dict['schema']['properties']['is_hennepin'] = 'float'
    new_data = []
    # create a new list containing only hennepin county
    for county in counties:
        if county['properties']['CTY_NAME'] == "Hennepin":
            county['properties']['is_hennepin'] = 1
            new_data.append(county)
    counties_dict['data'].close()
    geospatial_data_writer(counties_dict, new_data) #output

# outputs a new shapefile containing only hennepin county. It has a new attribute named "is_hennepin" that has a 1 in it.
geospatial_data_manipulator("./mn_county_boundaries.shp")    