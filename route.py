import yaml

# 函数：检查 YAML 文件的有效性
def check_yaml(yaml_file):
    try:
        # 尝试打开并加载 YAML 文件
        with open(yaml_file, 'r') as file:
            routes = yaml.safe_load(file)

        # 内部递归函数：检查路由树的有效性
        def check_route_tree(route_dict, parent_keys=set(), path=''):
            for key, val in route_dict.items():
                # 检查重复键
                if key in parent_keys:
                    raise ValueError(f"Duplicate key '{key}' found in path '{path}'.")
                # 检查 'path' 字段的存在性
                if 'path' not in val:
                    raise ValueError(f"Missing 'path' for key '{key}' in path '{path}'.")
                # # 检查 'path' 字段的类型
                # if not isinstance(val['path'], str):
                #     raise ValueError(f"Path for key '{key}' in path '{path}' is not a string.")

                new_path = f"{path}/{val['path']}".strip('/')
                new_parent_keys = parent_keys.copy()
                new_parent_keys.add(key)

                # 如果存在子节点，递归检查
                if 'children' in val:
                    if not isinstance(val['children'], dict):
                        raise ValueError(f"Children of key '{key}' in path '{new_path}' is not a dict.")
                    check_route_tree(val['children'], new_parent_keys, new_path)

        # 从根节点开始检查路由树
        check_route_tree(routes)
        print(f"YAML file '{yaml_file}' is valid.")
    except Exception as e:
        print(f"Error in YAML file '{yaml_file}': {e}")
        
        
def recurse(data, keys=None, accumulated_path="", collect_all=False):
    if keys is None:
        keys = []
    if not keys and not collect_all:
        return accumulated_path if accumulated_path else '/'
    
    if not collect_all:
        if not keys:
            return accumulated_path  # 确保即使是空列表也返回累积路径或根路径
        current_key = keys[0]
        if current_key in data:
            node = data[current_key]
            node_path = node.get('path', '')
            full_path = f"{accumulated_path}/{node_path}".strip('/') if node_path else accumulated_path
            if 'children' in node and len(keys) > 1:
                return recurse(node['children'], keys[1:], full_path, collect_all)
            else:
                return full_path
        else:
            return ''  # 当前键不在数据中
    else:
        routes = []
        for key, val in data.items():
            current_path = f"{accumulated_path}/{val['path']}".strip('/') if val['path'] else accumulated_path
            if 'children' in val:
                routes += recurse(val['children'], accumulated_path=current_path, collect_all=True)
            else:
                routes.append(current_path if current_path else '/')
        return routes



# Route 类定义
class Route:
    _instance = None

    # 创建或返回类的单例实例
    def __new__(cls, route_file=None):
        if cls._instance is None:
            cls._instance = super(Route, cls).__new__(cls)
            cls._instance.route_file = route_file if route_file is not None else "routes.yaml"
            cls._instance._init_routes()
        return cls._instance

    def _init_routes(self):
        # 加载并构建路由树
        self.route_tree = self._load_routes(self.route_file)

    # 加载路由配置文件并构建路由树
    @staticmethod
    def _load_routes(yaml_file):
        with open(yaml_file) as file:
            routes = yaml.safe_load(file)
            return Route._build_route_tree(routes)

    # 构建路由树
    @staticmethod
    def _build_route_tree(route_dict, parent_path=''):
        route_tree = {}
        for key, val in route_dict.items():
            current_path_segment = val['path']
            node = {'path': current_path_segment}
            if 'children' in val:
                node['children'] = Route._build_route_tree(val['children'], current_path_segment)
            route_tree[key] = node
        return route_tree

    # 获取指定路由键的路径

    @classmethod
    def get_route_path(cls, key):
        instance = cls._instance
        if instance is None:
            raise Exception("Route instance is not created yet.")

        keys = key.split('.')
        data = instance.route_tree

        # 确保 recurse 总是返回一个字符串
        path = recurse(data, keys) or '/'
        # 这里不需要使用 lstrip，因为 recurse 已经确保了正确的格式
        return path


    # 列出所有路由
    @classmethod
    def list_routes(cls):
        instance = cls._instance
        if instance is None:
            raise Exception("Route instance is not created yet.")
        all_routes = recurse(instance.route_tree, collect_all=True)
        all_routes = ['/' + route.lstrip('/') for route in all_routes]
        return all_routes
