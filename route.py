import yaml


def check_yaml(yaml_file):
    try:
        with open(yaml_file, 'r') as file:
            routes = yaml.safe_load(file)

        def check_route_tree(route_dict, parent_keys=set(), path=''):
            for key, val in route_dict.items():
                # 检查是否有重复的键
                if key in parent_keys:
                    raise ValueError(f"Duplicate key '{key}' found in path '{path}'.")

                # 检查是否有缺失的 'path' 字段
                if 'path' not in val:
                    raise ValueError(f"Missing 'path' for key '{key}' in path '{path}'.")

                # 检查 'path' 字段是否为字符串
                if not isinstance(val['path'], str):
                    raise ValueError(f"Path for key '{key}' in path '{path}' is not a string.")

                new_path = f"{path}/{val['path']}".strip('/')
                new_parent_keys = parent_keys.copy()
                new_parent_keys.add(key)

                # 如果有子节点，递归检查子树
                if 'children' in val:
                    # 检查 'children' 字段是否为字典
                    if not isinstance(val['children'], dict):
                        raise ValueError(f"Children of key '{key}' in path '{new_path}' is not a dict.")
                    check_route_tree(val['children'], new_parent_keys, new_path)

        # 从根节点开始检查路由树
        check_route_tree(routes)
        print(f"YAML file '{yaml_file}' is valid.")
    except Exception as e:
        print(f"Error in YAML file '{yaml_file}': {e}")

def recurse(data, keys, accumulated_path=""):
    if not keys:
        return accumulated_path

    current_key = keys[0]
    if current_key in data:
        node = data[current_key]
        node_path = node.get('path', '')
        # 正确地更新完整路径
        full_path = f"{accumulated_path}/{node_path}".strip('/')

        if 'children' in node and len(keys) > 1:
            return recurse(node['children'], keys[1:], full_path)
        elif len(keys) == 1:
            return full_path
        else:
            return ''  # 表示后续没有更多的路径可以匹配
    else:
        return ''  # 当前键不在数据中


class Route:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Route, cls).__new__(cls)
            cls._instance._init_routes()  # 确保调用初始化函数
        return cls._instance

    def _init_routes(self):

        self.route_tree = self._load_routes("routes.yaml")

    @staticmethod
    def _load_routes(yaml_file):
        with open(yaml_file) as file:

            routes = yaml.safe_load(file)
            return Route._build_route_tree(routes)



    @staticmethod
    def _build_route_tree(route_dict, parent_path=''):
        route_tree = {}
        for key, val in route_dict.items():
            # 对于每个节点，构建当前节点的完整路径
            current_path_segment = val['path']
            full_path = f"{parent_path}/{current_path_segment}".strip('/')

            # 为当前节点创建一个新的字典条目，包括路径和可能的子节点
            node = {'path': current_path_segment}  # 使用相对路径而非完整路径

            # 如果存在子节点，递归构建子树
            if 'children' in val:
                node['children'] = Route._build_route_tree(val['children'], full_path)

            route_tree[key] = node

        return route_tree




    @classmethod
    def get_route_path(cls, key):
        instance = cls._instance
        if instance is None:
            raise Exception("Route instance is not created yet.")

        keys = key.split('.')
        data = instance.route_tree

        # 使用独立的 recurse 函数
        path = recurse(data, keys).lstrip('/')
        if not path:
            raise ValueError(f"路由键 '{key}'在配置文件里没有设定")
        
        
        return '/' + path


    @classmethod
    def list_routes(cls):
        instance = cls._instance
        if instance is None:
            raise Exception("Route instance is not created yet.")
        
        route_tree = instance.route_tree
        
        def recurse(node, prefix=''):
            routes = []
            for key, val in node.items():
                # 构建当前节点的完整路径
                current_path = f"{prefix}/{val['path']}".strip('/')
                
                # 如果当前节点有子节点，则递归遍历子节点
                if 'children' in val:
                    routes += recurse(val['children'], current_path)
                else:
                    # 如果没有子节点，则当前节点是一个终点，直接添加到路由列表中
                    routes.append(current_path)
            
                return routes
        
        # 从根节点开始递归遍历路由树
        all_routes = recurse(route_tree)
        
        # 确保所有路径都以斜线开头
        all_routes = ['/' + route if not route.startswith('/') else route for route in all_routes]
        
        return all_routes

