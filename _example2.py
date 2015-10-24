import yaml
meme=[2,3,[4,5]]
print meme



data = {'a':2, 'b':{'x':3, 'y':{'t1': 4, 't2':5}}}
print yaml.dump(data, default_flow_style=False)
