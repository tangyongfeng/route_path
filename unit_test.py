from route import Route,check_yaml

print (check_yaml('test_routes.yaml'))


route = Route('test_routes.yaml')

# # 二级路由请求
# print(route.get_route_path('level1.level2'))

# # 三级路由请求（包含动态参数）
# print(route.get_route_path('level1.level2.level3_dynamic'))

# # 四级路由请求
# print(route.get_route_path('level1.level2.level3_dynamic.level4'))

# # 五级路由请求（包含动态参数）
# print(route.get_route_path('level1.level2.level3_dynamic.level4.level5_dynamic'))

# # 六级路由请求
# print(route.get_route_path('level1.level2.level3_dynamic.level4.level5_dynamic.level6'))

# # 七级路由请求（包含动态参数）
# print(route.get_route_path('level1.level2.level3_dynamic.level4.level5_dynamic.level6.level7_dynamic'))

# # 八级路由请求
# print(route.get_route_path('level1.level2.level3_dynamic.level4.level5_dynamic.level6.level7_dynamic.level8'))

# # 九级路由请求（包含动态参数）
# print(route.get_route_path('level1.level2.level3_dynamic.level4.level5_dynamic.level6.level7_dynamic.level8.level9_dynamic'))

# # 十级路由请求
# print(route.get_route_path('level1.level2.level3_dynamic.level4.level5_dynamic.level6.level7_dynamic.level8.level9_dynamic.level10'))

# # 简单路由请求
# print(route.get_route_path('simple_path'))

# # 深层嵌套路由请求
# print(route.get_route_path('deep_nested.nested1.nested2.nested3.nested4_dynamic.nested5'))

# # 特殊字符路由请求
# print(route.get_route_path('special_chars.char_test'))
# print(route.get_route_path('special_chars.emoji_test'))
# print(route.get_route_path('special_chars.space_test'))
# print(route.get_route_path('special_chars.dash_test'))
# all_routes =route.list_routes()
# for item in all_routes:
#     print (item)
# route = Route()
all_routes =route.list_routes()
for item in all_routes:
    print (item)
    
    
print (route.get_route_path('root'))
