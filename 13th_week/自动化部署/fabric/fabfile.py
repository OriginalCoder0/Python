"""
  fabric 使用
"""

from fabric.api import *


def hello():
    #local('touch hello')
    run('touch fabric.test')

