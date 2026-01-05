import os
import shutil

for version in os.listdir('versions'):
	shutil.make_archive('builds/SaplingsToDeadBushes' + str(version), 'zip', 'versions/' + str(version))