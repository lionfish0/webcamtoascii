from distutils.core import setup
setup(
  name = 'webcamtoascii',
  packages = ['webcamtoascii'],
  version = '1.01',
  description = 'Converts webcam to ascii video',
  author = 'Mike Smith',
  author_email = 'm.t.smith@sheffield.ac.uk',
  url = 'https://github.com/lionfish0/webcamtoascii.git',
  download_url = 'https://github.com/lionfish0/webcamtoascii.git',
  keywords = ['demo','webcam','ascii art'],
  classifiers = [],
  install_requires=['numpy','opencv-python'],
  scripts=['bin/webcamtoascii'],
)
