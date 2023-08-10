import sys
import platform

if sys.stdin.isatty():
    sys.exit('Script expecting python versions list from pyenv in a pipe')

isOsx = platform.machine() == 'aarch64'
inputStr = sys.stdin.read()

# Exclude exact
exclude = []
# Exclude versions with substring
excludeStrings = []

# Exclude first line with hint and non production python versions
excludeStrings.extend(['Available', 'versions', 'alpha', 'beta', 'dev', 'src'])

# Exclude pythons types:
# [ironpython] - for dotNet
# [jython] - for Java
# [micropython] - doesn't support pip (it uses upip)
excludeStrings.extend(['ironpython', 'jython', 'micropython'])

# This python versions doesn't support -m command (<=2.3.*) or pip (2.4.*)
exclude.extend(['2.1.3', '2.2.3', '2.3.7', '2.4.0', '2.4.1', '2.4.2', '2.4.3', '2.4.4', '2.4.5', '2.4.6'])

# This python versions depends on specific SSL versions and requires aditional install debug and actions
exclude.extend(['2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.5.4', '2.5.5', '2.5.6', '2.6.0', '2.6.1', '2.6.2', '2.6.3', '2.6.4', '2.6.5', '2.6.6', '2.6.7', '2.6.8', '2.6.9', '2.7.0', '2.7.1', '2.7.2', '2.7.3', '2.7.4', '2.7.5', '2.7.6', '2.7.7', '2.7.8', '2.7.9', '2.7.10', '2.7.11', '2.7.12', '3.0.1', '3.1.0', '3.1.1', '3.1.2', '3.1.3', '3.1.4', '3.1.5', '3.2.0', '3.2.1', '3.2.2', '3.2.3', '3.2.4', '3.2.5', '3.2.6', '3.3.0', '3.3.1', '3.3.2', '3.3.3', '3.3.4', '3.3.5', '3.3.6', '3.3.7', '3.4.0', '3.4.1', '3.4.2', '3.4.3', '3.4.4', '3.4.5', '3.4.6', '3.4.7', '3.4.8', '3.4.9', '3.4.10', '3.5.0', '3.5.1', '3.5.2'])

# [micropython]
# [stackless]
#   build debugging required
#
# [Miniforge3-4.10.1-1]:
#   checksum mismatch: Miniforge3-4.10.1-1-Linux-aarch64.sh (file is corrupt)
#   expected 64ec2e626c1c71332a73081fe482d08e, got a8f153f64a8c8b47eb70b75679f3ad20
exclude.extend(['micropython-1.9.3', 'micropython-1.9.4', 'micropython-1.10', 'micropython-1.11', 'micropython-1.14', 'miniforge3-4.10.1-1', 'stackless-2.7.2', 'stackless-2.7.3', 'stackless-2.7.4', 'stackless-2.7.5', 'stackless-2.7.6', 'stackless-2.7.7', 'stackless-2.7.8', 'stackless-2.7.9', 'stackless-2.7.10', 'stackless-2.7.11', 'stackless-2.7.12', 'stackless-3.2.2', 'stackless-3.2.5', 'stackless-3.3.5', 'stackless-3.3.7', 'stackless-3.4.2', 'stackless-3.4.7'])

if isOsx:
    exclude.extend(['activepython', 'anaconda', 'GraalPython', 'miniconda', 'pypy3.7-7.3.2', 'pypy3.7-7.3.3', 'pypy-c-jit-latest', 'pypy-stm-2.3', 'pypy-stm-2.5.1', 'pypy-1.6', 'pypy-1.7', 'pypy-1.8', 'pypy-1.9', 'pypy-2.0', 'pypy-2.0.1', 'pypy-2.0.2', 'pypy-2.1', 'pypy-2.2', 'pypy-2.2.1', 'pypy-2.3', 'pypy-2.3.1', 'pypy-2.4.0', 'pypy-2.5.0', 'pypy-2.5.1', 'pypy-2.6.0', 'pypy-2.6.1', 'pypy-4.0.0', 'pypy-4.0.1', 'pypy-5.0.0', 'pypy-5.0.1', 'pypy-5.1', 'pypy-5.1.1', 'pypy-5.3', 'pypy-5.3.1', 'pypy-5.4', 'pypy-5.4.1', 'pypy-5.6.0', 'pypy-5.7.0', 'pypy-5.7.1', 'pypy2-5.3', 'pypy2-5.3.1', 'pypy2-5.4', 'pypy2-5.4.1', 'pypy2-5.6.0', 'pypy2-5.7.0', 'pypy2-5.7.1', 'pypy2.7-5.8.0', 'pypy2.7-5.9.0', 'pypy2.7-5.10.0', 'pypy2.7-6.0.0', 'pypy2.7-7.0.0', 'pypy2.7-7.1.0', 'pypy2.7-7.1.1', 'pypy2.7-7.2.0', 'pypy2.7-7.3.0', 'pypy2.7-7.3.1', 'pypy3-2.3.1', 'pypy3-2.4.0', 'pypy3.5-c-jit-latest', 'pypy3.5-5.8.0', 'pypy3.5-5.9.0', 'pypy3.5-5.10.0', 'pypy3.5-5.10.1', 'pypy3.5-6.0.0', 'pypy3.5-7.0.0', 'pypy3.6-7.0.0', 'pypy3.6-7.1.0', 'pypy3.6-7.1.1', 'pypy3.6-7.2.0', 'pypy3.6-7.3.0', 'pypy3.6-7.3.1', 'pypy3.6-7.3.2', 'pypy3.6-7.3.3', 'pyston' ])

lines = inputStr.splitlines()
versions = []
for line in lines:
    versions.append(line.strip())

result = []
for version in versions:
    notInExcludes = True

    for exStr in excludeStrings:
        if version.find(exStr) + 1:
            notInExcludes = False
            break

    if notInExcludes:
        for ex in exclude:
            if version == ex:
                notInExcludes = False
                break

    if notInExcludes:
        result.append(version)

print(' '.join(result))
