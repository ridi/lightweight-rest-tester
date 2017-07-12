import copy


class ParameterSet(object):
    """Generate all the possible combinations of given parameters that consist of keys and values."""
    @classmethod
    def generate(cls, params):
        """Generate all the possible combinations of given parameters."""
        param_keys = [key for key in params.keys()]
        if len(param_keys) <= 0:
            return [{}]

        return cls.generate_inner(params, param_keys, {})

    @classmethod
    def generate_inner(cls, params, param_keys, curr_set):
        """Generate all the possible combinations recursively."""
        curr_key = param_keys[0]
        curr_value = params[curr_key]

        """Convert to list (if not) to simplify the rest of parts."""
        value_list = curr_value if isinstance(curr_value, list) else [curr_value]

        param_set_list = []
        for value in value_list:
            curr_set[curr_key] = value

            if len(param_keys) == 1:
                """If no more key (of parameters) are left,"""
                param_set_list.append(copy.deepcopy(curr_set))
            else:
                new_param_set_list = cls.generate_inner(params, param_keys[1:], curr_set)
                param_set_list.extend(new_param_set_list)

        return param_set_list
