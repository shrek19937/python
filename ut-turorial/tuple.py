def mkdir(path):
    path.rsplit('/', 1)
    
    return parent_dir

dir = "/etc/crond"
print(mkdir(dir))

print("/etc/crond"[:dir.rfind("/")])

