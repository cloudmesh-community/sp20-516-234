from cloudmesh.common.Shell import Shell

result = Shell.git('branch', "--list")

print(result)

