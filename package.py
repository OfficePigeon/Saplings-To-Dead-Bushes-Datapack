import os
import shutil

for archive in os.listdir('builds'):
	if archive.endswith('.zip'):
		os.remove('builds/' + str(archive))
for version in os.listdir('versions'):
	shutil.make_archive('builds/SaplingsToDeadBushes' + str(version), 'zip', 'versions/' + str(version))