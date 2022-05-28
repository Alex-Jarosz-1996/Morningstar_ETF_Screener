from pickletools import read_int4
import sys
import subprocess

def getAllPackages():
    # declaring all packages used in the Morningstar ETF package
    configurePackages = ['sys', 'subprocess']
    etfPackages = ['pandas']
    displayPackages = ['tkinter', 'pandastable']
    unitTestPackages = ['unittest']
    
    # creating a list of all packages
    allPackages = list(configurePackages)
    allPackages.extend(etfPackages)
    allPackages.extend(displayPackages)
    allPackages.extend(unitTestPackages)
    
    return allPackages

def install():
    packagesRequired = getAllPackages()
    numPackages = len(packagesRequired)

    print(f"Number of packages to install: {numPackages}\n\n")
    errorList = []
    for count, p in enumerate(packagesRequired, start=1):
        print(f"Installing package: {p}")
        print(f"{count} / {numPackages}")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{p}'])
        except Exception as e:
            errorList.append(p)
            print(f"Error: {e}")

    if not errorList:
        print('All packages successfully installed')
    else:
        print(errorList, ' did not install. ')
    
if __name__ == "__main__":
    install()
    
    