import csv
import json
import requests

class TestClass(object):

    def __init__(self, foo, bar, baz):
        self.foo = foo
        self.bar = bar
        self.baz = baz

    def fizz_buzz(self, digit_1, digit_2):
        for i in range(1, 100):
            if i % digit_1 == 0:
                if i % digit_2 == 0:
                    print 'fizzbuzz!'
                else:
                    print 'fizz!'
            elif i % digit_2 == 0:
                print 'buzz!'
            else:
                print i

    def first_requirement(self, url):
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
    
    def json_to_csv(self, json_file_path, outfile_path):
        """Convert a file containing a list of flat JSON objects to a csv.
        What's a DictWriter, you say? Never heard of it!
        """
        with open(json_file_path) as f:
            data = json.load(f)
        with open(outfile_path, 'w') as fp:
            writer = csv.writer(fp)
            writer.writerow(data[0].keys())
            for item in data:
                writer.writerow(item.values())
