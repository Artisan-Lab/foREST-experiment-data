from tool.tools import annotation_table, external_key_dict


class StringMatch:

    @staticmethod
    def is_path_variable(_str):
        if _str[0] == '{' and _str[-1] == '}':
            return _str[1:-2]
        else:
            return False

    @staticmethod
    def find_field_in_dic(dic, field_name, field_type):
        if isinstance(dic, dict):
            for key in dic:
                if key == field_name and type(dic[key]).__name__ == field_type:
                    value = dic[key]
                    return value
                else:
                    value = StringMatch.find_field_in_dic(dic[key], field_name, field_type)
                    if value:
                        return value
        elif isinstance(dic, list):
            if (dic is not None) and (len(dic) > 0) and isinstance(dic[0], dict):
                for sub_dic in dic:
                    value = StringMatch.find_field_in_dic(sub_dic, field_name, field_type)
                    if value:
                        return value
        return None

    @staticmethod
    def get_value_from_external(api_path, api_method, field_name, location):
        if api_path in external_key_dict:
            if api_method in external_key_dict[api_path]:
                for external_key in external_key_dict[api_path][api_method]:
                    if external_key[field_name] == field_name and external_key[location] == location:
                        return external_key['value']
        return None

    @staticmethod
    def get_real_name_from_external(api_path, api_method, field_name, location):
        if api_path in annotation_table:
            if api_method in annotation_table[api_path]:
                for external_key in annotation_table[api_path][api_method]:
                    if external_key['field_name'] == field_name and external_key['location'] == location:
                        return external_key['real_field_name']
        return None



