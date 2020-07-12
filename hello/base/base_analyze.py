import yaml


def analyze_data(file_name, case_name):
    f = open("./data/%s.yaml" % file_name, "r")
    data = yaml.load(f, Loader=yaml.FullLoader)
    data = data[case_name]

    temp_list = list()
    for i in data.values():
        temp_list.append(i)
    f.close()
    return temp_list