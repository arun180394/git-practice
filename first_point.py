url = 'http://mysafeinfo.com/api/data?list=englishmonarchs&format=json'
def solve_point_1(url):
    data = requests.get(url).json()
    
    ctynames = set([rec.get('cty', '')for rec in data])
    final_data_dict = {}
    data_dict = {}
    for i in ctynames:
        for rec in data:
            if rec['cty'] == i:
                data_dict.setdefault(rec['hse'], []).append(rec['nm'])
        final_data_dict[i] = data_dict
        data_dict = {}
    
    return final_data_dict

data = solve_point_1(url)
print(data)
